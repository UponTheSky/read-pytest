# Installing pytest
- venv, pip, pypi

# Running pytest

## Test Discovery
- how pytest looks for the files(**test discovery**)
  - no specification / filename(s) / directory(s)
  - specific functions: `pytest <filepath>::<function_name>`
  - naming convention: start with `test_`(filename, function) / `Test`(class)

- flags:
  - `-v`(verbose)
  - `--tb=no`(no tracebacks)

## Test Outcomes
- passed, failed, skipped(`@pytest.mark.skip()`, `@pytest.mark.skipif()`)
- xfail(this test should fail: `@pytest.mark.xfail`), xpass
- error(exception happened either during the execution of a fixture, or hook function)