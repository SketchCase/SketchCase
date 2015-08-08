var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

module.exports = React.createClass({
    propTypes: {
        id: React.PropTypes.string.isRequired,
        name: React.PropTypes.string.isRequired
    },

    render() {
        var id = { id: this.props.id };

        return (
            <li>
                <Link to='artboards' params={id}>{this.props.name}</Link>
            </li>
        );
    }
});