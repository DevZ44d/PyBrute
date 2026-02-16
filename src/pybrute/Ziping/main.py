from __future__ import annotations
import zipfile
import time
from pathlib import Path
from typing import List, Optional, Tuple
from colorama import Fore


class ZipCracker:
    def __init__(
        self,
        zip_files: List[str | Path],
        wordlists: List[str | Path],
    ):
        self.zip_paths = [Path(p).resolve() for p in zip_files]
        self.wordlist_paths = [Path(p).resolve() for p in wordlists]

        # Validation
        for p in self.zip_paths:
            if not p.is_file():
                raise FileNotFoundError(f"ZIP file not found: {p}")
            if not zipfile.is_zipfile(p):
                raise ValueError(f"Not a valid ZIP: {p}")

        for p in self.wordlist_paths:
            if not p.is_file():
                raise FileNotFoundError(f"Wordlist not found: {p}")

        if not self.zip_paths:
            raise ValueError("No ZIP files given")
        if not self.wordlist_paths:
            raise ValueError("No wordlists given")

    def _try_one_wordlist(
        self,
        zip_path: Path,
        wordlist_path: Path
    ) -> Tuple[Optional[str], int, float]:

        start = time.perf_counter()
        attempts = 0

        try:
            with wordlist_path.open(encoding="utf-8", errors="replace") as f:
                for line in f:
                    password = line.rstrip("\r\n")
                    if not password:
                        continue

                    attempts += 1

                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zf:
                            zf.extractall(
                                pwd=password.encode('utf-8', errors='replace')
                            )

                        # لو وصل هنا يبقى الباسورد صح
                        elapsed = time.perf_counter() - start
                        return password, attempts, elapsed

                    except:
                        continue

        except Exception as e:
            print(f"  ! Error with wordlist {wordlist_path.name}: {e}")

        elapsed = time.perf_counter() - start
        return None, attempts, elapsed

    def start(self) -> None:
        total_attempts = 0
        total_time = 0.0
        found_count = 0

        print(
            f"{Fore.WHITE}\nCracking {Fore.RED}{len(self.zip_paths)} {Fore.WHITE}ZIP file(s) "
            f"with {Fore.RED}{len(self.wordlist_paths)} {Fore.WHITE}wordlist(s)"
        )
        print("═" * 70)

        for idx, zip_path in enumerate(self.zip_paths, 1):

            print(f"  {idx:2}. {zip_path.name} ", end="", flush=True)

            found = None
            used_wordlist = None

            for wl in self.wordlist_paths:

                pwd, att, elapsed = self._try_one_wordlist(zip_path, wl)

                total_attempts += att
                total_time += elapsed

                if pwd:
                    found = pwd
                    used_wordlist = wl.name
                    break

            if found:
                found_count += 1
                print(
                    f"\r  {idx:2}. {zip_path.name} → "
                    f"{Fore.RED}{found}{Fore.WHITE} "
                    f"| found in ({Fore.RED}{used_wordlist}{Fore.WHITE})"
                )
            else:
                print(f"\r  {idx:2}. {zip_path.name} → not found")

        print("═" * 70)

        if total_time > 0:
            avg_speed = total_attempts / total_time
            print(f"Total attempts : {total_attempts:,}")
            print(f"Total time     : {total_time:.2f} s")
            print(f"Avg speed      : {avg_speed:,.0f} pw/s")
        else:
            print("Attempts : very small wordlist")
            print("Time     : <0.01 s")
            print("Speed    : N/A")

        print(f"Cracked {found_count}/{len(self.zip_paths)} file(s)")


