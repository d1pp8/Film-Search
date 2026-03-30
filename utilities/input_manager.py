def check_choice(question: str, valid_choices: list):

    """ FOR MENU Checking the validity of the answer to the question """

    valid_choices = {valid.lower() for valid in valid_choices}
    while True:
        value = input(question).strip().lower()
        if value in valid_choices:
            return value
        print(f"\n⭕ Please enter one of: {', '.join(sorted(valid_choices))}")




def get_valid_input(question: str, validator, gener):

    """ Validator function to check the presence of data """

    while True:
        value = input(question).strip()
        result = validator(value, gener)

        if result:
            return  result

        if result is None:
            print("\n❌ Invalid input")



def validate_year_input(value:str, gener):

    """ Is the year entered by the user valid? """

    if "-" in value:

        # Parsing by "-", to get two values
        parts = value.split("-")
        if len(parts) != 2:
            return None

        start, end = parts
        if not(start.isdigit() and end.isdigit()):
            return None

        # The first year of the range cannot be greater than the second
        start, end = int(start), int(end)
        if start > end:
            return None

        # If the entered range is not entered correctly, then information is displayed about the range in which we have films.
        elif start < gener["min_year"] or end > gener["max_year"]:
            print_range_checker(gener)
            return False


        # If the dates are entered correctly and two different dates are received, we return the values
        return start, end

    # If one date is entered, I return it.
    if value.isdigit():
        value = int(value)
        if value < gener["min_year"] or value > gener["max_year"]:
            print_range_checker(gener)
            return False

        year = int(value)
        return year, year

    # Default return
    return None



def print_range_checker(gener):

        """ Function to display an error if the user entered an incorrect year """

        print(f"\n❌No results for \'{gener['name']}\' in range \'{gener['min_year']}\'-\'{gener['max_year']}\'")
        print(f"➡️We have movies in the \'{gener['name']}\' only from {gener["min_year"]}-{gener["max_year"]} years.")






def get_user_gener(genres):

    """ Get selected gener from user input """

    #Create dictionaries for searching by id and name
    genres_by_id = {genre["category_id"]: genre for genre in genres}
    genres_by_name = {genre_id["name"].lower(): genre_id for genre_id in genres}

    while True:
        value = input(
                    "- Select the genre (\'ID\'/ or \'name\')"
                    "\n- Write \'0\' for Exit"
                    "\n\n🎈Your option: "
                    ).strip().lower()

        # For exit from func
        if value == "0":
            return None

        # Check if the value was a number
        if value.isdigit():
            value = int(value)
            if value in genres_by_id:
                return genres_by_id[value]

            print("\n❌Invalid number")
            continue


        # Check if the value was a word
        if value in genres_by_name:
            return genres_by_name[value]

        print("\n❌Invalid name")