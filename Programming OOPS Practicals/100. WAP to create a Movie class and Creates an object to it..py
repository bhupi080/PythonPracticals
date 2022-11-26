class Movie:
    def __init__(self,name,genre,budget):
        self.name = name
        self.genre = genre
        self.budget = budget
    def display(self):
        print("Movie = ",self.name)
        print("Genre = ",self.genre)
        print("Budget = ",self.budget)

ob = Movie("Dhamal","Comedy","10 Cr")
ob.display()

