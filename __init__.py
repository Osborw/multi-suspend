# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    ids = mw.col.find_cards("tag:#AK_Step1_v11::#UWorld::0-99::01")
    print('match length: ', len(ids))
    if len(ids) == 0:
        showInfo('sori no matches')
    else:
        mw.col.sched.unsuspendCards(ids)

    # show a message box
    # showInfo("Card count: %d" % cardCount)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
