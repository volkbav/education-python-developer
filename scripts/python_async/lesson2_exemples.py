import asyncio
from typing import Self


class AsyncRange:
    def __init__(self, n: int) -> None:
        self.n = n
        self.i = 0

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> int:
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.i += 1
        return self.i


async def main() -> None:
    async for number in AsyncRange(5):
        print(number)


asyncio.run(main())
