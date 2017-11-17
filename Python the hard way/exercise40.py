# Modules , CLasses and object


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
        self.index = (self.index - 1 )
        self.jump()

    def sing(self):
        for line in self.lyrics:
            print(line) 

song1 = ["Happy Birthday to you",
         "I dont Wanna get sued",
         "So I`ll stop right there",
         "------"]


song2 = ["They rally around the family",
         "With pocket full of shells",
         "------"]                   

song3 = ["Never mind I will find ",
         "Someone like you",
         "------" ]

song4 = ["I let it fall,my heart,",
         "As it fell,you rose to claim it",
         "------"]

disk = [song1,song2,song3,song4]

myCD = Song(disk)
myCD.sing()

myCD.next()
myCD.sing()

myCD.prev()
myCD.sing()

myCD.prev()
myCD.sing()

myCD.prev()
myCD.sing()

myCD.prev()
myCD.sing()
