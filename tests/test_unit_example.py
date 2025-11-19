import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # add project root

from app import add_item_to_list

def test_add_item_to_list_adds_non_empty_string():
    data = []
    add_item_to_list(data, "Milk")
    assert data == ["Milk"]


def test_add_item_to_list_ignores_empty_string():
    data = []
    add_item_to_list(data, "")
    assert data == []