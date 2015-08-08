var React = require('react');
var Router = require('react-router');
var Route = Router.Route;
var Comp = require('./components');

var routes = (
    <Route handler={Comp.App}>
        <Route path='/' handler={Comp.DocumentList}/>
        <Route name='artboards' path='/:id/artboards' handler={Comp.ArtboardList}>
            <Route path=':id'/>
        </Route>
    </Route>
);

Router.run(routes, Router.HistoryLocation, (Root) => {
  React.render(<Root/>, document.getElementById('app'));
});