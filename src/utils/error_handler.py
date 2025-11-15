from functools import wraps
from src.utils.colorizer import Colorizer


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return Colorizer.error(f"ValueError: {str(e)}")
        except KeyError as e:
            return Colorizer.error(f"KeyError: {str(e)}")
        except IndexError as e:
            return Colorizer.error(f"IndexError: {str(e)}")
        except Exception as e:
            return Colorizer.error(f"Error: {str(e)}")

    return inner
