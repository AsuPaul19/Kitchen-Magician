import React, { Component } from 'react';
import apisorder from './apisorder';

import { BrowserRouter, Route, Link } from 'react-router-dom';

import { render } from '@testing-library/react';

export default class Home extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <ol>
            <li>
              <Link to='/allensun7'>
                <button>Allen Sun</button>
              </Link>
            </li>

            <li>
              <Link to='/apisorder'>
                <button>Jeff Cheng</button>
              </Link>
            </li>

            <li>
              <Link to='/Kebit01'>
                <button>Kevin Ortiz</button>
              </Link>
            </li>

            <li>
              <Link to='/KevinWeiHadExtra'>
                <button>Kevin Wei</button>
              </Link>
            </li>

            <li>
              <Link to='/npng16'>
                <button>Nicole Pang</button>
              </Link>
            </li>

            <li>
              <Link to='/AsuPaul19'>
                <button>Paul Asu</button>
              </Link>
            </li>
          </ol>

          <hr />

          <Route path='/allensun7' />
          <Route path='/apisorder' component={apisorder} />
          <Route path='/Kebit01' />
          <Route path='/KevinWeiHadExtra' />
          <Route path='/npng16' />
          <Route path='/AsuPaul19' />
        </div>
      </BrowserRouter>
    );
  }
}
