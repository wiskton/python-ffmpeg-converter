import os

FOLDER_FFMPEG = './'
FOLDER_IN = "{}entrada/".format(FOLDER_FFMPEG)
FOLDER_OUT = "{}saida/".format(FOLDER_FFMPEG)

files = os.listdir(FOLDER_IN)
FORMAT_OUT = raw_input("Qual formato deseja converter? (Ex: avi, mp4, mp3, ogg, etc): ")

for file in files:
    filename, file_extension = os.path.splitext(file)
    file_in = '"{}{}"'.format(FOLDER_IN, file)
    file_out = '"{}{}.{}"'.format(FOLDER_OUT, filename, FORMAT_OUT)
    os.system('{}ffmpeg -i {} {}'.format(FOLDER_FFMPEG, file_in, file_out))