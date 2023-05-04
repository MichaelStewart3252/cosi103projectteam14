const express = require('express');
const router = express.Router();
const User = require('../models/User');
const checkLoginStatus = require("../middlewares/checkLoginStatus");

const { Configuration, OpenAIApi } = require("openai");
// const configuration = new Configuration({
//     apiKey:user.APIKEY
// });
// // const configuration = new Configuration({apiKey: User.APIKEY});
// const openai = new OpenAIApi(configuration);


router.get('/prompt/Harry', 
  isLoggedIn, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Harry");  
});


router.post('/prompt/harrypost', checkLoginStatus, async (req, res) => {
  let course = req.body.course;  
  let prompt = `generate a recipe for ${course}`;
  const user = await User.findOne({username:req.session.username});
  const configuration = new Configuration({
    apiKey: user.APIKEY
  });
  const openai = new OpenAIApi(configuration);
  const completion = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: prompt,
    max_tokens: 1024,
    temperature: 0.8,  
  });
  console.log(completion);
  let response = completion.data.choices[0].text;
  res.locals.updated = false; 
  res.render('Harry', {response});
});

module.exports = router;




