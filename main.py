import os
from prettytable import PrettyTable
from math import pow


class SizeFolder:
    schema_size_files = {
        'B': pow(2, 0),
        'KB': pow(2, 10),
        'MB': pow(2, 20),
        'GB': pow(2, 30)
    }

    def __init__(self, path: str):
        self.path = path

    def get_folders(self) -> list[str]:
        """Get all folders in the current directory"""
        return os.listdir(self.path)

    def get_size(self) -> dict[str, int]:
        """
        Returns a sorted dictionary where the key
        is the folder and the value is the size of its contents in bytes
        """
        size = {i: os.stat(i).st_size for i in self.get_folders()}
        size_folders = {k: v for k, v in sorted(size.items(), key=lambda x: x[1], reverse=True)}
        return size_folders

    def change_size_format(self, size) -> str:
        """
        Converting from bytes to the maximum available
        unit of measurement greater than zero
        """
        if size == 0:
            return "0 B"
        return next(f'{size // j} {i}' for i, j in reversed(self.schema_size_files.items()) if size >= j)

    def table_info(self):
        """Tabular presentation of data"""
        table = PrettyTable()
        table.field_names = ["№", 'Folder/file', 'Size']
        [table.add_row((i + 1, j[0], self.change_size_format(j[1]))) for i, j in enumerate(self.get_size().items())]
        return table


if __name__ == "__main__":
    try:
        try:
            print(SizeFolder(os.getcwd()).table_info())
        except FileNotFoundError as e:
            print(f'[INFO] {e}')
    except KeyboardInterrupt:
        print('[INFO] End')
