animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
new = list(animal_movies)
new.append('Dumbo')
new.append('Zootopia')

animal_movies = tuple(new)

print("Updated animal movies:", animal_movies)