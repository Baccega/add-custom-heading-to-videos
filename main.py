import fnmatch
import ffmpeg
import os

INPUT_FOLDER_NAME='input'
OUTPUT_FOLDER_NAME= 'output'

# The heading will show from 0 to HEADING_TIME seconds
HEADING_TIME=10

# Get this from runnning `python3 get_filenames_from_input.py`
CUSTOM_HEADINGS_LIST = {}
 

def get_file_names_from_os():
    # Excludes .txt
    videos_list =[f for f in os.listdir(INPUT_FOLDER_NAME) if not fnmatch.fnmatch(f, '*.txt')]
    dict = {}
    for video in videos_list:
        dict[video] = video
    return dict

def main():    
    print("Edit videos")

    os.listdir(INPUT_FOLDER_NAME)

    # If there are custom heading
    if(CUSTOM_HEADINGS_LIST):
        video_dict = CUSTOM_HEADINGS_LIST
    else:
        video_dict = get_file_names_from_os()

    for video_file_name, heading in video_dict.items():
        input_stream = ffmpeg.input("{}/{}".format(INPUT_FOLDER_NAME, video_file_name))
        video = input_stream.video
        audio = input_stream.audio
        video.filter(
            "drawtext",
            fontfile="font.ttf",
            text=heading,
            fontcolor="white",
            fontsize=26,
            box=1,
            boxcolor="black@0.5",
            boxborderw=5,
            x=10,
            y="h-th-10",
            enable="lte(t,{})".format(HEADING_TIME),
        ).output(audio, '{}/Edited-{}}'.format(OUTPUT_FOLDER_NAME, video_file_name)).run()


if __name__ == "__main__":
    main()
