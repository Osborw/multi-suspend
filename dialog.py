from aqt.qt import *
from aqt.utils import showInfo

class OsceDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Multi-Unsuspend")
        self.layout = QVBoxLayout()

        label1 = QLabel("Enter tags below. Each tag should be one line")
        self.tags = QPlainTextEdit()
        self.layout.addWidget(label1)
        self.layout.addWidget(self.tags)

        self.button = QPushButton("Unsuspend")
        self.button.clicked.connect(self.unsuspendCardsByTags)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def unsuspendCardsByTags(self):

        tagsList = self.tags.toPlainText().strip().split('\n')
        print(tagsList[0], tagsList[-1])
        self.close() 