import os
from telethon.sync import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

proxy_address = os.environ.get("PROXY_ADDR")
proxy_username = os.environ.get("PROXY_USERNAME")
proxy_pass = os.environ.get("PROXY_PASSWORD")

use_proxy = proxy_address and proxy_username and proxy_pass

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
creator_id = int(os.environ.get("CREATOR_ID"))
bot_token = os.environ.get("BOT_TOKEN")

bot = TelegramClient(session="my_session", api_hash=api_hash, api_id=api_id, proxy={
    'proxy_type': 'http', # (mandatory) protocol to use (see above)
    'addr': proxy_address,      # (mandatory) proxy IP address
    'port': 3128,           # (mandatory) proxy port number
    'username': proxy_username,      # (optional) username if the proxy requires auth
    'password': proxy_pass      # (optional) password if the proxy requires auth
} if use_proxy else None).start(bot_token=bot_token)

# async def main():
#    await 

with bot:
    print('inside with')
    bot.send_message(creator_id, "testing ")
    @bot.on(events.NewMessage(pattern="/info"))
    async def handler(event):
        print('got message')
        user_id = event.message.from_id
        user_entity = await bot.get_entity(user_id)
        await bot.send_message(user_id, f'Your ID:{user_entity.id}\nName:{user_entity.first_name} {user_entity.last_name}\nUsername:@{user_entity.username}\n<a href=t.me/{user_entity.username}>Link to your profile</a>', parse_mode='html')
    bot.run_until_disconnected()
    


