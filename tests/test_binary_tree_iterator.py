import pytest

from pythonisms.binary_tree_iterator import BinarySearchTree

def test_for_in():
    tree = BinarySearchTree([1, 22, 3, 4, 5])
    actual = tree.pre_order()
    expected = [1, 22, 3, 4, 5]
    assert actual == expected
