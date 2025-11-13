from collections import UserDict
from src.models.fields_notes import Content
from src.models.fields_notes import Title, Content 

class Note:
    def __init__(self, title, content=None):
        if not title:
            raise ValueError("Title is required")
        self.title = Title(title)
        self.content = Content(content)

    def edit_content(self, new_content):
        """Edit note content."""
        self.content = Content(new_content)

    def __str__(self) -> str:
        title_str = f"Title: {self.title.value}"
        content_str = f"Content: {self.content}" if self.content else ""
        return "\n".join(filter(None, [title_str, content_str]))


class NotesBook(UserDict):
    def add_note(self, note: Note):
        """Add a new note by title."""
        self.data[note.title.value] = note

    def find_note_by_title(self, title):
        """Find a note by title."""
        search_title = title.lower()
        for key, note in self.data.items():
            if key.lower() == search_title:
                return note
        return None 
    

    def search_notes_by_keyword(self, keyword):
        """Find note by keyword"""
        keyword = keyword.lower()
        found_notes = []
        for note in self.data.values():
            title_match = keyword in note.title.value.lower()
            content_match = False
            if note.content and note.content.value:
                content_match = keyword in note.content.value.lower()
            if title_match or content_match:
                found_notes.append(note) 
        return found_notes

    def delete_note(self, title):
        """Delete a note by title."""
        if title in self.data:
            del self.data[title]
            return f"Note with title: '{title}' successfully deleted."
        return f"Note with title: '{title}' not found."
    
    def change_note(self, title, new_content):
        """Change the note by title."""
        note = self.find_note_by_title(title)
        if note:
            note.content = Content(new_content) if new_content else note.content
            return f"Note with title: '{title}' successfully edited."
        else:
            return f"Note with title: '{title}' not found."

    def __str__(self):
        if not self.data:
            return "No notes available."
        return "\n\n".join(str(note) for note in self.data.values())