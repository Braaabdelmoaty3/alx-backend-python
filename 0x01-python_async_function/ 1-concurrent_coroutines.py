#!/usr/bin/env python3
import asyncio,random

wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    1. import wait_random
    2.write wait_n that take 2 argument (n,max_delay)
    3.
    """
    list_delay =[]
    await random.uniform(0, wait_random)
    await random.uniform(n)
