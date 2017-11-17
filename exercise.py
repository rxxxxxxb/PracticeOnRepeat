class Song: 
    def __init__(self,disk):
        self.index = 0
        self.disk = disk
        self.jump()

    def jump(self):
        self.lyrics = self.disk[self.index] 

    def next(self):
        self.index = (self.index + 1)
        self.jump()

    def prev(self):
        self.index = self.index - 1        
        self.jump()

    def sing(self):
        for line in self.lyrics:
            print(line)    

song1 = ["hisahfuifw"]
song2 = ["adasdhisahfuifw"]
song3 = ["hisasdadadahfuifw"]

disk = [song1,song2,song3]

cd = Song(disk)

cd.sing()
cd.next()
#cd.next()
cd.sing()

cd.prev()
cd.sing()