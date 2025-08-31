import time
from threading import Thread
import sys

lyrics = [
    ("Ondeh, Uda, janlah baitu bana", 0.05),
    ("Denai ko indaklah nan sarupo itu", 0.05),
    ("Dek hanyo takuik mancaliak Uda", 0.05),
    ("Acok mabuak-mabuakan", 0.06),
    ("Dulu denai lah suko mancaliak Uda bakawan", 0.11),
    ("Raso-raso ko ado, tapi denai diamkan", 0.12),
    ("Ah, wadaw-wadaw, ini anak gaga lai", 0.06),
    ("Su bale Jawa, tambah bening aja lai", 0.06),
    ("Gaya semakin beda", 0.05),
    ("Bibir merah merah", 0.06),
    ("Aduh Mama", 0.05),
    ("Mama, ini siapa punya anak?", 0.06)

   
]
delays = [0, 2.0, 4.5, 7.0, 9.0, 14.0, 19.5, 22.0, 25.0, 26.3, 27.5, 28.4]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
