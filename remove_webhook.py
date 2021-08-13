from helpers import _clear,_setTitle,_printText,_copyFile,colors

class RemoveWebhook:
    def __init__(self,configs,webhooks,webhook_cfgs) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [RemoveWebhook]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                  ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗
                                  ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝
                                  ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  
                                  ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  
                                  ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗
                                  ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.configs = configs
        self.webhooks = webhooks
        self.webhook_cfgs = webhook_cfgs

    def _remove(self,file,searchExp):
        if (file.endswith('.loli')) or (file.endswith('.anom')):
            with open(file, 'r+',encoding='utf8',errors='ignore') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if searchExp not in line:
                        f.write(line)
                f.truncate()

    def _removeWebhook(self):
        for i in range(len(self.webhook_cfgs)):
            if (self.webhook_cfgs[i].endswith('.loli')) or (self.webhook_cfgs[i].endswith('.anom')):
                _copyFile(f'[GetWebhooks]/{self.webhook_cfgs[i]}',f'[RemoveWebhooks]/{self.webhook_cfgs[i]}')
                _printText(colors['bcyan'],colors['lpurple'],'COPIED',self.webhook_cfgs[i])
                for j in range(len(self.webhooks)):
                    self._remove(f'[RemoveWebhooks]/{self.webhook_cfgs[i]}',self.webhooks[j])
                _printText(colors['bcyan'],colors['lpurple'],'REMOVED',self.webhook_cfgs[i])

    def _start(self):
        self._removeWebhook()