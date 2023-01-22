# Using tmp_path and tmp_path_factory
- `tmp_path`: function-scope
- `tmp_path_factory`: session-scope, `mktemp(<sub_dir>)`, for creating multiple temporary directories
- except these points, other things are almost identical

```py
def test_tmp_path(tmp_path):
  file = tmp_path / 'file.txt'
  file.write_text('hello')

  assert file.read_text() == 'hello'

def test_tmp_path_factory(tmp_path_factory):
  path = tmp_path_factory.mktemp('sub')
  file = path / 'file.txt' 
  file.write_text('hello')
  # ...
```

- the path remains for a while in case of failure tests
- pytest eventually cleans up the test data 

# Using capsys
- capsys: enables the capturing of writes to stdout and stderr
- rather than calling `subprocess.run`, we call the method that implements a command in the CLI directly, and 
use capsys to read the output

```py
def test_version_v2(capsys):
  card.cli.version()
  output = capsys.readouterr().out.rstrip()
  # ...
```
- also we can disable pytest's functionality of capturing normal output
