import os
import unittest

from converter_video_to_audio import convert_video_to_mp3


class TestConverter(unittest.TestCase):
    def test_01_convert_video_to_audio_positive(self):
        input_directory = r"D:\python\converterVideoToAudio\test_video"
        output_directory = r"D:\python\converterVideoToAudio\test_audio"
        file_input = os.listdir(r"D:\python\converterVideoToAudio\test_video")
        convert_video_to_mp3(input_directory, output_directory)
        file_output = os.listdir(r"D:\python\converterVideoToAudio\test_audio")
        files = []
        for file in file_input:
            file = os.path.splitext(file)[0]+'.mp3'
            files.append(file)
        self.assertEqual(files, file_output)

    def test_02_convert_video_to_audio_no_output_folder(self):
        input_directory = r"D:\python\converterVideoToAudio\test_video"
        output_directory = r"D:\python\converterVideoToAudio\test_something" # the directory is not exist
        file_input = os.listdir(r"D:\python\converterVideoToAudio\test_video")
        convert_video_to_mp3(input_directory, output_directory)
        file_output = os.listdir(r"D:\python\converterVideoToAudio\test_something")
        files = []
        for file in file_input:
            file = os.path.splitext(file)[0] + '.mp3'
            files.append(file)
        self.assertEqual(files, file_output)

    def test_03_convert_video_to_audio_negative(self):
        input_directory = r"D:\python\converterVideoToAudio\test_video"
        output_directory = r"D:\python\converterVideoToAudio\test_audio"
        file_input = os.listdir(r"D:\python\converterVideoToAudio\test_video")
        new_file_pdf = open(r"D:\python\converterVideoToAudio\test_video\new_file.pdf", "w")
        new_file_pdf.close()
        convert_video_to_mp3(input_directory, output_directory)
        file_output = os.listdir(r"D:\python\converterVideoToAudio\test_audio")
        files = []
        for file in file_input:
            file = os.path.splitext(file)[0] + '.mp3'
            files.append(file)
        self.assertEqual(files, file_output)


if __name__ == '__main__':
    unittest.main()