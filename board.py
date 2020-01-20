# Tictactoe Qt ( 0's and X's)
# 15/11/2019
# Version 0.2
# Author Rick Townsend

# Import the Qt libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


# Create our Board class with QWidget class as parent
class Board(QWidget):
    def __init__(self, parent=None):
        # Initialise the parent widget
        super(Board, self).__init__(parent)
        self.setMinimumSize(10, 10)
        self.setWindowTitle("TicTacToe")
        # Create horizontal and vertical boxes (containers) and set alignments
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        # Create a menu bar and add a File menu with entries for 'New game' and 'Quit'
        self.menu_bar = QMenuBar(self)
        file_menu = self.menu_bar.addMenu("File")
        # Add an action to the 'New game' menu entry
        new_game_action = QAction(QtGui.QIcon('new_game.png'), 'New game', self)
        file_menu.addAction(new_game_action)
        new_game_action.triggered.connect(self.new_game)
        new_game_action.setShortcut('Ctrl+N')
        file_menu.addSeparator()
        # Add an action to the 'Quit' menu entry
        exit_action = QAction(QtGui.QIcon('exit.png'), 'Quit', self)
        file_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        self.menu_bar.show()
        # Add a stretch spacer so expanding the window does not mess up our board
        hbox.addStretch(0)
        # Add a label to contain messages; 'Play', 'Win', 'Draw'.
        self.label = QLabel("Play")
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)
        # Add a label to contain warnings.
        self.labelWarn = QLabel("")
        self.labelWarn.setAlignment(Qt.AlignCenter)
        # Create a grid layout & set the spacing
        grid = QGridLayout()
        grid.setSpacing(0)

        self.board = [0]*9
        self.button = [0]*9
        self.player = "O"
        k = 0
        # Create our board of 9 buttons and put them in a grid
        for i in range(0, 3):
            for j in range(0, 3):
                self.button[k] = QPushButton()
                self.button[k].setMinimumSize(25, 25)
                self.button[k].setMaximumSize(25, 25)
                grid.addWidget(self.button[k], i, j)
                k = k + 1

        vbox.addLayout(grid)
        vbox.addWidget(self.labelWarn)
        vbox.addStretch(0)
        hbox.addLayout(vbox)
        hbox.addStretch(0)
        self.setLayout(hbox)

        self.button[0].clicked.connect(lambda: self.on_button_clicked(0))
        self.button[1].clicked.connect(lambda: self.on_button_clicked(1))
        self.button[2].clicked.connect(lambda: self.on_button_clicked(2))
        self.button[3].clicked.connect(lambda: self.on_button_clicked(3))
        self.button[4].clicked.connect(lambda: self.on_button_clicked(4))
        self.button[5].clicked.connect(lambda: self.on_button_clicked(5))
        self.button[6].clicked.connect(lambda: self.on_button_clicked(6))
        self.button[7].clicked.connect(lambda: self.on_button_clicked(7))
        self.button[8].clicked.connect(lambda: self.on_button_clicked(8))

    # Reset our board array and clear the text in our buttons
    def new_game(self):
        for i in range(0, 9):
            self.board[i] = 0
            self.button[i].setText("")
            self.label.setText("")
            self.labelWarn.setText("")
        self.player = "X"
        self.toggle_buttons(True)

    def on_button_clicked(self, n):
        # Check for valid move, space is empty
        self.labelWarn.setText("")
        if self.board[n] != 0:
            self.labelWarn.setText("Invalid move")
            return
        # Enter move into the board array
        self.board[n] = self.player
        self.button[n].setText(self.player)
        # Check for win or draw
        win = self.check_win()
        if win:
            self.end_game()
        self.set_player()

    def toggle_buttons(self, on_off):
        for i in range (9):
            self.button[i].setEnabled(on_off)

    def end_game(self):
        self.labelWarn.setText("Game over")
        self.toggle_buttons(False)

    # Alternate players
    def set_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    # Test for a win or a draw
    def check_win(self):
        count = 0
        win = 0
        i = 0
        # Check for 3 O's or X's in rows
        while i < 7:
            if self.board[i] == 'O' and self.board[i + 1] == 'O' and self.board[i + 2] == 'O':
                self.label.setText("O won")
                return 1
            if self.board[i] == 'X' and self.board[i + 1] == 'X' and self.board[i + 2] == 'X':
                self.label.setText("X won")
                return 2
            i = i + 3

        # Check for 3 O's or X's in columns
        for i in range(0, 3):
            if self.board[i] == 'O' and self.board[i + 3] == 'O' and self.board[i + 6] == 'O':
                self.label.setText("O won")
                return 1
            if self.board[i] == 'X' and self.board[i + 3] == 'X' and self.board[i + 6] == 'X':
                self.label.setText("X won")
                return 2

        # Check for 3 O's or X's in diagonals
        if ((self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O') or (
                self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O')):
            self.label.setText("O won")
            return 1
        if ((self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X') or (
                self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X')):
            self.label.setText("X won")
            return 2

        # Check for a draw
        for i in range(9):
            if self.board[i] != 0:
                count = count + 1
            if count == 9:
                self.label.setText("Game is a draw")
                return 3
        return
