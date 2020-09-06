

import React, { Component } from 'react';
import Home from './Home';

import {
  BrowserRouter,
  Route,
  Link,
} from 'react-router-dom';

import { render } from '@testing-library/react';


class App extends Component {

  render() {
    return (
      <BrowserRouter>
        <div>
          
          <hr />

          <center>
            <h3>
              Welcome to Fridge Magician
            </h3>
          </center>            

          <ul>
            <li>
              <Link to='/'>
                <button>Home</button>
              </Link>
            </li>
          </ul>

          <hr />

          <Route exact path='/' component={ Home } />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
