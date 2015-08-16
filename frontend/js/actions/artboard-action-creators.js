var Dispatcher = require('../dispatcher/dispatcher');
var ActionTypes = require('../constants/action-types');

module.exports = {
    recievedAllForDocument: function (artboards) {
        var documentId = null;

        if (artboards.length > 0) {
            documentId = artboards[0].document_id;
        }

        Dispatcher.dispatch({
            type: ActionTypes.RECIEVED_ARTBOARDS,
            artboards: artboards,
            documentId: documentId
        });
    },

    recieved: function (artboard) {
        Dispatcher.dispatch({
            type: ActionTypes.RECIEVED_ARTBOARD,
            artboard: artboard,
            documentId: artboard.document_id
        });
    }
};