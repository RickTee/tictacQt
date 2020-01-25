# Ticton_off=None0's and X's)
# 15/11/2019
# Version 0.4
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
        # Create a label to contain warnings.
        self.labelWarn = QLabel("")
        self.labelWarn.setAlignment(Qt.AlignCenter)
        # Create a grid layout & set the spacing
        grid = QGridLayout()
        grid.setSpacing(0)

        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.button = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        self.O_X = ['f', 'X', 'O']
        # Create our board of 9 buttons and put them in a grid
        for i in range(0, 3):
            for j in range(0, 3):
                self.button[i][j] = QPushButton()
                self.button[i][j].setMinimumSize(25, 25)
                self.button[i][j].setMaximumSize(25, 25)
                grid.addWidget(self.button[i][j], i, j)

        vbox.addLayout(grid)
        # Add the warnings label
        vbox.addWidget(self.labelWarn)
        vbox.addStretch(0)
        hbox.addLayout(vbox)
        hbox.addStretch(0)
        self.setLayout(hbox)

        self.button[0][0].clicked.connect(lambda: self.on_button_clicked(0, 0))
        self.button[0][1].clicked.connect(lambda: self.on_button_clicked(0, 1))
        self.button[0][2].clicked.connect(lambda: self.on_button_clicked(0, 2))
        self.button[1][0].clicked.connect(lambda: self.on_button_clicked(1, 0))
        self.button[1][1].clicked.connect(lambda: self.on_button_clicked(1, 1))
        self.button[1][2].clicked.connect(lambda: self.on_button_clicked(1, 2))
        self.button[2][0].clicked.connect(lambda: self.on_button_clicked(2, 0))
        self.button[2][1].clicked.connect(lambda: self.on_button_clicked(2, 1))
        self.button[2][2].clicked.connect(lambda: self.on_button_clicked(2, 2))

    # Reset our board array and clear the text in our buttons
    def new_game(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = 0
                self.button[i][j].setText("")
        self.label.setText("")
        self.labelWarn.setText("")
        self.player = 1
        self.toggle_buttons(True)

    def on_button_clicked(self, i, j):
        # If this is the ai's turn
        #if self.player == 2:
            #i, j = self.best_move()
        # Check for valid move, space is empty
        self.labelWarn.setText("")
        if self.board[i][j] != 0:
            self.labelWarn.setText("Invalid move")
            return
        # Enter move into the board array
        self.board[i][j] = self.player
        self.button[i][j].setText(self.O_X[self.player])
        # Check for win or draw
        win = self.check_win()  #
        if win == 1:
            self.label.setText("X won")
        if win == 2:
            self.label.setText("X won")
        if win == 3:
            self.label.setText("Game is a draw")
        if win:
            self.end_game()
        self.set_player()

    def toggle_buttons(self, on_off):
        for i in range(0, 3):
            for j in range(0, 3):
                self.button[i][j].setEnabled(on_off)

    def end_game(self):
        self.labelWarn.setText("Game over")
        self.toggle_buttons(False)

    # Alternate players
    def set_player(self):
        if self.player == 1:
            self.player = 2
            i, j = self.best_move()
            self.on_button_clicked(i, j)
        else:
            self.player = 1

    # Test for a win or a draw
    def check_win(self):
        count = 0
        # Check for 3 O's or X's in rows
        for i in range(0, 3):
            if self.board[i][0] == 2 and self.board[i][1] == 2 and self.board[i][2] == 2:
                return 1
            if self.board[i][0] == 1 and self.board[i][1] == 1 and self.board[i][2] == 1:
                return 2

        # Check for 3 O's or X's in columns
        for j in range(0, 3):
            if self.board[0][j] == 2 and self.board[1][j] == 2 and self.board[2][j] == 2:
                return 1
            if self.board[0][j] == 1 and self.board[1][j] == 1 and self.board[2][j] == 1:
                return 2

        # Check for 3 O's or X's in diagonals
        if ((self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2) or (
                self.board[0][2] == 2 and self.board[1][1] == 2 and self.board[2][0] == 2)):
            return 1
        if ((self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (
                self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1)):
            return 2

        # Check for a draw
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] != 0:
                    count = count + 1
        if count == 9:
            return 3
        return False

    # Minimax algorithm chooses ai move ('O')
    INFINITY = 99999999
    ai = 2
    human = 1

    def best_move(self):
        # AI to make its turn
        best_score = -self.INFINITY
        move = [0, 0]
        for i in range(3):
            for j in range(3):
                # Is the spot available?
                if self.board[i][j] == 0:
                    self.board[i][j] = self.ai
                    score = self.minimax(0, False)
                    self.board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        move = i, j
        return move

    scores = {1: 10, 2: -10, 3: 0}

    def minimax(self, depth, is_maximizing):
        result = self.check_win()
        if result:
            return self.scores[result]

        if is_maximizing:
            best_score = -self.INFINITY
            for i in range(3):
                for j in range(3):
                    # Is the spot available?
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.ai
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = self.INFINITY
            for i in range(3):
                for j in range(3):
                    # Is the spot available?
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.human
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = 0
                        best_score = min(score, best_score)

            return best_score

    # Print out the board for debugging
    def dump(self):
        print(self.board)
