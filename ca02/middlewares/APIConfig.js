
const { Configuration, OpenAIApi } = require("openai");
const User = require('../models/User');

module.exports = {
  generateResponse: async (req, res, prompt) => {

    const user = await User.findOne({username:req.session.username});
    const configuration = new Configuration({
      apiKey: user.APIKEY
    });
    const openai = new OpenAIApi(configuration);
    try{
        const openai = new OpenAIApi(configuration);
        const completion = await openai.createCompletion({
          model: "text-davinci-003",
          prompt: prompt,
          max_tokens: 1024,
          temperature: 0.8,  
        });
        // console.log(completion);
        let response = completion.data.choices[0].text;
        return response

      }catch(error){
        console.error('incorrect api key');
        res.render('/')
      }
}
  
}
