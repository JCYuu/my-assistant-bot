import asyncio
import starrailcard
import os
from dotenv import load_dotenv
from starrailcard.src.api import api

load_dotenv(dotenv_path='../.env')
proxy_addr = os.environ.get('PROXY_ADDR')
proxy_user = os.environ.get('PROXY_USERNAME')
proxy_pass = os.environ.get('PROXY_PASSWORD')


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    async with starrailcard.Card(proxy=f'http://{proxy_user}:{proxy_pass}@{proxy_addr}:3128', save=True, character_id='1220, 1112', boost_speed=True) as card:
        print(card)
        
        data = await card.create(602286238, style=2)
        await card.create_profile(602286238)
    print(data)

asyncio.run(main())