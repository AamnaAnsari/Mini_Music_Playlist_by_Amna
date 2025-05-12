import streamlit as st
import os

# ----- Song Class -----
class Song:
    def __init__(self, title, artist, audio_path):
        self.title = title
        self.artist = artist
        self.audio_path = audio_path

    def display_info(self):
        return f"🎶 {self.title} by {self.artist}"

    def get_audio(self):
        return self.audio_path


# ----- Playlist Class -----
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def get_titles(self):
        return [song.title for song in self.songs]

    def get_song_by_title(self, title):
        return next((song for song in self.songs if song.title == title), None)

    def display_playlist(self):
        return [song.display_info() for song in self.songs]


# -----  UI with Streamlit -----
def main():
    st.title("🎧 Mini Music Playlist 🎶 By Amna")

    # playlist
    playlist = Playlist()
    playlist.add_song(Song("Pal Pal Song", "Afusic", "Audios/Afusic - Pal Pal (Official Music Video) Prod. @AliSoomroMusic.mp3"))
    playlist.add_song(Song("Rewrite The Stars", "Annie Marie & James Authur", "Audios/rewrite the stars (speed up  lyrics).mp3"))
    playlist.add_song(Song("Hona tha Pyaar", "Atif Aslam", "Audios/Hona Tha Pyar- Atif Aslam(Lyrics).mp3"))
    playlist.add_song(Song("Haseen", "Tailwinder", "Audios\HASEEN - TALWIINDER, NDS, RIPPY (Official Visualizer).mp3"))

    # Display Playlist
    st.subheader("📜 Playlist")
    for song_info in playlist.display_playlist():
        st.write(song_info)

    # Song Selection
    selected_title = st.selectbox("Choose a song to play", playlist.get_titles())
    selected_song = playlist.get_song_by_title(selected_title)

    if selected_song:
        st.subheader(f"🎧 Now Playing: {selected_song.title} by {selected_song.artist}")
        audio_path = selected_song.get_audio()

        # check krta hai ke agr local file exist krti hai ya nhi ya phr url hai 
        if audio_path.startswith("http") or os.path.exists(audio_path):
            st.audio(audio_path)
        else:
            st.error("Audio file not found!")


if __name__ == "__main__":
    main()
