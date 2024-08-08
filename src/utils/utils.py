import os
import subprocess

from job import Job


def alert(msg: str) -> None:
    print(f"[ info ] {msg}")


def check_cronie_running() -> bool:
    """
    checks is cronie is installed or running for scheduling tasks\n
    :return True if cronie.service is running else False
    """

    if os.system("systemctl status cronie > /dev/null 2>&1") != 0:
        alert("cronie is not installed or cronie.service is not running.")
        return False

    return True


def check_rsync_available() -> bool:
    """
    checks is rsync is installed\n
    :return True if rsync is installed (by checking the version) else False
    """

    if os.system("rsync -V > /dev/null 2>&1") != 0:
        alert("rsync is probably not installed.")
        return False

    return True


def init() -> None:
    """
    creates the /home/user/.pyserversync_jobs dir to store the generated files\n
    :return: None
    """
    # get the name of the user even when running as sudo
    name = subprocess.run(['logname'], stdout=subprocess.PIPE).stdout.decode('utf-8').removesuffix("\n")
    # -p makes it idempotent
    os.system(f"mkdir -p /home/{name}/.pyserversync_jobs")


def load_saved_jobs() -> list[Job]:
    files = os.listdir(".pyserversync_jobs")
    with open("/etc/crontab", "r") as crontab:
        cron_file = crontab.read()

    # cron_file += "\ntesttt\n"
    #
    # with open("/etc/crontab", "w") as crontab:
    #     crontab.write(cron_file)

    # TODO this is ugly and not very fault tolerant. use regex or metadata files myb
    # for f in files:
    #     with open(f".pyserversync_jobs/{f}", "r") as scriptfile:
    #         script = scriptfile.read()
    #         lines = script.split("\n")
    #         job = Job()
    #         job.name = f.removesuffix(".sh")
    #
    #         args = lines[2].split(" ")
    #         job.src = args[2]
    #         job.dst = args[3]
    #
    #         job.notifications = "notify-send" in lines[-1]
    #         job.twoway = lines[2].startswith("rsync") and lines[3].startswith("rsync")
    #         job.enabled = None
    #
    #         job.script_path = f".pyserversync_jobs/{f}"
