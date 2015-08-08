var BaseStore = require('./base-store');
var WebAPI = require('../utils/web-api');
var ActionTypes = require('../constants/action-types');

var _documents = [];

class DocumentStore extends BaseStore {
    getAll() {
        if (_documents.length < 1) {
            WebAPI.fetch(WebAPI.Routes.Documents());
        }
        
        return _documents;
    }
}

// export and register in dispatcher
module.exports = new DocumentStore(function (action) {
    switch (action.type) {
        case ActionTypes.RECIEVE_DOCUMENTS:
            _documents = action.documents;
            this.emitChange();
            break;
    }
});