# Tictactoe Qt ( 0's and X's)
# 05/11/2019
# Version 0.2
# Author Rick Townsend

from PyQt5.QtWidgets import *
# Import our Board class
from board import Board

if __name__ == "__main__":
    
    app = QApplication([])
    # Create a Board object
    tbl = Board()
    # Tell the application to draw the tbl object on the screen
    tbl.show()
    # Run the application
    app.exec_()
