"""
:Author: Seth Johnson
:Date: 10-30-2023
:Description:

Executes the program to prompt a user with a UI used to help compute a bill of sale.
"""
### Import packages ###
from gui import *
from logic import *

### Variable Declaration ###

### UDF Declaration ###

## Main Function ##
def main():
    """
    Callstack:
    main.py > logic.Logic() > gui.GUI().setupGUI()
    """
    app = QApplication([]) # Generate an application
    remote = TVRemote() # Calling Logic to initiate applet
    remote.show() # Calls window to show
    app.exec() # Execute application

if __name__ == "__main__":
    main()