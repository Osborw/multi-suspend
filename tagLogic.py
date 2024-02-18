from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

def createFullTag (tagNumber):
    tagInt = int(tagNumber)

    #TODO: Add error handling here to catch if its letters

    tagPrefix = '#AK_Step1_v11::#UWorld::'

    if tagInt <= 0:
        #TODO: Add error handling here to throw if its less than 0
        print('Error: ' + tagNumber + ' is too low! There are no UWorld tags that go below 1.')
    elif tagInt > 0 and tagInt < 10:
        #convert single digit to two digit string
        return tagPrefix + '0-99::' + '0' + str(tagInt)
    elif tagInt >= 10 and tagInt <= 99:
        #add to 0-99 tag
        return tagPrefix + '0-99::' + str(tagInt)
    elif tagInt >= 100 and tagInt <= 999:
        #add to 100-999 tag
        lowerBound = round(tagInt, -2)
        upperBound = lowerBound + 99
        return tagPrefix + '100-999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    elif tagInt >= 1000 and tagInt <= 9999:
        #add to 1000 - 9999 tag
        lowerBound = round(tagInt, -3)
        upperBound = lowerBound + 999
        return tagPrefix + '1000-9999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    elif tagInt >= 10000 and tagInt <= 99999:
        #add to 10000 - 99999 tag
        lowerBound = round(tagInt, -3)
        upperBound = lowerBound + 999
        return tagPrefix + '10000-99999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    else:
        #TODO: Add error handling here to throw if its too high a number
        print('Error: ' + tagNumber + ' is too high! There are no UWorld tags that go above 99999.')

def unsuspendCardsByTag(tag) -> None:

    print('Unsuspending card with tag ' + tag)
    ids = mw.col.find_cards('tag:' + tag)

    if len(ids) == 0:
        #TODO: throw error that no tag matches, but don't crash and burn
        showInfo('Found no matches by tag ' + tag + '. Perhaps that tag does not exist or is typed incorrectly.')
    else:
        mw.col.sched.unsuspendCards(ids)
