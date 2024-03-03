from moviepy.editor import VideoFileClip
import os
import threading


def convert_file(
    input_file,
    output_file,
    codec="libx264",
    audio_codec="aac",
    audio_sample_rate=44100,
    audio_bitrate="128k",
):
    # Load the video clip
    clip = VideoFileClip(input_file)

    # Change codec and audio settings
    clip.write_videofile(
        output_file,
        codec=codec,
        audio_codec=audio_codec,
        audio_fps=audio_sample_rate,
        audio_bitrate=audio_bitrate,
    )


threades = 0


def convert_files(files):
    global threades
    threads = []
    threades += 1
    for input_file, output_file in files:
        thread = threading.Thread(target=convert_file, args=(input_file, output_file))
        print("Thread" + str(threades) + "running")
        thread.start()
        threads.append(thread)
    print(threads)
    # Wait for all threads to finish
    for thread in threads:
        thread.join()


input_dir = "./input/"

if not os.path.isdir(input_dir):
    raise LookupError(
        "Input folder does not exists,Create an input folder and Move the files you want to convert into it, then retry script"
    )
extensions = [
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".flv",
    ".wmv",
    ".webp",
    ".mpg",
    ".mpeg",
    ".ogv",
    ".3gp",
    ".3g2",
    ".ts",
    ".m4v",
    ".rm",
    ".rmvb",
]
video_files = []

for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    if (
        os.path.isfile(file_path)
        and os.path.splitext(filename)[1].lower() in extensions
    ):
        video_files.append(filename)

if not video_files:
    raise FileNotFoundError(
        f"Input folder is empty or contains unsupported video files\nSupported files : {str(extensions)}"
    )

# Example usage

files_to_convert = [(f"{input_dir}/{x}", f"./output/{x}") for x in video_files]

convert_files(files_to_convert)
