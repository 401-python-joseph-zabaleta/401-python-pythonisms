import pytest

from pythonisms.ll_iterator import LinkedList


def test_str():

    ll = LinkedList([1, 2, 3])

    actual = str(ll)
    expected = '{ 1 } --> { 2 } --> { 3 } --> None'

    assert actual == expected

def test_for_in():

    ll = LinkedList([1, 2, 3])

    items_list = []

    for item in ll:
        items_list.append(item)

    assert items_list == [1, 2, 3]


def test_list_comprehension():

    ll = LinkedList([1, 2, 3])

    increased_ll = [item + 1 for item in ll]

    assert increased_ll == [2, 3, 4]

def test_list_cast():
    items_list = [1, 2, 3]

    ll = LinkedList(items_list)

    assert list(ll) == items_list

def test_range():
    num_range = range(1,20)

    ll = LinkedList(num_range)

    assert len(ll) == 19

def test_next():

    ll = LinkedList([1, 2, 3])

    iterator = iter(ll)

    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

def test_stop_iteration():

    ll = LinkedList([1, 2, 3])

    iterator = iter(ll)

    with pytest.raises(StopIteration):
        while True:
            ll = next(iterator)

def test_equals():
    ll_a = LinkedList([1, 2, 3])
    ll_b = LinkedList([1, 2, 3])

    assert ll_a == ll_b

def test_get_item():

    ll = LinkedList([1, 2, 3])

    assert ll[2] == 3

def test_get_item_index_error():
    ll = LinkedList([1, 2, 3])

    with pytest.raises(IndexError):
        ll[10000000000]