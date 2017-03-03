class Bookstore(object):
    # store = Bookstore("Rmotr's bookstore")
    def __init__ (self, name):
        self.name =name
        self.books=[] ## start an empty list for books
        
        ## def returns All books is bookstore
    def get_books(self):
        return self.books
        
        ## def adds books to bookstore list in books
    def add_book(self,title):  
        self.books.append(title)  ## yes that looks better
    
    
    ## searches the books in the bookstore by book title, or book author,or both    
    def search_books(self,title=None, author=None):
        a_list=[]
        for book in self.books:
            if title and title.lower() in book.title.lower(): ## but it doesnt matter since we are not 
                a_list.append(book)
            if author and author == book.author:
                a_list.append(book)
        return a_list ## the problem is here 
                
class Author(object):
        ## Constructor for Author
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        

    def get_books(self):
        return self.books
    
    
    
class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        
    
    
