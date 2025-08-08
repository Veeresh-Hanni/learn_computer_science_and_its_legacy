class Camera:
    def take_photo(self):
        print("Photo captured 📷")

class MusicPlayer:
    def play_music(self):
        print("Playing music 🎵")

class Smartphone(Camera, MusicPlayer):
    def browse_internet(self):
        print("Browsing the internet 🌐")

# Test
phone = Smartphone()
phone.take_photo()        # Inherited from Camera
phone.play_music()        # Inherited from MusicPlayer
phone.browse_internet()   # Defined in Smartphone
