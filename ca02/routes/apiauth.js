/*
  This router defines the following routes
  /save (post)
  /change (get and post)
  /use (get)

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



router.use((req,res,next) => {
  if (req.session.APIKEY != null) {
    console.log("apikey found in session:", req.session.APIKEY)
    res.locals.APIsaved = true

    // res.locals.APIKEY = req.session.APIKEY
  } else {
    res.locals.APIsaved = false

    // res.locals.APIKEY = null                                                  
  }

  next()
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
        res.redirect('/')
      }else {
          User.findOneAndUpdate({username:req.session.username}, { APIKEY: apikey }, {new: true})
            .then(async (updatedUser) => {
                const configuration = new Configuration({
                  apiKey: updatedUser.APIKEY
                });
           
                const openai = new OpenAIApi(configuration);
             
                console.log('before', openai)
                // this checks if the apikey is valid by making a request to openai
                await openai.createCompletion({
                  model: "text-davinci-003",
                  prompt: 'check api key',
                  max_tokens: 1024,
                  temperature: 0.8,  
                });

                req.session.APIKEY = apikey
                res.locals.APIsaved = true
                // res.locals.APIKEY = apikey
          
                
                console.log("apikey added successfully:", updatedUser); 
                res.redirect('/')
                
            })
            .catch((error) => {
                console.error( error.response.data.error)
                res.redirect('/?invalidKey=true')
            });
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
