import sys
import pytest
# tests run from StringFinder directory with "py.test"
sys.path.append("")
from Finder import Finder

# Test the initialization of the object
def test_object_const():
    object_ref = Finder(["apple"])
    assert object_ref.map_of_string_array == {"apple": {'a': 1, 'p': 2, 'l': 1, 'e': 1}}


def test_object_const_2():
    object_ref = Finder(["apple", "orange"])
    expected_map = {
                    "apple": {'a': 1, 'p': 2, 'l': 1, 'e': 1},
                    "orange": {'o': 1, 'r': 1, 'a': 1, 'n': 1, 'g': 1, 'e': 1}
                    }
    assert object_ref.map_of_string_array == expected_map


# Test different inputs for the find method
def test_find_func():
    object_ref = Finder(["apple", "orange", "peach", "banana"])
    assert object_ref.find("banana") == ["banana"]


def test_find_func2():
    object_ref = Finder(["bbaannaannaa", "banana", "bnnnaa"])
    assert object_ref.find("banana") == ["banana"]


def test_find_func3():
    object_ref = Finder(["ananab"])
    assert object_ref.find("banana") == ["ananab"]


def test_find_func4():
    object_ref = Finder(["banana"])
    assert object_ref.find("orange") == []


# Test large array (100000 strings)
@pytest.mark.timeout(1)
def test_find_func5():
    i = 0
    number_array = []
    while i < 100000:
        number_array.append(str(i))
        i = i + 1
    object_ref = Finder(number_array)
    assert object_ref.find("574") == ["457", "475", "547", "574", "745", "754"]


# Mass run of find function (50k runs)
@pytest.mark.timeout(5)
def test_find_func5():

    i = 0
    number_array = []
    while i < 100:
        number_array.append(str(i))
        i = i + 1
    object_ref = Finder(number_array)

    i = 0
    while i < 50000:
        object_ref.find(str(i))
        i = i + 1


# If array passes in something other than strings
def test_find_parameters_num():
    object_ref = Finder([1])
    assert object_ref.find("1") != ["1"]


# method works with symbols
def test_find_parameters_symbols():
    object_ref = Finder(["@$&-"])
    assert object_ref.find("$-&@") == ["@$&-"]


# method works with foreign characters e.g. umlaut
def test_find_parameters_foreign_chars():
    object_ref = Finder(["schöneberg"])
    assert object_ref.find("schöneberg") == ["schöneberg"]


# method works regardless of case
def test_find_parameters_case():
    object_ref = Finder(["OrAnGE"])
    assert object_ref.find("OrAnGE") == ["OrAnGE"]