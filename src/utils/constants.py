DATE_FORMAT = "%d.%m.%Y"

COMMANDS_INFO = [
    ("hello", "hello", "Greets the user"),
    ("help", "help", "Shows all available commands"),

    ("add", "add [name]", "Add a new contact"),
    ("find", "find [name]", "Find contact by name"),
    ("change", "change [name] [old_phone] [new_phone]", "Change an existing phone"),
    ("phone", "phone [name]", "Show phone(s) of a contact"),
    ("delete-phone", "delete-phone [name]", "Delete contact phone number"),
    ("search-phone", "search-phone [phone]", "Search contacts by phone number"),

    ("all", "all", "Show all contacts"),
    ("delete", "delete [name]", "Delete a contact"),
    ("search", "search [keyword]", "Search contacts by keyword"),

    ("add-email", "add-email [name] [email/new_email]", "Add/change an email"),
    ("add-birthday", "add-birthday [name] [DD.MM.YYYY]", "Add/change a birthday date"),
    ("show-birthday", "show-birthday [name]", "Show birthday for a contact"),
    ("birthdays", "birthdays/birthdays [days]", "Show birthdays in next N days (default 7)"),

    ("add-address", "add-address [name]", "Add an address to a contact"),
    ("delete-address", "delete-address [name]", "Delete a contact address"),
    ("find-city", "find-city [city]", "Find contacts by city"),
    ("search-address", "search-address [query]", "Search in all addresses"),
    ("show-addresses", "show-addresses", "Show all addresses"),

    ("add-note", "add-note", "Add a new note"),
    ("show-notes", "show-notes", "Show all notes"),
    ("find-note", "find-note [title]", "Find notes by title"),
    ("edit-note", "edit-note", "Edit a note"),
    ("delete-note", "delete-note", "Delete a note"),

    ("add-tag", "add-tag [title] [tag]", "Add a tag to a note"),
    ("find-tag", "find-tag [tag]", "Find notes by tag"),

    ("exit", "exit", "Exit the assistant"),
    ("close", "close", "Exit the assistant"),
]
