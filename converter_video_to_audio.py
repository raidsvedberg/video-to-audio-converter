from pydub import AudioSegment
import os

input_directory = input('enter the input directory: ')
output_directory = input('enter the output directory: ')

def convert_video_to_mp3(input_directory, output_directory):

    if not os.path.exists(output_directory):
                os.makedirs(output_directory)

    for file in os.listdir(input_directory):
        try:
            input_path = os.path.join(input_directory, file)
            video = AudioSegment.from_file(input_path)

            name, _ = os.path.splitext(file)
            output_path = os.path.join(output_directory, f"{name}.mp3")

            video.export(output_path, format="mp3")
            print(f"Converted '{file}' to MP3: '{output_path}'")

        except Exception as error:
            print(f"Error converting '{file}': {error}")

if __name__ == '__main__':
    convert_video_to_mp3(input_directory, output_directory)

