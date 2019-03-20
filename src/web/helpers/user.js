debug_user = {
  user_id: 0,
  display_name: 'Debug User',
  email: 'debuug@thebookworm.com',
  password_hash: '$2b$10$AMucDjhYc1I.TWtHUCudb.mcwh5AIkrUQfFyD/wKJ1JqPq6.J6RO.',
  creation_time: '2019-02-21 18:27:36.3877',
  preferences_json: '{}',
  created_from: 'DEBUG',
  login_allowed: 0
};
jon_user = {
  user_id: 1,
  display_name: 'Jonathan Shahen',
  email: 'debuug@thebookworm.com',
  password_hash: '$2b$10$AMucDjhYc1I.TWtHUCudb.mcwh5AIkrUQfFyD/wKJ1JqPq6.J6RO.',
  creation_time: '2019-02-21 18:27:36.3877',
  preferences_json: '{}',
  created_from: 'Web Signin Page',
  login_allowed: 1
};

// Set this to a user, if you want to always be logged in as a debug user
var always_logged_in_user = null;//jon_user;



module.exports = {
  getUser: (session) => {
    if (always_logged_in_user) {
      return always_logged_in_user;
    }
    if (session.user) {
      return session.user;
    } else {
      return null;
    }
  }
};
