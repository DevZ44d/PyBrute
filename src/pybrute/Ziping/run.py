from .Banners import banner
from .main import ZipCracker
from colorama import Fore
from typing import List
import random, time
from pathlib import Path


class BruteForce:
    def __init__(self):
        self.ran = random.randint(0, len(banner) - 1)

    def print_banner(self) -> str:
        return banner[self.ran]

    def show_banner(self):
        banner_text = self.print_banner()
        for line in banner_text.splitlines():
            time.sleep(0.05)
            print(Fore.RED + line)

    def start(self, zip_files: List[str | Path], wordlists: List[str | Path],):
        self.show_banner()
        _x = ZipCracker(zip_files=zip_files, wordlists=wordlists)
        _x.start()


