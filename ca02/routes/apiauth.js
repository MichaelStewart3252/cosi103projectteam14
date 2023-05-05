/*
  This router defines the following routes
  /save (post)
  /change (get and post)
  /use (get)
  /delete (get)

  When the user logs in or signs in, 
  it adds their apikey to the req.session for use in the app.js controller
  and it sets the res.locals properties for use in the view
  res.locals.APIsaved
  res.local.APIKEY
*/

const express = require('express');
const router = express.Router();
const { Configuration, OpenAIApi } = require("openai");

const checkLoginStatus = require('../middlewares/checkLoginStatus');
const User = require('../models/User')



router.use( async (req,res,next) => {

  await User.findOne({username:req.session.username})
  .then((user) => {
    if(user == null){
      next()
    }else{
      if (user.APIKEY != null) {
        console.log("apikey found in db:", user.APIKEY)
        res.locals.APIsaved = true
      } else {
        res.locals.APIsaved = false
        console.log("apikey not found in db")
                                               
      }
      next()
    }
  })
  .catch((error) => {
    console.log('Error finding user:', error);
  
  }
  );
})

// when a user signed in and want to save their apikey
// it adds them to the User model and redirects to route
// as an apisaved user.
router.post('/save',
  checkLoginStatus,
  async (req,res,next) =>{
    try {
      const {apikey,apikey2} = req.body
      if (apikey != apikey2){
        console.log('api keys do not match')
        res.redirect('/')
      }else {
          try{
            const configuration = new Configuration({
              apiKey: apikey
            });
        
            const openai = new OpenAIApi(configuration);
          
   
            // this checks if the apikey is valid by making a request to openai
            await openai.createCompletion({
              model: "text-davinci-003",
              prompt: 'check api key',
              max_tokens: 1024,
              temperature: 0.8,  
            });
            // if the apikey is valie it adds it to the user model
            await User.findOneAndUpdate({username:req.session.username}, { APIKEY: apikey }, {new: true})


            req.session.APIKEY = apikey
            res.locals.APIsaved = true 
            // res.locals.APIKEY = apikey
      
            res.redirect('/?invalidKey=false')

          }catch(error){
            console.log('error message', error)
            // console.error(error.response.data.error)
            res.redirect('/?invalidKey=true')
          }
        }
    }catch(e){
      next(e)
    }
  })

router.get('/deleteAPIKEY', checkLoginStatus, async (req,res,next) =>{  
  User.findOneAndUpdate({username:req.session.username}, { APIKEY: null }, {new: true})
  .then((updatedUser) => {
    console.log('apikey deleted successfully:', updatedUser);
  })
  .catch((error) => {
    console.log('Error deleting apikey:', error);
  });
  res.locals.APIsaved = false
  req.session.APIKEY = null
  res.redirect('/')
})

router.checkLoginStatus = checkLoginStatus;


module.exports = router;
