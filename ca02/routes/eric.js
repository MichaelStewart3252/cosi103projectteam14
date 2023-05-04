const express = require('express');
const router = express.Router();
const User = require('../models/User');
const checkLoginStatus = require("../checkLoginStatus");

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: "",
});
// const configuration = new Configuration({apiKey: User.APIKEY});
const openai = new OpenAIApi(configuration);


router.get('/prompt/Eric', 
  isLoggedIn, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("promptEric");  
});


router.post('/prompt/ericpost', checkLoginStatus, async (req, res) => {
  let date = req.body.course;  
  let prompt = `Enter the president you're wanting to know the birthday for ${date}`;
  const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: prompt,
    max_tokens: 1024,
    temperature: 0.8,  
  });
  console.log(completion);
  let response = completion.data.choices[0].text;
  res.locals.updated = false; 
  res.render('promptEric', {response});
});
module.exports = router;
