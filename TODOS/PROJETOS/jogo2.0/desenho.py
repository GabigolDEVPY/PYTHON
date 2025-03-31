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
          |   O
          |   
          |   
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |   |
          |   
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |  /|
          |   
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |  /|\\
          |   
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |  /|\\
          |  / 
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |  /|\\
          |  / \\
          |   
    =========
    """,
    """
          +---+
          |   |
          |   X
          |  /|\\
          |  / \\
          |   
    =========
    """,
    """
          +---+
          |   |
          |  (O)
          |  /|\\
          |  / \\
          |   
    =========
    """,
    """
          +---+
          |   |
          |   O
          |  /|\\
          |  / \\
         _|_   
    =========
    """
]

def op_print(lifes, formed):
    if lifes == 10:
        print(f"{stages[0]}             {formed}")
    elif lifes == 9:
        print(f"{stages[1]}             {formed}")
    elif lifes == 8:
        print(f"{stages[2]}             {formed}")
    elif lifes == 7:
        print(f"{stages[3]}             {formed}")
    elif lifes == 6:
        print(f"{stages[4]}             {formed}")
    elif lifes == 5:
        print(f"{stages[5]}             {formed}")
    elif lifes == 4:
        print(f"{stages[6]}             {formed}")
    elif lifes == 3:
        print(f"{stages[7]}             {formed}")
    elif lifes == 2:
        print(f"{stages[8]}             {formed}")

    elif lifes == 1:
        print(f"{stages[9]}             {formed}")

