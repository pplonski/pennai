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
import { render } from 'react-dom';
import configStore from './config/configStore';
import configSocket from './config/configSocket';
import Root from './components/Root';

const store = configStore();
configSocket(store);

/**
* Root react-redux component - base/root for website, uses helper config files to
* configure the redux store & create socket io server that broadcasts redux actions
* depeneding on respective network event
*
*/
render(
  <Root store={store} />,
  document.getElementById('app')
);
