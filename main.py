#taking the input as the audio and converting it into the sentence

from fpdf import FPDF
import speech_recognition as s_r
import easygui
import os

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
   
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone

# words=r.recognize_google(audio)
my_string = r.recognize_google(audio)

#save the sentence into the txt file

with open("myfile.txt", "w") as f:
    f.write(my_string)

#convert the txt file into the pdf
 
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size = 15)

f = open("myfile.txt", "r")

for x in f:
 	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

result=pdf.output("mygfg.pdf")
path = easygui.diropenbox() # easygui is used to get a path
name = "mygfg.pdf" # the name of the file
path = os.path.join(path, name)  # this is the full pathname