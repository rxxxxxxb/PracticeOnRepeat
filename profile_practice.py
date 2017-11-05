class Author():
    def __init__(self,name,book,publishedTime):
        self.name = name
        self.book = book
        self.publishedTime= publishedTime

    def info(self):
        print("Writer name :" ,self.name.title()) 
        print("Book name :" ,self.book.title())  
        print("Published Year :" ,self.publishedTime.title())   


greene = Author('Robert Greene','laws of power','1998')

greene.info()          