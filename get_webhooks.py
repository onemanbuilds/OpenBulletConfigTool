from helpers import _clear,_setTitle,_printText,_readFile,_copyFile,colors

class GetWebhooks:
    def __init__(self,configs) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [GetWebhooks]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                                 ██████╗ ███████╗████████╗
                                                ██╔════╝ ██╔════╝╚══██╔══╝
                                                ██║  ███╗█████╗     ██║   
                                                ██║   ██║██╔══╝     ██║   
                                                ╚██████╔╝███████╗   ██║   
                                                 ╚═════╝ ╚══════╝   ╚═╝   
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.configs = configs

    def _getWebhooks(self):
        open('[GetWebhooks]/webhooks.txt', 'w',encoding='utf8',errors='ignore').close()
        for config in self.configs:
            current_content = _readFile(f'[Configs]/{config}','r',1)
            try:
                for line in current_content:
                    if 'https://discordapp.com/api/webhooks/' in line:
                        webhook = 'https://'+line.split('https://')[1].replace('"','').strip()
                        _printText(colors['bcyan'],colors['lpurple'],'FOUND',config)
                        with open(f'[GetWebhooks]/webhooks.txt','a',encoding='utf8',errors='ignore') as f:
                            f.write(f'{webhook}\n')
                        _copyFile(f'[Configs]/{config}',f'[GetWebhooks]/{config}')
                        _printText(colors['bcyan'],colors['lpurple'],'COPIED',config)
            except Exception:
                pass


    def _start(self):
        self._getWebhooks()