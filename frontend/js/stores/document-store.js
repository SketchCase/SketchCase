var BaseStore = require('./base-store');
var WebAPI = require('../utils/web-api');
var ActionTypes = require('../constants/action-types');

var _documents = [];
var _fetchedAll = false;

function _upsertDocument(doc) {
    for (var i = 0; i < _documents.length; i++) {
        if (_documents[i].id === doc.id) {
            _documents[i] = doc;
            return;
        }
    }

    _documents.push(doc);
}

class DocumentStore extends BaseStore {
    getAll() {
        if (!_fetchedAll) {
            WebAPI.fetch(WebAPI.Routes.Documents());
            _fetchedAll = true;
        }
        
        return _documents;
    }

    get(id) {
        for (var doc of _documents) {
            if (doc.id === id) {
                return doc;
            }
        }

        WebAPI.fetch(WebAPI.Routes.Document(id));
        return null;
    }
}

// export and register in dispatcher
module.exports = new DocumentStore(function (action) {
    switch (action.type) {
        case ActionTypes.RECIEVED_DOCUMENTS:
            _documents = action.documents;
            this.emitChange();
            break;

        case ActionTypes.RECIEVED_DOCUMENT:
            _upsertDocument(action.document);
            this.emitChange()
            break;
    }
});