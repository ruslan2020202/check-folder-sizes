from .size_folders import *


def main():
    try:
        print(SizeFolder(os.getcwd()).table_info())
    except KeyboardInterrupt:
        print('[INFO] End')


if __name__ == "__main__":
    main()
