/*
  transaction.js -- Router for transaction in views
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User')


isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}


router.post('/prompt',
  isLoggedIn,
  async (req, res, next) => {
    const show = req.query.show
    res.render('prompt');
});

router.get('/prompt', isLoggedIn, async (req, res, next) => {
    const show = req.query.show;
    if (show === 'Michael') {
   
        
    } else if (show === 'sortByAmount') {
      
    } else if (show === 'sortByDescription') {
      
  
    
    } else if (show === 'sortByDate') {
     
    }
    
  });

module.exports = router;