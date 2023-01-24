import pytest
import os
import hello_world

words = "Hello World!\n"
filename = 'hello.txt'

def test_without_fixture():
  curr_dir = os.path.dirname(hello_world.__file__)
  file = f'{curr_dir}/{filename}'

  # hello_world.hello()

  with open(file, 'r') as f:
    assert f.read() == words
    
def test_with_fixture(tmp_path, monkeypatch):
  monkeypatch.chdir(tmp_path)

  file = f'{tmp_path}/{filename}'

  # hello_world.hello()

  # print(tmp_path)

  with open(file, 'r') as f:
    assert f.read() == words