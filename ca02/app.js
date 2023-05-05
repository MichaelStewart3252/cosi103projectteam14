const createError = require('http-errors');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const layouts = require("express-ejs-layouts");
const api_auth_router = require('./routes/apiauth');
const pw_auth_router = require('./routes/pwauth');
const promptRouter = require('./routes/prompt');
const harryRouter = require('./routes/harry');
const xiaoranRouter = require('./routes/xiaoran');
const ericRouter = require('./routes/eric');
const michaelRouter = require('./routes/michael');
const mingRouter = require('./routes/ming');

const checkLoginStatus = require('./middlewares/checkLoginStatus');


/* **************************************** */
/*  Connecting to a Mongo Database Server   */
/* **************************************** */
const mongodb_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/pwdemo';
console.log('MONGODB_URI=', mongodb_URI);

const mongoose = require( 'mongoose' );

mongoose.set('strictQuery', true);

mongoose.connect( mongodb_URI);

const db = mongoose.connection;


db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log("we are connected!!!")
});



/* **************************************** */
/* Enable sessions and storing session data in the database */
/* **************************************** */
const session = require("express-session"); // to handle sessions using cookies 
var MongoDBStore = require('connect-mongodb-session')(session);

const store = new MongoDBStore({
  uri: mongodb_URI,
  collection: 'mySessions'
});

// Catch errors                                                                      
store.on('error', function(error) {
  console.log(error);
});



/* **************************************** */
/* creating the app */
/* **************************************** */
var app = express();

app.use(session({
  secret: 'This is a secret',
  cookie: {
    maxAge: 1000 * 60 * 60 * 24 * 7 // 1 week                                        
  },
  store: store,
  // Boilerplate options, see:                                                       
  // * https://www.npmjs.com/package/express-session#resave                          
  // * https://www.npmjs.com/package/express-session#saveuninitialized               
  resave: true,
  saveUninitialized: true
}));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));



app.use(pw_auth_router)

app.use(api_auth_router)

app.use(layouts);

app.get('/', (req,res,next) => {

  // variable to check if the user entered an invalid key
  let invalidKey = false;
  if (req.query.hasOwnProperty('invalidKey')) {
   invalidKey = req.query.invalidKey
  }

  res.render('index', {invalidKey: invalidKey});
})

app.get('/team' , (req,res,next) => {
  res.render('team');
});

app.get('/about', 
  checkLoginStatus,
  (req,res,next) => {
    res.render('about');
  }
)

app.get('/prompt',
  checkLoginStatus,
  (req,res,next) => {
    res.render('prompt');
  }
)


app.use(promptRouter);
app.use(harryRouter);
app.use(xiaoranRouter);
app.use(ericRouter);
app.use(michaelRouter);
app.use(mingRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
