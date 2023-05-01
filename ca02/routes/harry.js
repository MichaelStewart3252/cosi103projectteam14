const express = require('express');
const router = express.Router();
const User = require('../models/User')

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: "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",
});
// const configuration = new Configuration({apiKey: User.APIKEY});
const openai = new OpenAIApi(configuration);


isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

router.get('/prompt/Harry', 
  isLoggedIn, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("promptHarry");  
});


router.post('/prompt/post', isLoggedIn, async (req, res) => {
  let course = req.body.course;  
  let prompt = `generate a recipe for ${course}`;
  const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: prompt,
    max_tokens: 1024,
    temperature: 0.8,  
  });
  console.log(completion);
  let response = completion.data.choices[0].text;
  res.locals.updated = false; 
  res.render('promptHarry', {response});
});
module.exports = router;




