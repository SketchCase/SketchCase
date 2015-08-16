var React = require('react');
var Router = require('react-router');
var RouteHandler = Router.RouteHandler;
var ArtboardStore = require('../stores/artboard-store');
var DocumentStore = require('../stores/document-store');
var ArtboardItem = require('./artboard-list-item');

module.exports = React.createClass({
    getInitialState() {
        return {
            document: DocumentStore.get(this.props.params.id),
            artboards: ArtboardStore.getAllForDocument(this.props.params.id)
        };
    },

    componentDidMount() {
        ArtboardStore.on(ArtboardStore.CHANGE_EVENT, this._onChange);
        DocumentStore.on(DocumentStore.CHANGE_EVENT, this._onChange);
    },

    componentWillUnmount() {
        ArtboardStore.removeListener(ArtboardStore.CHANGE_EVENT, this._onChange);
        DocumentStore.removeListener(DocumentStore.CHANGE_EVENT, this._onChange);
    },

    render() {
        var listItems = [];
        var doc = this.state.document || {};

        for (var item of this.state.artboards) {
            listItems.push(<ArtboardItem key={listItems.length} item={item}/>);
        }

        return (
            <div>
                <div className='container'>
                    <div className='col-12'>
                        <h1>{doc.name}</h1>
                    </div>
                    {listItems}
                </div>
                <RouteHandler/>
            </div>
        );
    },

    _onChange() {
        this.setState({
            document: DocumentStore.get(this.props.params.id),
            artboards: ArtboardStore.getAllForDocument(this.props.params.id)
        });
    }
});