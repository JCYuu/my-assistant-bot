import asyncio
import starrailcard

async def main():
    async with starrailcard.Card() as card:
        data = await card.create(602286238, style=2)
    print(data)

asyncio.run(main())