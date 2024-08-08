import os


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


