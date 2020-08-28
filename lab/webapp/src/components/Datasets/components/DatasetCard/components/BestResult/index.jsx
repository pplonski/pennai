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
import { Segment, Header, Progress } from 'semantic-ui-react';
import { formatAlgorithm } from '../../../../../../utils/formatter';

function BestResult({ result, hasMetadata }) {
  const getNoResultMessage = () => {
    if(!hasMetadata) {
      return 'You must upload a metadata file in order to use this dataset.';
    }

    return 'No results yet, build a new experiment to start.';
  };

  const getResultLink = () => `/#/results/${result._id}`;

  const getPercent = () => (result.score * 100).toFixed(2);

  if(!result) {
    return (
      <Segment inverted attached className="panel-body">
        {getNoResultMessage()}
      </Segment>
    );
  }

  // add label for best results
  var label = "";
  if (result.prediction_type == "classification") {
    label = "Balanced Accuracy";
  } else if (result.prediction_type == "regression") {
    label = "R2";
  }

  return (
    <Segment
      inverted
      attached
      href={getResultLink()}
      className="panel-body best-result"
    >
      <Header inverted size="small">
        {'Best Result'}
        <Header.Subheader>
          <div>{formatAlgorithm(result.algorithm)}</div>
          <span>{`#${result._id}`}</span>
        </Header.Subheader>
      </Header>
      <Progress
        inverted
        progress
        percent={getPercent()}
        className="accuracy-score"
        label={label}
      />
    </Segment>
  );
}

export default BestResult;
