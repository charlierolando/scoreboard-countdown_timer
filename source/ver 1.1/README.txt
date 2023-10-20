Very simple Scoreboard and Countdown Timer GUI using Tkinter (ver 1.1)
• How to use: https://github.com/charlierolando/scoreboard-countdown_timer/tree/main#how-to-use
- pip install tk
- python scoreboard+timer_countdown.py

• Editing tools: https://github.com/charlierolando/scoreboard-countdown_timer/tree/main#editing-tools
- Change default Timer value:
  - TIMER_DEFAULT_VAL = 10  # Default starting time: 10 seconds
- Change default Team name:
  - team_name = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"] # set team name
- Change default Font sizes:
  - DISPLAY_SCORE_FONT_SIZES_MULTIPLIER = 3.2 # 3.5 # set score font sizes multiplier
- Change default Countdown pos:
  - Cannot change the default Countdown position because the position is adaptive to the screen width

• Note:
- 'score.txt' will be created to store score data
- 'audio1.wav'to play a sound when time is up
- 'audio2.wav' to play a sound when time is 3s left
- charlierolando.github.io