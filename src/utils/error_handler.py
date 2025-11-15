from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"ValueError: {str(e)}"
        except KeyError as e:
            return f"KeyError: {str(e)}"
        except IndexError as e:
            return f"IndexError: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

    return inner
