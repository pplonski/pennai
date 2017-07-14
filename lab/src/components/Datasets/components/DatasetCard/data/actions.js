import * as api from './api';
import { getIsTogglingAI } from './reducer';

export const ACTION_PREFIX = 'DATASET_';
export const DATASET_UPDATE = 'DATASET_UPDATE';
export const AI_TOGGLE_UPDATE = ACTION_PREFIX + 'AI_TOGGLE_UPDATE';
export const AI_TOGGLE_REQUEST = ACTION_PREFIX + 'AI_TOGGLE_REQUEST';
export const AI_TOGGLE_SUCCESS = ACTION_PREFIX + 'AI_TOGGLE_SUCCESS';
export const AI_TOGGLE_FAILURE = ACTION_PREFIX + 'AI_TOGGLE_FAILURE';

export const toggleAI = (id, nextAIState) => (dispatch, getState) => {
  if(getIsTogglingAI(getState(), id)) {
    return Promise.resolve();
  }

  dispatch({
    type: AI_TOGGLE_REQUEST,
    id
  });

  return api.toggleAI(id, nextAIState).then(
    response => {
      dispatch({
        type: AI_TOGGLE_SUCCESS,
        receivedAt: Date.now(),
        id,
        nextAIState,
        response
      });
    },
    error => {
      dispatch({
        type: AI_TOGGLE_FAILURE,
        receivedAt: Date.now(),
        message: error.message || 'Something went wrong.',
        id
      });
    }
  );
};

export const updateAIToggle = (id, nextAIState) => (dispatch) => {
  dispatch({
    type: AI_TOGGLE_UPDATE,
    id,
    nextAIState
  });
};

export const updateDataset = (dataset) => (dispatch) => {
  dispatch({
    type: DATASET_UPDATE,
    dataset
  });
};