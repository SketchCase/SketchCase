var React = require('react');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var ArtboardStore = require('../stores/artboard-store');
var ArtboardItem = require('./artboard-list-item');

module.exports = React.createClass({
    getInitialState() {
        return {
            artboards: ArtboardStore.getAllForDocument(this.props.params.id)
        };
    },

    componentDidMount() {
        ArtboardStore.on(ArtboardStore.CHANGE_EVENT, this._onChange);
    },

    componentWillUnmount() {
        ArtboardStore.removeListener(ArtboardStore.CHANGE_EVENT, this._onChange);
    },

    render() {
        var listItems = [];

        for (var item of this.state.artboards) {
            listItems.push(<ArtboardItem key={listItems.length} item={item}/>);
        }

        return (
            <div>
                <ul>{listItems}</ul>
                <RouteHandler/>
            </div>
        );
    },

    _onChange() {
        this.setState({
            artboards: ArtboardStore.getAllForDocument(this.props.params.id)
        });
    }
});