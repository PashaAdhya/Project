import time
from threading import Thread
import sys

lyrics = [
    ("Perempuankuuuuu", 0.1),
    ("Engkau Cintakuuu", 0.11),
    ("Tak Mungkin Bisaaa Bilaaa Akuuu", 0.11),
    ("Jauh Darimuu", 0.123),
    ("Bisaa Bilaa", 0.1),
    ("Ku Pastii Sedihh", 0.1),
    ("Ku Cintaaa Engkauuu", 0.1),
    ("Cintaaa Padaa", 0.09),
    ("Perempuankuuuu", 0.15)
]
delays = [0, 3.0, 7.0, 12.0, 15.0, 18.0, 22.0, 24.0, 26.0]

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
