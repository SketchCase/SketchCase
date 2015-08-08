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
        var latestRevision = revisions[0] || {};

        return (
            <div className='artboard-detail'>
                <div className='artboard-detail-image-holder'>
                    <img src={'/' + latestRevision.image_url}/>
                </div>
            </div>
        );
    },

    _onChange() {
        _updateState.call(this, this.props);
    }
});