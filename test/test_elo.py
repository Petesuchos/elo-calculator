import pytest
from elopy.elo import transformed_rating, normalized_score, rating_variation, calculate_rating, invert_score


def test_transformed_rating():
    rating = 1000
    transformed = 10 ** (rating/400)
    assert transformed_rating(rating) == transformed


def test_normalized_score_win():
    assert normalized_score('win') == 1
    assert normalized_score('1') == 1
    assert normalized_score(1) == 1


def test_normalized_score_draw():
    assert normalized_score('draw') == 0.5
    assert normalized_score('tie') == 0.5
    assert normalized_score('0.5') == 0.5
    assert normalized_score(0.5) == 0.5


def test_normalized_score_loss():
    assert normalized_score('loss') == 0
    assert normalized_score('0') == 0
    assert normalized_score(0) == 0


def test_invert_score_win():
    assert invert_score('win') == 0
    assert invert_score('1') == 0
    assert invert_score(1) == 0


def test_invert_score_draw():
    assert invert_score('draw') == 0.5
    assert invert_score('tie') == 0.5
    assert invert_score('0.5') == 0.5
    assert invert_score(0.5) == 0.5


def test_invert_score_loss():
    assert invert_score('loss') == 1
    assert invert_score('0') == 1
    assert invert_score(0) == 1


def test_normalized_score_exception():
    with pytest.raises(ValueError) as e:
        normalized_score('xyz')
    assert e.value.args[0] == 'Invalid value for score. Choose from [win, draw, tie, loss, 1, 0.5, 0]'


def test_invert_score_exception():
    with pytest.raises(ValueError) as e:
        invert_score('xyz')
    assert e.value.args[0] == 'Invalid value for score. Choose from [win, draw, tie, loss, 1, 0.5, 0]'


def test_rating_variation():
    assert rating_variation(1000, 1000, 1, 20) == 10
    assert rating_variation(1000, 1000, 0, 20) == -10
    assert rating_variation(1000, 1000, 0.5, 20) == 0


def test_calculate_rating():
    assert calculate_rating(1000, 1000, 1, 20) == 1010
    assert calculate_rating(1000, 1000, 0, 20) == 990
    assert calculate_rating(1000, 1000, 0.5, 20) == 1000
    assert calculate_rating(1000, 1800, 1, 20, round_rating=True) == 1020
    assert calculate_rating(1000, 1800, 1, 20, round_rating=False) == pytest.approx(1019.8, 0.1)






