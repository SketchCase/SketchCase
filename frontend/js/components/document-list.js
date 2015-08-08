var React = require('react');
var DocumentStore = require('../stores/document-store');
var DocumentItem = require('./document-list-item');

module.exports = React.createClass({
    getInitialState() {
        return {
            documents: DocumentStore.getAll()
        };
    },

    componentDidMount() {
        DocumentStore.on(DocumentStore.CHANGE_EVENT, this._onChange);
    },

    componentWillUnmount() {
        DocumentStore.removeListener(DocumentStore.CHANGE_EVENT, this._onChange);
    },

    render() {
        var items = this.state.documents;
        var listItems = [];

        for (var item of items) {
            listItems.push(<DocumentItem key={listItems.length} id={item.id} name={item.name}/>);
        }

        return (
            <ul>
                {listItems}
            </ul>
        );
    },

    _onChange() {
        this.setState({
            documents: DocumentStore.getAll()
        });
    }
});