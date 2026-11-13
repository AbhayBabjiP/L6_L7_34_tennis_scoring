
from hypothesis import given, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread


@given(st.text() | st.none())
def test_parse_score_no_crash(s):
    parse_score(s)


@given(st.text() | st.none())
def test_game_lead_no_crash(s):
    game_lead(s)


@given(st.text() | st.none())
def test_set_spread_no_crash(s):
    set_spread(s)
