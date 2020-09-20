'use strict';
module.exports = function(app) {
  var recordlist = require('../controllers/controller');

  app.route('/records')
    .get(recordlist.list_all_records)
    .post(recordlist.create_a_record)

  app.route('/findrecord')
    .get(recordlist.read_a_record)
};