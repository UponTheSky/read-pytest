import pytest

@pytest.fixture
def list_data():
  """
  This is list_data fixture
  """
  return [1, 2, 3, 4, 5]

@pytest.fixture(scope='module')
def tuple_data():
  print('-- tuple setup --')
  yield ('a', 'b', 'c')
  print('-- tearing down the tuple --')

def test_list(list_data):
  number = 3
  assert number in list_data

def test_tuple(tuple_data):
  char = 'd'
  assert char in tuple_data

def test_tuple2(tuple_data):
  assert len(tuple_data) == 3
