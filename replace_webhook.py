from helpers import _clear,_setTitle,_printText,_copyFile,colors

class ReplaceWebhook:
    def __init__(self,configs,webhooks,webhook_cfgs) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [ReplaceWebhooks]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                 ██████╗ ███████╗██████╗ ██╗      █████╗  ██████╗███████╗
                                 ██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝██╔════╝
                                 ██████╔╝█████╗  ██████╔╝██║     ███████║██║     █████╗  
                                 ██╔══██╗██╔══╝  ██╔═══╝ ██║     ██╔══██║██║     ██╔══╝  
                                 ██║  ██║███████╗██║     ███████╗██║  ██║╚██████╗███████╗
                                 ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)
        
        self.configs = configs
        self.webhooks = webhooks
        self.webhook_cfgs = webhook_cfgs

        self.webhook_url = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Webhook URL:{colors["lpurple"]} '))
        print('')

    def _replace(self,file,searchExp,replaceExp):
        with open(file,'r+',encoding='utf8',errors='ignore') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if searchExp in line:

                    line = line.replace(searchExp,replaceExp)
                f.write(line)
            f.truncate()

    def _replaceWebhooks(self):
        for i in range(len(self.webhook_cfgs)):
            if (self.webhook_cfgs[i].endswith('.loli')) or (self.webhook_cfgs[i].endswith('.anom')):
                _copyFile(f'[GetWebhooks]/{self.webhook_cfgs[i]}',f'[ReplaceWebhooks]/{self.webhook_cfgs[i]}')
                _printText(colors['bcyan'],colors['lpurple'],'COPIED',self.webhook_cfgs[i])
                for j in range(len(self.webhooks)):
                    self._replace(f'[ReplaceWebhooks]/{self.webhook_cfgs[i]}',self.webhooks[j],self.webhook_url)
                _printText(colors['bcyan'],colors['lpurple'],'REPLACED',self.webhook_cfgs[i])
        
    def _start(self):
        self._replaceWebhooks()
            