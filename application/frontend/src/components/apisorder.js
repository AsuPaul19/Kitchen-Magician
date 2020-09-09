import React from 'react';
import penguin from '../images/penguin.jpg';

const apisorder = () => {
  return (
    <div>
      <center>
        <img src={penguin} alt="this is Jeff's avatar" />
      </center>
      <h5>
        <p>
          Jeff is a second-year graduate student in Computer Science at San
          Francisco State University.
          <br />
          He graduated with a Bachelor of Arts in Economics, with a certified
          minor in Computer Science, from the University of California, Davis.
          <br />
          <br />
          He is interested in enhancing user-experience, preferrably for those
          with special needs.
          <br />
          <br />
          Jeff enjoys drawing, reading, and hiking in his spare time.
        </p>
      </h5>
    </div>
  );
};

export default apisorder;
