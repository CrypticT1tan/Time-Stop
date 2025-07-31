# Imported Files
from util import resource_path

# Imported Modules
import tkinter as tk
import math
from playsound3 import playsound
from PIL import Image, ImageTk

# General Class with attributes used for both time tools
class TimeApp:
    def __init__(self):
        # Formatting/style stuff
        self.font = "Helvetica"
        self.title_size = 30
        self.display_size = 45
        self.button_size = 15
        self.window_color = "#f0b8b8"

        # Creating main window
        self.window = tk.Tk()
        self.window.config(bg="#f0b8b8")
        self.window.title("Timer")

        # Setting up title Label
        self.title = tk.Label(text="TIMER", fg="red", font=(self.font, self.title_size, "bold"),
                           width=30, bg=self.window_color)
        self.title.grid(row=0, column=0, columnspan=2)

        # Creating the Timer Icon Image
        self.timer_icon_image = Image.open(resource_path("assets/timer_icon.png"))
        self.timer_icon_image_resized = self.timer_icon_image.resize((64, 64))
        self.timer_icon = ImageTk.PhotoImage(self.timer_icon_image_resized)

        # Creating the Stopwatch Icon Image
        self.stopwatch_icon_image = Image.open(resource_path("assets/stopwatch_icon.png"))
        self.stopwatch_icon_image_resized = self.stopwatch_icon_image.resize((64, 64))
        self.stopwatch_icon = ImageTk.PhotoImage(self.stopwatch_icon_image_resized)

        # Creating the Canvas for the Icons
        self.canvas = tk.Canvas(width=64, height=64, bg=self.window_color,
                                   highlightbackground=self.window_color)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.create_image(32, 32, image=self.timer_icon)

        # Creating the Entry Box for Timer
        self.timer_entry = tk.Entry(font=(self.font, self.button_size), justify="center",
                                 highlightbackground=self.window_color)
        self.timer_entry.grid(row=2, column=0, columnspan=2)
        self.timer_entry.insert(0, "Enter time (HH:MM:SS)")

        # When the timer is reset, these bound events will allow the cursor to exit the entry box
        self.timer_entry.bind("<FocusIn>", self.cursor_in)
        self.timer_entry.bind("<FocusOut>", self.cursor_out)

        # Creating the Display for the Timer
        self.display = tk.Label(text="00:00:00", font=(self.font, self.display_size),
                                   bg=self.window_color)
        self.display.grid(row=3, column=0, columnspan=2)

        # Creating the Reset Button for Timer
        self.reset_button = tk.Button(text="Reset", font=(self.font, self.button_size), fg="red",
                                   command=self.timer_reset, highlightbackground=self.window_color)
        self.reset_button.grid(row=4, column=0)

        # Creating the Start/Stop Button for Timer
        self.startstop_button = tk.Button(text="Start", font=(self.font, self.button_size),
                                             fg="green", command=self.timer_start,
                                             highlightbackground=self.window_color)
        self.startstop_button.grid(row=4, column=1)

        # Creating the Dropdown Menu to Switch Tools
        self.option = tk.StringVar(self.window)
        self.options = ["Timer", "Stopwatch"]
        self.option.set(self.options[0])
        self.dropdown = tk.OptionMenu(self.window, self.option, *self.options, command=self.switch_mode)
        # *self.options unpacks a list (options) as individual arguments
        self.dropdown.grid(row=5, column=0, columnspan=2)

        # Used later in program for timer display and alarm sound respectively
        self.timer = None
        self.sound = None
        # Used for stopwatch display
        self.stopwatch = None

    # Note: Assigning this function to self.dropdown automatically passes in a parameter for option op, so we account for it
    def switch_mode(self, op) -> None:
        """
        Function to switch between the Timer/Stopwatch Modes of the application
        :param op: the option being switched to
        """
        # Changing to Timer
        if op == "Timer" and self.title.cget("text") != "TIMER":
            # Changing the window and title to fit the mode
            self.window.title("Timer")
            self.window_color = "#f0b8b8"
            self.window.config(bg=self.window_color)
            self.title.config(text="TIMER", fg="red", bg=self.window_color)
            # Destroying the previous canvas, then recreating it
            self.canvas.destroy()
            self.canvas = tk.Canvas(width=64, height=64, bg=self.window_color,
                                 highlightbackground=self.window_color)
            self.canvas.grid(row=1, column=0, columnspan=2)
            self.canvas.create_image(32, 32, image=self.timer_icon)
            # Creating the Entry Box for Timer
            self.timer_entry = tk.Entry(font=(self.font, self.button_size), justify="center",
                                     highlightbackground=self.window_color)
            self.timer_entry.grid(row=2, column=0, columnspan=2)
            self.timer_entry.insert(0, "Enter time (HH:MM:SS)")
            # When the timer is reset, these bound events will allow the cursor to exit the entry box
            self.timer_entry.bind("<FocusIn>", self.cursor_in)
            self.timer_entry.bind("<FocusOut>", self.cursor_out)
            # Reconfiguring the Display for the Timer
            # Cancelling the current stopwatch, if there is one
            try:
                self.window.after_cancel(self.stopwatch)
            except ValueError:
                pass
            self.display.config(text="00:00:00", bg=self.window_color)
            self.display.grid(row=3, column=0, columnspan=2)
            # Reconfiguring the Reset Button for Timer
            self.reset_button.config(text="Reset", font=(self.font, self.button_size), fg="red",
                                       command=self.timer_reset, highlightbackground=self.window_color)
            self.reset_button.grid(row=4, column=0)
            # Reconfiguring the Start/Stop Button for Timer
            self.startstop_button.config(text="Start",
                                           fg="green", command=self.timer_start,
                                           highlightbackground=self.window_color)
            self.startstop_button.grid(row=4, column=1)
        # Changing to stopwatch
        elif op == "Stopwatch" and self.title.cget("text") != "STOPWATCH":
            # Changing the window and title to fit the mode
            self.window.title("Stopwatch")
            self.window_color = "#D1FFBD"
            self.window.config(bg=self.window_color)
            self.title.config(text="STOPWATCH", fg="green", bg=self.window_color)
            # Destroying the previous canvas, then recreating it
            self.canvas.destroy()
            self.canvas = tk.Canvas(width=64, height=64, bg=self.window_color,
                                 highlightbackground=self.window_color)
            self.canvas.grid(row=1, column=0, columnspan=2)
            self.canvas.create_image(32, 32, image=self.stopwatch_icon)
            # Deleting Timer Entry
            self.timer_entry.destroy()
            self.display.config(text="00:00.00", bg=self.window_color)
            self.display.grid(row=2, column=0, columnspan=2)
            # Reconfiguring the Reset Button for Stopwatch
            # Cancelling the current timer, if there is one
            try:
                self.window.after_cancel(self.timer)
                self.sound.stop()
            except (ValueError, AttributeError):
                pass
            self.reset_button.config(text="Reset", font=(self.font, self.button_size), fg="red",
                                     command=self.stopwatch_reset, highlightbackground=self.window_color)
            self.reset_button.grid(row=3, column=0)
            # Reconfiguring the Start/Stop Button for Stopwatch
            self.startstop_button.config(text="Start",
                                         fg="green", command=self.stopwatch_start,
                                         highlightbackground=self.window_color)
            self.startstop_button.grid(row=3, column=1)

    # Functions for Timer
    def cursor_in(self, event) -> None:
        """
        Function to remove placeholder text from entry when cursor is in entry
        :param event: used to denote that this function is an event
        """
        if self.timer_entry.get() == "Enter time (HH:MM:SS)":
            self.timer_entry.delete(0, tk.END)

    def cursor_out(self, event) -> None:
        """
        Function to create placeholder text when cursor not in entry
        :param event: used to denote that this function is an event
        """
        if self.timer_entry.get() == "":
            self.timer_entry.insert(0, "Enter time (HH:MM:SS)")

    def timer_start(self) -> None:
        """
        Function to start the timer from the current time entered
        """
        # Pausing the timer when the button says "Stop"
        if self.startstop_button.cget("text") == "Stop":
            # Don't pause when the timer is done or when 00:00:00 is entered
            if self.timer_entry.get() != "00:00:00" and self.display.cget("text") != "00:00:00":
                self.timer_stop()
                self.startstop_button.config(text="Start", fg="green")
        else:
            # All time displays are 8 chars long
            if len(self.timer_entry.get()) == 8:
                # There are cases where timer_entry box may have invalid input value, causing ValueError
                try:
                    # Once the timer finishes
                    if self.display.cget("text") == "00:00:00":
                        if self.timer_entry.get()[2] == ":" and self.timer_entry.get()[5] == ":":
                            # Get the hr, min, and sec count from the entry box
                            hr_count = int(self.timer_entry.get()[0:2])
                            min_count = int(self.timer_entry.get()[3:5])
                            sec_count = int(self.timer_entry.get()[6:8])
                    else:
                        # Get the hr, min, and sec count from current timer display while paused
                        curr_time_str = self.display.cget("text")
                        hr_count = int(curr_time_str[0:2])
                        min_count = int(curr_time_str[3:5])
                        sec_count = int(curr_time_str[6:8])
                except ValueError:
                    pass
                else:
                    try:
                        # Checking if hrs, mins, and secs are all between 0, 59 for secs and mins, or 0, 99 for hrs
                        if 0 <= hr_count <= 99 and 0 <= min_count <= 59 and 0 <= sec_count <= 59:
                            if not hr_count == min_count == sec_count == 0:
                                # Only allow start button to change to stop if not 00:00:00
                                self.startstop_button.config(text="Stop", fg="red")
                            # Calculate second total
                            sec_total = sec_count + min_count * 60 + hr_count * 3600
                            # Send sec_total to timer_count, where the countdown begins
                            self.timer_count(sec_total)
                    except UnboundLocalError:
                        pass

    def timer_stop(self) -> None:
        """
        Function to pause the timer at current time displayed
        """
        # timer is a global variable, this deals with cases where "Stop" is pressed before timer is created
        try:
            self.window.after_cancel(self.timer)
        except ValueError:
            pass

    def timer_reset(self) -> None:
        """
        Function to reset the timer to 00:00:00
        """
        self.timer_stop()
        # All time displays have to be 8 chars in length (HH:MM:SS)
        if len(self.timer_entry.get()) == 8:
            # Deal with cases with inputs that don't match HH:MM:SS structure
            try:
                # If the timer entry isn't empty or doesn't have a placeholder
                if self.timer_entry.get() != "Enter time (HH:MM:SS)" or self.timer_entry.get() != "":
                    hr_count = int(self.timer_entry.get()[0:2])
                    min_count = int(self.timer_entry.get()[3:5])
                    sec_count = int(self.timer_entry.get()[6:8])
                    # Deals with hr, min, and sec values that are less than 10 (need a 0 in front)
                    if hr_count < 10:
                        hr_count = f"0{hr_count}"
                    if min_count < 10:
                        min_count = f"0{min_count}"
                    if sec_count < 10:
                        sec_count = f"0{sec_count}"
                    if 0 <= int(hr_count) <= 59 and 0 <= int(min_count) <= 59 and 0 <= int(sec_count) <= 59:
                        self.display.config(text=f"{hr_count}:{min_count}:{sec_count}")
            except ValueError:
                pass
        self.startstop_button.config(text="Start", fg="green")
        # Removes the cursor from the entry box and focuses it on the timer frame
        self.window.focus_set()
        # Stop the alarm timer sound (sound is a global variable)
        # In cases it doesn't exist, deal with the AttributeError
        try:
            self.sound.stop()
        except AttributeError:
            pass

    def timer_count(self, sec_total) -> None:
        """
        Function for the timer display and update in real time
        :param sec_total: total number of seconds to count down from
        """
        curr_sec = sec_total % 60 # Number of seconds, limited by 60
        curr_min = math.floor(sec_total / 60) % 60 # Number of minutes, limited by 60
        curr_hr = math.floor(sec_total/ 3600) % 100 # Number of hours, limited by 100
        # Deal with cases where secs, mins, or hrs less than 10 (need 0 in front)
        if curr_sec < 10:
            curr_sec = f"0{curr_sec}"
        if curr_min < 10:
            curr_min = f"0{curr_min}"
        if curr_hr < 10:
            curr_hr = f"0{curr_hr}"
        self.display.config(text=f"{curr_hr}:{curr_min}:{curr_sec}")
        # As long as timer display doesn't show 00:00:00, create timer
        if self.display.cget("text") != "00:00:00":
            try:
                self.timer = self.window.after(1000, self.timer_count, sec_total - 1)
            except ValueError:
                pass
        else:
            # Otherwise, stop the timer when done
            self.timer_stop()
            # # Notify user when their timer is up ("" used for text longer than one word)
            # os.system(f"terminal-notifier -message \"Click Reset To Restart Timer!\" -subtitle \"Timer Has Reached 00:00:00\" -title \"Time's Up!\"")
            # To play the alarm sound when the timer reaches 00:00:00
            self.sound = playsound(resource_path("assets/timer_alarm.mp3"), block=False)

    def stopwatch_start(self) -> None:
        """
        Function to start the stopwatch from the current time displayed
        """
        # Number of seconds is curr_time / 100
        # Number of minutes is curr_time / 6000
        if self.display.cget("text") == "00:00.00":
            # Starting the stopwatch
            self.stopwatch_count(0)
            self.startstop_button.config(text="Stop", fg="red")
        else:
            # Stopping the stopwatch
            if self.startstop_button.cget("text") == "Stop":
                self.startstop_button.config(text="Start", fg="green")
                self.stopwatch_stop()
            else:
                # Remembering the time the stopwatch displays while paused when unpausing it
                minutes_display_count = int(self.display.cget("text")[0:2])
                second_display_count = int(self.display.cget("text")[3:5])
                centi_display_count = int(self.display.cget("text")[6:])
                total_centi_count = centi_display_count + (second_display_count * 100) + (minutes_display_count  * 6000)
                self.stopwatch_count(total_centi_count)
                self.startstop_button.config(text="Stop", fg="red")

    def stopwatch_stop(self) -> None:
        """
        Function to pause the stopwatch at the current time displayed
        """
        # To deal with cases where stopwatch doesn't exist yet and the "Stop" button is pressed (stopwatch is a global variable)
        try:
            self.window.after_cancel(self.stopwatch)
        except ValueError:
            pass

    def stopwatch_reset(self) -> None:
        """
        Function to reset the stopwatch back to 00:00.00
        """
        self.stopwatch_stop()
        self.display.config(text="00:00.00")
        self.startstop_button.config(text="Start", fg="green")

    def stopwatch_count(self, curr_time) -> None:
        """
        Function for the stopwatch display and update in real time
        :param curr_time: the current time in centiseconds
        """
        curr_cs = curr_time % 100 # Number of centiseconds, limited by 100
        curr_sec = math.floor(curr_time / 100) % 60 # Number of seconds, limited by 60
        curr_min = math.floor(curr_time / 6000) % 100 # Number of minutes, limited by 100
        # Dealing with cs, sec, and min values less than 10 (need a 0 in front)
        if curr_cs < 10:
            curr_cs = f"0{curr_cs}"
        if curr_sec < 10:
            curr_sec = f"0{curr_sec}"
        if curr_min < 10:
            curr_min = f"0{curr_min}"
        self.display.config(text=f"{curr_min}:{curr_sec}.{curr_cs}")
        # Setting the stopwatch attribute to continuously increasing the stopwatch time by 1 every centisecond
        self.stopwatch = self.window.after(10, self.stopwatch_count, curr_time + 1)