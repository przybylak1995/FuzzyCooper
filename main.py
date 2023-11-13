import sys
import argparse
import fuzzer
import load_wordlist
import pyfiglet


def main():
    ascii_banner = pyfiglet.figlet_format("!Fuzzy Cooper!")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description='URL Fuzzer', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to wordlist file')

    args = parser.parse_args()

    if args.help is not None:
        parser.print_help()
        sys.exit(0)

    url = args.url
    wordlist = load_wordlist.load_words(args.wordlist)

    fuzzer.fuzz_url(url, wordlist)


if __name__ == "__main__":
    main()
