"""
A Basic Weight Converter Application.

The project requires knowledge of functional programming hence, the solution is
provided in functional approach. The same problem can also be solved using
object-oriented approach.

As the project is intended to the programmers of basic understanding, the
solution is  optimum and you might see lot of repetition and simple
logics throughout the code

The solution requires python version 3.8 or higher

"""

# Multipliers to convert kg to different values


POUNDS = 2.20462262
OUNCES = 35.2739619


def kg_to_lbs(kg):
    return kg * POUNDS


def lbs_to_kg(lbs):
    return lbs / POUNDS


def kg_to_oz(kg):
    return kg * OUNCES


def oz_to_kg(oz):
    return oz / OUNCES


def display_line(char="-"):
    print(char * 60)


options = {
    "1": {"title": "KG to Pound", "function": kg_to_lbs},
    "2": {"title": "Pound to KG", "function": lbs_to_kg},
    "3": {"title": "KG to Ounce", "function": kg_to_oz},
    "4": {"title": "Ounce to KG", "function": oz_to_kg},
}


def run():
    while True:
        print("Weight Converter")
        display_line()
        for key, value in options.items():
            print(f'{key}. {value["title"]}')

        print("\n0. Exit")
        display_line()

        select = input("Choose an option: ")
        display_line()
        if select == "0":
            print("Exiting now !!")
            exit(0)

        option = options.get(select)
        if option is None:
            print(f"Invalid option selected: '{option}'")
            continue

        while True:
            print(option["title"])
            display_line()
            try:
                value = float(input(f"Enter value in {option['title'].split()[0]}: "))
            except Exception:
                print("Invalid number supplied")
                continue
            print(f"{value} {option['title']} is {option['function'](value)}")
            display_line()
            if input("Do you want to Calculate again?? [y/n]: ").lower() == "n":
                break


if __name__ == "__main__":
    """
    If the application is directly opened from the commandline, the application
    should automatically run, otherwise, it will import the functions to the
    other module
    """
    run()
