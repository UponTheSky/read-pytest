import pytest

pytestmark = pytest.mark.all

@pytest.mark.odd
def test_one():
    pass


def test_two():
    pass

@pytest.mark.odd
def test_three():
    pass

@pytest.mark.testclass
class TestClass:
    def test_four(self):
        pass

    @pytest.mark.odd
    def test_five(self):
        pass


@pytest.mark.parametrize("x", [6, 7])
def test_param(x):
    pass
