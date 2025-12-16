import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager


@asynccontextmanager
async def database_connection() -> AsyncGenerator[str, None]:
    """Контекстный менеджер для работы с базой данных"""
    print("Открытие соединения с БД")
    conn = "db_connection"
    try:
        yield conn
    finally:
        print("Закрытие соединения с БД")
        await asyncio.sleep(0.1)


async def fetch_user_data(user_id: int) -> dict[str, str]:
    """Получение данных пользователя с таймаутом"""
    try:
        async with asyncio.timeout(5):
            async with database_connection() as conn:
                print(f"Запрос к БД через {conn} для пользователя {user_id}")
                await asyncio.sleep(2)  # имитация запроса
                return {"id": str(user_id), "name": "User"}
    except asyncio.CancelledError:
        print("Операция отменена, ресурсы освобождены")
        raise  # Важно: пробрасываем исключение дальше


async def main() -> None:
    try:
        user = await fetch_user_data(123)
        print(f"Получены данные: {user}")
    except asyncio.TimeoutError:
        print("Превышено время ожидания ответа от БД")


if __name__ == "__main__":
    asyncio.run(main())