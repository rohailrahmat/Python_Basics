class MyFirstClass:
    print("Who wrote this!!")
    index = "author-book"

    def hand_list(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book
        print(philosopher + " wrote this book " + book)

obj = MyFirstClass()

obj.hand_list("Sun Tzu", "Art of War")
