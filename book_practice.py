class Author:
    def __init__(self,book):
       # self.name = name
        self.books = book
       # self.publishedTime= publishedTime
        

    def info(self):
        print("Writer name :" ,self.name.title()) 
      
        print("Published Year :" ,self.publishedTime.title())   

    # def booklist(self):
    #     book = ['b1','b2','b3']
    #     for b in ['b1','b2','b3']:
    #         self.books.append(book)

    # def addBook(self,book):
    #     self.books.append(book)    
            



    # def print(self):
    #     print(self.books)

    def show(self):
        
        for book in self.books:
            print("Book name : " ,book)


bookG = ['Mastery','Laws of power','art of Seduction']

greene = Author(bookG)
greene.name = 'Robert Greene'
greene.publishedTime ='1998' 

greene.info()
greene.show()
# for b in book:
#     greene.addBook(b)
print("\n")
bookM = ['Outliers','Blink','Tipping point']

malcolm = Author(bookM)
malcolm.name = "Malcolm Gladwell"
malcolm.publishedTime = '2010'
malcolm.info()
malcolm.show()
   
