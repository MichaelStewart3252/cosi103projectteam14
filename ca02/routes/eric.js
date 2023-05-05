const express = require('express');
const router = express.Router();

const checkLoginStatus = require("../middlewares/checkLoginStatus");
const { generateResponse } = require("../middlewares/APIConfig");


router.get('/prompt/Eric', 
  isLoggedIn, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Eric");  
});


router.post('/prompt/ericpost', checkLoginStatus, async (req, res) => {
  let date = req.body.date;  
  let prompt = `Enter the president you're wanting to know the birthday for ${date}`;
  try{
    const response = await generateResponse(req, res, prompt, date);
    res.locals.updated = false; 
    res.render('Eric', {response});
  }catch{
    res.render('/')
  }
});

module.exports = router;