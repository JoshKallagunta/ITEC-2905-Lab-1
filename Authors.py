
class Author:
    def _init_(self, name):
        self.name = name
        self.books = []
    
    def publish(self, book_title):
        self.books.append(book_title)

   # def __str__(self, publish)
        
        

def main():

    josh = Author('Josh Kallagunta')
    josh.publish('Book 1')
    josh.publish('Book 2')

    print(josh) 

    jake = Author('Jake')
    print(jake)

main()


