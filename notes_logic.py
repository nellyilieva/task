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
    

