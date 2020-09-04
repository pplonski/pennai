"""~This file is part of the PennAI library~

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

"""
import pandas as pd
from .base import BaseRecommender
import numpy as np
import pdb

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(module)s: %(levelname)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class RandomRecommender(BaseRecommender):
    """Penn AI random recommender.

    Recommends random machine learning algorithms and parameters from the possible 
    algorithms fetched from the server.

    Parameters
    ----------
    ml_type: str, 'classifier' or 'regressor'
        Recommending classifiers or regressors. Used to determine ML options.

    metric: str (default: accuracy for classifiers, mse for regressors)
        The metric by which to assess performance on the datasets.
    
    ml_p: Dataframe
        Contains all the machine learning / algorithm combinations available for 
        recommendation.
    """


    def __init__(self, ml_type='classifier', metric=None, ml_p=None):
        """Initialize recommendation system."""
        super().__init__(ml_type, metric, ml_p)

    def update(self, results_data, results_mf=None, source='pennai'):
        """Update ML / Parameter recommendations.

        Parameters
        ----------
        results_data: DataFrame 
                columns corresponding to:
                'algorithm'
                'parameters'
                self.metric

        results_mf: DataFrame, optional 
               columns corresponding to metafeatures of each dataset in 
               results_data.
        """
        # update trained dataset models and hash table
        super().update(results_data, results_mf, source)

    def recommend(self, dataset_id=None, n_recs=1, dataset_mf=None):
        """Return a model and parameter values expected to do best on dataset.

        Parameters
        ----------
        dataset_id: string
            ID of the dataset for which the recommender is generating 
            recommendations.
        n_recs: int (default: 1), optional
            Return a list of len n_recs in order of estimators and parameters 
            expected to do best.
        """
        # dataset hash table
        super().recommend(dataset_id, n_recs, dataset_mf)

        # return ML+P for best average y
        #print(self.ml_p)
        try:
            ml_rec,p_rec,phash_rec,rec_score=[],[],[],[]

            for i in np.arange(n_recs):
                n=0
                rec_not_new = True
                # while (rec_not_new and n<10):
                    #print(self.ml_p)
                ml_tmp = np.random.choice(self.ml_p['algorithm'].unique())
                p_tmp = np.random.choice([mlp.split('|')[1] for mlp in
                    self.mlp_combos if ml_tmp in mlp])
                        # self.mlp_.loc[self.ml_p['algorithm']==ml_tmp,'parameters']
                        # ).items()))
                # if dataset_id is not None:
                #     rec_not_new = (dataset_id + '|' + ml_tmp + '|' + p_tmp in
                #                    self.trained_dataset_models)
                # else:
                #     rec_not_new = False
                # if n==999:
                #     print('warning: tried 10 times (and failed) to find a novel 
                # recommendation')
                ml_rec.append(ml_tmp)
                phash_rec.append(p_tmp)
                p_rec.append(self.param_htable[int(p_tmp)])
                rec_score.append(0) 
            # if a dataset is specified, do not make recommendations for
            # algorithm-parameter combos that have already been run
            
            #if dataset_id is not None:
            #    rec = [r for r in rec if dataset_id + '|' + r not in
            #           self.trained_dataset_models]

            #ml_rec = [r.split('|')[0] for r in rec]
            #p_rec = [r.split('|')[1] for r in rec]
            #rec_score = [0 for r in rec]
        except AttributeError:
            logger.error('rec:', rec)
            logger.error('self.scores:', self.scores)
            logger.error('self.w:', self.w)
            raise AttributeError

        self.update_trained_dataset_models_from_rec(dataset_id, ml_rec, phash_rec)

        return ml_rec, p_rec, rec_score
