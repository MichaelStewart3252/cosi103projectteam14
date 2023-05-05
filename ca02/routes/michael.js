const express = require('express');
const router = express.Router();
const User = require('../models/User');
const ApiRequest = require('../models/apiRequest');
const checkLoginStatus = require("../middlewares/checkLoginStatus");

const { Configuration, OpenAIApi } = require("openai");
// const configuration = new Configuration({
//     apiKey: "",
// });
// // const configuration = new Configuration({apiKey: User.APIKEY});
// const openai = new OpenAIApi(configuration);


router.get('/prompt/Michael', 
  checkLoginStatus, 
  async (req, res) => {  
    res.locals.updated = true;
    res.render("Michael");  
});


router.post('/prompt/michael/post', checkLoginStatus, async (req, res) => {
  let ds = req.body.ds;  
  let prompt = `Tell me about the computer data structure ${ds}?`;
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
    const apiRequest = new ApiRequest(
      {
        timestamp: Date.now(),
        input: ds,
        prompt: prompt,
        response: response,
        userId: req.session.user._id
      });
  await apiRequest.save();
  res.render('Michael', {response});
});
module.exports = router;


