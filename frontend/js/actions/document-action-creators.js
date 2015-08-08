var Dispatcher = require('../dispatcher/dispatcher');
var ActionTypes = require('../constants/action-types');

module.exports = {
    recievedAll: function (documents) {
        Dispatcher.dispatch({
            type: ActionTypes.RECIEVE_DOCUMENTS,
            documents: documents
        });
    }
};