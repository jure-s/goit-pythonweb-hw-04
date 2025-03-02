import pytest
import asyncio
from pathlib import Path
from sorter.file_reader import read_folder
from sorter.file_copier import copy_file

@pytest.mark.asyncio
async def test_full_sorting_process(tmp_path):
    """Перевірка всього процесу сортування."""
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    
    (source_dir / "file1.txt").write_text("Тест")
    (source_dir / "file2.jpg").write_text("Фото")

    destination_dir = tmp_path / "sorted"

    files = await read_folder(source_dir)
    copy_tasks = [copy_file(file, destination_dir) for file in files]
    await asyncio.gather(*copy_tasks)

    assert (destination_dir / "txt" / "file1.txt").exists()
    assert (destination_dir / "jpg" / "file2.jpg").exists()
