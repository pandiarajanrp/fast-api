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
  assert all(add) is True
  assert any(false_list) is True