def binary_choice(query = "Confirm"):

    option = None
    while option != 'y' and option != 'n':
        option = input(f"{query} (Y/N)? ").lower()

    return option == 'y'