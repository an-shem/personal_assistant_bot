from tabulate import tabulate
from src.utils.colorizer import Colorizer
from src.utils.constants import COMMANDS_INFO
from src.utils.constants import DATE_FORMAT

def show_commands():
    table = []
    
    for cmd, description in COMMANDS_INFO.items():
        colored_cmd = Colorizer.highlight(cmd)
        colored_desc = Colorizer.info(description)
        table.append([colored_cmd, colored_desc])
    
    print(Colorizer.success("\nAvailable commands:\n"))
    print(
        tabulate(
            table,
            headers=[Colorizer.commandline("Command"), Colorizer.commandline("Description")],
            tablefmt="grid",

        )
)
    

def show_contacts_table(contacts):
    """Pretty prints contact list in a table format."""
    
    table = []
    for contact in contacts:
        table.append([
            Colorizer.highlight(contact.name.value),
            Colorizer.info(", ".join([p.value for p in contact.phones]) if contact.phones else ""),
            Colorizer.info(contact.email.value if hasattr(contact, "email") and contact.email else ""),
            Colorizer.info(contact.address.value if hasattr(contact, "address") and contact.address else ""),
            Colorizer.info(contact.birthday.value.strftime(DATE_FORMAT) if hasattr(contact, "birthday") and contact.birthday else ""),
        ])

    print(Colorizer.highlight("CONTACT LIST:"))
    print(tabulate(
        table,
        headers=[Colorizer.commandline("Name"), Colorizer.commandline("Phones"), Colorizer.commandline("Email"), Colorizer.commandline("Address"), Colorizer.commandline("Birthday")],
        tablefmt="fancy_grid"
    ))
