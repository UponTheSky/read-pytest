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

# Using monkeypatch
- but rather than using `capsys` fixture, it is better off using "Typer" library(`typer.testing.CliRunner`)
- **monkeypatch**: a dynamic modification of a class or module during runtime -> why use it?
  - replacing input/output dependencies with objects or functions for testing
  - when a test ends, regardless of pass or fail, the original unpatched code is restored

- when mocking an imported library, you need to patch from the *module that imports that library* first, rather than the library itself

```py
monkeypatch.setattr(cards.cli.pathlib.Path, "home", fake_home)
```

# design for testability
- add functionality to SW to make it easier to test
  - undocumented API or parts of the API that are turned off for release
  - or the API is extended and made public
 