from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import math

tagPrefixDict = {
    'Step_1_v11': '#AK_Step1_v11::#UWorld::',
    'Step_2_v11': '#AK_Step2_v11::#UWorld::',
    'Step_1_v12': '#AK_Step1_v12::#UWorld::',
    'Step_2_v12': '#AK_Step2_v12::#UWorld::',
}

def createFullTag (tagNumber, stepVersion):

    if 'v12' in stepVersion:
        return createFullTagV12(tagNumber, stepVersion)
    else:
        return createFullTagV11(tagNumber, stepVersion)

def createFullTagV11 (tagNumber, stepVersion):

    tagInt = None
    try:
        tagInt = int(tagNumber)
    except ValueError:
        raise Exception('This is not a number. UWorld question IDs are numbers.')

    tagPrefix = tagPrefixDict[stepVersion] 

    if tagInt is None:
        raise Exception('Invalid tag. Tag should be a number.')
    elif tagInt <= 0:
        raise Exception('This UWorld ID is too low! UWorld tags do not go below 1.')
    elif tagInt > 0 and tagInt < 10:
        #convert single digit to two digit string
        return tagPrefix + '0-99::' + '0' + str(tagInt)
    elif tagInt >= 10 and tagInt <= 99:
        #add to 0-99 tag
        return tagPrefix + '0-99::' + str(tagInt)
    elif tagInt >= 100 and tagInt <= 999:
        #add to 100-999 tag
        lowerBound = math.floor(tagInt/100) * 100
        upperBound = lowerBound + 99
        return tagPrefix + '100-999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    elif tagInt >= 1000 and tagInt <= 9999:
        #add to 1000 - 9999 tag
        lowerBound = math.floor(tagInt/1000) * 1000
        upperBound = lowerBound + 999
        return tagPrefix + '1000-9999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    elif tagInt >= 10000 and tagInt <= 99999:
        #add to 10000 - 99999 tag
        lowerBound = math.floor(tagInt/1000) * 1000
        upperBound = lowerBound + 999
        return tagPrefix + '10000-99999::' + str(lowerBound) + '-' + str(upperBound) + '::' + str(tagInt)
    else:
        raise Exception('This UWorld ID is too high! UWorld tags do not go above 99999.')

def createFullTagV12 (tagNumber, stepVersion):

    tagInt = None
    try:
        tagInt = int(tagNumber)
    except ValueError:
        raise Exception('This is not a number. UWorld question IDs are numbers.')

    tagPrefix = tagPrefixDict[stepVersion] 

    if tagInt is None:
        raise Exception('Invalid tag. Tag should be a number.') 

    return tagPrefix + str(tagInt)


def unsuspendCardsByTag(tag) -> None:

    print(tag)
    ids = mw.col.find_cards('tag:' + tag)

    if len(ids) == 0:
        raise Exception('Found no matches by tag ' + tag + '. Perhaps that tag does not exist or is typed incorrectly.')
    else:
        mw.col.sched.unsuspendCards(ids)

def loadLastUsedTagPrefix() -> str:

    config = mw.addonManager.getConfig(__name__)
    lastUsedTagPrefix = config['lastUsedTagPrefix']

    return lastUsedTagPrefix

def saveLastUsedTagPrefix(tagPrefix) -> None:

    newConfig = {
        'lastUsedTagPrefix': tagPrefix
    } 

    mw.addonManager.writeConfig(__name__, newConfig)

def getLastUsedTagPrefixIndex() -> int:

    lastUsedTagPrefix = loadLastUsedTagPrefix()

    tagPrefixes = list(tagPrefixDict.keys())
    if not lastUsedTagPrefix in tagPrefixes:
        return 0
    else:
        return tagPrefixes.index(lastUsedTagPrefix)