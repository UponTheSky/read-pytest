import pytest
from cards import Card

def test_start_from_done(cards_db):
    index = cards_db.add_card(Card("second edition", state="done"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second edition", state="in prog"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

def test_start_from_todo(cards_db):
    index = cards_db.add_card(Card("second edition", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

@pytest.mark.parametrize('state', ['done', 'in prog', 'todo'])
def test_start_param_function(cards_db, state):
    index = cards_db.add_card(Card("second edition", state=state))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

@pytest.fixture(params=['done', 'in prog', 'todo'])
def state(request):
    return request.param

def test_start_param_fixture(cards_db, state):
    index = cards_db.add_card(Card("second edition", state=state))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'

def pytest_generate_tests(metafunc):
    if 'state_' in metafunc.fixturenames:
        metafunc.parametrize('state_', ['done', 'in prog', 'todo'])
        
def test_start_param_hook(cards_db, state_):
    index = cards_db.add_card(Card("second edition", state=state_))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'
