from .size_folders import *
import tqdm
import time


def main():
    try:
        try:
            size__dir = SizeFolder(os.getcwd()).table_info()
            for _ in tqdm.tqdm('[INFO] Loading...'):
              time.sleep(0.1)
            print(size__dir)
        except FileNotFoundError as e:
            print(f'[INFO] {e}')
    except KeyboardInterrupt:
        print('[INFO] End')


if __name__ == "__main__":
    main()
