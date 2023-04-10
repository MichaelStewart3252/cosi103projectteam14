/*
  transaction.js -- Router for transaction in views
*/
const express = require('express');
const router = express.Router();
const ToDoItem = require('../models/ToDoItem')
const Transaction = require('../models/Transaction')
const User = require('../models/User')


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}


router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
    const show = req.query.show;
    const records = await Transaction.find().lean();
    for (let i = 0; i < records.length; i++) {
      const record = records[i];
      record.dateFormatted = new Date(record.date).toLocaleDateString();
    }
    res.render('showTransaction', {records, show});
});


router.get('/sortBy/', isLoggedIn, async (req, res, next) => {
  const show = req.query.show;
  let records = [];
  if (show === 'sortByCategory') {
    
  } else if (show === 'sortByAmount') {
    
  } else if (show === 'sortByDescription') {
    
  } else if (show === 'sortByDate') {
    
  }
  
  res.render('showTransaction', { records, show });
});

/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const createdAt = new Date(req.body.createdAt).toLocaleDateString();
      const transaction = new Transaction(
        {
          description: req.body.description,
          amount: req.body.amount,
          category: req.body.category,
          createdAt: new Date(createdAt),
          userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});

router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      
});


router.get('/transaction/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
     
});


router.post('/transaction/updateTransaction/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      
});


router.get('/transaction/byCategory',
  isLoggedIn,
  async (req, res, next) => {
    
});

module.exports = router;
