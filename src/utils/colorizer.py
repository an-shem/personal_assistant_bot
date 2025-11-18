from colorama import Fore, Style, init

init(autoreset=True)


class Colorizer:
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"
    HIGHLIGHT = "highlight"
    COMMANDLINE = "commandline"

    @staticmethod
    def colorize(message: str, msg_type: str = INFO) -> str:
        colors = {
            Colorizer.INFO: Fore.CYAN,
            Colorizer.WARNING: Style.BRIGHT + Fore.YELLOW,
            Colorizer.ERROR: Fore.RED,
            Colorizer.SUCCESS: Fore.GREEN,
            Colorizer.HIGHLIGHT: Fore.MAGENTA + Style.BRIGHT,
            Colorizer.COMMANDLINE: Fore.BLUE + Style.BRIGHT,
        }
        color = colors.get(msg_type, Fore.WHITE)
        return f"{color}{message}{Style.RESET_ALL}"

    @staticmethod
    def info(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.INFO)

    @staticmethod
    def warning(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.WARNING)

    @staticmethod
    def error(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.ERROR)

    @staticmethod
    def success(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.SUCCESS)

    @staticmethod
    def highlight(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.HIGHLIGHT)

    @staticmethod
    def commandline(message: str) -> str:
        return Colorizer.colorize(message, Colorizer.COMMANDLINE)
