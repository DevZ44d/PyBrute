from __future__ import annotations
import hashlib
import os
import time
from colorama import Fore, init
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

init(autoreset=True)


@dataclass(frozen=True)
class HashInfo:
    name: str
    constructor: Callable[..., Any]
    hex_length: int


SUPPORTED: Dict[str, HashInfo] = {
    "md5":        HashInfo("MD5",        hashlib.md5,      32),
    "sha1":       HashInfo("SHA-1",      hashlib.sha1,     40),
    "sha224":     HashInfo("SHA-224",    hashlib.sha224,   56),
    "sha256":     HashInfo("SHA-256",    hashlib.sha256,   64),
    "sha384":     HashInfo("SHA-384",    hashlib.sha384,   96),
    "sha512":     HashInfo("SHA-512",    hashlib.sha512,  128),
    "sha3-256":   HashInfo("SHA3-256",   hashlib.sha3_256, 64),
    "blake2b":    HashInfo("BLAKE2b",    hashlib.blake2b, 128),
    "blake2s":    HashInfo("BLAKE2s",    hashlib.blake2s,  64),
}


def guess_hash_info(hexstr: str) -> Optional[HashInfo]:
    hexstr = hexstr.strip().lower()
    if not all(c in "0123456789abcdef" for c in hexstr):
        return None
    length = len(hexstr)
    for info in SUPPORTED.values():
        if length == info.hex_length:
            return info
    return None


class Brute:
    def __init__(
        self,
        hashes: List[str],
        wordlists: List[str | Path],
    ):
        self.hashes = [h.strip().lower() for h in hashes if h.strip()]
        self.wordlist_paths = [Path(p).resolve() for p in wordlists]

        for p in self.wordlist_paths:
            if not p.is_file():
                raise FileNotFoundError(f"Not a file: {p}")

        if not self.hashes:
            raise ValueError("No hashes provided")
        if not self.wordlist_paths:
            raise ValueError("No wordlists provided")

    def _check_hash(self, candidate: str, target: str, info: HashInfo) -> bool:
        try:
            h = info.constructor(candidate.encode("utf-8", "replace")).hexdigest()
            return h == target
        except:
            return False

    def _try_wordlist(
        self,
        target: str,
        info: HashInfo,
        wl: Path
    ) -> Tuple[Optional[str], int, float]:

        start = time.perf_counter()
        attempts = 0
        found = None

        with wl.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                cand = line.rstrip("\r\n")
                if not cand:
                    continue

                attempts += 1

                if self._check_hash(cand, target, info):
                    found = cand
                    break

        elapsed = time.perf_counter() - start
        return found, attempts, elapsed

    def start(self) -> None:

        total_attempts = 0
        total_time = 0.0
        found_count = 0

        print(f"{Fore.WHITE}\nCracking {Fore.RED}{len(self.hashes)} {Fore.WHITE}hash(es) with {Fore.RED}{len(self.wordlist_paths)} {Fore.WHITE}wordlist(s)")
        print("═" * 70)

        for idx, target in enumerate(self.hashes, 1):

            info = guess_hash_info(target)
            if not info:
                print(f"  {idx:2}. {target[:12]}… → unsupported format/length")
                continue

            print(f"  {idx:2}. {target[:12]}… ({info.name:<8}) ", end="", flush=True)

            found = None
            used_wordlist = None

            for wl in self.wordlist_paths:

                pwd, att, elapsed = self._try_wordlist(target, info, wl)

                total_attempts += att
                total_time += elapsed

                if pwd:
                    found = pwd
                    used_wordlist = wl.name
                    break
            if found:
                found_count += 1
                print(f"→ {Fore.RED}{found} {Fore.WHITE}| found in ({Fore.RED}{used_wordlist}{Fore.WHITE})")
            else:
                print("→ not found")

        print("═" * 70)

        if total_time > 0.001:
            avg_speed = total_attempts / total_time
            print(f"Attempts : {Fore.RED}{total_attempts:,}{Fore.WHITE}")
            print(f"Time     : {Fore.RED}{total_time:.2f} {Fore.WHITE}s")
            print(f"Speed    : {Fore.RED}{avg_speed:,.0f} {Fore.WHITE}H/s")
        else:
            print("Attempts : very small wordlist")
            print("Time     : < 0.01 s")
            print(f"Speed    : N/A ({Fore.RED}too fast to measure accurately{Fore.WHITE})")

        print(f"Cracked {found_count}/{len(self.hashes)} hash(es)")



