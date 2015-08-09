var React = require('react');

module.exports = React.createClass({
    propTypes: {
        revisions: React.PropTypes.array.isRequired,
        onItemClick: React.PropTypes.func
    },

    render() {
        var revisions = this.props.revisions;
        var listItems = [];

        for (var revision of revisions) {
            listItems.push(<li key={listItems.length} onClick={this._onClick.bind(this, listItems.length)}>{revision.id}</li>)
        }

        return (
            <ul className='revision-list'>
                {listItems}
            </ul>
        );
    },

    _onClick(index) {
        var revision = this.props.revisions[index];
        var onItemClick = this.props.onItemClick;
        onItemClick(revision);
    }
});