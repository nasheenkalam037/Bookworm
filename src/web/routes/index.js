var express = require("express");
var session = require('express-session')
var router = express.Router();
const db = require("../db");


my_book = {
  title: "The perks of Being A Wallflower",
  book_cover: '/images/book_cover_placeholder.png',
  authors: ["Stephen Chbosky"],
  synopsis: "I am the synopsis text, text, text, text, text, text "
};
my_deal = {
  image_class: "fab fa-amazon",
  rating: "4/5",
  link_to_buy: "#"
};
my_book_long = {
  title: "The perks of Being A Wallflower",
  book_cover: '/images/book_cover_placeholder.png',
  authors: ["Stephen Chbosky"],
  synopsis: "I am the synopsis text, text, text, text, text, text ",
  deals: [my_deal, my_deal, my_deal]
};
dummy_data = {
  title: "The Bookworm",
  user: undefined,
  bookoftheday: my_book,
  books: [my_book_long, my_book_long, my_book_long, my_book_long],
  recommendations: [my_book, my_book, my_book, my_book]
};

sql_top_books_landing = 'SELECT * FROM "BookDetails" ORDER BY amazon_rating DESC NULLS LAST LIMIT 15';

/* GET home page. */
router.get("/", async function(req, res, next) {
  // Variable has to be named 'rows'
  var {rows} = await db.query(sql_top_books_landing);

  console.log(rows);

  res.render("index", {
    title: "The Bookworm",
    user: (req.session.user)? req.session.user : null,
    bookoftheday: my_book,
    books: rows,
    recommendations: [my_book, my_book, my_book, my_book]
  });
});


module.exports = router;
