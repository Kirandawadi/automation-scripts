import requests
import sys, os

discordUrl = os.getenv(DISCORD_URL)         #test_channel

def DiscordWebHook(discordUrl):
    botName = "crontest"   
    #message = f'```yaml\n [{sys.argv[1]}]: Finished Bheem Script for {sys.argv[2]}``` Results stored in **folder**: {sys.argv[3]}'
    fd = os.open("/home/kdn00b/automation/crontest/subdomains.txt",os.O_RDWR)
    message = os.read(fd, 10000)
    #print(f'{message}')
    os.close(fd)

    data = {
    "content": message, 
    "username": botName
    }   
    response = requests.post(discordUrl, json=data) 
    if (response.status_code == 204):
    	print('Notified ')
    else:
    	print('Some error occured.')

def getHooks():
	if (discordUrl):
		DiscordWebHook(discordUrl)
	else:
		print("Please add a discord web Hook!")


getHooks()
