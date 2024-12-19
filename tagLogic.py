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
    elif tagInt <= 106510:
        #v11 has 5 tags that are 100,000+, but go no higher than 106,510.
        return tagPrefix + '*::' + str(tagInt)
    else:
        raise Exception('This UWorld ID is too high! UWorld tags for v11 do not go above 106510.')

def createFullTagV12 (tagNumber, stepVersion):

    tagInt = None
    try:
        tagInt = int(tagNumber)
    except ValueError:
        raise Exception('This is not a number. UWorld question IDs are numbers.')

    tagPrefix = tagPrefixDict[stepVersion] 

    if tagInt is None:
        raise Exception('Invalid tag. Tag should be a number.') 

    return tagPrefix + '*::' + str(tagInt)


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