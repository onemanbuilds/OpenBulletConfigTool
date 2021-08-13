from helpers import _clear,_setTitle,_printText,_getRandomProxy,colors
from threading import Thread,active_count
import requests

class SpamWebhooks:
    def __init__(self,webhooks) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [SpamWebhooks]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                            ███████╗██████╗  █████╗ ███╗   ███╗
                                            ██╔════╝██╔══██╗██╔══██╗████╗ ████║
                                            ███████╗██████╔╝███████║██╔████╔██║
                                            ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
                                            ███████║██║     ██║  ██║██║ ╚═╝ ██║
                                            ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.webhooks = webhooks

        self.use_proxy = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}[1]Proxy [2]Proxyless:{colors["bcyan"]} '))
        self.proxy_type = None

        if self.use_proxy == 1:
            self.proxy_type = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}[1]Https [2]Socks4 [3]Socks5:{colors["lpurple"]} '))

        self.threads = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Threads:{colors["lpurple"]} '))
        self.message = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Message:{colors["lpurple"]} '))
        self.session = requests.session()
        print('')

    def _spam(self,webhook_url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Pragma':'no-cache',
            'Accept':'*/*',
            'Content-Type':'application/json'
        }

        payload = {'content':self.message}

        proxy = _getRandomProxy(self.use_proxy,self.proxy_type,'proxies.txt')

        try:
            response = self.session.post(webhook_url,headers=headers,proxies=proxy,json=payload)
            webhook_token = webhook_url.split('/')[-1]
            if response.status_code == 401:
                _printText(colors['red'],colors['lpurple'],'INVALID',webhook_token)
            elif response.status_code == 404:
                _printText(colors['yellow'],colors['lpurple'],'UNKNOWN',webhook_token)
            elif response.status_code == 204:
                _printText(colors['bcyan'],colors['lpurple'],'SENT',webhook_token)
            else:
                self._spam(webhook_url)
        except Exception:
            self._spam(webhook_url)


    def _start(self):
        threads = []

        for webhook_url in self.webhooks:
            run = True

            while run:
                if active_count()<=self.threads:
                    thread = Thread(target=self._spam,args=(webhook_url,))
                    threads.append(thread)
                    thread.start()
                    run = False
        for x in threads:
            x.join()

        print('')
        _printText(colors['yellow'],colors['lpurple'],'FINISHED','Process done!')