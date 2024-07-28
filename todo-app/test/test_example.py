import pytest

def test_equal_or_not():
  assert 3 == 3

def test_instance_of():
  assert isinstance("hello", str) is True
  assert isinstance("10", int) is not True

def test_boolean():
  assert (3 == 3) is True
  assert ("hello" == "test") is not True

def test_list():
  add = [1,3,5,7,9]
  false_list = [False, False]
  assert 1 in add
  assert 6 not in add 
  #assert all(add) is True
  #assert any(false_list) is True

class Employee:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name

#fixture
@pytest.fixture
def default_employee():
  return Employee("Pandiarajan", "Rajagopal", 32)


def test_employee_data(default_employee):
  assert default_employee.first_name == "Pandiarajan"