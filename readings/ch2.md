# Installing the Sample Application
- application code vs test code

# Writing Knowledge-Building Tests
- not exhaustive: no corner cases, failure cases
- try to understand how the datastructure works

# Using assert Statements
- just use `assert <expression>`
- **assertion rewriting**: intercepts `assert` calls and replaces them with information

# Failing with pytest.fail() and Exceptions
- not only assertion failures, but raised exceptions also make tests fail
- so what is the mechanism?
  - basically, a test fails if there is a raised exception
  - either just an exception, or `AssertionError` by an assertion failure, or `pytest.fail()` call which also raises an exception

- `pytest.fail`: no assertion rewriting(not much info) / but useful in an assertion helper

# Writing Assertion Helper Functions
- **assertion helper**: a function that is used to wrap up a complicated assertion check => kind of customized assertion
- using `pytest.fail`
- `__tracebackhide__`

# Testing for Expected Exceptions

```py
with pytest.raises(MyException, match=match_regex):
  # statements that raises 'MyException'

with pytest.raises(MyException) as exc_info:
  # statements that raises 'MyException'

# do sth with exc_info
```

# Structuring Test Functions
- **Arrange-Act-Assert** / **Given-When-Then**: separate a test into stages
  - getting ready to do sth
  - do sth
  - check to see if it worked

- a common antipattern: arrange-assert-act-assert-act-assert ...
  - not focusing on testing one specific behavior
  - hard for other developers to understand the purpose of the test

# Grouping Tests with Classes
- organizing tests into a set of groups
- you don't have to stick to class-related OOP practices

# Running a Subset of Tests
- running only a small amount of tests(not all) => good for debugging
- pattern: `pytest -k <pattern>`
  - run tests that contain a substring that matches the pattern
  - if you want to exclude a certain pattern: `pytest -k "<pattern> and not <excluded_pattern>"`
  - more advanced filtering: `or, not, and` keywords
