
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def IMDB(movie):
    if movie.get('imdb') >= 5.5:
        return True
    else:
        return False
    
    
def sublist(movies_list):
    new_list = []
    for movie in movies_list:
        if IMDB(movie):
            new_list.append(movies)
    return new_list


def category(category, movies_list):
    category_list = []
    for movie in movies_list:
        if movie.get ('category') == category:
            category_list.append(movie)
    return category_list


def averageIMDB (movies_list):
    sumOfIMDBs = 0
    count = 0
    for movie in movies_list:
        sumOfIMDBs += movie.get('imdb')
        count += 1
    return sumOfIMDBs/count

def averageIMDB_cat (category, movies_list):
    category_list = []
    for movie in movies_list:
        if movie.get('category') == category:
            category_list.append(movie)
    sumOfmovies = 0
    count = 0
    for movie in category_list:
        sumOfmovies += movie.get('imdb')
        count += 1
    return sumOfmovies/count


print(IMDB(movies[0]))
print(sublist(movies))
print(category('Detective', movies))
print(averageIMDB(movies))
print(averageIMDB_cat('Drama', movies))