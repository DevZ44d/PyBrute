import argparse
import sys
from colorama import Fore
from .Ziping.run import BruteForce as ZipBruteForce
from .Hashing.run import BruteForce as HashBruteForce
from .main import versions, help_m

def main():
    parser = argparse.ArgumentParser(
        prog="PyBrute",
        description="PyBrute - Hash & ZIP BruteForce Tool",
        add_help=False
    )
    parser.add_argument("-H", "--hash", action="append", dest="hashes", help="Hash to crack (can be used multiple times)")
    parser.add_argument("-Z", "--zip", action="append", dest="zips", help="Zip file to crack (can be used multiple times)")
    parser.add_argument("-w", "--wordlist", action="append", dest="wordlists", help="Wordlist file (can be used multiple times)")
    parser.add_argument("-h", "--help", action="store_true", dest="show_help", help="Show help message")
    parser.add_argument("-v", "--version",action="store_true",dest="show_version",help="Show PyBrute version")

    args = parser.parse_args()
    if args.show_help:
        print(help_m())
        sys.exit(0)

    if args.show_version:
        print(versions())
        sys.exit(0)

    if len(sys.argv) == 1:
        print(help_m())
        sys.exit(0)

    if args.hashes and args.zips:
        print(f"[{Fore.RED}ERROR{Fore.WHITE}] Cannot use `{Fore.RED}-H{Fore.WHITE}` and `{Fore.RED}-Z{Fore.WHITE}` together.")
        sys.exit(1)

    if (args.hashes or args.zips) and not args.wordlists:
        print(f"[{Fore.RED}ERROR{Fore.WHITE}] You must provide at least one wordlist using `{Fore.RED}-w{Fore.WHITE}`")
        sys.exit(1)

    if args.hashes:
        run_hash_attack = HashBruteForce()
        run_hash_attack.brute(
            hashes=args.hashes,
            wordlists=args.wordlists
        )

    elif args.zips:
        run_zip_attack = ZipBruteForce()
        run_zip_attack.start(
            zip_files=args.zips,
            wordlists=args.wordlists
        )

    else:
        print(f"[{Fore.RED}ERROR{Fore.WHITE}] No valid arguments provided. Use `{Fore.RED}-h{Fore.WHITE}` for help.")



if __name__ == "__main__":
    main()
