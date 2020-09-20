'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var recordSchema = new Schema({
    "pref": {
    type: String
    },
    "name": {
    type: String,
    required: 'Kindly enter the name of the person'
  },
  "ministry": {
    type: String,
  },
  "urls":{
      type: String,
  }
});

module.exports = mongoose.model('Records', recordSchema);