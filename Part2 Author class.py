# Class called Author
# The Author has a name and a list of books published
# The author cannot publish two books of the same name

class Author:
    def __init__(self,name):
        self.name = name # initializes Authors name
        self.books = []

    def publish(self, title):
        if self.unique(title):
            self.books.append(title)
    
    def unique(self, title): 
        uniqueItems = set(self.books) # gets rid of duplicates
        if title not in uniqueItems: # checks to see if the book is already in the list
            return True
        else: # produces errors if the book being entered is already in the list
            print(f'\n**ERROR**\nThis book "{title}" has the same name as a book currently in the book list')            
                
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

    shrek = Author('Shrek')
    shrek.publish('Good to be an ogre')
    shrek.publish('Shrek\'s greatest hits')
    shrek.publish('How to be the best ogre')
    shrek.publish('Me and donkey')
    shrek.publish('Shrek\'s greatest hits')
    shrek.publish('Me and Fiona')
    shrek.publish('How to be the best ogre')
    shrek.publish('Good to be an ogre')
    
    print(f'\n{shrek}')

if __name__=="__main__": 
    main() 