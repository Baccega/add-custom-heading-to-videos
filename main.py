import fnmatch
import os

INPUT_FOLDER_NAME = "input"
OUTPUT_FOLDER_NAME = "output"

# The heading will show from 0 to HEADING_TIME seconds
HEADING_TIME = 10

# Get this from runnning `python3 get_filenames_from_input.py`
CUSTOM_HEADINGS_LIST = {}
 

def get_file_names_from_os():
    # Excludes .txt
    videos_list = [
        f for f in os.listdir(INPUT_FOLDER_NAME) if not fnmatch.fnmatch(f, "*.txt")
    ]
    dict = {}
    for video in videos_list:
        dict[video] = video
    return dict


def main():    
    print("Edit videos")

    os.listdir(INPUT_FOLDER_NAME)

    # If there are custom heading
    if CUSTOM_HEADINGS_LIST:
        video_dict = CUSTOM_HEADINGS_LIST
    else:
        video_dict = get_file_names_from_os()

    for video_file_name, heading in video_dict.items():
        input_video = "{}/{}".format(INPUT_FOLDER_NAME, video_file_name)
        font_file = "font.ttf"
        output_video = "{}/Edited-{}.mkv".format(
            OUTPUT_FOLDER_NAME, os.path.splitext(video_file_name)[0]
        )

        ffmpeg_create_heading_command = """ffmpeg -y \
            -i '{}' -vf \
            drawtext='fontfile={}: \
            text={}: \
            fontcolor=white: \
            fontsize=(h/15): \
            box=1: \
            boxcolor=black@0.5: \
            boxborderw=5: \
            x=(w-text_w)/2: \
            y=h-th-10:' \
            -ss 0 \
            -t {} \
            -c:a copy \
            heading.mkv""".format(
            input_video, font_file, heading, HEADING_TIME
        )

        ffmpeg_copy_video_command = """ffmpeg -y \
            -ss {} \
            -i "{}" \
            -c:v copy -c:a copy \
            rest.mkv""".format(
            HEADING_TIME, input_video
        )

        ffmpeg_concat_command = 'ffmpeg -y -i heading.mkv -i rest.mkv -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [vv] [aa]" -map "[vv]" -map "[aa]" "{}"'.format(
            output_video
        )

        os.system(ffmpeg_create_heading_command)
        os.system(ffmpeg_copy_video_command)
        os.system(ffmpeg_concat_command)

    os.remove("heading.mkv")
    os.remove("rest.mkv")


if __name__ == "__main__":
    main()
