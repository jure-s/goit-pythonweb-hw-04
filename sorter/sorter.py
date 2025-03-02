import asyncio
from pathlib import Path
from sorter.file_reader import read_folder
from sorter.file_copier import copy_file
from sorter.logger import log_info, log_error

async def sort_files(source_folder: Path, destination_folder: Path, move: bool = False):
    """Основна функція сортування файлів за розширенням."""
    if not source_folder.exists() or not source_folder.is_dir():
        log_error(f"Помилка: Папка {source_folder} не існує або не є директорією.")
        return

    log_info(f"Розпочато сортування файлів з {source_folder} у {destination_folder}")

    files = await read_folder(source_folder)

    if not files:
        log_info("Файлів для сортування не знайдено.")
        return

    copy_tasks = []
    for i, file in enumerate(files, 1):
        print(f"({i}/{len(files)}) Обробляємо {file.name}...")
        copy_tasks.append(copy_file(file, destination_folder, move))

    await asyncio.gather(*copy_tasks)

    log_info("Сортування завершено.")
