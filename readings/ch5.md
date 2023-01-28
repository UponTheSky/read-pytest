- how to run many test cases with only one test function?
- **parametrization**: adding parameters to our test functions and passing in multiple sets of arguments, 
  to test to create new test cases

- how to parametrize?: in this order:
    - functions
    - fixtures
    - hook function: `pytest_generate_tests`

# Testing Without Parametrize
- to fully test a function, we need to feed more edge cases as much as possible
- parametrized testing: sending multiple sets of data through the same test
- without parametrized testing: repeating the same logic with only different inputs => ineffcient
    - but what if just running a loop inside a test function?
    - only single test case: hard to detect which case causes the problem
    - moreover, if one case fails, then the subsequent iterations stop

# Parametrizing Functions
- use `@pytest.mark.parametrize()` decorator for each test function

```py
@pytest.mark.parametrize(
    "argname1, argname2",
    [(arg1_1, arg2_1), (arg1_2, arg2_2)]
)
```

# Parametrizing Fixtures
- if a fixture is parametrized, then the test functions depending on this fixture is run several times

```py
@pytest.fixture(params=['a', 'b', 'c'])
def state(request):
    return request.param
```
- why use in a fixture?
    - when the input is related to setup/teardown logics
    - when multiple tests are depending on the same fixture

# Parametrizing with pytest_generate_tests
- hook function: `pytest_generate_tests`
- *hook function*: 
    - often used by plugins to alter the normal operation flow of pytest
    - defined in test files and conftest.py

```py
def pytest_generate_tests(metafunc):
    if 'arg1' in metafunc.fixturenames:
        metafunc.parametrize('arg1', ['a', 'b', 'c'])
```

- this method is useful since we can directly modify the parametrization list(`['a', 'b', 'c']`)
    - we could base our parametrization list on a command-line flag: `metafunc.config.getoption('--myflag')`
    - if one argument is related to another argument's presence
    - could parametrize two related parameters at the same time

# Using Keywords to Select Test Cases
- using `-k` to select from many test cases made from parametrization
- `-k <name_of_the_parameter_you_want_to_select>`
