var express = require("express");
var session = require("express-session");
var router = express.Router();
const db = require("../db");

// SECURITY SETTINGS
const bcrypt = require("bcrypt");
const saltRounds = 10;
// SECURITY SETTINGS

/* GET Sign Up page. */
router.get("/signup", function(req, res, next) {
  res.render("signup", {
    title: "The Bookworm Signup Page",
    user: (req.session.user)? req.session.user : null
  });
});
/* GET Sign In page. */
router.get("/signin", function(req, res, next) {
  res.render("signin", {
    title: "The Bookworm Signin Page",
    user: (req.session.user)? req.session.user : null
  });
});
/* GET Sign In page. */
router.get("/signout", function(req, res, next) {
  console.log("[SIGNOUT] session:", req.session);
  if(req.session.user) {
    req.session.user = null;
  }
  res.redirect('/');
});

// Public account
router.get("/:userId(\d+)", function(req, res, next) {
  res.render("public_account", {
    title: "The Bookworm Signin Page",
    user: (req.session.user)? req.session.user : null
  });
});
// Private account
router.get("/me", function(req, res, next) {
  res.render("private_account", {
    title: "The Bookworm Signin Page",
    user: (req.session.user)? req.session.user : null
  });
});

///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////

const sql_insert_new_user = `
INSERT INTO public."Users"(
	display_name, email, password_hash, created_from, login_allowed)
	VALUES ($1, $2, $3, 'Website Signin Page', 1) RETURNING *;
`;

router.post("/signup", async function(req, res, next) {
  var error = undefined;
  var p = req.body;
  if (
    "fullname" in p &&
    "email" in p &&
    "password" in p &&
    "confirmation_password" in p
  ) {
    if (p.fullname.length > 1 && p.email.length > 1 && p.password.length > 1) {
      if (p.password == p.confirmation_password) {
        var hash = bcrypt.hashSync(p.password, saltRounds);

        try {
          var { rows } = await db.query(sql_insert_new_user, [
            p.fullname,
            p.email,
            hash
          ]);

          console.log(rows);

          if (rows.length == 1) {
            req.session.user = rows[0];
          }else{
            error = "Unable to add user to table";
          }
        } catch (e) {
          error =
            "Duplicate Email found in table, did you forget your password?";
        }
      } else {
        error = "Passwords do not match";
      }
    } else {
      error = "All fields must have length greater than 1";
    }
  } else {
    error = "Not All Variables given in request";
  }

  console.log("[SIGNUP] error:", error);

  if (error) {
    // failed, show same page
    res.render("signup", {
      title: "The Bookworm Signup Page",
      error: error
    });
  } else {
    // success
    res.redirect("/");
  }
});

const sql_select_user = 'SELECT * FROM public."Users" WHERE email = $1;';
router.post("/signin", async function(req, res, next) {
  var error = undefined;
  var p = req.body;
  if ("email" in p && "password" in p) {
    if (p.email.length > 1 && p.password.length > 1) {
      try {
        var { rows } = await db.query(sql_select_user, [p.email]);
        console.log(rows);
        if (rows.length == 1) {
          if (bcrypt.compareSync(p.password, rows[0].password_hash) == true) {
            req.session.user = rows[0];
          }else{
            // wrong password
            error = "Incorrect email/password combination";
          }
        } else {
          error = "Incorrect email/password combination";
        }
      } catch (e) {
        error = "Unknown error occurred";
        console.error('Signin Error:', e);
      }
    } else {
      error = "All fields must have length greater than 1";
    }
  } else {
    error = "Not All Variables given in request";
  }

  console.log("[SIGNIN] error:", error);
  console.log("[SIGNIN] session:", res.session);

  if (error) {
    // failed, show same page
    res.render("signin", {
      title: "The Bookworm Signup Page",
      error: error
    });
  } else {
    // success
    res.redirect("/");
  }
});

module.exports = router;
