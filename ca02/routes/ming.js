const express = require('express');
const router = express.Router();

const checkLoginStatus = require("../middlewares/checkLoginStatus");
const { generateResponse } = require("../middlewares/APIConfig");

router.get('/prompt/Ming', 
  checkLoginStatus, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Ming");  
});


router.post('/prompt/ming/post', checkLoginStatus, async (req, res) => {
  let input = req.body.input;  
  let prompt = `which nba player has the most ${input}?`;
  try{
    const response = await generateResponse(req, res, prompt, input);
    res.locals.updated = false; 
    res.render('Ming', {response});
  }catch{
    res.render('Ming')
  }
});
module.exports = router;


