# Class called Author
# The Author has a name and a list of books published


class Author:
    def __init__(self,name):
        self.name = name # initializes Authors name
        self.books = []

    def publish(self, title):
        self.books.append(title) # Appends the books
      
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books' # if true set a else set b
        return f'Name: {self.name} \nBooks Published: {titles}'


def main():
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(f'\n{shakespeare}')

    chris = Author('Bruce Wayne')
    print(f'\n{chris}')

if __name__=="__main__": 
    main() 