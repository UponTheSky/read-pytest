- *markers*: a way to tell pytest that there's something special about a particular test
    - just like a tag or label
    - for any reason that you have for separating out some tests

# Using Builtin Markers
- most commonly used: `parametrize, skip, skipif, xfail`

# Skipping Tests with pytest.mark.skip
- skip the test you want it to be skipped
    - e.g.: testing for not yet implemented features
    - `reason=<str>`: `<str>` part specifies the reason for skipping this test(for documentation purpose)

-  `-ra`
    - `-r`: tells pytest to report reasons for different test results at the end of the session(default is the same as `-rfE`)
    - `-a`: all except passed

# Skipping Tests Conditionally with pytest.mark.skipif
- if we want to skip a test function in a certain condition
- for example, different OS system ....

# Expecting Tests to Fail with pytest.mark.xfail
- we know that this test **should** fail: `pytest.mark.xfail(condition, reason, run, strict)`
- `condition, reason`: same as `skipif`
- `run`: you can choose the function to be skipped by not running it
- `strict`: if you want to check strictly that this test should fail(not allowing xpass), set it as `True`

- results:
    - `XFAIL`: failing as expected
    - `XPASS`: unexpected success(when strict=False)
    - `FAILED`: unexpected success(when strict=True)

- so why we're using it?
    - TDD: you know at first this test will fail, so mark it as xfail
    - temporary mark: a feature needs fixing but you can't do it right away

- not recommended
    - thinking of implementing them in the future
    - YAGNI('Ya Aren't Gonna Need It'): allways implement things when you actually need them

# Selecting Tests with Custom Markers
- for some special cases, we want to segment a subset of tests
    - *smoke*: about the main system
    - *exception*: expected exceptions

- `-m <your_custom_mark>`: run only tests marked as `<your_custom_mark>`
- how to register custom markers?: `pytest.ini`
    - `<marker_name>:<description>`

```ini
[pytest]
markers = 
    smoke: subset of tests
```

# Marking Files, Classes, and Parameters
- files
    - if pytest sees a `pytestmark` attribute in a test module, it will apply the markers to 
      all the tests in that module
    - if you want multiple markers, then use list

- classes: applies to all the methods within that class

- parametrized cases

```py
@pytest.mark.parametrize(
    "start_state",
    ["todo", pytest.param("in prog", marks=pytest.mark.smoke), "done"]
)
```

- fixture: applies to all the tests using this fixture

```py
@pytest.fixture(
    params=["todo", pytest.param("in prog", marks=pytest.mark.smoke), "done"]
)
```

# Using “and,” “or,” “not,” and Parentheses with Markers
- just like when we're using the keyword option(`-k`), we can use `and, or, not` and parentheses to
  filter some test cases
- of course, we can combine it with `-k` option as well

# Being Strict with Markers
- `--strict-markers`: when we missspel a marker, then we get an error instead of a warning
- always recommended: error is easy to catch than warning, so useful in CI/CD pipelines
- you can set it also in `pytest.ini`

```py
[pytest]
addopts = 
    --strict-markers
```

# Combining Markers with Fixtures
- how to flexibly change the fixture already defined?
- customized marker:
    - first we declare a marker
    - then we modify the fixture to detect if the marker is used
    - and then read the value supplied as a marker parmeter to figure out how many cards to prefill

- `faker`: pytest fixture that randomly generate fake data

```py
@pytest.fixture
def cards_db(session_cards_db, request, faker):
    # ...

    fake.seed_instance(101)
    m = request.node.get_closest_marker('num_cards')
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(Card(summary=faker.sentence(), owner=faker.first_name()))
    
    return db
```

- `request.node`: pytest's representation of a test
- `get_closest_marker`: returns a `Marker` object if the test is marked with `num_cards`
    - "closest": function, class, module... pick the closest one

# Listing Markers
- `pytest --markers`
