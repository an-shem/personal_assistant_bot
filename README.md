# Personal Assistant Bot JakBot (Python / Neoversity)
![JakBot](JakBot.png)

Console application-assistant for working with contacts and notes.  
The project as implemented within the course **Python Programming (Neoversity / GoIT)**.

---

## 📌 Main features

### 📇 Contacts

- Adding a contact with:
  - a name;
  - one or more phone numbers;
  - an e-mail address;
  - a date of birth;
  - one or more postal addresses.
- Searching for contacts:
  - by name;
  - by phone number;
  - by any field (name, phone, e-mail, DOB, address).
- Editing and deleting contacts.
- Adding/deleting addresses.
- Searching for contacts by city.
- Displaying all contacts in a table format.
- Showing upcoming birthdays (e.g., for the next 7 days).

### 📝 Notes

- Adding, viewing, editing and deleting notes.
- Search notes by title.
- Adding tags to a note.
- Search notes by tag.
- Sorting results by number of tags.

### 💾 Data storage

- Contacts and notes **stored between launches**.
- The module is used `pickle`.

---

## 🔧 Requirements

- Python **3.10+**
- Supported OS: Windows /Linux /macOS

---

## 📥 Installation

### 1. Repository cloning

```bash
git clone https://github.com/an-shem/ppersonal_assistant_bot.git
cd personal_assistant_bot
```


### 2. Creation and activation of a virtual environment (recommended)
`python -m venv venv`

## Linux / macOS:
`source .venv/bin/activate`

## Windows:
`.venv\Scripts\activate`

### 3. Setting dependencies
`pip install -r requirements.txt`

### 4. ▶️ Launching the application
`python main.py`

## 🧭 Basic commands
### 🔹 Systemic

| Command          | Description                             |
| ---------------- | --------------------------------------- |
| `hello`          | Greeting.                               |
| `help`           | Shows the list of available commands.   |
| `exit` / `close` | Save data and terminate the application. |

### 🔹 Working with contacts
| Command         | Description                                     |
| --------------- | ----------------------------------------------- |
| `add`           | Add a new contact.                              |
| `change`        | Change the phone number.                        |
| `phone`         | Show the contact's phone numbers.               |
| `search-phone`  | Search by phone number.                         |
| `all`           | Show all contacts in a table format.            |
| `delete`        | Delete a contact.                               |
| `search`        | Search for a contact by any field.              |
| `add-email`     | Add an e-mail.                                  |
| `add-birthday`  | Add a date of birth.                            |
| `show-birthday` | Show the date of birth.                         |
| `birthdays`     | Contacts with birthdays in the next N days.     |

### 🔹 Working with addresses
| Command          | Description                          |
| ---------------- | ------------------------------------ |
| `add-address`    | Add an address.                      |
| `delete-address` | Delete an address.                   |
| `find-city`      | Find contacts by city.               |
| `search-address` | Search for an address by keyword.    |
| `show-addresses` | Show all addresses.                  |

### 🔹 Working with notes
| Command       | Description                      |
| ------------- | -------------------------------- |
| `add-note`    | Add a note.                      |
| `show-notes`  | Show all notes.                  |
| `find-note`   | Find a note by title.            |
| `edit-note`   | Edit a note.                     |
| `delete-note` | Delete a note.                   |
| `add-tag`     | Add tag(s) to a note.            |
| `find-tag`    | Find notes by tag.               |


## 🧾 Examples of using
### ➕ Add a contact
`add John 0501234567`
Next, the JekBot will offer to add e-mail, DN, address.

### 🔍 Search
```
search John
search 0501
search Berlin
search john@example.com
```
### 📝 Notes
```
add-note
add-tag "Shopping list" #food #home
find-tag food
```


## 💽 Where the data is stored
Storage files are located in the directory:
`src/storage/`

## Files:
- `addressbook.pkl` — saved contacts
- `notes.pkl` — saved notes


## 🗂 Project structure

```text
.
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
└── src
    ├── models
    │   ├── fields_notes.py
    │   ├── name.py
    │   ├── notes_book.py
    │   ├── phone.py
    │   └── record.py
    ├── storage
    │   └── storage.py
    └── utils
        ├── __init__.py
        ├── cli_input.py
        ├── colorizer.py
        ├── constants.py
        ├── error_handler.py
        ├── handler_commands.py
        ├── parse_input.py
        ├── tabulate_helpers.py
        └── validation.py
```


### 💼 Contacts

[![GitHub](https://camo.githubusercontent.com/4fcd516e2fde608afc9ddd1330de295d23981c27a9b9d695f8abe51f70a1efc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/an-shem) Andrii Shemet __Team Lead/Developer__  

[![GitHub](https://camo.githubusercontent.com/4fcd516e2fde608afc9ddd1330de295d23981c27a9b9d695f8abe51f70a1efc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/Gilona-itsme) Ilona Hil __Scrum Master/Developer__  

[![GitHub](https://camo.githubusercontent.com/4fcd516e2fde608afc9ddd1330de295d23981c27a9b9d695f8abe51f70a1efc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/User-Student1) Illia Serhunin __Developer__  

[![GitHub](https://camo.githubusercontent.com/4fcd516e2fde608afc9ddd1330de295d23981c27a9b9d695f8abe51f70a1efc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/Nikita-Sivtsov) Nikita Sivtsov __Developer__  

