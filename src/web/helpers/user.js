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

// Set this to true, if you want to always be logged in as a debug user
always_logged_in = false;



module.exports = {
  getUser: (session) => {
    if (always_logged_in === true) {
      return debug_user;
    }
    if (session.user) {
      return session.user;
    } else {
      return null;
    }
  }
};
