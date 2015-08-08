var Dispatcher = require('../dispatcher/dispatcher');
var ActionTypes = require('../constants/action-types');

module.exports = {
    recievedAll: function (revisions) {
        var artboardId = null;

        if (revisions.length > 0) {
            artboardId = revisions[0].artboard_id;
        }

        Dispatcher.dispatch({
            type: ActionTypes.RECIEVE_REVISIONS,
            revisions: revisions,
            artboardId: artboardId
        });
    }
};