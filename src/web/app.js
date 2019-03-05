var createError = require('http-errors');
var express = require('express');
var session = require('express-session');
var exphbs = require('express-handlebars');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var accountRouter = require('./routes/account');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));

app.engine(
  'hbs',
  exphbs({
    defaultLayout: path.join(__dirname, 'views/layouts/layout.hbs'),
    extname: '.hbs',
    helpers: require(path.join(__dirname, './helpers/helpers.js')) // same file that gets used on our client
  })
);
app.set('view engine', 'hbs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(
  session({
    secret: 'Z7XdYxII3sznMAsfmgdAGNCUsufbSHLqZHX6adNN3atgNDVCTlukt8Cw1ZQk',
    cookie: { maxAge: 60000 },
    resave: false,
    saveUninitialized: true
  })
);

app.use('/', indexRouter);
app.use('/account', accountRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  if (req.originalUrl.startsWith('/images/book_covers/')) {
    res.redirect('/images/book_cover_placeholder.png');
  } else if (req.originalUrl.startsWith('/images/authors/')) {
    res.redirect('/images/author_placeholder.png');
  } else {
    // render the error page
    res.status(err.status || 500);
    res.render('error');
  }
});

module.exports = app;
