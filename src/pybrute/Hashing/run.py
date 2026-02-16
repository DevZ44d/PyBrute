from .Banners import Banners
import random
import time
from colorama import Fore
from .main import Brute
from typing import List


class BruteForce:
    def __init__(self):
        self.ran = random.randint(0, len(Banners) - 1)

    def print_banner(self) -> str:
        return Banners[self.ran]

    def show_banner(self):
        banner_text = self.print_banner()
        for line in banner_text.splitlines():
            time.sleep(0.05)
            print(Fore.RED + line)

    def brute(self, hashes: List[str], wordlists: List[str]):
        self.show_banner()

        bf = Brute(
            hashes=hashes,
            wordlists=wordlists,
        )
        bf.start()
