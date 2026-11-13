
from hypothesis import given, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread


# -------------------------------------------------
# 1. FUZZ TESTS: Check that invalid inputs do not crash
# -------------------------------------------------

@given(st.text() | st.none())
def test_parse_score_no_crash(s):
    result = parse_score(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and all(isinstance(x, int) for x in result)
    )


@given(st.text() | st.none())
def test_game_lead_no_crash(s):
    result = game_lead(s)
    assert result is None or isinstance(result, int)


@given(st.text() | st.none())
def test_set_spread_no_crash(s):
    result = set_spread(s)
    assert result is None or isinstance(result, int)


# -------------------------------------------------
# 2. VALID INPUT TESTS: Verify correct calculations
# -------------------------------------------------

@given(
    st.integers(min_value=0, max_value=10000),
    st.integers(min_value=0, max_value=10000)
)
def test_parse_score_valid(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


@given(
    st.sampled_from(['0', '15', '30', '40']),
    st.sampled_from(['0', '15', '30', '40'])
)
def test_game_lead_valid(a, b):
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    assert game_lead(f"{a}-{b}") == points[a] - points[b]


@given(
    st.lists(
        st.integers(min_value=0, max_value=10000),
        min_size=1,
        max_size=50
    )
)
def test_set_spread_valid(games):
    games_csv = ','.join(map(str, games))
    assert set_spread(games_csv) == max(games) - min(games)


# -------------------------------------------------
# 3. EDGE CASE TESTS
# -------------------------------------------------

def test_parse_score_edge_cases():
    assert parse_score("3-2") == (3, 2)
    assert parse_score("1,,2") is None
    assert parse_score("abc-def") is None
    assert parse_score("1-2-3") is None
    assert parse_score(None) is None


def test_game_lead_edge_cases():
    assert game_lead("40-30") == 1
    assert game_lead("0-40") == -3
    assert game_lead("50-30") is None
    assert game_lead("abc") is None
    assert game_lead(None) is None


def test_set_spread_edge_cases():
    assert set_spread("6,4,7") == 3
    assert set_spread("5") == 0
    assert set_spread("") is None
    assert set_spread("1,,3") is None
    assert set_spread("abc,3") is None
    assert set_spread(None) is None
