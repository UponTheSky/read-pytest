from unittest import mock
import my_info


def test_my_home_returns_correct_value():
    with mock.patch.object(my_info, 'home_dir', return_value='/users/fake_user'):
        value = my_info.home_dir()
        assert value == "/users/fake_user"


def test_my_home_is_called():
    with mock.patch.object(my_info.Path, 'home') as mocked_home:
        my_info.home_dir()
        mocked_home.assert_called_once()
    # check to see if Path.home() was called
