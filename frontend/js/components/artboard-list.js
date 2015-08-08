var React = require('react');
var ArtboardStore = require('../stores/artboard-store');

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
            listItems.push(<li key={item.id}>{item.name}</li>);
        }

        return (
            <ul>{listItems}</ul>
        );
    },

    _onChange() {
        this.setState({
            artboards: ArtboardStore.getAllForDocument(this.props.params.id)
        });
    }
});