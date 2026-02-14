from utils.files.move_file_with_partition import move_file_adding_timestmap, MoveFileError

from argparse import ArgumentParser

def run():

    try:
        move_file_adding_timestmap()
    except MoveFileError as e:
        print(e)
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("Folder to watch", default=".")

    parser.parse_args()

    
