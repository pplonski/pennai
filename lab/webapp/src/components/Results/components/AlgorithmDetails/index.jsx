/* This file is part of the PennAI library.

Copyright (C) 2017 Epistasis Lab, University of Pennsylvania

PennAI is maintained by:
    - Heather Williams (hwilli@upenn.edu)
    - Weixuan Fu (weixuanf@pennmedicine.upenn.edu)
    - William La Cava (lacava@upenn.edu)
    - and many other generous open source contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

*/
import React from 'react';
import InvertedCard from '../../../InvertedCard';
import { Header, Grid } from 'semantic-ui-react';
import { formatAlgorithm, formatParam } from 'utils/formatter';

function AlgorithmDetails({ algorithm, params }) {
  return (
    <InvertedCard 
      header="Algorithm"
      content={
        <div>
          <Header inverted size="small" content={formatAlgorithm(algorithm)} />
          <Grid columns={2}>
            {Object.entries(params).map(([param, value]) => (
              <Grid.Column key={param}>
                <Header
                  inverted
                  size="tiny"
                  color="grey"
                  content={formatParam(param)}
                  subheader={value.toString()}
                />
              </Grid.Column>
            ))}
          </Grid>
        </div>
      }
    />
  );
}

export default AlgorithmDetails;