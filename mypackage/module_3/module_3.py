from mypackage.module_1 import module_1


def wrapper_for_print_and_type(parameters_dict):
    """
    Wrapper function for the print_a_string and type_an_object functions found
    in module_1 and module_2 respectively.

    See Also
    --------
    module_1.module_2
    module_2.module_2

    Parameters
    ----------
    parameters_dict : dict

    Dictionary containint the input parameters for the print_a_string and
    type_an_object functions:

        string_to_print : str
        The string to be printed to the console

        object_to_type : obj
        The object to check the type of.

    Returns
    -------
    return_dict : dict
    Dictionary containing the results of the print_a_string and type_an_object
    functions:

        my_string : str
        The string that was printed to the console

        my_type : obj
        The object to check the type of.

    Examples
    --------
    wrapper_for_print_and_type({'Hello Mango!', 3.6})
    """

    # Unpacking the input dictionary
    string_to_print = module_1.print_a_string(parameters_dict)

    # Applying the functions

    return len(string_to_print)
