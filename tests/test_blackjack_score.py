from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  # Arrange
  # Face cards should add ten to score
  hand = ["King", 5]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 15

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = [9, "Ace"]

  score = blackjack_score(hand)

  assert score == 20


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = [2, "Ace", "King"]

  score = blackjack_score(hand)

  assert score == 13

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [5, 1]

  score = blackjack_score(hand)

  assert score == "Invalid card"


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, "Ace", "Jack", 8, 9, 4]

  score = blackjack_score(hand)

  assert score == "Invalid hand length"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [10, "King", "Ace", "Queen"]

  score = blackjack_score(hand)

  assert score == "Bust"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ["Ace", "Ace", "King"]

  score = blackjack_score(hand)

  assert score == 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    hand = ["Ace", "Ace", "Ace", "Ace"]

    score = blackjack_score(hand)

    assert score == 14