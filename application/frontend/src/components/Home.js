import React, { Component } from 'react';
import apisorder from './apisorder';
import allensun7 from './allensun7';
import KevinWeiHadExtra from './KevinWeiHadExtra.js';
import kebit01 from './kebit01';
import npng16 from './npng16';
import asupaul from './asupaul';

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
              <Link to='/kebit01'>
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
              <Link to='/asupaul'>
                <button>Paul Asu</button>
              </Link>
            </li>
          </ol>

          <hr />

          <Route path='/allensun7' component={allensun7} />
          <Route path='/apisorder' component={apisorder} />
          <Route path='/kebit01' component={kebit01} />
          <Route path='/KevinWeiHadExtra' component={KevinWeiHadExtra} />
          <Route path='/npng16' component={npng16} />
          <Route path='/asupaul' component={asupaul} />
        </div>
      </BrowserRouter>
    );
  }
}
