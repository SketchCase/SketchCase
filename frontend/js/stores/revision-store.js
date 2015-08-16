var BaseStore = require('./base-store');
var WebAPI = require('../utils/web-api');
var ActionTypes = require('../constants/action-types');

var _revisions = {};

class RevisionStore extends BaseStore {
    getAllForArtboard(id) {
        if (_revisions[id] === undefined) {
            WebAPI.fetch(WebAPI.Routes.Revisions(id));
            _revisions[id] = [];
        }

        return _revisions[id];
    }
}

// export and register in dispatcher
module.exports = new RevisionStore(function (action) {
    switch (action.type) {
        case ActionTypes.RECIEVED_REVISIONS:
            _revisions[action.artboardId] = action.revisions;
            this.emitChange();
            break;
    }
});