/* ~This file is part of the PennAI library~

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
import { Provider } from 'react-redux';
import { Router, Route, IndexRedirect, hashHistory } from 'react-router';

import App from '../App';
import Datasets from '../Datasets';
import FileUpload from '../FileUpload';
import Dataset from '../Dataset';
import Experiments from '../Experiments';
import Builder from '../Builder';
import Results from '../Results';
import Admin from '../Admin';
import NotFound from '../NotFound';

/**
* Use react router to delineate different parts of website; essentially links
*/
function Root({ store }) {
  return (
    <Provider store={store}>
      <Router history={hashHistory} onUpdate={() => window.scrollTo(0, 0)}>
        <Route path="/" component={App}>
          <IndexRedirect to="datasets" />
          <Route path="upload_datasets" component={FileUpload} />
          <Route path="datasets" component={Datasets} />
          <Route path="datasets/:id" component={Dataset} />
          <Route path="experiments" component={Experiments} />
          <Route path="builder" component={Builder} />
          <Route path="results/:id" component={Results} />
          <Route path="admin" component={Admin} />
          <Route path="*" component={NotFound} />
        </Route>
      </Router>
    </Provider>
  );
}

export default Root;
