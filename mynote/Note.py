import datetime


last_id = 0

class Note(object):
    def __init__(self, memo, tag):
        self.memo = memo
        self.tag = tag
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tag

class NoteBook(object):
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id,tags):
        for note in self.notes:
            if note.id == note_id:
                note.tag = tags
                break

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

