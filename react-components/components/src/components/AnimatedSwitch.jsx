import React from 'react';
import { Route, Switch } from 'react-router-dom';

import { TransitionGroup, CSSTransition } from 'react-transition-group';
import { withRouter } from 'react-router-dom';

import Page from './route-test/Page';
import Home from './route-test/Home';

import '../animation.css';

const AnimatedSwitch = withRouter(({ location }) => {
  return (
    <TransitionGroup>
      <CSSTransition key={location.key} classNames='fade' timeout={2000}>
        <Switch>
          <Route path='/page' component={Page} />
          <Route path='/' component={Home} />
        </Switch>
      </CSSTransition>
    </TransitionGroup>
  );
});

export default AnimatedSwitch;
