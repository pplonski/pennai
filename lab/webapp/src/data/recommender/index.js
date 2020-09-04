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
import { combineReducers } from 'redux';
import { 
  FETCH_RECOMMENDER_REQUEST, 
  FETCH_RECOMMENDER_SUCCESS, 
  FETCH_RECOMMENDER_FAILURE
} from './actions';

const data = (state = {}, action) => {
  switch(action.type) {
    case FETCH_RECOMMENDER_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};

const isFetching = (state = false, action) => {
  switch(action.type) {
    case FETCH_RECOMMENDER_REQUEST:
      return true;
    case FETCH_RECOMMENDER_SUCCESS:
    case FETCH_RECOMMENDER_FAILURE:
      return false;   
    default:
      return state;
  }
};

const error = (state = null, action) => {
  switch(action.type) {
    case FETCH_RECOMMENDER_FAILURE:
      return action.payload;
    default:
      return state;  
  }
};

const recommender = combineReducers({
  data,
  isFetching,
  error
});

export default recommender;