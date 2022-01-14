# https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt
import requests
import threading
import time
from threading import Thread
from proxy_checking import ProxyChecker
from colorama import Fore
checker = ProxyChecker()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check(proxy, list_):
    #print(f'Check proxy {proxy}')
    r = checker.check_proxy(proxy)
    if r["status"] == True:
        print(Fore.GREEN + f'[+] Valid proxy - {proxy}')
        try:
            if r['type'] == 'http':
                list_['http'].append(proxy)
            else:
                list_['https'].append(proxy)

        except:
            pass
    else:
        print(Fore.RED + f'[-] Invalid proxy - {proxy}')


def get_proxy():

    proxies_http = []
    proxies = {'https': [], 'http': []}
    proxies_http_ = requests.get(
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt').text.split('\n')
    proxies_http_ = requests.get(
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt').text.split('\n')

    for proxy in proxies_http_:
        th = Thread(target=check, args=(proxy, proxies))
        th.start()
    while threading.active_count() != 1:
        pass

    print(Fore.LIGHTCYAN_EX + f'[*] Parsed {len(proxies_http)} proxies!')
    return proxies
