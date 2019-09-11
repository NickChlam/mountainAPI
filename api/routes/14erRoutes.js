'use strict';
module.exports = function(app) {

    var fourteener = require('../controllers/14erController');


    //routes

    app.route('/fourteeners')
        .get(fourteener.list_all_14ers);

    app.route('/fourteeners/:mountain')
        .get(fourteener.get_mountain);
}