from pytube import YouTube
from ytmusicapi import YTMusic
from tkinter import *
from tkinter import messagebox as MessageBox
from moviepy.editor import VideoFileClip,AudioFileClip
import os
#from mutagen.easyid3 import EasyID3

def accion():
    enlace=music.get()
    mp3 = YouTube(enlace)
    # descarga = mp3.streams.filter(only_audio=TRUE).first()
    descarga = mp3.streams.get_highest_resolution()
    song = descarga.download()

    base = os.path.abspath(song)
    mp4_file = base
    mp3_file =base.replace('mp4','mp3')
    print(mp4_file)
    print(mp3_file)

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio

    # os.rename(song, mp3_file)
    open(mp3_file, 'x')

    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()

    os.remove(mp4_file)

    # tag = eyeD3.Tag()
    # tag.link(mp3_file)
    # print (tag.getArtist())
    # print (tag.getAlbum())
    # print (tag.getTitle())


def popup():
    MessageBox.showinfo("Sobre mi", "Enlace a mi perfil de linkedIn: ")

root = Tk()
root.config(bd=15)
root.title("Youtube videos to mp3")

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas info", menu=helpmenu)
helpmenu.add_command(label="informacion del autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa para descargar audios de youtube\n")
instrucciones.grid(row=0, column=1)

music = Entry(root)
music.grid(row=1, column=1)

boton = Button(root, text="Descargar :)", command=accion)
boton.grid(row=2, column=1)

root.mainloop()