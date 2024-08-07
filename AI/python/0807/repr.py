class Book:
    def __init__(self,title,isbn):
        self.__title = title
        self.__isbn = isbn

    def __repr__(self):
        return 'ISBN : ' + self.__isbn + ', Name : '+self.__title

book = Book('The Python Tutorial','44245367') 
book2 = Book('The Machine Language','789465436')
print(book)
print(book2)