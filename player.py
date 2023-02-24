from tkinter import *
from tkinter.messagebox import showinfo
import customtkinter as ct
from pygame import mixer
from pytube import YouTube
from moviepy.editor import *
import os


app = ct.CTk()
app.geometry("550x600+500+50")
app.resizable(False, False)
app.title("Baixe musicas direto do YouTube")


# seção onde vai ficar o campo e o botão de download
panelHeader = PanedWindow(app)

lbl_link = ct.CTkLabel(panelHeader, text="Copie e cole a url do video aqui!")
lbl_link.grid(column=0, row=0, padx=10, sticky=W)

campo = ct.CTkEntry(panelHeader, width=330)
campo.grid(column=0, row=1, padx=10, pady=10, sticky=W)

# função download
def download(link):
    
    # faço o download do video
    pasta = "C:/Users/Dell/Desktop/APP MUSICA"
    downloader = YouTube(link).streams.get_highest_resolution()
    downloader.download(pasta)

    # aqui faço a converção de video para mp3
    mp4 = ".mp4"
    mp3 = ".mp3"
    
    video_file = downloader.title+mp4
    audio_file = downloader.title+mp3
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    
    
    # acessar o diretorio para listar as musicas
    os.chdir(pasta)
    arquivos = os.listdir()
    for musica in arquivos:
        if musica == audio_file:
            listbox.insert(END, musica)
    
    
    # mensagem de sucesso
    showinfo("Sucesso", "Download comcluido com sucesso!!")
            

# função para dar play na musica
def play():
    musica = listbox.get(ACTIVE)
    mixer.music.load(musica)
    mixer.music.play()
    lbl_reproduzindo["text"] = f"Reproduzindo: {musica}"

def pause():
    mixer.music.pause()
    


btn_download = ct.CTkButton(panelHeader, text="Download", command=lambda:download(campo.get()))
btn_download.grid(column=1, row=1, padx=5, pady=10, sticky=W)

lbl_lista = ct.CTkLabel(panelHeader, text="Lista de Reprodução")
lbl_lista.grid(column=0, row=2, padx=10, pady=10, sticky=W)

panelHeader.grid(column=0, row=0, padx=10, pady=10, sticky=W, columnspan=3)


# sessão do meio do app
panelSection = PanedWindow(app)

listbox = Listbox(panelSection, width=80, height=20)
listbox.grid(column=0, row=1, padx=10, sticky=W)

panelSection.grid(column=0, row=1, padx=10, pady=10, sticky=W, columnspan=3)


# sessão footer do app
panelFooter = PanedWindow(app)

lbl_reproduzindo = Label(panelFooter, text="")
lbl_reproduzindo.grid(column=0, row=0, pady=5, padx=5, sticky=W, columnspan=2)

btn_play = ct.CTkButton(panelFooter, text="Play", command=play)
btn_play.grid(column=0, row=1, padx=10, sticky=W)

btn_pause = ct.CTkButton(panelFooter, text="Pause", command=pause)
btn_pause.grid(column=1, row=1, padx=10, sticky=W)


panelFooter.grid(column=0, row=2, padx=10, sticky=W, columnspan=2)

mixer.init()
app.mainloop()