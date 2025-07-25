# Function Definition
def nanuFirstFunction() -> None:
    print("Nanu First Function")
    # Calling 2 Function inside 1 Function
    nanuSecondFunction()


def nanuSecondFunction() -> None:
    print("Nanu Second Function")
    # Calling 1 Function inside 2 Function
    nanuFirstFunction()

    """
    # Cause Error
    RecursionError: maximum recursion depth exceeded

    """


# Function Invocation
nanuFirstFunction()
