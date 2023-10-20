# scoreboard+timer_countdown.py ver 1.1
# charlierolando.github.io

import tkinter as tk # pip install tk
import time
import winsound

# from tkinter import messagebox

TIMER_DEFAULT_VAL = 10  # Default starting time: 10 seconds

team_name = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"] # set team name

DISPLAY_SCORE_FONT_SIZES_MULTIPLIER = 3.2 # 3.5 # set score font sizes multiplier

# Try to open score.txt on read mode (r)
# If file not found, make score.txt
try:
    with open('score.txt', 'r') as score:
        lines = score.readlines()
except FileNotFoundError:
    save_this = ['0', '0', '0', '0', '0']
    for i in range(5):
        save_this[i] = save_this[i] + '\n'
    with open('score.txt', 'w') as score:
        score.writelines(save_this)
    with open('score.txt', 'r') as score:
        lines = score.readlines()
        
class Scoreboard_CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer and Scoreboard - charlierolando.github.io")

        self.centre_point_x = int(self.root.winfo_width() * 0.5)
        
        self.time_remaining = tk.IntVar()
        self.time_remaining.set(TIMER_DEFAULT_VAL)
        self.is_running = False
        
        self.minutes = self.time_remaining.get() // 60
        self.seconds = self.time_remaining.get() % 60

        # Bind the on_resize function to the window resize event
        self.root.bind("<Configure>", self.on_resize)

        ### display score
        self.points = [int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4])]
        
        self.label_teams = []
        self.label_points = []
        
        self.label_ = tk.Label(root, text="", font=("Helvetica", int(10*DISPLAY_SCORE_FONT_SIZES_MULTIPLIER)))
        self.label_.grid(row=1, columnspan="10", pady=65)
        
        for i in range(5):
            self.label__ = tk.Label(root, text="", font=("Helvetica", int(20*DISPLAY_SCORE_FONT_SIZES_MULTIPLIER)))
            self.label__.grid(row=i+2, column=0, padx=8, sticky="w")

            team_label = tk.Label(root, text=team_name[i], font=("Helvetica", int(20*DISPLAY_SCORE_FONT_SIZES_MULTIPLIER)))
            team_label.grid(row=i+2, column=1, sticky="w")
            self.label_teams.append(team_label)
            
            self.label___ = tk.Label(root, text=":", font=("Helvetica", int(20*DISPLAY_SCORE_FONT_SIZES_MULTIPLIER)))
            self.label___.grid(row=i+2, column=2, sticky="w")
            
            points_label = tk.Label(root, text=str(self.points[i]), font=("Helvetica", int(20*DISPLAY_SCORE_FONT_SIZES_MULTIPLIER)))
            points_label.grid(row=i+2, column=3, padx=22, sticky="w")
            self.label_points.append(points_label)
            
            btn_increase = tk.Button(root, text="+", command=lambda i=i: self.update_points(i, 25))
            btn_increase.grid(row=i+2, column=4, padx=5, sticky="w")
            
            btn_decrease = tk.Button(root, text="-", command=lambda i=i: self.update_points(i, -25))
            btn_decrease.grid(row=i+2, column=5, padx=5, sticky="w")
        ### display score

        ### time countdown        
        self.label_timer = tk.Label(root, text="00:00", font=("Helvetica", 120), highlightthickness=0, bd=0)
        self.label_timer.place(x=self.centre_point_x, y=8+75, anchor=tk.CENTER)
        self.label_timer.config(text=f"{TIMER_DEFAULT_VAL // 60:02}:{TIMER_DEFAULT_VAL % 60:02}")
        
        self.timer_label = tk.Label(root, textvariable=self.format_time(), font=("Helvetica", 60))
        self.timer_label.grid(pady=0, bg=None)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.place(x=self.centre_point_x+34, y=8+160, anchor=tk.CENTER)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.place(x=self.centre_point_x+93, y=8+160, anchor=tk.CENTER)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.place(x=self.centre_point_x+153, y=8+160, anchor=tk.CENTER)
        self.reset_button.config(state=tk.DISABLED)
        
        self.time_label = tk.Label(root, text="Time (seconds):", font=("Helvetica", 12))
        self.time_label.place(x=self.centre_point_x-121, y=8+160, anchor=tk.CENTER)
        
        self.time_entry = tk.Entry(root, textvariable=self.time_remaining, font=("Helvetica", 12), width=4)  # Set the width to 4 characters
        self.time_entry.place(x=self.centre_point_x-41, y=8+160, anchor=tk.CENTER)
        
        """
        self.update_points_button = tk.Button(root, text="Update Points", command=self.update_points_button)
        self.update_points_button.place(x=self.centre_point_x+120, y=8+160, anchor=tk.CENTER)
        """
        ### time countdown

        # self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # self.label.grid(pady=0, bg=None)

    """
    def update_points_button(self):
        self.points = [int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4])]
        for i in range(5):
            self.label_points[i].config(text=str(self.points[i]))
    """
    
    def on_resize(self, event):            
        # Ubah nilai offset lapangan
        self.centre_point_x = int(self.root.winfo_width() * 0.5)
        
        self.label_timer.place(x=self.centre_point_x, y=8+75, anchor=tk.CENTER)
        self.start_button.place(x=self.centre_point_x+34, y=8+160, anchor=tk.CENTER)
        self.pause_button.place(x=self.centre_point_x+93, y=8+160, anchor=tk.CENTER)
        self.reset_button.place(x=self.centre_point_x+153, y=8+160, anchor=tk.CENTER)
        self.time_label.place(x=self.centre_point_x-121, y=8+160, anchor=tk.CENTER)
        self.time_entry.place(x=self.centre_point_x-41, y=8+160, anchor=tk.CENTER)
        # self.update_points_button.place(x=self.centre_point_x+120, y=8+160, anchor=tk.CENTER)

    def update_points(self, team_index, value):
        self.points[team_index] += value
        self.label_points[team_index].config(text=str(self.points[team_index]))

        save_this = ['', '', '', '', '']
        for i in range(5):
            save_this[i] = str(self.points[i]) + '\n'
    
        # Open file .txt on write mode (w)
        with open('score.txt', 'w') as score:
            score.writelines(save_this)
        
    def format_time(self):
        self.minutes = self.time_remaining.get() // 60
        self.seconds = self.time_remaining.get() % 60
        return f"{self.minutes:02}:{self.seconds:02}"
        
    def start_timer(self):
        self.reset_button.config(state=tk.DISABLED)
        if not self.is_running and self.time_remaining.get() > 1:
            time.sleep(0.5) # delay 0.5s
            self.is_running = True
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.time_entry.config(state=tk.DISABLED)
            
    def update_timer(self):
        if self.time_remaining.get() > 1 and self.is_running:
            self.time_remaining.set(self.time_remaining.get() - 1)
            self.timer_label.config(text=self.format_time())
            self.root.after(1000, self.update_timer)
            self.label_timer.config(text=f"{self.minutes:02}:{self.seconds:02}")
            self.label_timer.configure(fg="black")
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
        
            if self.time_remaining.get() == 3:
                # Play a sound when time is 3s left
                winsound.PlaySound("audio2.wav", winsound.SND_ASYNC)

        elif self.time_remaining.get() > 0 and self.is_running:
            # Play a sound when time is up
            winsound.PlaySound("audio1.wav", winsound.SND_ASYNC)

            # messagebox.showinfo("Timer Expired", "Time's up!")

            self.time_remaining.set(self.time_remaining.get() - 1)
            self.timer_label.config(text=self.format_time())
            self.root.after(1000, self.update_timer)
            self.label_timer.config(text=f"{self.minutes:02}:{self.seconds:02}")

            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.time_entry.config(state=tk.NORMAL)
            self.label_timer.configure(fg="red")

        else:
            self.is_running = False
            self.pause_button.config(state=tk.DISABLED)
            self.time_entry.config(state=tk.NORMAL)
            self.label_timer.configure(fg="red")
            self.reset_button.config(state=tk.NORMAL)


    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        if not self.is_running:
            self.time_remaining.set(int(self.time_entry.get()))
            self.timer_label.config(text=self.format_time())
            self.time_remaining.set(TIMER_DEFAULT_VAL)
            self.label_timer.config(text=f"{TIMER_DEFAULT_VAL // 60:02}:{TIMER_DEFAULT_VAL % 60:02}")
            self.label_timer.configure(fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    GUI = Scoreboard_CountdownTimer(root)
    root.mainloop()
