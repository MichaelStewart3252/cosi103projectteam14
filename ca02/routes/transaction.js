/*
  transaction.js -- Router for transaction in views
*/
const express = require('express');
const router = express.Router();
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
    const records = await Transaction.find({userId:req.user._id}).lean();
    res.render('showTransaction', {records, show});
});


router.get('/sortBy', isLoggedIn, async (req, res, next) => {
  const show = req.query.show;
  if (show === 'sortByCategory') {
    let records = 
    await Transaction.find({userId:req.user._id}).sort({category: 1})
    res.render("sortByCategory", {records})
      
  } else if (show === 'sortByAmount') {
    let records =
    await Transaction.find({userId:req.user._id}).sort({amount: -1})
    res.render("sortByAmount", {records})

  } else if (show === 'sortByDescription') {
    let records = 
    await Transaction.find({userId:req.user._id}).sort({description: 1})
    res.render("sortByDescription", {records})

  
  } else if (show === 'sortByDate') {
    let records = 
      await Transaction.find({userId:req.user._id}).sort({date:-1})
      res.render("sortByDate", {records})
  }
  
});

/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const date = new Date(req.body.date).toDateString();
      console.log(date)
      const transaction = new Transaction(
        {
          description: req.body.description,
          amount: req.body.amount,
          category: req.body.category,
          date:  date,
          userId: req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});

router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
    console.log("inside /transaction/remove/:itemId")
    await Transaction.deleteOne({_id:req.params.itemId});
    res.redirect('/transaction')
});

router.get('/transaction/editTransaction/:itemId',
  isLoggedIn,
  async (req, res, next) => {
    console.log("inside /transaction/editTransaction/:itemId")
    const item = 
     await Transaction.findById(req.params.itemId);
    res.locals.item = item
    res.locals.updated = true;
    res.render('editTransaction')
});


router.post('/transaction/updateTransaction',
isLoggedIn,
async (req, res, next) => {

  const {description, amount, category, date, itemId} = req.body;
  const updateData = {
    description: description, 
    amount: amount,
    category: category,
    dateFormatted: date
  }

  await Transaction.findByIdAndUpdate(itemId, updateData, { new: true })
  .then(() => {
    res.locals.updated = false;
    console.log('item updated!')
    res.render('editTransaction');
  })

});

router.get('/transaction/byCategory',
  isLoggedIn,
  async (req, res, next) => {
    let records = 
          await Transaction.aggregate([
            { $match: { userId: req.user._id } },            
            {$group: {               
                _id: '$category',
                total: { $sum: '$amount' }
                }},
              {$sort: {total: -1,}},
            
            ])
 
      res.render('byCategory', {records});
});


module.exports = router;