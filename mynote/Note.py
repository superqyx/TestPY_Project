import datetime


last_id = 0

class Note(object):
    def __init__(self, memo, tag):
        self.memo = memo
        self.tag = tag
        self.create_date = datetime.datetime.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tag

class NoteBook(object):
    def __init__(self):
        self.notes = []

    def __find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        self.__find_note(note_id).memo = memo

    def modify_tags(self, note_id,tags):
        self.__find_note(note_id).tag = tags

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

