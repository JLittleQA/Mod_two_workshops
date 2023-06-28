import Pycharmproject
import pytest

def setup():
    Pycharmproject.lib_catagory_num= [{'Id': 9, 'book': '1984'}, {'Id': 8, 'book': 'Animal Farm'}]

def test_addItem(): 
    assert Pycharmproject.addItem(10, "Dracula") == [{'Id': 9, 'book': '1984'}, {'Id': 8, 'book': 'Animal Farm'}, {'Id': 10, 'book': 'Dracula'}]
    assert Pycharmproject.addItem(11,"Frankenstein") == [{'Id': 9, 'book': '1984'}, {'Id': 8, 'book': 'Animal Farm'}, {'Id': 10, 'book': 'Dracula'}, {'Id': 11, 'book': 'Frankenstein'}]


def test_removeItem():
    assert Pycharmproject.removeItem(9) == [{'Id': 8, 'book': 'Animal Farm'}, {'Id': 10, 'book': 'Dracula'}, {'Id': 11, 'book': 'Frankenstein'}]
    assert Pycharmproject.removeItem(11) == [{'Id': 8, 'book': 'Animal Farm'}, {'Id': 10, 'book': 'Dracula'}]

def test_updateItem(): 
    assert Pycharmproject.updateItem(8, "Count of Monte Cristo") == [{'Id': 8, 'book': 'Count of Monte Cristo'}, {'Id': 10, 'book': 'Dracula'}]
    assert Pycharmproject.updateItem(10, "Oliver Twist") == [{'Id': 8, 'book': 'Count of Monte Cristo'}, {'Id': 10, 'book': 'Oliver Twist'}]

def tearDown(): 
    Pycharmproject.lib_catagory_num = []