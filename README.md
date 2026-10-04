# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game is to guess the random number and will output an score based on the attempts made. 
- [ ] Detail which bugs you found.
I found 4 different bugs within the game, first being the logic error with the hints, as guess is higher than the actual secret number it tells users to "go higher" rather than "go lower". The second logic error that occurred was for the different ranges of guesses depending on the difficulty, as the normal level seem to have a higher difficulty compared to hard. For UI errors I found that the initial screen inaccurately displays the number of attempts left. For example, in the "normal" level it would display 7 attempts rather than 8 which is the preset number of attempts. Lasgt I noticed that the new game button did not work. 
 [ ] Explain what fixes you applied.
First I applied the logic error with the ranges, I asked AI to change the ranges to be in order of difficulty, so the more difficult the level was the higher the range. While I fixed this error, the AI also fixed the the attempts display along with it. Next I worked on the logic error with the guesses, as I asked to move the method while correcting the go higher/lower error. Lastly I asked AI to fix the issue with the "new game" button. As I was looking through the code, I asked AI to look at the app.py code specifically when it changes the states and resets the game ads a whole. 
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1.User enters a guess of 23
2. Game returns "Too Low Guess HIGHER"
3. Score is updated after each guess.
4. User enters 45, and game shows "Too high guess LOWER" 
5. Game ends after user correctly guesses or used up their amount of attemtpts. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
