import asyncio


async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)
    return f"Данные с {url}"


async def main() -> None:
    # Хорошо: создаём задачи и сохраняем ссылки
    task1 = asyncio.create_task(fetch_data("api.example.com/users"), name="fetch_users")
    task2 = asyncio.create_task(fetch_data("api.example.com/posts"), name="fetch_posts")

    # Хорошо: ожидаем завершения всех задач
    results = await asyncio.gather(task1, task2)
    print(results)

    # Проверяем, нет ли утечек задач
    tasks = [t for t in asyncio.all_tasks() if not t.done() and t != asyncio.current_task()]
    if tasks:
        print(f"Внимание: найдено {len(tasks)} незавершённых задач")
        for task in tasks:
            print(f"  - {task.get_name()}")


if __name__ == "__main__":
    asyncio.run(main())