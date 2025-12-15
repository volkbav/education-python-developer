import asyncio
from random import uniform

async def download_file(file_id: int):
    print(f"Начало скачивания файла {file_id}")
    await asyncio.sleep(uniform(1, 3))
    print(f"Завершен скачивание файла {file_id}")

async def process_file(file_id: int):
    print(f"Начало обработки файла {file_id}")
    await asyncio.sleep(uniform(1, 2))
    print(f"Завершена обработка файла {file_id}")

async def main() -> None:
    for i in range(1, 4):
        await download_file(i)
        await process_file(i)


if __name__ == "__main__":
    asyncio.run(main())