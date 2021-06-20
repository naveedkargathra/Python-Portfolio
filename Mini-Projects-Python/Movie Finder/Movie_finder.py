MENU_PROMPT = "\n Enter 'a' to Add Movie, 'l' to List All Movies, 'f' to FInd Movie, 'q' to Quit."

movies = []

def add_movie():
    title = input("Enter title of the movie:")
    director = input("Enter the name of the Director:")
    year = input("Enter the Year of release:")

    movies.append({
        "title" : title,
        "director" : director,
        "year": year
    })

def list_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def find_movie():
    Title = input("Enter the Title")


    for movie in movies:
        if Title == movie["title"]:
            print_movie(movie)


user_input = { 'a': add_movie, 'l': list_movie, 'f' : find_movie}

def menu():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection in user_input:
            selected_function = user_input[selection]
            selected_function()
        else:
            print("Unknown Command, Please enter command again")
            
        selection = input(MENU_PROMPT)

menu()
