var Dispatcher = require('../dispatcher/dispatcher');
var ActionTypes = require('../constants/action-types');

module.exports = {
    recievedAll: function (documents) {
        Dispatcher.dispatch({
            type: ActionTypes.RECIEVED_DOCUMENTS,
            documents: documents
        });
    },

    recieved: function (doc) {
        Dispatcher.dispatch({
            type: ActionTypes.RECIEVED_DOCUMENT,
            document: doc
        });
    }
};