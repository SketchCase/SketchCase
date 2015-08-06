var React = require('react');
var Router = require('react-router');
var Route = Router.Route;

React.render((
	<Route>
        <Route path=""/>
        <Route path=":id/artboards">
            <Route path=":id"/>
        </Route>
	</Route>
), document.getElementById('app'));