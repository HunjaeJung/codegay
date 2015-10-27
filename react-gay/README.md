# react-gay

## [How to communicate between React components](http://ctheu.com/2015/02/12/how-to-communicate-between-react-components/#child_to_parent)

React component가 서로 커뮤니테이션하는데에는 총 3가지 채널이 있습니다.
- Owner to ownee
- Ownee to owner
- They are not related


1. How an owner can talk to its ownee

 가장 기본적으로 사용하는 `this.props.something`으로 합니다. 

2. Hierarchy problem

 그런데 이렇게 하다보면 hierarchy 문제가 있어요. child의 child의 child..에게 계속해서 `this.props.something`을 전달해줘야하니까요.

3. Context

 Context는 아직 React팀에서 Documentation으로 공식 support하고 있지는 않지만, 굉장히 유용하고, 이미 많이 사용되고 있는 기능입니다. Dynamic tree of components를 가지고 있을때, 부모에서 선언하면 모든 children들에서 사용가능합니다.
  ```
  The concept of context is easy to understand:

    – one component makes a JS object at disposal that will be available for _any_ of its children components, grand children and so on, without them to being passed down explicitely.
    – any child can use this.context to access this object (passed behind the scene by React)

  But, to use it, you have to follow some rules :

    – define getChildContext on the parent to return what is the context (any JS object)
    – define childContextTypes on the parent to define what is the type of each property in this context (React.PropTypes.)
    – define contextTypes on a (child) component that want to read from its context (which property does it want to read)
  ```

4. How a ownee can talk to its owner

 그렇다면 ownee에서 owner에게는 어떻게 데이터를 보낼 수 있을까요?  owner의 함수를 props으로 보내고, ownee 함수에서 해당 함수를 파라미터와 함께 호출합니다!

 ```
    var MyContainer = React.createClass({
        getInitialState: function() {
            return { checked: false };
        },
        onChildChanged: function(newState) {
            this.setState({ checked: newState });
        },
        render: function() {
            return  <div>
                      <div>Are you checked ? {this.state.checked ? 'yes' : 'no'}</div>
                      <ToggleButton text="Toggle me" initialChecked={this.state.checked} callbackParent={this.onChildChanged} />
                    </div>;
        }
    });

    var ToggleButton = React.createClass({
      getInitialState: function() {
        // we ONLY set the initial state from the props
        return { checked: this.props.initialChecked };
      },
      onTextChanged: function() {
        var newState = !this.state.checked;
        this.setState({ checked: newState });
        this.props.callbackParent(newState); // hey parent, I've changed!
      },
        render: function() {
            return <label>{this.props.text}: <input type="checkbox" checked={this.state.checked} onChange={this.onTextChanged}/></label>;
        }
    });
 ```

5. More details about the React event system

6. Using the same callback

7. Help me, my components are not related!

8. Events in React

9. Conclusion


