package Inheritance;

interface Camera {
    void takePhoto();
}

interface MusicPlayer {
    void playMusic();
}

class Smartphone implements Camera, MusicPlayer {
    public void takePhoto() {
        System.out.println("Photo captured 📷");
    }

    public void playMusic() {
        System.out.println("Playing music 🎵");
    }

    public void browseInternet() {
        System.out.println("Browsing the internet 🌐");
    }
}

public class MultipleInheritance {
    public static void main(String[] args) {
        Smartphone phone = new Smartphone();
        phone.takePhoto();
        phone.playMusic();
        phone.browseInternet();
    }
}
