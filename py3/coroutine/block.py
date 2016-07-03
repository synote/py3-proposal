#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import datetime
import asyncio
import time
import sys

print(sys.version)

async def anything(i):
    """
    A coroutine function
    """
    print(i, datetime.datetime.now())

    #explicitly wait on sleep
    await asyncio.sleep(i)
    # task return value
    return i, datetime.datetime.now()



if __name__ == '__main__':
    import logging
    LOG = logging.getLogger('asyncio')
    LOG.setLevel(logging.DEBUG)
    import gc
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    tasks = [loop.create_task(anything(i))
                for i in range(1, 4)]

    try:
        loop.run_until_complete(asyncio.wait(tasks))

        print("the tasks results are:")
        for task in tasks:
            print(*task.result())

    finally:
        loop.close()