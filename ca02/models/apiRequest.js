'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;

var apiRequestSchema = Schema( {
    timestamp: { type: Date, default: Date.now },
    endpoint: String,
    prompt: String,
    responseStatusCode: Number,
    responseBody: Object,
} );

module.exports = mongoose.model( 'apiRequest', apiRequestSchema );