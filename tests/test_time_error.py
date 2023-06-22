from lib.time_error import *
from unittest.mock import Mock

def test_time_error():
    requester_mock = Mock()
    response_mock = Mock()
    timer_mock = Mock()
    time_error = TimeError(requester_mock, timer_mock)

    timer_mock.time.return_value = 1687426002.5
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1687426002}

    assert time_error.error() == -0.5

    # response_mock_return_value = 1687426002 
