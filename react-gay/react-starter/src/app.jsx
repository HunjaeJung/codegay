var React = require('react');
var ReactDom = require('react-dom');

var Hello = React.createClass({
  render: function() {
    return <h1 className="red">
      Hello!
    </h1>
  }
});

var element = React.createElement(Hello, {});
ReactDom.render(element, document.querySelector('.container'));
