/*
  This router defines the following routes
  /save (post)
  /change (get and post)
  /use (get)

  When the user logs in or signs in, 
  it adds their apikey to the req.session for use in the app.js controller
  and it sets the res.locals properties for use in the view
  res.locals.APIsaved
  res.local.APIKEY
*/

const express = require('express');
const router = express.Router();
// const bcrypt = require('bcrypt');
// const saltRounds = 10;
const checkLoginStatus = require('../checkLoginStatus');
const User = require('../models/User')


// this next route is also middleware that modifies the
// req and res objects for later routes to access.
// First, it checks the session variable: req.session
// if it has a apikey then it means the user has saved their apikey in
// and it can send the apikey to the views
// via res.locals.  It also adds the user to req.user
// so it can be accessed in two ways: res.locals.user or req.user
// if the user hasn't logged in (or has logged out),
// it sets the apikey to null just to be safe
//

router.use((req,res,next) => {
  if (req.session.APIKEY != null) {
    console.log("apikey found in session:", req.session.APIKEY)
    res.locals.APIsaved = true
    res.locals.APIKEY = req.session.APIKEY
  } else {
    res.locals.APIsaved = false
    res.locals.APIKEY = null
  }
  next()
})

// when a user signed in and want to save their apikey
// it adds them to the User model and redirects to route
// as an apisaved user.
router.post('/save',
  checkLoginStatus,
  async (req,res,next) =>{
    try {
      const {apikey,apikey2} = req.body
      if (apikey != apikey2){
        res.redirect('/')
      }else {
          User.findOneAndUpdate({username:req.session.username}, { APIKEY: apikey })
            .then((updatedUser) => {
                console.log("apikey added successfully:", updatedUser);
            })
            .catch((error) => {
                console.error("Error adding apikey:", error);
            });
            
          res.locals.APIsaved = true
          res.locals.APIKEY = apikey
          req.session.APIKEY = apikey
          res.redirect('/')
        }

    }catch(e){
      next(e)
    }
  })



router.checkLoginStatus = checkLoginStatus;


module.exports = router;
