from utils import database
from utils.database import add_drama

MENU_PROMPT = "\nEnter 'a' to add a drama, 'l' to see your dramas, 'r' to mark a drama as finished, 'd' to delete a drama" \
              ", or 'q' to quit: "

# user_choice = {
#    "a": add_drama(),
# }
"""
Enter:
- 'a' to add a new drama
- 'l' to list all dramas

- 'r' to mark a drama as finished
- 'd' to delete a drama
- 'q' to quit

Your choice: 
"""


def menu():
    database.create_drama_table()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            prompt_add_drama()
        elif selection == 'l':
            list_dramas()
        elif selection == 'r':
            prompt_watch_drama()
        elif selection == 'd':
            prompt_delete_drama()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


def prompt_add_drama():
    name = input('Enter the name of the drama: ')
    episodes = input('Enter the number of episodes: ')

    database.add_drama(name, episodes)


def list_dramas():
    dramas = database.get_all_dramas()
    for drama in dramas:
        watched = 'YES' if drama['watched'] else 'NO'
        print(f"{drama['name']} has {drama['episodes']} episodes, watched: {watched}")


def prompt_watch_drama():
    name = input('Enter the name of the drama you finished: ')
    database.mark_drama_as_read(name)
    print(f"{name} has been marked as watched")


def prompt_delete_drama():
    name = input('Enter the name of the drama you want to remove: ')
    database.delete_drama(name)


menu()
