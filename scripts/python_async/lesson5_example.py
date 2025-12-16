import asyncio
import time
from dataclasses import dataclass


@dataclass
class Config:
    """Конфигурация для управления конкурентностью"""

    max_concurrent: int = 5
    queue_size: int = 10
    timeout: float = 30.0


async def fetch_with_limits(url: str, sem: asyncio.Semaphore, config: Config) -> str:
    """Загрузка с ограничениями и таймаутом"""
    async with sem:
        try:
            async with asyncio.timeout(config.timeout):
                await asyncio.sleep(0.5)
                return f"Данные с {url}"
        except asyncio.TimeoutError:
            return f"Таймаут для {url}"


async def main() -> None:
    config = Config(max_concurrent=3, queue_size=5)
    sem = asyncio.Semaphore(config.max_concurrent)

    urls = [f"site-{i}" for i in range(10)]

    # Используем as_completed для ранней обработки
    tasks = [
        asyncio.create_task(fetch_with_limits(url, sem, config), name=f"fetch_{url}")
        for url in urls
    ]

    results = []
    for coro in asyncio.as_completed(tasks):
        try:
            result = await coro
            results.append(result)
            print(f"Обработан результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

    print(f"\nВсего обработано результатов: {len(results)}")


if __name__ == "__main__":
    asyncio.run(main())