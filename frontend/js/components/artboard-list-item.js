var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

module.exports = React.createClass({
    propTypes: {
        item: React.PropTypes.object.isRequired
    },

    render() {
        var params = { 
            id: this.props.item.document_id, 
            aid: this.props.item.id
        };

        return (
            <div className='col-3'>
                <div className='artboard-list-item'>
                    <Link to='artboard' params={params}>{this.props.item.name}</Link>
                </div>
            </div>
        );
    }
});