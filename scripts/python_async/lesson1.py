import asyncio
import time


# Синхронная версия
def sync_task(n: int) -> None:
    print(f"Синхронная задача {n} начата")
    time.sleep(1)
    print(f"Синхронная задача {n} завершена")


# Асинхронная версия
async def async_task(n: int) -> None:
    print(f"Асинхронная задача {n} начата")
    await asyncio.sleep(1)
    print(f"Асинхронная задача {n} завершена")

def sync_main() -> None:
    start = time.time()

    for i in range(1, 6):
        sync_task(i)

    print("Синхронное время выполнения:", time.time() - start)


async def async_main() -> None:
    start = time.time()

    tasks = [async_task(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)

    print("Асинхронное время выполнения:", time.time() - start)


if __name__ == "__main__":
    print("=== Синхронная версия ===")
    sync_main()

    print("\n=== Асинхронная версия ===")
    asyncio.run(async_main())