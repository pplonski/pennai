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
import { combineReducers } from 'redux';
import { createSelector } from 'reselect';
import dataset from './dataset';
import {
  FETCH_DATASETS_REQUEST,
  FETCH_DATASETS_SUCCESS,
  FETCH_DATASETS_FAILURE
} from './actions';
import {
  TOGGLE_AI_REQUEST,
  TOGGLE_AI_SUCCESS,
  TOGGLE_AI_FAILURE,
  AI_UPDATE,
  DATASET_UPDATE,
  UPLOAD_DATASET_REQUEST,
  UPLOAD_DATASET_SUCCESS,
  UPLOAD_DATASET_FAILURE
} from './dataset/actions';

const byId = (state = {}, action) => {
  switch(action.type) {
    case FETCH_DATASETS_SUCCESS:
      return action.payload.reduce((map, d) => {
        map[d._id] = d;
        return map;
      }, {});
    case DATASET_UPDATE:
      return Object.assign({}, state, {
        [action.dataset._id]: dataset(state[action.dataset._id], action)
      });
    case TOGGLE_AI_REQUEST:
    case TOGGLE_AI_SUCCESS:
    case TOGGLE_AI_FAILURE:
    case AI_UPDATE:
      return Object.assign({}, state, {
        [action.id]: dataset(state[action.id], action)
      });
    default:
      return state;
  }
};

const fileUpload = (state = {}, action) => {
  switch (action.type) {
    case UPLOAD_DATASET_REQUEST:
      let test = dataset(state, action);
      //return {...state, dataset(state, action)};
      return {...state, test};
    case UPLOAD_DATASET_SUCCESS:
      let test2 = dataset(state, action);
      //return {...state, dataset(state, action)};
      return {...state, test2};
    case UPLOAD_DATASET_FAILURE:
      let test3 = dataset(state, action);
      //return {...state, dataset(state, action)};
      return {...state, test3};
    default:
      return state;
  }
};

const allIds = (state = [], action) => {
  switch(action.type) {
    case FETCH_DATASETS_SUCCESS:
      return action.payload.map(d => d._id);
    default:
      return state;
  }
};

const isFetching = (state = false, action) => {
  switch(action.type) {
    case FETCH_DATASETS_REQUEST:
      return true;
    case FETCH_DATASETS_SUCCESS:
    case FETCH_DATASETS_FAILURE:
      return false;
    default:
      return state;
  }
};

const error = (state = null, action) => {
  switch(action.type) {
    case FETCH_DATASETS_FAILURE:
      return action.payload;
    default:
      return state;
  }
};

const datasets = combineReducers({
  byId,
  allIds,
  isFetching,
  error
});

// selector for alphabetizing
const getAllIds = (state) => state.datasets.allIds;
const getById = (state) => state.datasets.byId;
export const getSortedDatasets = createSelector(
  [getAllIds, getById],
  (allIds, byId) =>
    allIds
      .map(id => byId[id])
      .sort((a, b) => {
        const A = a.name.toLowerCase();
        const B = b.name.toLowerCase();
        return A > B ? 1 : A < B ? -1 : 0;
      })
);

export default datasets;
