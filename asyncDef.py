import asyncio
import random


async def myCoroutine():
    process_time = random.randint(2, 5)
    print('Will sleep for %d seconds' % process_time)
    await asyncio.sleep(process_time)
    print('This task has been completed')

loop = asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(myCoroutine())
loop.close()
