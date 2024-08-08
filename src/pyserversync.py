from utils.utils import *
from ui.main_window import app, call


if check_cronie_running() and check_rsync_available():
    print("cronie and rsync are present")

app.exec()
