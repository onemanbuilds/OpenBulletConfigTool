from helpers import _clear,_setTitle,_printText,_readFile,colors
from add_webhook import AddWebhook
from duplicate_remover import DuplicateRemover
from get_webhooks import GetWebhooks
from remove_webhook import RemoveWebhook
from replace_webhook import ReplaceWebhook
from spam_webhooks import SpamWebhooks
from time import sleep
from os import listdir

class Menu:
    def __init__(self) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [Menu]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                          ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
                                          ████╗ ████║██╔════╝████╗  ██║██║   ██║
                                          ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
                                          ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
                                          ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
                                          ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

    def _menu(self):        
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [Menu]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                          ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
                                          ████╗ ████║██╔════╝████╗  ██║██║   ██║
                                          ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
                                          ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
                                          ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
                                          ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.configs = listdir("[Configs]/")
        self.webhooks = _readFile('[GetWebhooks]/webhooks.txt','r',1)
        self.webhook_cfgs = listdir("[GetWebhooks]/")

        options = ['Get Webhooks','Remove Duplicates','Spam Discord Webhooks','Remove Webhooks','Add Webhook','Replace Webhooks']
        counter = 0
        for option in options:
            counter+=1
            _printText(colors['bcyan'],colors['lpurple'],str(counter),option)
        print('')

        selected = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Select something:{colors["lpurple"]} '))

        if selected == 1:
            GetWebhooks(self.configs)._start()
            sleep(2)
            self._menu()
        elif selected == 2:
            DuplicateRemover(self.configs,self.webhooks)._menu()
            sleep(2)
            self._menu()
        elif selected == 3:
            SpamWebhooks(self.webhooks)._start()
            sleep(2)
            self._menu()
        elif selected == 4:
            RemoveWebhook(self.configs,self.webhooks,self.webhook_cfgs)._start()
            sleep(2)
            self._menu()
        elif selected == 5:
            AddWebhook(self.configs)._start()
            sleep(2)
            self._menu()
        elif selected == 6:
            ReplaceWebhook(self.configs,self.webhooks,self.webhook_cfgs)._start()
            sleep(2)
            self._menu()
        else:
            self._menu()