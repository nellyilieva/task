from dataclasses import dataclass
import notes_manager

@dataclass
class Note:
    id: int
    title: str
    content: str

    def to_dict(self):
        return {"id": self.id, "title": self.title, "content": self.content,}
    
    def from_dict(data):
        return Note(id=data["id"], title=data["title"], content=data["content"],)
    

def add_note(title, content):
    data = load_notes()

    note = Note(
        id=data["next_id"],
        title=title,
        content=content,
    )

    data["next_id"] += 1
    data["notes"].append(note.to_dict())

    save_notes(data)
    return note

def list_notes():
    data = load_notes()
    return [Note.from_dict(n) for n in data["notes"]]

def get_note(note_id):
    data = load_notes()

    for n in data["notes"]:
        if n["id"] == note_id:
            return Note.from_dict(n)

    raise KeyError(f"Note with id {note_id} not found")

def delete_note(note_id):
    data = load_notes()

    original_len = len(data["notes"])
    data["notes"] = [n for n in data["notes"] if n["id"] != note_id]

    if len(data["notes"]) == original_len:
        raise KeyError(f"Note with id {note_id} not found")

    save_notes(data)
