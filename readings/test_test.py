import pytest

@pytest.fixture
def one():
  print("before test: setup")

  yield 1

  print("after test: teardown")

def test_one(one):
  print("during the test")
  assert one == 1

def test_exception(one):
  raise Exception("exception")

def test_assertfail(one):
  assert one == 2