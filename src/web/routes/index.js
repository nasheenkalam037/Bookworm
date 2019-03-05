var express = require('express');
var session = require('express-session');
var router = express.Router();
const db = require('../db');

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

sql_top_books_landing =
  'SELECT * FROM "BookDetails" ORDER BY amazon_rating DESC NULLS LAST LIMIT 15';

/* GET home page. */
router.get('/', async function(req, res, next) {
  // Variable has to be named 'rows'
  var { rows } = await db.query(sql_top_books_landing);

  console.log(rows);

  res.render('index', {
    title: 'The Bookworm',
    user: req.session.user ? req.session.user : null,
    bookoftheday: my_book,
    books: rows,
    recommendations: [my_book, my_book, my_book, my_book]
  });
});

sql_book_details = 'SELECT * FROM "Books" WHERE book_id = $1 LIMIT 1';
sql_book_authors =
  'SELECT * FROM "Author" as a INNER JOIN "AuthorBooks" ab on ' +
  'a.author_id = ab.author_id WHERE ab.book_id = $1';
sql_book_categories =
  'SELECT * FROM "Categories" as c INNER JOIN "BookCategories" bc on ' +
  'c.categories_id = bc.category_id WHERE bc.book_id = $1 ORDER BY category_id ASC';
/* GET book details page. */
router.get('/book/:bookId(\\d+)/:bookTitle', async function(req, res, next) {
  var { rows } = await db.query(sql_book_details, [req.params['bookId']]);
  if (rows.length == 1) {
    book = rows[0];
    var { rows } = await db.query(sql_book_authors, [req.params['bookId']]);
    book['authors'] = rows;
    var { rows } = await db.query(sql_book_categories, [req.params['bookId']]);
    book['categories'] = rows;

    res.render('details', {
      title: 'The Bookworm',
      user: req.session.user ? req.session.user : null,
      book: book
    });
  } else {
    // render the error page
    res.status(404);
    res.render('error', {
      message:
        'We are sorry, the book you are searching for could not be found.'
    });
  }
});


sql_author_details = 'SELECT * FROM "Author" WHERE author_id = $1';
sql_author_books =
  'SELECT * FROM "BookDetails" ' +
  'WHERE book_id in ( '+
  'SELECT book_id FROM "AuthorBooks" WHERE author_id = $1 ' +
  ') ORDER BY book_id ASC';
sql_coauthors =
  'SELECT distinct a.* FROM "Author" as a ' +
  'INNER JOIN "AuthorBooks" ab on a.author_id = ab.author_id ' +
  'WHERE ab.book_id in ( ' +
  'SELECT book_id FROM "AuthorBooks" WHERE author_id = $1 ' +
  ') AND ab.author_id != $1';
/* GET book details page. */
router.get('/author/:authorId(\\d+)/:authorName', async function(
  req,
  res,
  next
) {
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
      message:
        'We are sorry, the book you are searching for could not be found.'
    });
  }
});

/* GET Search page. */
router.get('/search', function(req, res, next) {
  res.render('search', {
    title: 'The Bookworm Search Page',
    user: req.session.user ? req.session.user : null,
    books: [my_book, my_book]
  });
});

module.exports = router;
