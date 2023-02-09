# # "#Convert MP4 to WAV?"
import os
os.system

src = "maroon-5-memories-lyrics.mp4"
dst = "test.wav"

os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(src,"mp4"))

os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(dst,"","wav"))



# #Source: ``https://stackoverflow.com/questions/49669298``

# from os import path
# from pydub import AudioSegment

# # files
# src = "maroon-5-memories-lyrics.mp4"
# dst = "test.wav"

# # convert mp4 to wav
# sound = AudioSegment.from_file(src,format="mp4")
# sound.export(dst, format="wav")







