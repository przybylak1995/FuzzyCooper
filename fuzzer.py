import all_requests
import re


def fuzz_url(url, wordlist):
    for word in wordlist:
        change_word(url,word)


def change_word(url,word):
    words_between = re.findall(r"!(.*?)!", url)
    for i in range(0, len(words_between)):
        new_url = url.replace(words_between[i], word)
        new_url = new_url.replace("!", "")
        all_requests.get_request(new_url)