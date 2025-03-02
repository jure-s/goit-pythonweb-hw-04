import aiofiles
import shutil
from pathlib import Path
from sorter.logger import log_info, log_error

async def copy_file(file_path: Path, destination_folder: Path, move: bool = False):
    """Асинхронно копіює або переміщує файл у відповідну підпапку у цільовій папці."""
    if not file_path.exists():
        log_error(f"Файл {file_path} не існує.")
        return

    file_extension = file_path.suffix.lstrip(".").lower() or "unknown"
    target_dir = destination_folder / file_extension

    try:
        target_dir.mkdir(parents=True, exist_ok=True)

        if move:
            shutil.move(file_path, target_dir / file_path.name)
            log_info(f"Файл {file_path} переміщено до {target_dir}")
        else:
            async with aiofiles.open(file_path, "rb") as src, aiofiles.open(target_dir / file_path.name, "wb") as dst:
                await dst.write(await src.read())
            log_info(f"Файл {file_path} асинхронно скопійовано до {target_dir}")

    except Exception as e:
        log_error(f"Помилка копіювання {file_path}: {e}")
