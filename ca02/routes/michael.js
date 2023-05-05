const express = require('express');
const router = express.Router();
const checkLoginStatus = require("../middlewares/checkLoginStatus");
const { generateResponse } = require("../middlewares/APIConfig");


router.get('/prompt/Michael', 
  checkLoginStatus, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Michael");  
});


router.post('/prompt/michael/post', checkLoginStatus, async (req, res) => {
  let ds = req.body.ds;  
  let prompt = `Tell me about the computer data structure ${ds}?`;
  try{
    const response = await generateResponse(req, res, prompt, ds);
    res.locals.updated = false; 
    res.render('Michael', {response});
  }catch{
    res.render('/')
  }

});
module.exports = router;


