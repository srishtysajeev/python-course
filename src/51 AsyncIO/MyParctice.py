"""
Following the tutorial found at: https://realpython.com/async-io-python/

"""

# import asyncio

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await asyncio.sleep(1)
#     print("Three")
#     await asyncio.sleep(1)

# async def main():
#     await asyncio.gather(count(), count(), count())
#     # for _ in range(3): 
#     #     count()

# if __name__ == "__main__":
#     import time

#     start = time.perf_counter() # takes a snapshot of the current time
#     asyncio.run(main())
#     elapsed = time.perf_counter( ) - start
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")


import asyncio
import random

COLORS = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

async def main():
    return await asyncio.gather(
        makerandom(1, 9),
        makerandom(2, 8),
        makerandom(3, 8),
    )

async def makerandom(delay, threshold=6):
    color = COLORS[delay]
    print(f"{color}Initiated makerandom({delay}).")
    while (number := random.randint(0, 10)) <= threshold:
        print(f"{color}makerandom({delay}) == {number} too low; retrying.")
        await asyncio.sleep(delay)
    print(f"{color}---> Finished: makerandom({delay}) == {number}" + COLORS[0])
    return number

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
