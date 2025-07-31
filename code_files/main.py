# Imported Files
from app import TimeApp

# Makes sure this is the main file being run and not an import being used in another file (for terminal scripts)
if __name__ == "__main__":
    # Create the main program window
    time_app = TimeApp()
    # Prevent the window from closing immediately after code execution
    time_app.window.mainloop()
    # Error handling to deal with cases where the sound attribute still has value "None"
    # For after the program closes, stop the sound of the alarm
    try:
        time_app.sound.stop()
    except AttributeError:
        pass
