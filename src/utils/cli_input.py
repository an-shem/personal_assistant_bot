from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.document import Document
from prompt_toolkit.filters import Condition
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.history import FileHistory


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
        Prompt with autocomplete only for the first word.
        """

        def first_word_completer():
            """
            Return completer ONLY if cursor is at the first word.
            """
            doc: Document = self.session.default_buffer.document

            # cursor is at first word if:
            # - everything before cursor has no spaces
            before = doc.text_before_cursor

            if " " not in before.strip():
                return self.completer
            return None

        completer = first_word_completer() if enable_completion else None

        return self.session.prompt(
            [("class:prompt", text)],
            completer=completer,
            style=self.style
        )