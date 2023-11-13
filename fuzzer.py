import all_requests
import re


def fuzz_url(url, wordlist, method):
    for word in wordlist:
        change_word(url,word, method)


def change_word(url,word, method):
    words_between = re.findall(r"BANG", url)
    for i in range(0, len(words_between)):
        new_url = url.replace(words_between[i], word)
        new_url = new_url.replace("!", "")

        if method == "GET":
            all_requests.get_request(new_url)
        elif method == "GQL":
            all_requests.graphql_request(new_url)