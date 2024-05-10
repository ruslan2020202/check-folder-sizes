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

    def get_size_folder(self, dir: str) -> int:
        """Gets the size of the contents of a folder"""
        total = 0
        try:
            for i in os.scandir(dir):
                if i.is_file():
                    total += i.stat().st_size
                elif i.is_dir():
                    if not i.is_symlink():
                        total += self.get_size_folder(i.path)
        except NotADirectoryError:
            return os.stat(dir).st_size
        except PermissionError or FileNotFoundError:
            return 0
        return total

    def assembly_dictionary(self) -> dict[str, int]:
        """
        Returns a sorted dictionary where the key
        is the folder and the value is the size of its contents in bytes
        """
        size = {}
        for i in os.scandir(self.path):
            if i.is_file():
                size[i.name] = i.stat().st_size
            elif i.is_dir():
                size[i.name] = self.get_size_folder(i.path)
        size_folders = {k: v for k, v in sorted(size.items(), key=lambda x: x[1], reverse=True)}
        return size_folders

    def change_size_format(self, size: int) -> str:
        """
        Converting from bytes to the maximum available
        unit of measurement greater than zero
        """
        if size == 0:
            return "0 B"
        return next(f'{round((size / j), 2)} {i}' for i, j in reversed(self.schema_size_files.items()) if size >= j)

    def table_info(self):
        """Tabular presentation of data"""
        table = PrettyTable()
        table.field_names = ["№", 'Folder/file', 'Size']
        [table.add_row((i + 1, j[0], self.change_size_format(j[1]))) for i, j in enumerate(self.assembly_dictionary().items())]
        return table
