const express = require('express');
const router = express.Router();
const User = require('../models/User');
const checkLoginStatus = require("../middlewares/checkLoginStatus");

const { Configuration, OpenAIApi } = require("openai");
// const configuration = new Configuration({
//     apiKey: "",
// });
// const configuration = new Configuration({apiKey: User.APIKEY});
// const openai = new OpenAIApi(configuration);


router.get('/prompt/Eric', 
  isLoggedIn, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Eric");  
});


router.post('/prompt/ericpost', checkLoginStatus, async (req, res) => {
  let date = req.body.date;  
  let prompt = `Enter the president you're wanting to know the birthday for ${date}`;
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
  res.render('Eric', {response});
});

module.exports = router;