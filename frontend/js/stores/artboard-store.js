var BaseStore = require('./base-store');
var WebAPI = require('../utils/web-api');
var ActionTypes = require('../constants/action-types');

var _artboards = {};

function _upsertArtboard(documentId, artboard) {
    var artboards = _artboards[documentId] || [artboard];

    for (var i = 0; i < artboards.length; i++) {
        if (artboards[i].id === artboard.id) {
            artboards[i] = artboard; 
            break;
        }
    }

    _artboards[documentId] = artboards;
}

class ArtboardStore extends BaseStore {
    getAllForDocument(id) {
        if (_artboards[id] === undefined) {
            WebAPI.fetch(WebAPI.Routes.Artboards(id));
            _artboards[id] = [];
        }
        
        return _artboards[id];
    }

    getArtboardFromDocument(documentId, artboardId) {
        var artboards = _artboards[documentId] || [];

        for (var artboard of artboards) {
            if (artboard.id === artboardId) {
                return artboard;
            }
        }

        WebAPI.fetch(WebAPI.Routes.Artboard(artboardId));
        return null;
    }
}

// export and register in dispatcher
module.exports = new ArtboardStore(function (action) {
    switch (action.type) {
        case ActionTypes.RECIEVE_ARTBOARDS:
            _artboards[action.documentId] = action.artboards;
            this.emitChange();
            break;

        case ActionTypes.RECIEVE_ARTBOARD:
            _upsertArtboard(action.documentId, action.artboard);
            this.emitChange();
            break;
    }
});