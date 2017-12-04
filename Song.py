class Song:
    def __init__(self,album):
        self.album = album
        self.index = 0
        self.jump()

    def jump(self):    
        self.lyrics = self.album[self.index]

    def forward (self):
        self.index = self.index +1
        self.jump()

    def Back(self):
        self.index = self.index - 1
        self.jump()     

    def play(self):
        for lyric in self.lyrics:
            print(lyric)    

song1 = ["Hellllooooo"]        
song2 = ["From the other side"]

album= [song1,song2]

album = Song(album)

album.play()
album.forward()
album.play()
album.Back()
album.play()