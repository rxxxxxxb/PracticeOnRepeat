class Song:
    def __init__(self,album):
        self.album = album
        self.index = 0
        self.start()

    def start(self):
        self.lyrics = self.album[self.index]     

    def next(self):
        self.index = self.index + 1     
        self.start()

    def play(self):
        for lyric in self.lyrics:
            print(lyric)

song1 = ["akhakhfa"]

song2 = ["jkdbkqelwnle"]

album = [song1,song2]

disk = Song(album)

disk.play()
disk.next()
disk.play()
