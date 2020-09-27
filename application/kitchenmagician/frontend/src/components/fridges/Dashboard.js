import React, { Fragment } from 'react';

import Forms from './Forms';
import Fridges from './Fridges';

export default function Dashboard() {
  return (
    <Fragment>
      <Forms />
      <Fridges />
    </Fragment>
  );
}
