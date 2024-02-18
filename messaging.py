from aqt.utils import showInfo

def showErrors (errorList, successList, notFoundList):
    outputString = ''

    if len(successList) > 0:
        outputString += 'Successfully Unsuspended:\n'
    for tag in successList:
        outputString += tag + '\n' 

    if len(notFoundList) > 0:
        outputString += '\nTags Not Found:\n'
    for (tag, _) in notFoundList:
        outputString += tag + '\n'
    
    if len(errorList) > 0:
        outputString += '\nFailed to unsuspend:\n'
    for (tag, err) in errorList:
        outputString += tag + ' - ' + str(err) + '\n'

    showInfo(outputString.strip())

def showSuccess ():
    showInfo('All cards listed under tags successfully unsuspended!')