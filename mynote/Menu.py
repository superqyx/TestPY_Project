import sys
from Note import NoteBook, Note

class Menu(object):
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print('''
        Notebook Menu
        1. Show all notes
        2. Search notes
        3. Add note
        4. Modify note
        5. Quit
        ''')

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Wrong option")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tag, note.memo))

    def search_notes(self):
        filter = input("Input the filter:")
        notes= self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Input the memo:")
        self.notebook.new_note(memo)
        print("Memo has been added.")

    def modify_note(self):
        id = input("Input the note id:")
        memo  = input("Input the memo:")
        tags = input("Input the tags:")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print("Exit...")
        sys.exit(0)

if __name__ == '__main__':
    menu = Menu()
    menu.run()