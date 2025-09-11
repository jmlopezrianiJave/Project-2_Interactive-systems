from choice import Choice

class Node:
    def __init__(self, id: int, title: str, description: str, choices: list[Choice]):
        self.id = id
        self.title = title
        self.description = description
        self.choices = choices