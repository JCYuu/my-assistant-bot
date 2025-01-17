import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
proxy_addr = os.environ.get('PROXY_ADDR')
proxy_user = os.environ.get('PROXY_USERNAME')
proxy_pass = os.environ.get('PROXY_PASSWORD')
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    url = "https://starraillcard.up.railway.app/api/card"
    headers = {'Content-Type': 'application/json'}

    data = {
        "uid": "602286238",
        "name": "1112",
        "image": {"1302": "https://i.pximg.net/img-master/img/2023/06/20/16/53/28/109183352_p0_master1200.jpg"}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("message") is None:
                    print("Request successful")
                    print(data)
                else:
                    print("Request failed")
                    print(data.get("message"))
            else:
                print(f"Request failed with status code {response.status}")

asyncio.run(main())