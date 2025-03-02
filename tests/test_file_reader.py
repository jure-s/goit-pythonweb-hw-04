import pytest
import asyncio
from pathlib import Path
from sorter.file_reader import read_folder

@pytest.mark.asyncio
async def test_read_folder(tmp_path):
    """Перевірка, чи коректно зчитуються файли з директорії."""
    test_dir = tmp_path / "test_source"
    test_dir.mkdir()

    # Створюємо тестові файли
    (test_dir / "file1.txt").touch()
    (test_dir / "file2.jpg").touch()
    
    files = await read_folder(test_dir)

    assert len(files) == 2
    assert test_dir / "file1.txt" in files
    assert test_dir / "file2.jpg" in files
