var express = require("express");
var router = express.Router();
const db = require("../db");

my_user = {
  name: 'Jon',
  id: '1',
  image: '/images/headshot_placeholder.png'
};
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
  user: my_user,
  bookoftheday: my_book,
  books: [my_book_long, my_book_long, my_book_long, my_book_long],
  recommendations: [my_book, my_book, my_book, my_book]
};


/* GET home page. */
router.get("/", function(req, res, next) {
  res.render("index", dummy_data);
});
/* GET Sign Up page. */
router.get("/signup", function(req, res, next) {
  res.render("signup", {
    title: 'The Bookworm Signup Page'
  });
});
/* GET Sign In page. */
router.get("/signin", function(req, res, next) {
  res.render("signin", {
    title: 'The Bookworm Signin Page'
  });
});
/* GET book details page. */
router.get("/details", function(req, res, next) {
  res.render("details", dummy_data);
});

module.exports = router;
