from src.redis.config import Redis
import asyncio
import redis
from src.model.gptj import GPT
from src.redis.cache import Cache

redis = Redis()

async def main():
    json_client = redis.create_rejson_connection()
    await Cache(json_client).add_message_to_cache(token="n/a", message_data={
        "id": "1",
        "msg": "Hello",
        "timestamp": "2022-07-16 13:20:01.092109"
    })

    data = await Cache(json_client).get_chat_history(token="n/a")
    print(data)

if __name__ == "__main__":
    asyncio.run(main())