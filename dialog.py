from aqt.qt import *
from . import tagLogic
from . import messaging

class OsceDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("UWorld Batch Unsuspend")
        self.layout = QVBoxLayout()

        label1 = QLabel("Directions:\nUnsuspend multiple cards by entering their numbers below.\nNumbers should be on separate lines or comma separated.\nWhitespaces are removed.\n")
        self.layout.addWidget(label1)

        label2 = QLabel("Choose which version of cards you will be unsuspending.")
        self.layout.addWidget(label2)
        self.stepVersion = QComboBox() 
        self.stepVersion.insertItems(0, list(tagLogic.tagPrefixDict.keys()))
        self.stepVersion.setCurrentIndex(tagLogic.getLastUsedTagPrefixIndex())
        self.layout.addWidget(self.stepVersion)

        self.tags = QPlainTextEdit()
        self.layout.addWidget(self.tags)

        self.button = QPushButton("Unsuspend")
        self.button.clicked.connect(self.unsuspendCardsByTags)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def unsuspendCardsByTags(self):

        tagsList = getTagsFromText(self.tags.toPlainText())
        tagsVersion = self.stepVersion.currentText()
        errorList = []
        notFoundList = []
        successList = []

        tagLogic.saveLastUsedTagPrefix(tagsVersion)
        for tagNumber in tagsList:
            print(tagNumber)
            tag = None
            try:
                tag = tagLogic.createFullTag(tagNumber, tagsVersion)
            except Exception as err:
                errorList.append((tagNumber, err))
            if tag:
                try:
                    tagLogic.unsuspendCardsByTag(tag)
                    successList.append(tagNumber)
                except Exception as err:
                    notFoundList.append((tagNumber, err))

        self.tags.clear()
        self.close() 
        if len(errorList) > 0 or len(notFoundList) > 0:
            messaging.showErrors(errorList, successList, notFoundList)
        else:
            messaging.showSuccess()

def getTagsFromText(text: str):
    '''
    Should accept strings that delimit by newline (\n) or comma (,).
    Also makes sure to remove any whitespaces in between.
    '''
    return text.strip().replace('\n', ',').replace(' ', '').split(',')