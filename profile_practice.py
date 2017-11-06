class Author():
    def __init__(self,name,publishedTime):
        self.name = name
        self.books = []
        self.publishedTime= publishedTime

    def info(self):
        print("Writer name :" ,self.name.title()) 
      
        print("Published Year :" ,self.publishedTime.title())   

    def booklist(self):
        book = ['b1','b2','b3']
        for b in ['b1','b2','b3']:
            self.books.append(book)
        
            



    # def print(self):
    #     print(self.books)

    def show(self):
        for v,k in self.books:
            print(self.books)
                    


greene = Author('Robert Greene','1998')

greene.booklist()

greene.show()          