from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()
root.geometry("500x430")
root.wm_iconbitmap("C:/tkinterAudio/images/musicIcon.ico")
root.title("MP3 PLayer")

pygame.mixer.init()

def play_time():
    if stopped:
        return

    current_time = pygame.mixer.music.get_pos() / 1000

    #slider_label.config(text=f'Slider: {int(slider.get())} and Song Position:{current_time}')
    time_format = time.strftime('%M:%S',time.gmtime(current_time))
    #get song length with mutagen
    #current_song = music_list.curselection()
    song = music_list.get(ACTIVE)

    song = f'C:/tkinterAudio/musics/{song}.mp3'

    look_up_song = MP3(song)

    global song_length
    song_length = look_up_song.info.length
    actual_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    current_time += 1

    if int(slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {actual_song_length} ')
    elif paused:
        pass

    elif int(slider.get()) == int(current_time):
        #slider has not moved
        slider_position = int(song_length)

        slider.config(to=slider_position, value=int(current_time))
    else:
        #sldier has moved
        slider_position = int(song_length)

        slider.config(to=slider_position, value=int(slider.get()))

        time_format = time.strftime('%M:%S', time.gmtime(int(slider.get())))

        status_bar.config(text=f'Time Elapsed: {time_format} of {actual_song_length} ')

        next_time = int(slider.get()) + 1
        slider.config(value=next_time)

    # status_bar.config(text=f'Time Elapsed: {time_format} of {actual_song_length} ')
    #update slider position value to current song position
    #slider.config( value=int(current_time))



    #upadte time
    status_bar.after(1000, play_time)

def add_song():
    song = filedialog.askopenfilename(initialdir="C:/tkinterAudio/musics/",
                title="Choose A Song", filetypes=(("mp3 files","*.mp3"),))

    #strip out the directory info & .mp3 extension
    song = song.replace("C:/tkinterAudio/musics/", "")
    song = song.replace(".mp3", "")

    #add song to music_list
    music_list.insert(END, song)

def add_multiple_songs():
    songs = filedialog.askopenfilenames(initialdir="C:/tkinterAudio/musics/",
                title="Choose A Song", filetypes=(("mp3 files", "*.mp3"),))
    #loop through the song list and replace directory info and mp3
    for song in songs:
        song = song.replace("C:/tkinterAudio/musics/", "")
        song = song.replace(".mp3", "")

        music_list.insert(END, song)

def play():

    #set stop variable to false so song can play
    global stopped
    stopped = False
    song = music_list.get(ACTIVE)
    song = f'C:/tkinterAudio/musics/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #call the play_time function to get song length
    play_time()

    #Update slider to position
    # slider_position = int(song_length)
    # slider.config(to=slider_position, value=0)
    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

global stopped
stopped = False
def stop():
    #resetting slider and status bar
    status_bar.config(text='')
    slider.config(value=0)

    pygame.mixer.music.stop()
    music_list.select_clear(ACTIVE)

    #clear the status bar
    status_bar.config(text='')

    #set stop variable to true
    global stopped
    stopped = True

def next():
    # resetting slider and status bar
    status_bar.config(text='')
    slider.config(value=0)

    next_song = music_list.curselection()
    next_song = next_song[0]+1
    song = music_list.get(next_song)

    song = f'C:/tkinterAudio/musics/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #update bar selection
    music_list.select_clear(0, END)
    #activate new song bar
    music_list.activate(next_song)

    #draw active bar
    music_list.selection_set(next_song,last=None)

def back():
    # resetting slider and status bar
    status_bar.config(text='')
    slider.config(value=0)

    next_song = music_list.curselection()
    next_song = next_song[0] - 1
    song = music_list.get(next_song)

    song = f'C:/tkinterAudio/musics/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # update bar selection
    music_list.select_clear(0, END)
    # activate new song bar
    music_list.activate(next_song)

    # draw active bar
    music_list.selection_set(next_song, last=None)

#global pause variable
global paused
paused = False

def pause(is_paused):
    global paused
    pause = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def delete_one_song():
    stop()
    music_list.delete(ANCHOR)
    pygame.mixer.music.stop()
def delete_all_songs():
    stop()
    music_list.delete(0,END)
    pygame.mixer.music.stop()

def slide(x):
    #slider_label.config(text=f'{int(slider.get())} of {int(song_length)}')
    song = music_list.get(ACTIVE)
    song = f'C:/tkinterAudio/musics/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))

def volume_slide(x):
    pygame.mixer.music.set_volume(volume_slider.get())

    #current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)


master_frame = Frame(root)
master_frame.pack(pady=20)


music_list = Listbox(master_frame, bg="black", fg="yellow", width=60)
music_list.grid(row=0, column=0)

back_button_icon = PhotoImage(file="C:/tkinterAudio/images/back50.png")
play_button_icon = PhotoImage(file="C:/tkinterAudio/images/play50.png")
pause_button_icon = PhotoImage(file="C:/tkinterAudio/images/pause50.png")
stop_button_icon = PhotoImage(file="C:/tkinterAudio/images/stop50.png")
next_button_icon = PhotoImage(file="C:/tkinterAudio/images/forward50.png")

controlFrame = Frame(master_frame)
controlFrame.grid(row=1,column=0, pady=20)

volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

back_button = Button(controlFrame, image=back_button_icon, borderwidth=0, command=back)
play_button = Button(controlFrame, image=play_button_icon, borderwidth=0, command=play)
pause_button = Button(controlFrame, image=pause_button_icon, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controlFrame, image=stop_button_icon, borderwidth=0, command=stop)
next_button = Button(controlFrame, image=next_button_icon, borderwidth=0, command=next)

back_button.pack(side=LEFT,padx=13.5,pady=14)
play_button.pack(side=LEFT,padx=13.5,pady=14)
pause_button.pack(side=LEFT,padx=13.5,pady=14)
stop_button.pack(side=LEFT,padx=13.5,pady=14)
next_button.pack(side=LEFT,padx=13.5,pady=14)

#creating menu
main_menu = Menu(root)
root.config(menu=main_menu)

add_song_menu = Menu(main_menu)
main_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)
#add more than one song to the playlist
add_song_menu.add_command(label="Add more than one song to Playlist", command=add_multiple_songs)

remove_song_menu = Menu(main_menu)
main_menu.add_cascade(label="Remove Songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From The Playlist", command=delete_one_song)
remove_song_menu.add_command(label="Delete All Songs From The Playlist", command=delete_all_songs)


status_bar = Label(root, text='', bd=1, relief=GROOVE)
status_bar.pack(fill=X,side=BOTTOM, ipady=2)

#crate slider
slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
slider.grid(row=2, column=0, pady=10)

volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume_slide, length=125)
volume_slider.pack(pady=10)

#temporary silder label
# slider_label= Label(root, text='0')
# slider_label.pack(pady=10)



root.mainloop()