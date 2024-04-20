import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QFrame, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from functions import generate


class Sudoku(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.title = 'Sudoku'
        self.width = 400
        self.height = 0
        self.matrix = matrix
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.mainLayout = QHBoxLayout()
        self.Menu()
        self.setLayout(self.mainLayout)

    def Menu(self):
        menu = QGroupBox("Sudoku")
        layout = QVBoxLayout()

        btn = QPushButton("Solve a Sudoku")
        btn.clicked.connect(lambda : self.on_button_clicked(0))
        layout.addWidget(btn)
    
        btn = QPushButton("Generate a Sudoku")
        btn.clicked.connect(lambda : self.on_button_clicked(1))
        layout.addWidget(btn)


        menu.setLayout(layout)
        self.mainLayout.addWidget(menu)

    def sudoku(self):
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
                        if self.matrix[i+x][j+y] > 0:
                            label.setStyleSheet("background-color: #FFFFE6;")
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

    # def setMatrix(self, matrix):
    #     self.matrix = matrix
    #     self.updateGridLayout()

    # def updateGridLayout(self):
    #     for i in range(len(self.matrix)):
    #         for j in range(len(self.matrix[0])):
    #             label = self.cell_labels[i][j]
    #             label.setText(str(self.matrix[i][j]))
    #             if self.matrix[i][j] > 0:
    #                 label.setStyleSheet("background-color: #FFFFE6;")

    def on_button_clicked(self, option):
        if option:
            self.matrix = generate("hard")
            self.clearMainLayout()
            self.sudoku()
            
        else:
            print("Solve button pressed")

    def clearMainLayout(self):
        while self.mainLayout.count():
            item = self.mainLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
if __name__ == '__main__':
    matrix = [[0]*9 for _ in range(9)] 
    app = QApplication(sys.argv)
    # ex = Sudoku(matrix)
    sudoku_app = Sudoku(matrix)
    sudoku_app.show()
    sys.exit(app.exec_())

