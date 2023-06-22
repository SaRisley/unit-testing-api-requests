from lib.cat_facts import *
from unittest.mock import Mock

def test_cat_facts():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"fact":"A cat's normal pulse is 140-240 beats per minute, with an average of 195.","length":73}

    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()
    assert result == "Cat fact: A cat's normal pulse is 140-240 beats per minute, with an average of 195."