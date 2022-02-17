from httplib2 import Response
import requests
import sys

def ascii() -> str:
    print(
        "\n"
    ".------..------..------..------..------..------..------..------.\n"
    "|W.--. ||C.--. ||S.--. ||J.--. ||O.--. ||K.--. ||E.--. ||R.--. |\n"
    "| :/\: || :/\: || :/\: || :(): || :/\: || :/\: || (\/) || :()Ped: |\n"
    "| :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: || ()() |\n"
    "| '--'W|| '--'C|| '--'S|| '--'J|| '--'O|| '--'K|| '--'E|| '--'R|\n"
    "`------'`------'`------'`------'`------'`------'`------'`------'\n"
    )


def argvs_condition() -> bool:
    if "-u" in sys.argv and "-w" in sys.argv and len(sys.argv) == 5:
        return True
    else:
        print("Use wcsjoker.py -u host -w wordlist\n")
        sys.exit()


def get_argvs() -> list:
    url = sys.argv[sys.argv.index("-u") + 1]
    wordlist = sys.argv[sys.argv.index("-w") + 1]
    return [url, wordlist]


def filter_response_http(resp: Response) -> str:
    resp = str(resp)
    return resp.split("[")[1].split("]")[0]


if __name__ == "__main__":
    ascii()
    if argvs_condition():
        url, wordlist = get_argvs()
        for i in open(wordlist, "r"):
            url_ready = f"{url}{i}"
            r = filter_response_http(requests.get(f"{url_ready}"))
            match r:
                case "200":
                    print(f"[+] {url_ready}")
                case "401":
                    print(print(f"[-] {url_ready}"))
