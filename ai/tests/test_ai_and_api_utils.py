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
"""
Test the api engine (ai.py) and the labAPi methods (api_utils.py) together by simulating the 
responses that would be returned by GETing, POSTing and PUTing requests to the lab server.
"""
import os
os.environ["LAB_HOST"] = "lab"
os.environ['LAB_PORT'] = "5080"
os.environ['APIKEY'] = "aaaaa"

from ai.ai import AI
import ai.ai
import sys
from unittest.mock import Mock, patch
from nose.tools import nottest, raises
import lab_api_mocker as mocker



#===========================================
# Tests
#===========================================
@patch('requests.request', side_effect=mocker.mocked_requests_request)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
def test_ai_init_args(mock_request, mock_post):
	lab_connection_args = {}
	pennai = AI(
		rec_class=None,
		api_path='http://lab:5080',
		user="testuser",
        verbose=True, 
        n_recs=1, 
        warm_start=False,
        datasets={},
        use_knowledgebase=False
    )

@patch('requests.request', side_effect=mocker.mocked_requests_request)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
def test_ai_init_knowledgebase(mock_request, mock_post):
    lab_connection_args = {}
    pennai = AI(
        rec_class=None,
        api_path='http://lab:5080',
        user="testuser",
        verbose=True, 
        n_recs=1, 
        warm_start=False,
        datasets={},
        use_knowledgebase=True
    )

@patch('requests.request', side_effect=mocker.mocked_requests_request)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
def test_ai_init(mock_request, mock_post):
	lab_connection_args = {}
	pennai = AI()

@patch('requests.request', side_effect=mocker.mocked_requests_request)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
def test_ai_random_recommender(mock_request, mock_post):
    lab_connection_args = {}
    pennai = AI()

@patch('requests.request', side_effect=mocker.mocked_requests_request_no_datasets)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
@patch('time.sleep', side_effect=[None, None, SystemExit]) #Third time time.sleep() is called, SystemExit exception is raised
@patch('sys.argv', ["a", "b"])
def test_main_command_line_exit_with_exception(mock_request, mock_post, mock_sleep):
    testargs = ["ai"]
    with patch.object(sys, 'argv', testargs):
        aiProc = ai.ai.main()

@patch('requests.request', side_effect=mocker.mocked_requests_request)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
@patch('time.sleep', side_effect=[None, None, SystemExit]) #Third time time.sleep() is called, SystemExit exception is raised
@patch('sys.argv', ["a", "b"])
def test_main_command_line_exit_with_exception_running_exp(mock_request, mock_post, mock_sleep):
    testargs = ["ai"]
    with patch.object(sys, 'argv', testargs):
        aiProc = ai.ai.main()

@nottest
@raises(Exception)
@patch('requests.request', side_effect=mocker.mocked_requests_request_invalid_launch_experiment)
@patch('requests.post', side_effect=mocker.mocked_requests_post)
@patch('time.sleep', side_effect=[None, None, None, None, SystemExit]) #fifth time time.sleep() is called, SystemExit exception is raised
@patch('sys.argv', ["a", "b"])
def test_main_command_line_queue_exception(mock_request, mock_post, mock_sleep):
    """
    exception should be raised when trying to parse the result launch_experiment()
    """
    testargs = ["ai"]
    with patch.object(sys, 'argv', testargs):
        aiProc = ai.ai.main()