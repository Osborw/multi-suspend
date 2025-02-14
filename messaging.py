from aqt.utils import showInfo
from aqt.qt import *
from . import tagLogic
from . import messaging

class PostRunMessaging(QDialog):
    def __init__(self, errorList, successList, notFoundList):
        QDialog.__init__(self)
        self.setWindowTitle("Results")
        self.setFixedWidth(550)
        self.layout = QVBoxLayout()

        scroll = QScrollArea(self)
        self.layout.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        scroll.setWidget(scrollContent)

        outputString = ''
        
        if len(successList) > 0:
            outputString += str(len(successList)) + ' card(s) successfully unsuspended\n'

        if len(notFoundList) > 0:
            outputString += '\nTags Not Found:\n'
        for (tag, _) in notFoundList:
            outputString += tag + '\n'
        
        if len(errorList) > 0:
            outputString += '\nFailed to Unsuspend:\n'
        for (tag, err) in errorList:
            outputString += '"' + tag + '"' + ' -> ' + str(err) + '\n'

        finalString = outputString.strip()
        label1 = QLabel(finalString)
        scrollLayout.addWidget(label1)

        self.setLayout(self.layout)

# def showErrors (errorList, successList, notFoundList):
#     outputString = ''

#     if len(successList) > 0:
#         outputString += 'Successfully Unsuspended:\n'
#     for tag in successList:
#         outputString += tag + '\n' 

#     if len(notFoundList) > 0:
#         outputString += '\nTags Not Found:\n'
#     for (tag, _) in notFoundList:
#         outputString += tag + '\n'
    
#     if len(errorList) > 0:
#         outputString += '\nFailed to Unsuspend:\n'
#     for (tag, err) in errorList:
#         outputString += '"' + tag + '"' + ' -> ' + str(err) + '\n'

#     showInfo(outputString.strip())

def showSuccess ():
    showInfo('All cards listed under tags successfully unsuspended!')