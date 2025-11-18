from tabulate import tabulate
from src.utils.colorizer import Colorizer
from src.utils.constants import COMMANDS_INFO
from src.utils.constants import DATE_FORMAT


def show_commands():
    table = []

    for cmd, usg, description in COMMANDS_INFO:
        colored_cmd = Colorizer.highlight(cmd)
        colored_usg = Colorizer.info(usg)
        colored_desc = Colorizer.commandline(description)
        table.append([colored_cmd, colored_usg, colored_desc])

    print(Colorizer.success("\nAvailable commands:\n"))
    print(
        tabulate(
            table,
            headers=[
                Colorizer.commandline("Command"),
                Colorizer.commandline("Usage"),
                Colorizer.commandline("Description"),
            ],
            tablefmt="grid",
        )
    )


def show_contacts_table(contacts):
    """Pretty prints contact list in a table format."""

    contacts = list(contacts)
    if not contacts:
        print(Colorizer.warning("No contacts to display."))
        return

    table = []

    for contact in contacts:
        phones_str = ""
        if getattr(contact, "phones", None):
            phones_str = "\n".join(
                Colorizer.info(p.value + ",") for p in contact.phones
            )

        email_str = ""
        if getattr(contact, "email", None):
            email_str = contact.email.value

        birthday_str = ""
        if getattr(contact, "birthday", None) and contact.birthday.value:
            try:
                birthday_str = contact.birthday.value.strftime(DATE_FORMAT)
            except AttributeError:
                birthday_str = str(contact.birthday.value)

        addresses_str = ""
        if getattr(contact, "addresses", None):
            addresses_str = "\n".join(
                Colorizer.info(addr.get_full_address() + ",")
                for addr in contact.addresses
            )

        table.append(
            [
                Colorizer.highlight(contact.name.value),
                phones_str,
                Colorizer.info(email_str),
                addresses_str,
                Colorizer.info(birthday_str),
            ]
        )

    print(Colorizer.highlight("CONTACT LIST:"))
    print(
        tabulate(
            table,
            headers=[
                Colorizer.commandline("Name"),
                Colorizer.commandline("Phone(s)"),
                Colorizer.commandline("Email"),
                Colorizer.commandline("Address(es)"),
                Colorizer.commandline("Birthday"),
            ],
            tablefmt="fancy_grid",
        )
    )
