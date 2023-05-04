'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var apiRequestSchema = Schema( {
    timestamp: Date,
    prompt: String,
    input: String, 
    response: String,
    userId: String
} );

module.exports = mongoose.model( 'apiRequest', apiRequestSchema );