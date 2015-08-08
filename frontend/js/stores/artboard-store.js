var BaseStore = require('./base-store');
var WebAPI = require('../utils/web-api');
var ActionTypes = require('../constants/action-types');

var _artboards = {};

class ArtboardStore extends BaseStore {
    getAllForDocument(id) {
        if (_artboards[id] === undefined) {
            WebAPI.fetch(WebAPI.Routes.Artboards(id));
        }
        
        return _artboards[id] || [];
    }
}

// export and register in dispatcher
module.exports = new ArtboardStore(function (action) {
    switch (action.type) {
        case ActionTypes.RECIEVE_ARTBOARDS:
            _artboards[action.documentId] = action.artboards;
            this.emitChange();
            break;
    }
});