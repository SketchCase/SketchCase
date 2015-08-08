var React = require('react');
var Router = require('react-router');
var Link = Router.Link;
var ArtboardStore = require('../stores/artboard-store');
var RevisionStore = require('../stores/revision-store');

function _updateState(props) {
    this.setState({
        artboard: ArtboardStore.getArtboardFromDocument(
            props.params.id,
            props.params.aid),
        revisions: RevisionStore.getAllForArtboard(props.params.aid)
    });
}

module.exports = React.createClass({
    getInitialState() {
        return {
            artboard: ArtboardStore.getArtboardFromDocument(
                this.props.params.id,
                this.props.params.aid),
            revisions: RevisionStore.getAllForArtboard(this.props.params.aid)
        }
    },

    componentDidMount() {
        ArtboardStore.on(ArtboardStore.CHANGE_EVENT, this._onChange);
        RevisionStore.on(RevisionStore.CHANGE_EVENT, this._onChange);
    },

    componentWillUnmount() {
        ArtboardStore.removeListener(ArtboardStore.CHANGE_EVENT, this._onChange);
        RevisionStore.removeListener(RevisionStore.CHANGE_EVENT, this._onChange);
    },

    componentWillReceiveProps(nextProps) {
        _updateState.call(this, nextProps);
    },

    render() {
        var revisions = this.state.revisions;
        var revisionItems = [];

        for (var revision of revisions) {
            revisionItems.push(<li key={revisionItems.length}>{revision.id}</li>);
        }

        var artboard = this.state.artboard || {};

        return (
            <div>
                <h1>{artboard.name}</h1>
                <ul>{revisionItems}</ul>
            </div>
        );
    },

    _onChange() {
        _updateState.call(this, this.props);
    }
});