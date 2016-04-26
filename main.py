#programa que suma archivos de audio
#disenado por santiago granados e ismael lopez
#programacion de audio aplicada
#universidad de san buenaventura
from seno import Seno
from reproducir import Play
from Tkinter import *
import tkFileDialog
import pyaudio
import  wave
import struct
from delay import delay
from scipy.io.wavfile import read

ventana = Tk()
ventana.title('DELAY ')
ventana.geometry("610x450")
ventana.configure(bg="white")
#imageL=PhotoImage(file="sumaudioimg.gif")
#lblImagen=Label(ventana,image=imageL).place(x=1,y=160)

audio_file_name = ''
audio_file_name2 = ''
Audio1=[]
global primero, segundo
cuadro= Label(ventana, fg="black", padx=15, pady=10, text="Frecuencia:\n (Fq del tono a generar)")
cuadro.pack(side=TOP)
tono=Entry(ventana, bd=5,insertwidth=1)
tono.pack(side=TOP, padx=15, pady=10)
cuadro1= Label(ventana, fg="black", padx=15, pady=10, text="Cuadros:\n (# de frames )")
cuadro1.pack(side=TOP)
frames=Entry(ventana, bd=5, insertwidth=1)
frames.pack(side=TOP, padx=15, pady=10)
cuadro2= Label(ventana, fg="black", padx=15, pady=10, text="Fase:").place(x=400,y=70)

#tiempo
Dt= Label(ventana, fg="black", padx=15, pady=10, text="(Tiempo)")
Dt.pack(side=TOP)
dt=Entry(ventana, bd=5, insertwidth=1)
dt.pack(side=TOP, padx=15, pady=10)
#n de rep
nr= Label(ventana, fg="black", padx=15, pady=10, text="Numero Repeticiones")
nr.pack(side=TOP)
rep=Entry(ventana, bd=5, insertwidth=1)
rep.pack(side=TOP, padx=15, pady=10)


#tono=Entry(ventana, bd=5, insertwidth=1).place(x=110,y=60)
def porframes():
    h=float(tono.get())
    fram=int(frames.get())
    a=Seno(44100,16,h,fram)

    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()


def pi():
    periodo=1/(float(tono.get()))
    piseg= periodo/2
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)

def pi2():
    periodo=1/(float(tono.get()))
    piseg= periodo/4
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()

def pi4():
    periodo=1/(float(tono.get()))
    piseg= periodo/8
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()
def pi8():
    periodo=1/(float(tono.get()))
    piseg= periodo/16
    piframes= int(piseg*44100)
    h=float(tono.get())
    a=Seno(44100,16,h,piframes)
    tonito= a.generar()
    z=Play(tonito)
    y=z.generar()



def open_masker():
    global audio_file_name


    audio_file_name = tkFileDialog.askopenfilename(filetypes=(("Audio Files", ".wav"),   ("All Files", "*.*")))
    rf = wave.open(audio_file_name, 'rb')
    prof = rf.getsampwidth()
    channels = rf.getnchannels()
    rate = rf.getframerate()
    audioN = pyaudio.PyAudio()
    streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
    datos = rf.readframes(1024)


    while datos != '':

            streamN.write(datos)
            datos = rf.readframes(1024)

    print rate,channels

    Audio1 = read(audio_file_name)[1]
    frame=rf.getnframes()


    print "array",Audio1, "FRAMES!!!!", frame

    return Audio1

def archivo():
    global Audio

    Audio=open_masker()

    print "nuevo",Audio
    return Audio

def repeticiones():
    global Audio
    h=Audio
    tiempo=float(dt.get())
    nr=int(rep.get())

    a=delay(44100,16,h,tiempo,nr)
    a.generar()







#tono=Entry(ventana, bd=5, insertwidth=1).place(x=110,y=60)


b1 = Button(ventana,text="Reproducir",command=porframes ,font=("Agency FB", 14),width=10).place(x=450,y=160)
b2 = Button(ventana,text="Pi",command=pi,font=("Arial Black", 14),width=10).place(x=400,y=100)
b3 = Button(ventana,text="Pi/2",command=pi2,font=("Arial Black", 14),width=10).place(x=500,y=100)
b4 = Button(ventana,text="Pi/4",command=pi4, font=("Arial Black", 14),width=10).place(x=400,y=130)
b5 = Button(ventana,text="Pi/8",command=pi8,font=("Arial Black", 14),width=10).place(x=500,y=130)

b6 = Button(ventana,text="delay",command=repeticiones,font=("Arial Black", 14),width=10).place(x=450,y=340)
b7=  Button(ventana,text="Archivo",command=archivo,font=("Arial Black", 14),width=10).place(x=450,y=310)
#b6 = Button(ventana,text="SUMA ESTEREO",font=("Agency FB", 14),width=20).place(x=210,y=80)





ventana.mainloop()