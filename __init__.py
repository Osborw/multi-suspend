from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from . import dialog

osceDialog = dialog.OsceDialog()

def main():
    osceDialog.show()
    # tag = '#AK_Step1_v11::#UWorld::0-99::01'
    # unsuspendCardsByTag(tag)
    # showInfo('Completed Successfully! All cards under provided tags are no unsuspended!')

def unsuspendCardsByTag(tag) -> None:

    ids = mw.col.find_cards('tag:' + tag)

    if len(ids) == 0:
        showInfo('Found no matches by tag ' + tag + '. Perhaps that tag does not exist or is typed incorrectly.')
    else:
        mw.col.sched.unsuspendCards(ids)

action = QAction("Multi-Unsuspend", mw)
qconnect(action.triggered, main)
mw.form.menuTools.addAction(action)
