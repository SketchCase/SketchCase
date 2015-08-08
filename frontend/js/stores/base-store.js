var EventEmitter = require('events').EventEmitter;
var Dispatcher = require('../dispatcher/dispatcher');

class BaseStore extends EventEmitter {
    CHANGE_EVENT: 'CHANGE';

    constructor(eventCallback) {
        super();
        this.dispatchToken = Dispatcher.register(eventCallback.bind(this));
    }

    emitChange() {
        this.emit(this.CHANGE_EVENT);
    }
}

module.exports = BaseStore;