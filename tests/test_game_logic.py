from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_easy_range():
    # Easy should be the smallest range
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    # Normal should be 1 to 50
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    # Hard should be 1 to 100 (previously 1 to 50, which was easier than Normal)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_range_increases_with_difficulty():
    # The upper bound should grow as difficulty goes up
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

def test_unknown_difficulty_falls_back_to_normal():
    # An unrecognized difficulty should use the Normal range
    assert get_range_for_difficulty("Unknown") == get_range_for_difficulty("Normal")

def test_hint_direction_matches_guess():
    # Regression test for swapped hints: a guess above the secret must say
    # go LOWER, and a guess below the secret must say go HIGHER.
    # Includes off-by-one guesses right next to the secret.
    secret = 50
    for guess in [51, 60, 100]:
        outcome, message = check_guess(guess, secret)
        assert outcome == "Too High"
        assert "LOWER" in message
        assert "HIGHER" not in message
    for guess in [1, 40, 49]:
        outcome, message = check_guess(guess, secret)
        assert outcome == "Too Low"
        assert "HIGHER" in message
        assert "LOWER" not in message


# --- New Game button regression tests (Streamlit UI) ---
from pathlib import Path
from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def _click_new_game(at):
    new_game_button = next(b for b in at.button if b.label.startswith("New Game"))
    new_game_button.click().run()


def test_new_game_after_win_lets_you_play_again():
    # Regression test: after winning, New Game used to leave status as "won",
    # so the app kept showing "You already won" and blocked new guesses.
    at = AppTest.from_file(APP_PATH).run()
    at.session_state.status = "won"
    at.session_state.score = 70
    at.session_state.history = [10, 25]
    at.run()
    assert any("already won" in s.value for s in at.success)

    _click_new_game(at)

    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0
    assert at.session_state.score == 0
    assert at.session_state.history == []
    assert not any("already won" in s.value for s in at.success)


def test_new_game_after_loss_lets_you_play_again():
    # Same bug applied to losing: "Game over" should go away after New Game.
    at = AppTest.from_file(APP_PATH).run()
    at.session_state.status = "lost"
    at.run()
    assert any("Game over" in e.value for e in at.error)

    _click_new_game(at)

    assert at.session_state.status == "playing"
    assert not any("Game over" in e.value for e in at.error)
