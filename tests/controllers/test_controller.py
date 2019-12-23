import pytest
from tests.fixtures import MockElasticsearch

from dkpostcodes.controllers.controller import Controller

def test_controller_class():
    id_ = 'testentity'
    data = {"code": "testentity", "name": "Test Entity"}

    # test a found entity
    a = Controller(id_, data)
    assert a.id == id_
    assert a.attributes["name"] == data["name"]
    assert a.found == True
    assert len(a.get_errors()) == 0

    # test internal functions
    assert a.parse_id(id_) == id_
    assert a.process_attributes(data) == data

    # test a non existant object
    a = Controller(id_, {})
    assert a.id == id_
    assert a.attributes.get("name") is None
    assert a.found == False
    assert len(a.get_errors()) == 1
    assert a.get_errors()[0]["status"] == '404' 

def test_controller_fetch():

    es = MockElasticsearch()

    a = Controller.get_from_es("TESTID", es, es_config={"es_index": "geo_postcode", "es_type": "_doc"})
    assert isinstance(a.id, str)
    assert len(a.attributes) > 4
    assert a.found == True
    assert len(a.get_errors()) == 0
