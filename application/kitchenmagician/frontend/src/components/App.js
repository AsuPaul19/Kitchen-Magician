// import React, { Component, Fragment } from 'react';
// import ReactDOM from 'react-dom';
// import { BrowserRouter, Route, Link } from 'react-router-dom';

// import Header from './layout/Header';
// import Dashboard from './fridges/Dashboard';

// class App extends Component {
//   render() {
//     return (
//       <Fragment>
//         <Header />;
//         <div className='container'>
//           <Dashboard />
//         </div>
//       </Fragment>
//     );
//   }
// }

// ReactDOM.render(<App />, document.getElementById('app'));

import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Home from './Home';

import { BrowserRouter, Route, Link } from 'react-router-dom';

import { render } from '@testing-library/react';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <hr />

          <center>
            <h3>Welcome to Fridge Magician</h3>
          </center>

          <ul>
            <li>
              <Link to='/'>
                <button>Home</button>
              </Link>
            </li>
          </ul>

          <hr />

          <Route exact path='/' component={Home} />
        </div>
      </BrowserRouter>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
