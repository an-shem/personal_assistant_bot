from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style


class Prompt:
    """Universal input wrapper using prompt_toolkit with autocomplete & history."""

    style = Style.from_dict({
        "prompt": "bold #00afff",
    })

    def __init__(self, commands=None, history_file="src/storage/command_history.txt"):

        self.commands = commands or []
        self.completer = WordCompleter(self.commands, ignore_case=True)
        self.session = PromptSession(
            history=FileHistory(history_file)
        )

    def ask(self, text=">>> ", enable_completion=True):
        """
        Custom prompt.
        """
        completer = self.completer if enable_completion else None

        return self.session.prompt(
            [("class:prompt", text)],
            completer=completer,
            style=self.style
        )
    

