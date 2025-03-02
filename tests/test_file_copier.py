import pytest
import asyncio
from pathlib import Path
from sorter.file_copier import copy_file

@pytest.mark.asyncio
async def test_copy_file(tmp_path):
    """Перевірка, чи коректно копіюються файли у відповідні підпапки."""
    source_file = tmp_path / "test.txt"
    source_file.write_text("Тестові дані")

    destination_dir = tmp_path / "sorted"
    
    await copy_file(source_file, destination_dir)

    target_file = destination_dir / "txt" / "test.txt"
    
    assert target_file.exists()
    assert target_file.read_text() == "Тестові дані"
