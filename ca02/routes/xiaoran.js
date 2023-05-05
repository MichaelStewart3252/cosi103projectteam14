const express = require('express');
const router = express.Router();

const checkLoginStatus = require("../middlewares/checkLoginStatus");
const { generateResponse } = require("../middlewares/APIConfig");


router.get('/prompt/Xiaoran', 
  checkLoginStatus, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Xiaoran");  
});


router.post('/prompt/xiaoran/post', checkLoginStatus, async (req, res) => {
  let date = req.body.date;  
  let prompt = `what day to celebrate on ${date}?`;
  try{
    const response = await generateResponse(req, res, prompt, date);
    res.locals.updated = false; 
    res.render('Xiaoran', {response});
  }catch{
    res.render('/')
  }
});
module.exports = router;


