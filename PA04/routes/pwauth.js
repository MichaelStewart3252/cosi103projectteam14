/*
  auth.js uses bcrypt and salt to encode passwords ...

  This router defines the following routes
  /signin (post)
  /login (get and post)
  /logout (get)

  When the user logs in or signs in, 
  it adds their user name and user object to the req.session for use in the app.js controller
  and it sets the res.locals properties for use in the view
  res.locals.loggedIn
  res.local.username
  res.locals.user
*/

const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const saltRounds = 10;
const User = require('../models/User')



// This is an example of middleware
// where we look at a request and print it on the console
// before continuing on with other steps!
router.use(function(req, res, next) {
  console.log(`${req.method} ${req.url} ${new Date()}`);
  next();
});

// this next route is also middleware that modifies the
// req and res objects for later routes to access.
// First, it checks the session variable: req.session
// if it has a username then it means the user has logged in
// and it can send the username and user object to the views
// via res.locals.  It also adds the user to req.user
// so it can be accessed in two ways: res.locals.user or req.user
// if the user hasn't logged in (or has logged out),
// it sets the user and username to null just to be safe
//
router.use((req,res,next) => {
  if (req.session.username) {
    res.locals.loggedIn = true
    res.locals.username = req.session.username
    res.locals.user = req.session.user
    req.user = req.session.user
  } else {
    res.locals.loggedIn = false
    res.locals.username = null
    res.locals.user = null
    req.user = null
  }
  next()
})


router.get("/login", (req,res) => {
  res.render("pwlogin")
})

// this handles the login form data
// it checks gets the username and passphrase from the form
// then it looks up the user with that username (if any)
// the user object stores a heavily encrypted version of the passphrase
// if the passphrase from the form has the same encryption, then
// the user has been authenticated
router.post('/login',
  async (req,res,next) => {
    try {
      const {username,passphrase} = req.body
      const user = await User.findOne({username:username})
      const isMatch = await bcrypt.compare(passphrase,user.passphrase );

      if (isMatch) {
        req.session.username = username //req.body
        req.session.user = user
        res.redirect('/')
      } else {
        console.log('incorrect username or passphrase ')
        req.session.username = null
        req.session.user = null
        res.redirect('/login')
      }
    }catch(e){
      next(e)
    }
  })

// when a user signs up it encrypts their password
// with multiple salted rounds (look it up!)
// and if the username has not already been claimed
// it adds them to the User model and redirects to route
// as an authenticated user.
router.post('/signup',
  async (req,res,next) =>{
    try {
      // here we use destructuring to get fields from req.body
      const {username,passphrase,passphrase2,age} = req.body
      if (passphrase != passphrase2){
        res.redirect('/login')
      }else {
        const encrypted = await bcrypt.hash(passphrase, saltRounds);

        // check to make sure that username is not already taken!!
        const duplicates = await User.find({username})
        
        if (duplicates.length>0){
          // it would be better to render a page with an error message instead of this plain text response
          res.send("username has already been taken, please go back and try another username")
        }else {
          // the username has not been taken so create a new user and store it in the database
          const user = new User(
            {username:username,
             passphrase:encrypted,
             age:age
            })
          
          await user.save()
          req.session.username = user.username
          req.session.user = user
          res.redirect('/')
        }
        
        
      }
    }catch(e){
      next(e)
    }
  })

router.get('/logout', (req,res) => {
  req.session.destroy()
  res.redirect('/');
})

// route middleware to make sure a user is logged in
function isLoggedIn(req, res, next) {
    if (res.locals.loggedIn){
      return next();
    } else {
      res.redirect('/login');
    }
}

router.isLoggedIn = isLoggedIn;


module.exports = router;
