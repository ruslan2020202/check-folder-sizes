from .size_folders import *


def main():
    try:
        try:
            print(SizeFolder(os.getcwd()).table_info())
        except FileNotFoundError as e:
            print(f'[INFO] {e}')
    except KeyboardInterrupt:
        print('[INFO] End')


if __name__ == "__main__":
    main()
