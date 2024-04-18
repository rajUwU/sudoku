import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Grid(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.title = 'Sudoku'
        self.width = 560
        self.height = 560
        self.matrix = matrix
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(0)  # Set horizontal spacing to 0
        grid_layout.setVerticalSpacing(0)    # Set vertical spacing to 0

        cell_size = 60  # Cell size
        subbox_size = cell_size * 3  # Size of each 3x3 sub-box

        for i in range(0, len(self.matrix), 3):
            for j in range(0, len(self.matrix[0]), 3):
                # Create a QLabel to represent each 3x3 sub-box
                box_label = QLabel()
                box_label.setAlignment(Qt.AlignCenter)
                box_label.setFixedSize(subbox_size, subbox_size)  # Set fixed size for the 3x3 box
                box_label.setFrameShape(QFrame.Box)
                box_label.setLineWidth(2) 
                grid_layout.addWidget(box_label, i, j, 3, 3)  # Span the box label across the sub-box

                # Add labels for each cell in the sub-box
                for x in range(3):
                    for y in range(3):
                        label = QLabel(str(self.matrix[i + x][j + y]))
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

        self.setLayout(grid_layout)
        self.setFixedSize(self.width, self.height)
        self.show()

    def setMatrix(self, matrix):
        self.matrix = matrix
        self.updateGridLayout()

    def updateGridLayout(self):
        for i in reversed(range(self.updateGridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                label = QLabel(str(self.matrix[i][j]))
                self.gridLayout.addWidget(label, i, j)

if __name__ == '__main__':
    matrix = [[0]*9 for _ in range(9)] 
    app = QApplication(sys.argv)
    ex = Grid(matrix)
    sys.exit(app.exec_())

