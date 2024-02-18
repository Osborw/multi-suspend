from aqt.utils import showInfo

def showErrors (errorList):
    errorString = 'Cards listed under most tags successfully unsuspended!\n\nExceptions:\n'
    for err in errorList:
        errorString += str(err) + '\n\n'
    showInfo(errorString.strip())

def showSuccess ():
    showInfo('All cards listed under tags successfully unsuspended!')