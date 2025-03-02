import asyncio
from pathlib import Path
from sorter.logger import log_info, log_error

async def read_folder(source_folder: Path) -> list[Path]:
    """Асинхронно читає всі файли у вихідній папці та її підпапках."""
    if not source_folder.exists():
        log_error(f"Папка {source_folder} не існує.")
        return []

    if not source_folder.is_dir():
        log_error(f"{source_folder} не є директорією.")
        return []

    log_info(f"Читаємо файли у папці: {source_folder}")
    file_list = []

    for file_path in source_folder.rglob("*"):  # Рекурсивно шукаємо файли
        if file_path.is_file():
            file_list.append(file_path)

    log_info(f"Знайдено {len(file_list)} файлів.")
    return file_list
