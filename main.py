#!/usr/bin/env python3
import argparse
import fuzzer
import load_wordlist
import pyfiglet
from termcolor import colored
import signal
import sys


def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C! Exiting...')
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

def main():
    ascii_banner = pyfiglet.figlet_format("!Fuzzy Cooper!")
    colored_banner = colored(ascii_banner, color='cyan', attrs=['bold'])
    print(colored_banner)

    parser = argparse.ArgumentParser(description='The Fuzz word is BANG ',
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Changed the argument name from 'help' to 'show_help'
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to wordlist file')
    parser.add_argument('-m', '--method', choices=['GET', 'POST','GQL'], default='GET', help='HTTP request method (GET, POST or GraphQL)')

    args = parser.parse_args()

    url = args.url
    wordlist = load_wordlist.load_words(args.wordlist)
    method = args.method

    fuzzer.fuzz_url(url, wordlist, method)


if __name__ == "__main__":
    main()
