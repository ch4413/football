

def type_an_object(object_to_type):
    """
    Prints the type of the supplied object to the console, and also returns
    the type.

    Parameters
    ----------
    object_to_type : obj
    The object to check the type of.

    Returns
    -------
    object_to_type : obj
    The object to check the type of.

    Examples
    --------
    object_to_type(1)
    """

    object_type = type(object_to_type)
    print(object_type)

    return object_type
