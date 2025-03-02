import asyncio
import argparse
import time
from pathlib import Path
from sorter.sorter import sort_files

async def main():
    parser = argparse.ArgumentParser(description="Асинхронний сортувальник файлів за розширенням")
    parser.add_argument("source", type=str, help="Шлях до вихідної папки")
    parser.add_argument("destination", type=str, help="Шлях до цільової папки")
    parser.add_argument("--move", action="store_true", help="Переміщувати файли замість копіювання")

    args = parser.parse_args()
    
    source_folder = Path(args.source)
    destination_folder = Path(args.destination)

    print(f"Сортуємо файли з {source_folder} у {destination_folder}...")
    
    start_time = time.time()
    await sort_files(source_folder, destination_folder, move=args.move)
    end_time = time.time()

    print(f"⏳ Час виконання: {end_time - start_time:.2f} секунд")
    print("Сортування завершено!")

if __name__ == "__main__":
    asyncio.run(main())
