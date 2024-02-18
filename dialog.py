from aqt.qt import *
from . import tagLogic
from . import messaging

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
        errorList = []
        for tagNumber in tagsList:
            print(tagNumber)
            #TODO: Potential errors to catch
            try:
                tag = tagLogic.createFullTag(tagNumber)
            except Exception as err:
                errorList.append(err)
            if tag:
                try:
                    tagLogic.unsuspendCardsByTag(tag)
                except Exception as err:
                    errorList.append(err)

        self.close() 
        if len(errorList) > 0:
            messaging.showErrors(errorList)
        else:
            messaging.showSuccess()