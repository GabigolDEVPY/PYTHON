stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      X   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

def op_print(lifes):
    if lifes == 10:
        print(stages[0])
    elif lifes == 9:
        print(stages[1])
    elif lifes == 8:
        print(stages[2])
    elif lifes == 7:
        print(stages[3])
    elif lifes == 6:
        print(stages[4])
    elif lifes == 5:
        print(stages[5])
    elif lifes == 4:
        print(stages[6])
    elif lifes == 3:
        print(stages[7])
    elif lifes == 2:
        print(stages[8])
    else: 
        print(stages[9])
