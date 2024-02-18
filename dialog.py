from aqt.qt import *
from . import tagLogic
from . import messaging

class OsceDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("UWorld Batch Unsuspend")
        self.layout = QVBoxLayout()

        label1 = QLabel("Directions:\nEnter tags below. Each tag should be one line.\n\nPlease give Anki a few seconds to process.")
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
        notFoundList = []
        successList = []
        for tagNumber in tagsList:
            print(tagNumber)
            tag = None
            try:
                tag = tagLogic.createFullTag(tagNumber)
            except Exception as err:
                errorList.append((tagNumber, err))
            if tag:
                try:
                    tagLogic.unsuspendCardsByTag(tag)
                    successList.append(tagNumber)
                except Exception as err:
                    notFoundList.append((tagNumber, err))

        self.close() 
        if len(errorList) > 0 or len(notFoundList) > 0:
            messaging.showErrors(errorList, successList, notFoundList)
        else:
            messaging.showSuccess()