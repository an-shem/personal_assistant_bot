from collections import UserDict
from src.models.fields_notes import Content
from src.models.fields_notes import Title, Content 

class Note:
    def __init__(self, title, content=None, tags=None):
        if not title:
            raise ValueError("Title is required")
        self.title = Title(title)
        self.content = Content(content) if content is not None else Content("")
        self.tags = self._parse_tag(tags)

    def _parse_tag(self, tags_input):
        if not tags_input:
            return set()

        if isinstance(tags_input, str):
            tags_list = tags_input.replace(',', ' ').split()
        elif isinstance(tags_input, (list, set, tuple)):
            tags_list = tags_input
        else:
            return set()

        clean_tags = {
            tag.strip().lstrip('#').lower()
            for tag in tags_list
            if tag.strip() 
        }
        return clean_tags

    def edit_content(self, new_content):
        """Edit note content."""
        self.content = Content(new_content)


    def add_tags(self, tags_string):
        if not hasattr(self, 'tags'): 
            self.tags = set()
        new_tags = self._parse_tag(tags_string) 
        self.tags.update(new_tags)


    def remove_tag(self, tag: str):
        normalized_tag = tag.strip().lstrip('#').lower()
        if normalized_tag in self.tags:
            self.tags.remove(normalized_tag)

   
    def __str__(self) -> str:
        title_str = f"Title: {self.title.value}"
        content_str = f"Content: {self.content}" if self.content else ""
        current_tags = getattr(self, "tags", set())
        tags_str = f"Tags: {', '.join(sorted([f'#{t}' for t in current_tags]))}" if current_tags else ""
        return "\n".join(filter(None, [title_str, content_str, tags_str]))


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

            tags_match = keyword in ' '.join(getattr(note, 'tags', set()))
            
            if title_match or content_match or tags_match:
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

    def search_notes_by_tag(self, tag: str):
        """Return list of notes that contain given tag."""
        normalized_tag = tag.strip().lstrip('#').lower() 
        if not normalized_tag:
            return []
            
        return [note for note in self.data.values() if normalized_tag in getattr(note, "tags", set())]


    def __str__(self):
        if not self.data:
            return "No notes available."
        return "\n\n".join(str(note) for note in self.data.values())