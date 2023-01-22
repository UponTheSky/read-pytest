- fixtures?
  - functions run by pytest before(sometimes after) the actual test functions
  - prepare for a data set, a known state
  - setup & teardown, scope, using multiple fixtures
  - tracing code execution through fixtures and test code

# Getting Started with Fixtures
- fixture: the fixture function itself, or the data it provides
- fixture in pytest: getting ready & cleaning up
- if an exception occurs at a fixture, it is not treated as a failure(as in the test code), but as an Error

# Using Fixtures for Setup and Teardown
- preparing and cleaning up the resources in a function is not desirable
- overall structure:

```py
@pytest.fixture
def data():
  resource = get_some_resource()

  yield resource

  clean_up_resource(resource)

def test_some_test(data):
  assert data == 1
```
- remark
  - the code after `yield`(teardown) is guaranteed to run regardless of what happens during the test
  - even when an exception is raised, or the assert fails

- you can use a fixture in multiple tests(for each!)

# Tracing Fixture Execution with –setup-show
- tracing from setup, test, to teardown
- `--setup-show` flag
- `F` means "function" scope(each function)

# Specifying Fixture Scope
- scope?  
  - defines the order of when the setup and teardown run relative to running of all the test functions using the fixture
  - how often the setup and teardown get run, when it's used by multiple test functions

- default: function scope
  - the setup portion of the fixture will run before each test that calls it(teardown is the same)

- how about a big and time consuming fixture?: too slow to run all the tests
  - it's better to have such a fixture to be run only once for all the tests
  - scope: function, class, module, package, session

```py
@pytest.fixture(scope="module")
def data():
  # ...
```

- the scope of a fixture is defined at the definition of it, not at the place where it is called
  - but except `session` and `package`!: these scopes are to be defined and effective only in `conftest.py` file(otherwise they're just like `module` scope)
- the test functions using a fixture don't control how often a fixture is set up and torn down

# Sharing Fixtures through conftest.py
- `conftest.py`: sharing fixtures among multiple test files
  - defined in the same directory or parent directory 

- a fixture can depend on other fixtures of their same scope or wider
- don't import `conftest.py`

# Finding Where Fixtures Are Defined
- fixtures are to be found either in a single test module or `conftest.py` files in multiple directories
- to find where our fixtures are, flag: `--fixtures`
- `--fixtures-per-test`: see what fixtures are used by each test and where the fixtures are defined

# Using Multiple Fixture Levels
- when fixtures depend on other fixtures, they can only use fixtures that have equal or wider scope

# Using Multiple Fixtures per Test or Fixture
- rather than separately defining fixtures(methods), we may return a bunch of data in a single fixture
- a fixture can also depending on other multiple fixtures, of course, of the same or wider scope

# Deciding Fixture Scope Dynamically
- at runtime, via command flag, we may change the scope of a fixture
- see: https://docs.pytest.org/en/6.2.x/fixture.html?highlight=dynamic#dynamic-scope

# Using autouse for Fixtures That Always Get Used
- `autouse=True`: automatically called fixture
- code that you want to run at certain times
- `-s` = `--capture=no`: tell pytest to turn off output capture(so that we can see the output of `print` function)
- not much recommended: choose named fixtures if possible

# Renaming Fixtures

```py
@pytest.fixture(name="some-fancy-name")
def hey():
  return 1
```

- you can just list this fixture as `some-fancy-name` instead of `hey`
- useful when you already have a variable name that is widely used(like `app`, `server`)
