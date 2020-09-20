'use strict';


var mongoose = require('mongoose'),
  Record = mongoose.model('Records');

exports.list_all_records = function(req, res) {
  Record.find({}, function(err, record) {
    // console.log("All_function");
    if (err)
      res.send(err);
    res.json(record);
  });
};

exports.create_a_record = function(req, res) {
  var new_record = new Record(req.body);
  new_record.save(function(err, record) {
    if (err)
      res.send(err);
    res.json(record);
  });
};

exports.read_a_record = function(req, res) {
  Record.findOne({name:req.body.name}, 
    function(err, record) {
      // console.log("find_one");
      console.log(req.body.name);
      if (err)
        res.send(err);
      res.json(record);
  });
};

