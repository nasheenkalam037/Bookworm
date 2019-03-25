var express = require('express');
var router = express.Router();
const db = require('../db');
const user = require('../helpers/user');

my_book = {
  book_id: 21,
  title: 'The perks of Being A Wallflower',
  book_cover: '/images/book_cover_placeholder.png',
  authors: ['Stephen Chbosky'],
  synopsis: 'I am the synopsis text, text, text, text, text, text '
};
my_deal = {
  image_class: 'fab fa-amazon',
  rating: '4/5',
  link_to_buy: '#'
};
my_book_long = {
  title: 'The perks of Being A Wallflower',
  book_cover: '/images/book_cover_placeholder.png',
  authors: ['Stephen Chbosky'],
  synopsis: 'I am the synopsis text, text, text, text, text, text ',
  deals: [my_deal, my_deal, my_deal]
};
dummy_data = {
  title: 'The Bookworm',
  user: undefined,
  bookoftheday: my_book,
  books: [my_book_long, my_book_long, my_book_long, my_book_long],
  recommendations: [my_book, my_book, my_book, my_book]
};

sql_top_books_landing = 'SELECT * FROM "BookDetails" ORDER BY amazon_rating DESC NULLS LAST,amazon_num_reviews DESC NULLS LAST LIMIT 15';
sql_todays_book_id = 'SELECT book_id FROM "BookOfTheDay" WHERE date <= now() ORDER BY date DESC limit 1'
sql_bookoftheday = 'SELECT * FROM "BookDetails" where book_id = ('+sql_todays_book_id+')';
sql_random_books = 'SELECT * FROM "BookDetails" order by random() LIMIT $1';

/* GET home page. */
router.get('/', async function(req, res, next) {
  // Variable has to be named 'rows'
  var top_books = await db.query(sql_top_books_landing);
  var bookoftheday = await db.query(sql_bookoftheday);

  var myuser = user.getUser(req.session);

  var recommendations = [my_book, my_book, my_book, my_book];
  if(myuser) {
    // TODO for logged in users
    console.log('Grabbing recommendations doe user', myuser);
  } else {
    console.log('Grabbing random recommendations');
    recommendations = await db.query(sql_random_books, [10]);
    recommendations = recommendations.rows
  }

  console.log(recommendations);

  res.render('index', {
    title: 'The Bookworm',
    user: myuser,
    bookoftheday: bookoftheday.rows[0],
    books: top_books.rows,
    recommendations: recommendations
  });
});

sql_top_books_all = 'SELECT * FROM "BookDetails" ORDER BY book_id DESC';

/* GET home page. */
router.get('/all', async function(req, res, next) {
  // Variable has to be named 'rows'
  var { rows } = await db.query(sql_top_books_all);

  console.log(rows);

  res.render('search', {
    title: 'The Bookworm',
    user: user.getUser(req.session),
    books: rows
  });
});

sql_author_details = 'SELECT * FROM "Author" WHERE author_id = $1';
sql_author_books =
  'SELECT * FROM "BookDetails" ' +
  'WHERE book_id in ( ' +
  'SELECT book_id FROM "AuthorBooks" WHERE author_id = $1 ' +
  ') ORDER BY book_id ASC';
sql_coauthors =
  'SELECT distinct a.* FROM "Author" as a ' +
  'INNER JOIN "AuthorBooks" ab on a.author_id = ab.author_id ' +
  'WHERE ab.book_id in ( ' +
  'SELECT book_id FROM "AuthorBooks" WHERE author_id = $1 ' +
  ') AND ab.author_id != $1';
/* GET book details page. */
router.get('/author/:authorId(\\d+)/:authorName', async function(req, res, next) {
  var { rows } = await db.query(sql_author_details, [req.params['authorId']]);
  if (rows.length > 0) {
    author_name = rows[0]['name'];
    author_id = rows[0]['author_id'];

    var { rows } = await db.query(sql_author_books, [req.params['authorId']]);
    books = rows;

    var { rows } = await db.query(sql_coauthors, [req.params['authorId']]);
    coauthors = rows;

    res.render('author', {
      title: 'The Bookworm',
      user: req.session.user ? req.session.user : null,
      author_id: author_id,
      author_name: author_name,
      coauthors: coauthors,
      books: books
    });
  } else {
    // render the error page
    res.status(404);
    res.render('error', {
      message: 'We are sorry, the book you are searching for could not be found.'
    });
  }
});


sql_category_details = 'SELECT * FROM "Categories" WHERE categories_id = $1';
sql_category_books =
  'SELECT * FROM "BookDetails" ' +
  'WHERE book_id in ( ' +
  'SELECT book_id FROM "BookCategories" WHERE category_id = $1 ' +
  ') ORDER BY title ASC';
/* GET book details page. */
router.get('/category/:categoryId(\\d+)/:categoryName', async function(req, res, next) {
  var { rows } = await db.query(sql_category_details, [req.params['categoryId']]);
  if (rows.length > 0) {
    category_name = rows[0]['name'];
    category_id = rows[0]['categories_id'];

    var { rows } = await db.query(sql_category_books, [req.params['categoryId']]);
    books = rows;

    res.render('book_list', {
      title: 'The Bookworm',
      user: req.session.user ? req.session.user : null,
      heading: 'Books in the <i>'+category_name+'</i> Category',
      books: books
    });
  } else {
    // render the error page
    res.status(404);
    res.render('error', {
      message: 'We are sorry, the book you are searching for could not be found.'
    });
  }
});

/* GET Search page. */
sql_search_title = 'SELECT * FROM public."BookDetails" WHERE title ILIKE $1';
router.get('/search', async function(req, res, next) {
  var books = [];
  if ('s' in req.query) {
    var searchTerm = '%' + req.query.s + '%';
    var { rows } = await db.query(sql_search_title, [searchTerm]);

    books = rows;
  }

  res.render('search', {
    title: 'The Bookworm Search Page',
    user: user.getUser(req.session),
    books: books,
    num_books: books.length,
    search_term: 's' in req.query ? req.query.s : null
  });
});

module.exports = router;
