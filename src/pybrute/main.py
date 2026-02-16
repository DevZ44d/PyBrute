from importlib.metadata import version, PackageNotFoundError
from colorama import Fore


def versions():
    try:
        pkg_version = version("pybrute")
    except PackageNotFoundError:
        pkg_version = "unknown"

    return f"""
{Fore.RED}PyBrute {Fore.WHITE}Version: {Fore.RED}{pkg_version}{Fore.WHITE}
Author: {Fore.RED}PyCodz{Fore.WHITE} .

({Fore.RED}PyPI{Fore.WHITE})      : https://pypi.org/project/PyBrute .
({Fore.RED}GitHub{Fore.WHITE})    : https://github.com/DevZ44d/PyBrute .
({Fore.RED}Telegram{Fore.WHITE})  : https://t.me/PyCodz .
({Fore.RED}Portfolio{Fore.WHITE}) : https://deep.is-a.dev .
"""


def help_m() -> str:
    return f"""
{Fore.RED}PyBrute{Fore.WHITE} - Advanced Hash & ZIP BruteForce Tool
Usage:
        {Fore.RED}PyBrute {Fore.WHITE}-[OPTIONS] "[FOR-OPTION]"

Options:
  {Fore.RED}-H, --hash{Fore.WHITE}          Hash to crack (can be used multiple times).
  {Fore.RED}-Z, --zip{Fore.WHITE}           ZIP file to crack (can be used multiple times).
  {Fore.RED}-w, --wordlist{Fore.WHITE}      Wordlist file (can be used multiple times).
  {Fore.RED}-v, --version{Fore.WHITE}       Show PyBrute version.
  {Fore.RED}-h, --help{Fore.WHITE}          Show this help message.
"""


