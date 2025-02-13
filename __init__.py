from aqt import mw
from aqt.utils import qconnect
from aqt.qt import *
from . import dialog

osceDialog = dialog.OsceDialog()

def main():
    osceDialog.show()

action = QAction("UWorld Batch Unsuspend - test", mw)
qconnect(action.triggered, main)
mw.form.menuTools.addAction(action)
