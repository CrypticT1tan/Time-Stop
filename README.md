# TIME:STOP

A timer/stopwatch application made with Python that can alternate between the two modes at the user's desire.

## Installation
Use package manager pip to install the following:

```bash
pip install playsound3
pip install pillow
pip install pyinstaller
```

## Usage

To build the executable file, use the terminal to go into the same directory as the main.py file and run the command below:

```bash
pyinstaller main.py --onefile --windowed --add-data "../assets:assets" --icon=../assets/clock.icns --name "<Desired Name of Executable>"
```

Open up the dist file to find a executable file with your desired name, and open it.

The Timer Mode consists of a entry box to input a time in HH:MM:SS format (HH=hours, MM=minutes, SS=seconds), a timer text display, and two buttons labeled "Reset" and "Start".
The red "Reset" button stops the timer and resets the timer display to the current input inside the entry box.
The green "Start" button will start the timer countdown based on the entry box input/time remaining in the display and change into a red "Stop" button when clicked.
The red "Stop" button will pause the timer and changes back to the green "Start button".

The Stopwatch Mode consists of a stopwatch display in MM:SS.CSCS format (MM=minutes, SS=seconds, CSCS=centiseconds) and two buttons labeled "Reset" and "Start".
The red "Reset" button stops the stopwatch and resets it back to 00:00.00. 
The green "Start" button works similarly to the one in the Timer Mode, except it triggers an addition of time rather than a subtraction.

A dropdown menu at the bottom is provided to switch between the Timer and Stopwatch Modes.

## Contact
For any questions, contact me at gavinkiosco@gmail.com or CrypticT1tan on GitHub.

## Attribution
Timer and Stopwatch Icons made by Freepik from www.flaticon.com  
Project inspired by the Pomodoro Timer program from Angela Yu's 100 Days of Code bootcamp on Udemy