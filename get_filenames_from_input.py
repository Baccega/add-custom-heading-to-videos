import os 
import fnmatch

INPUT_FOLDER='input'



def main():
    videos_list =[f for f in os.listdir(INPUT_FOLDER) if not fnmatch.fnmatch(f, '*.txt')]
    dict = {}
    for video in videos_list:
        dict[video] = "VIDEO_TITLE_HERE" 
    print("HEADINGS_LIST = {}".format(dict))

if __name__ == "__main__":
    main()
