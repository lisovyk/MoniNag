def validate_dict(dictionary, requirements):
    """Validate given dictionary for required keys.

    Args:
        dictionary(dict): Dictionary to validate.
        requirements(set): Set of required keys in dictionary.

    Returns:
        bool: The return value. True if valid, False otherwise.
    """

    return not bool(requirements ^ set(dictionary.keys()))