var request = require('superagent');
var DocumentActionCreators = require('../actions/document-action-creators');
var ArtboardActionCreators = require('../actions/artboard-action-creators');
var RevisionActionCreators = require('../actions/revision-action-creators');

module.exports = {
    APIRoot: '/api/v1',
    
    Routes: {
        Documents: () => [`/documents`, DocumentActionCreators.recievedAll],
        Document: (id) => [`/documents/${id}`, DocumentActionCreators.recieved],
        Artboards: (id) => [`/documents/${id}/artboards`, ArtboardActionCreators.recievedAllForDocument],
        Artboard: (id) => [`/artboards/${id}`, ArtboardActionCreators.recieved],
        Revisions: (id) => [`/artboards/${id}/revisions`, RevisionActionCreators.recievedAll],
        Revision: (id) => [`/revisions/${id}`]
    },

    fetch(route) {
        console.log(`Fetching ${route[0]}`);

        request
            .get(this.APIRoot + route[0])
            .end((err, res) => {
                if (err != null) {
                    // TODO handle errors
                }

                var data = res.body.data;
                
                if (data) {
                    route[1](data);
                }
            });
    },

    post(route, data) {

    }
};