import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QFrame, QGroupBox,
                              QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QComboBox, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from functions import generate, solve


class Sudoku(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.title = 'Sudoku'
        self.width = 260
        self.height = 0
        self.setFixedSize(self.width, self.height)
        self.matrix = matrix
        self.difficulty = "Easy"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.mainLayout = QVBoxLayout()
        self.Menu()
        self.setLayout(self.mainLayout)

    def Menu(self):
        menuWidget = QWidget()
        menuLayout = QVBoxLayout()

        # Add the "Solve a Sudoku" button
        solveBtn = QPushButton("Solve a Sudoku")
        solveBtn.clicked.connect(lambda: self.on_button_clicked(0))
        menuLayout.addWidget(solveBtn)

        def updateDifficulty(text):
            self.difficulty = text

        # Add the difficulty selector
        difficultyLayout = QFormLayout()
        difficultyDropDown = QComboBox()
        difficultyDropDown.addItems(["Easy", "Medium", "Hard"])
        difficultyLayout.addRow(QLabel("Difficulty:"), difficultyDropDown)
        difficultyDropDown.currentTextChanged.connect(updateDifficulty)
        menuLayout.addLayout(difficultyLayout)

        # Add the "Generate a Sudoku" button
        generateBtn = QPushButton("Generate a Sudoku")
        generateBtn.clicked.connect(lambda: self.on_button_clicked(difficultyDropDown.currentText()))
        menuLayout.addWidget(generateBtn)

        menuWidget.setLayout(menuLayout)
        self.mainLayout.addWidget(menuWidget)
            


    def createSudoku(self):
        self.width = 580
        self.height = 580
        sudoku_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(0)  # Set horizontal spacing to 0
        grid_layout.setVerticalSpacing(0)    # Set vertical spacing to 0
        sudoku_widget.setLayout(grid_layout)

        cell_size = 60  # Cell size
        subbox_size = cell_size * 3  # Size of each 3x3 sub-box

        for i in range(0, len(self.matrix), 3):
            for j in range(0, len(self.matrix[0]), 3):
                # Add labels for each cell in the sub-box
                for x in range(3):
                    for y in range(3):
                        label = QLabel(str(self.matrix[i + x][j + y]))
                        label.setObjectName("CellLabel")
                        label.setAlignment(Qt.AlignCenter)
                        label.setFixedSize(cell_size, cell_size)  # Set fixed size for each cell
                        label.setFrameShape(QFrame.Panel)
                        if self.matrix[i+x][j+y]:
                            label.setStyleSheet("background-color: #E6FFCC;")
                        # Increase font size
                        font = QFont()
                        font.setPointSize(14)
                        label.setFont(font)
                        grid_layout.addWidget(label, i + x, j + y)

                # Create a QLabel to represent each 3x3 sub-box
                box_label = QLabel()
                box_label.setAlignment(Qt.AlignCenter)
                box_label.setFixedSize(subbox_size, subbox_size)  # Set fixed size for the 3x3 box
                box_label.setFrameShape(QFrame.Box)
                box_label.setLineWidth(4) 
                grid_layout.addWidget(box_label, i, j, 3, 3)  # Span the box label across the sub-box

                

        self.setFixedSize(self.width, self.height)
        self.mainLayout.addWidget(sudoku_widget)

    def on_button_clicked(self, option):
        self.clearMainLayout()
        if option == 0:
            print('Option Selected:', option)
            self.solveSudoku()
        elif option == 1:
            print('Option Selected:', option)
            self.matrix = solve(self.matrix)
            if self.matrix:
                self.createSudoku()   
        else:
            print('Option Selected:', option)
            self.matrix = generate(option)
            self.createSudoku()

    def clearMainLayout(self):
        while self.mainLayout.count():
            item = self.mainLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def solveSudoku(self):
        self.matrix = [[0]*9 for _ in range(9)] 
        print(self.matrix)
        self.width = 580
        self.height = 600
        sudoku_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(0)  # Set horizontal spacing to 0
        grid_layout.setVerticalSpacing(0)    # Set vertical spacing to 0
        sudoku_widget.setLayout(grid_layout)

        cell_size = 60  # Cell size
        subbox_size = cell_size * 3  # Size of each 3x3 sub-box

        for i in range(0, len(self.matrix), 3):
            for j in range(0, len(self.matrix[0]), 3):
                # Create a QLabel to represent each 3x3 sub-box
                box_label = QLabel()
                box_label.setAlignment(Qt.AlignCenter)
                box_label.setFixedSize(subbox_size, subbox_size)  # Set fixed size for the 3x3 box
                box_label.setFrameShape(QFrame.Box)
                box_label.setLineWidth(4) 
                grid_layout.addWidget(box_label, i, j, 3, 3)  # Span the box label across the sub-box   
                for x in range(3):
                    for y in range(3):
                        font = QFont()
                        font.setPointSize(14)
                        cell = SudokuCell(self.matrix, i + x, j + y)
                        cell.setFont(font)
                        cell.setObjectName("CellLabel")
                        cell.setAlignment(Qt.AlignCenter)
                        cell.setFixedSize(cell_size, cell_size)
                        cell.setStyleSheet("QLineEdit { border: 1px solid #000000; background-color: transparent; }")
                        grid_layout.addWidget(cell, i + x, j + y)
                    
        self.setFixedSize(self.width, self.height)

        solveBtn = QPushButton("Solve")
        solveBtn.clicked.connect(lambda: self.on_button_clicked(1))
        self.mainLayout.addWidget(sudoku_widget)
        self.mainLayout.addWidget(solveBtn)



class SudokuCell(QLineEdit):
    def __init__(self, matrix, x, y, parent=None):
        super().__init__(parent)
        self.setMaxLength(1)  # Set maximum length to 1 character
        self.x = x
        self.y = y
        self.matrix = matrix
    def keyPressEvent(self, event):
        key = event.text()
        if key.isdigit():  # Check if the pressed key is a digit
            super().keyPressEvent(event)  # Allow the key press event
            self.setStyleSheet("background-color: #FFFFE6;")
        elif key == "\b":  # Allow backspace
            super().keyPressEvent(event)
            self.setStyleSheet("border: 1px solid #000000; background-color: transparent;")
        elif key == "\r" and self.text():  # Allow Enter
            super().keyPressEvent(event)
            self.setStyleSheet("background-color: #E6FFCC;")
            self.lower()
            self.matrix[self.x][self.y] = int(self.text())
            print(self.matrix)
        else:
            event.ignore()  # Ignore non-numeric characters
        
if __name__ == '__main__':
    matrix = [[""]*9 for _ in range(9)] 
    app = QApplication(sys.argv)
    # ex = Sudoku(matrix)
    sudoku_app = Sudoku(matrix)
    sudoku_app.show()
    sys.exit(app.exec_())

