
const { Configuration, OpenAIApi } = require("openai");
const User = require('../models/User');
const ApiRequest = require('../models/apiRequest');

module.exports = {
  generateResponse: async (req, res, prompt, input) => {

    const user = await User.findOne({username:req.session.username});
    const configuration = new Configuration({
      apiKey: user.APIKEY
    });
    try{
        const openai = new OpenAIApi(configuration);
        const completion = await openai.createCompletion({
          model: "text-davinci-003",
          prompt: prompt,
          max_tokens: 1024,
          temperature: 0.8,  
        });
        // console.log(completion);
        const response = completion.data.choices[0].text;
        try{
          const apiRequest = new ApiRequest(
            {
              timestamp: Date.now(),
              input: input,
              prompt: prompt,
              response: response,
              userId: req.session.user._id
            });
          await apiRequest.save();
          console.log('saved response in database')
        }catch(error){
          console.dir(error)
          console.error('could not save save response in database');
        }
        return response

      }catch(error){
        console.error( error.response.data.error)
        // console.error('incorrect api key');
        throw new Error('incorrect api key');
      }
}
  
}
