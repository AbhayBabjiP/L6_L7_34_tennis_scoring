"""Lab 6, stage 1: exercise normal game, set and match scoring paths."""

import pytest
from tennis_scoring import game_score, set_winner, match_status


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, "0-0"), (1, 2, "15-30"), (2, 3, "30-40"),
    (3, 3, "deuce"), (5, 5, "deuce"),
    (4, 3, "advantage A"), (3, 4, "advantage B"),
    (5, 3, "game A"), (3, 5, "game B"),
    (4, 0, "game A"), (0, 4, "game B"),
])
def test_game_scores(a, b, expected):
    assert game_score(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 4, "A"), (4, 6, "B"), (7, 6, "A"), (6, 7, "B"),
    (3, 2, None), (5, 5, None), (6, 5, None), (6, 6, None),
])
def test_set_scores(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize("a,b,best_of,expected", [
    (2, 0, 3, "A wins"), (0, 2, 3, "B wins"),
    (1, 1, 3, "decider"), (0, 0, 3, "in progress"),
    (3, 1, 5, "A wins"), (1, 3, 5, "B wins"),
    (2, 2, 5, "decider"), (1, 0, 5, "in progress"),
])
def test_match_scores(a, b, best_of, expected):
    assert match_status(a, b, best_of) == expected
