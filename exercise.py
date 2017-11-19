class Song:
    def __init__(self,album):
        self.album = album
        self.index = 0
        self.jump()

    def jump(self):
        self.lyrics = self.album[self.index]    

    def forward(self):
        self.index = self.index + 1
        self.jump()

    def play(self):
        for l in self.lyrics:
            print(l)

song1 =["ajklshfoaf"]            
song2 = ["dglknhgn"]

album = [song1,song2]

album = Song(album)

album.play()
album.forward()
album.play()
