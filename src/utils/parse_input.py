def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args