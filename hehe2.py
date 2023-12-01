import random
import webbrowser
import os

def spotify_song(song_url):
    try:
        os.system(f"start spotify:track:{song_url}")
    except:
        print("Error")

spotify_url = "https://open.spotify.com/intl-de/track/4PTG3Z6ehGkBFwjybzWkR8?si=93abf2f7b7e6419f"
track_id = spotify_url.split('/')[-1].split('?')[0]

number = random.randint(1, 10)

guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("Du hast mich Gewonnen")
else:
    spotify_song(track_id)
print()

