import requests
import sys, os

discordUrl = os.getenv(DISCORD_URL)         #test_channel

def DiscordWebHook(discordUrl):
    botName = "crontest"   
    #message = f'```yaml\n [{sys.argv[1]}]: Finished Bheem Script for {sys.argv[2]}``` Results stored in **folder**: {sys.argv[3]}'
    fd = os.open("just_found",os.O_RDWR)
    file_contents = os.read(fd, 10000)
    os.close(fd)
    str_data = file_contents.decode("utf-8")
    message = '***Found new subdomain:***\n' + str_data
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
