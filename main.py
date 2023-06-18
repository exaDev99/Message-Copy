import requests
import json
from discordwebhook import Discord

# Config

token = ""

hook = ""

ch_id = ""

meoaw = {
    'authorization':token
}

auth = requests.get(f"https://discord.com/api/v9/channels/{ch_id}/messages", headers=meoaw)

jsonn = json.loads(auth.text)

for user in jsonn:

    ch_id = user['channel_id']

    msg_id = user['id']

    time = user['timestamp']

    get_username = user['author']['username']

    get_id = user['author']['id']

    get_profile = user['author']['avatar']

    get_avatar = 'https://cdn.discordapp.com/avatars/' + get_id + "/" + get_profile + '.png'

    get_content = user['content']

    discord = Discord(url=hook)

    discord.post(username=get_username, avatar_url=get_avatar, content=get_content)

    print(" ")

    print("Get msg success !")

    print(" ")

# Code by Seriz Team | discord.gg/meoaw 