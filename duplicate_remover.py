from helpers import _clear,_setTitle,_printText,colors
from os.path import isfile
from os import remove
from hashlib import md5

class DuplicateRemover:
    def __init__(self,configs,webhooks) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [DuplicateRemover]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                          ██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗███████╗
                          ██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
                          ██║  ██║██║   ██║██████╔╝██║     ██║██║     ███████║   ██║   █████╗  
                          ██║  ██║██║   ██║██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██╔══╝  
                          ██████╔╝╚██████╔╝██║     ███████╗██║╚██████╗██║  ██║   ██║   ███████╗
                          ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.configs = configs
        self.webhooks = webhooks

    def _menu(self):        
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [DuplicateRemover] ^| [Menu]')
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

        options = ['Remove Duplicated Webhooks','Remove Duplicated Configs']
        counter = 0
        for option in options:
            counter+=1
            _printText(colors['bcyan'],colors['lpurple'],str(counter),option)
        print('')

        selected = int(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Select something:{colors["lpurple"]} '))

        if selected == 1:
            self._duplicateWebhookRemove()
        elif selected == 2:
            self._duplicateConfigRemove()
        else:
            self._menu()

    def _duplicateWebhookRemove(self):
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [DuplicateRemover] ^| [WebhookRemove]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                              ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                              ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                              ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                              ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                              ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                               ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)
        _printText(colors['bcyan'],colors['lpurple'],'BEFORE',str(len(self.webhooks)))
        cleaned_file = set(self.webhooks)
        open('[GetWebhooks]/webhooks.txt', 'w',encoding='utf8',errors='ignore').close()
        for line in cleaned_file:
            with open(f'[GetWebhooks]/webhooks.txt','a',encoding='utf8') as f:
                f.write(f'{line}\n')

        _printText(colors['bcyan'],colors['lpurple'],'AFTER',str(len(cleaned_file)))    
        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')

    def _duplicateConfigRemove(self):
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [DuplicateRemover] ^| [ConfigRemove]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                      ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ 
                                     ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ 
                                     ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
                                     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
                                     ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
                                      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ 
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        unique = []
        for config in self.configs:
            if isfile(config):
                filehash = md5(open(config, 'rb').read()).hexdigest()
                if filehash not in unique: 
                    unique.append(filehash)
                else: 
                    remove(config)
                    _printText(colors['bcyan'],colors['lpurple'],'REMOVED',config)
        print('')
        _printText(colors['bcyan'],colors['lpurple'],'FINISHED','Process done!')