var express = require('express');
var router = express.Router();
const db = require('../db');
const user = require('../helpers/user');

sql_book_details = 'SELECT * FROM "Books" WHERE book_id = $1 LIMIT 1';
sql_book_authors =
  'SELECT * FROM "Author" as a INNER JOIN "AuthorBooks" ab on ' + 'a.author_id = ab.author_id WHERE ab.book_id = $1';
sql_book_categories =
  'SELECT * FROM "Categories" as c INNER JOIN "BookCategories" bc on ' +
  'c.categories_id = bc.category_id WHERE bc.book_id = $1 ORDER BY category_id ASC';
sql_book_reviews =
  'SELECT r.*, u.display_name FROM "Reviews" as r ' +
  'inner join "Users" u on u.user_id = r.user_id ' +
  'where r.book_id = $1 ORDER BY date_created DESC';

async function getBook(bookId) {
  var { rows } = await db.query(sql_book_details, [bookId]);
  if (rows.length == 1) {
    book = rows[0];
    var authors = await db.query(sql_book_authors, [bookId]);
    var categories = await db.query(sql_book_categories, [bookId]);
    var reviews = await db.query(sql_book_reviews, [bookId]);
    book['authors'] = authors.rows;
    book['categories'] = categories.rows;
    book['reviews'] = reviews.rows;
  } else {
    book = null;
  }
  return book;
}

/* GET book details page. */
router.get('/:bookId(\\d+)/:bookTitle', async function(req, res, next) {
  var book = await getBook(req.params['bookId']);
  if (book) {
    res.render('details', {
      title: 'The Bookworm',
      user: user.getUser(req.session),
      book: book
    });
  } else {
    // render the error page
    res.status(404);
    res.render('error', {
      message: 'We are sorry, the book you are searching for could not be found.'
    });
  }
});

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

sql_insert_review =
  'INSERT INTO public."Reviews"(book_id, user_id, rating, review) VALUES ($1, $2, $3, $4) RETURNING *';
/**
 * Checks each of the parameters for the correct type, and then tries to save the new review
 * @param {int} bookId
 * @param {int} user_id
 * @param {float} rating
 * @param {text} review_comment
 */
async function saveReview(bookId, user_id, rating, review_comment) {
  bookId = parseInt(bookId);
  user_id = parseInt(user_id);
  rating = parseFloat(rating);
  if (Number.isInteger(bookId) && Number.isInteger(user_id) && Number.isInteger(rating)) {
    if (bookId >= 0 && user_id >= 0 && rating >= 0.0 && rating <= 5.0) {
      try {
        var { rows } = await db.query(sql_insert_review, [bookId, user_id, rating, review_comment]);
        console.log(rows);

        if (rows.length == 1) {
          return rows[0];
        }
      } catch (error) {
        console.error('Error when trying to save the review:', error);
        return false;
      }
    }
  }
  return false;
}

router.post('/:bookId(\\d+)/:bookTitle', async function(req, res, next) {
  var book = await getBook(req.params['bookId']);
  if (book) {
    var myuser = user.getUser(req.session);
    var success = false;
    var p = req.body;

    if (myuser && 'book_id' in p && 'review_comment' in p && 'rating' in p) {
      if (p.book_id == req.params['bookId']) {
        success = await saveReview(req.params['bookId'], myuser.user_id, p.rating, p.review_comment);
      } else {
        console.error('The hidden book id does not match the requested book id', p, req.params);
      }
    } else {
      console.error('Inproperly formed POST request to submit a review: (user, body of POST)', user, p);
    }

    res.render('details', {
      title: 'The Bookworm',
      user: user.getUser(req.session),
      book: book,
      submitted_review: true,
      success: success ? true : undefined
    });
  } else {
    // render the error page
    res.status(404);
    res.render('error', {
      message: 'We are sorry, the book you are searching for could not be found.'
    });
  }
});

module.exports = router;
