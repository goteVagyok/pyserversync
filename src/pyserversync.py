import subprocess
import sys

from PyQt6.QtWidgets import QTableWidgetItem

from job import Job
from utils.utils import *
from ui.main_window import app, call

if os.geteuid() != 0:
    # need sudo to edit the crontab file
    print("sudo privileges are needed to modify some files.")
    subprocess.call(['sudo', '.venv/bin/python3', *sys.argv])
    sys.exit()

if not (check_cronie_running() and check_rsync_available()):
    exit(1)

print("cronie and rsync are present")
init()

SAVED_JOBS = load_saved_jobs()


def save_sync():
    job = Job()

    job.name = call.sync_name_lineedit.text()
    job.src = call.sync_src_lineedit.text()
    job.dst = call.sync_dst_lineedit.text()

    job.notifications = call.notification_cb.isChecked()
    job.twoway = call.twoway_cb.isChecked()

# call.sync_save_btn.clicked.connect(save_sync)

# call.scheduled_jobs_table.setRowCount(1)
# call.scheduled_jobs_table.setColumnCount(4)
#
# call.scheduled_jobs_table.setItem(0, 0, QTableWidgetItem("asd"))
# call.scheduled_jobs_table.setItem(0, 1, QTableWidgetItem("asd"))
# call.scheduled_jobs_table.setItem(0, 2, QTableWidgetItem("asd"))
# call.scheduled_jobs_table.setItem(0, 3, QTableWidgetItem("asd"))
#
# call.scheduled_jobs_table.show()


app.exec()
