import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import preprocessing
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine

k = 10

epochs = 10
display_step = 10

learning_rate = 0.3

batch_size = 25

sql = 'SELECT user_id, book_id, rating, date_created FROM public."Reviews"'

engine = create_engine('postgresql://ece651_ml:TVL3MV0mguz0DOhLbbm2@localhost:5432/ece651')

# Reading dataset

df = pd.pandas.read_sql(sql, engine)

y = df.date_created
df = df.drop('date_created', axis=1)

df.columns = ['user', 'book', 'rating']

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)

train_data = X_train
test_data = X_test

num_books = df.book.nunique()
num_users = df.user.nunique()

print("USERS: {} BOOKS: {}".format(num_users, num_books))

# # Normalize in [0, 1]

u = df['user'].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(u.reshape(-1,1))
df_normalized = pd.DataFrame(x_scaled)
df['user'] = df_normalized

b = df['book'].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(b.reshape(-1,1))
df_normalized = pd.DataFrame(x_scaled)
df['book'] = df_normalized

r = df['rating'].values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(r.reshape(-1,1))
df_normalized = pd.DataFrame(x_scaled)
df['rating'] = df_normalized

# Convert DataFrame in user-book matrix
matrix = df.pivot(index='user', columns='book', values='rating')
matrix.fillna(0, inplace=True)

users = matrix.index.tolist()
books = matrix.columns.tolist()

matrix = matrix.values

print("Matrix shape: {}".format(matrix.shape))

# num_users = matrix.shape[0]
# num_books = matrix.shape[1]
# print("USERS: {} BOOKS: {}".format(num_users, num_books))

# Network Parameters
num_input = num_books   # num of books
num_hidden_1 = 10       # 1st layer num features
num_hidden_2 = 5        # 2nd layer num features (the latent dim)

X = tf.placeholder(tf.float64, [None, num_input])

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([num_input, num_hidden_1], dtype=tf.float64)),
    'encoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2], dtype=tf.float64)),
    'decoder_h1': tf.Variable(tf.random_normal([num_hidden_2, num_hidden_1], dtype=tf.float64)),
    'decoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_input], dtype=tf.float64)),
}

biases = {
    'encoder_b1': tf.Variable(tf.random_normal([num_hidden_1], dtype=tf.float64)),
    'encoder_b2': tf.Variable(tf.random_normal([num_hidden_2], dtype=tf.float64)),
    'decoder_b1': tf.Variable(tf.random_normal([num_hidden_1], dtype=tf.float64)),
    'decoder_b2': tf.Variable(tf.random_normal([num_input], dtype=tf.float64)),
}

# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']), biases['encoder_b1']))
    # Encoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']), biases['encoder_b2']))
    return layer_2

# Building the decoder
def decoder(x):
    # Decoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']), biases['decoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']), biases['decoder_b2']))
    return layer_2

# Construct model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

# Prediction
y_pred = decoder_op

# Targets are the input data.
y_true = X

# Define loss and optimizer, minimize the squared error
loss = tf.losses.mean_squared_error(y_true, y_pred)
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

predictions = pd.DataFrame()

# Define evaluation metrics
eval_x = tf.placeholder(tf.int32, )
eval_y = tf.placeholder(tf.int32, )
pre, pre_op = tf.metrics.precision(labels=eval_x, predictions=eval_y)

# Initialize the variables
init = tf.global_variables_initializer()
local_init = tf.local_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Train the Model
with tf.Session() as session:
    session.run(init)
    session.run(local_init)

    num_batches = int(matrix.shape[0] / batch_size)
    matrix = np.array_split(matrix, num_batches)

    for i in range(epochs):

        avg_cost = 0

        for batch in matrix:
            _, l = session.run([optimizer, loss], feed_dict={X: batch})
            avg_cost += l

        avg_cost /= num_batches

        print("Epoch: {} Loss: {}".format(i + 1, avg_cost))

        # if i % display_step == 0 or i == 1:
        #     print('Step %i: Minibatch Loss: %f' % (i, l))

    print("Predictions...")

    matrix = np.concatenate(matrix, axis=0)

    preds = session.run(decoder_op, feed_dict={X: matrix})

    # print(matrix)
    # print(preds)
    
    predictions = predictions.append(pd.DataFrame(preds))

    predictions = predictions.stack().reset_index(name='rating')
    predictions.columns = ['user', 'book', 'rating']
    predictions['user'] = predictions['user'].map(lambda value: users[value])
    predictions['book'] = predictions['book'].map(lambda value: books[value])

    print(predictions)

    keys = ['user', 'book']
    i1 = predictions.set_index(keys).index
    i2 = df.set_index(keys).index

    recs = predictions[~i1.isin(i2)]
    recs = recs.sort_values(['user', 'rating'], ascending=[True, False])
    recs = recs.groupby('user').head(k)
    recs.to_csv('prediction.csv', sep=',', index=False, header=False)

    # Save the variables to disk.
    save_path = saver.save(session, '/tmp/book_recommendation_model.ckpt')
    print("Model saved in path: %s" % save_path)

    # creare un vettore dove ci sono per ogni utente i suoi 10 movies

    # test = test_data

    # test = test.sort_values(['user', 'rating'], ascending=[True, False])

    #test = test.groupby('user').head(k) #.reset_index(drop=True)
    #test_list = test.as_matrix(columns=['item']).reshape((-1))
    #recs_list = recs.groupby('user').head(k).as_matrix(columns=['item']).reshape((-1))

    # print("Evaluating...")

    # p = 0.0
    # for user in users[:10]:
    #     test_list = test[(test.user == user)].head(k).values.flatten()
    #     recs_list = recs[(recs.user == user)].head(k).values.flatten()
        
    #     session.run(pre_op, feed_dict={eval_x: test_list, eval_y: recs_list})

    #     pu = precision_score(test_list, recs_list, average='micro')
    #     p += pu

    #     print("Precision for user {}: {}".format(user, pu))
    #     print("User test: {}".format(test_list))
    #     print("User recs: {}".format(recs_list))

    # p /= len(users)

    # p = session.run(pre)
    # print("Precision@{}: {}".format(k, p))

    # print("test len: {} - recs len: {}".format(len(test_list), len(recs_list)))
    
    # print("test list - type: {}".format(type(test_list)))
    # print(test_list)
    
    # print("recs list - type: {}".format(type(recs_list)))
    # print(recs_list)