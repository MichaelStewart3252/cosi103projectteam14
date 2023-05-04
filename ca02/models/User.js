
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var userSchema = Schema( {
  username:String,
  passphrase: String,
  age:Number,
  apiRequestHistory: [{ type: mongoose.Schema.Types.ObjectId, ref: 'apiRequest' }]
} );

module.exports = mongoose.model( 'User', userSchema );
