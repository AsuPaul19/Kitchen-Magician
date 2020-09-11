import React from 'react';
import kevininwilderness from '../images/kevininwilderness.jpeg';

const kebit01 = () => {
  return (
    <center>
      <body>
        <img
          src={kevininwilderness}
          alt="kevin's photo"
          width='500'
          height='600'
        />

        <div>
          <h2>
            <table>
              <p>
                Kevin Ortiz is a 4th year undergraduate at San Francisco State
                University.
                <br />
                Kevin's major is Computer Science On the days he is not in
                class, he walks his two dogs and also goes bike riding.
              </p>
              He also enjoys traveling and if he can live anywhere it will be
              anywhere that is near the beach!
            </table>
          </h2>
        </div>
      </body>
    </center>
  );
};

export default kebit01;
