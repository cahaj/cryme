def ansi(format, color, background):
    return f"\u001b[{format};{background};{color}m"

def ansireset():
    return "\u001b[0m"

def embed(title, ):
    pass