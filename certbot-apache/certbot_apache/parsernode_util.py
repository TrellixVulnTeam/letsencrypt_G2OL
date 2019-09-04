"""ParserNode utils"""


def validate_kwargs(kwargs, required_names):
    """
    Ensures that the kwargs dict has all the expected values. This function modifies
    the kwargs dictionary, and hence the returned dictionary should be used instead
    in the caller function instead of the original kwargs.

    :param dict kwargs: Dictionary of keyword arguments to validate.
    :param list required_names: List of required parameter names.
    """

    validated_kwargs = dict()
    for name in required_names:
        try:
            validated_kwargs[name] = kwargs.pop(name)
        except KeyError:
            raise TypeError("Required keyword argument: {} undefined.".format(name))

    # Raise exception if unknown key word arguments are found.
    if kwargs:
        unknown = ", ".join(kwargs.keys())
        raise TypeError("Unknown keyword argument(s): {}".format(unknown))
    return validated_kwargs


def parsernode_kwargs(kwargs):
    """
    Validates keyword arguments for ParserNode. This function modifies the kwargs
    dictionary, and hence the returned dictionary should be used instead in the
    caller function instead of the original kwargs.


    :param dict kwargs: Keyword argument dictionary to validate.

    :returns: Tuple of validated and prepared arguments.
    """

    # As ParserNode instances can be initialized with metadata alone, make sure
    # we permit it here as well.
    if "metadata" in kwargs:
        kwargs.setdefault("filepath", None)

    kwargs.setdefault("dirty", False)
    kwargs.setdefault("metadata", {})

    kwargs = validate_kwargs(kwargs, ["ancestor", "dirty", "filepath", "metadata"])
    return kwargs["ancestor"], kwargs["dirty"], kwargs["filepath"], kwargs["metadata"]


def commentnode_kwargs(kwargs):
    """
    Validates keyword arguments for CommentNode and sets the default values for
    optional kwargs. This function modifies the kwargs dictionary, and hence the
    returned dictionary should be used instead in the caller function instead of
    the original kwargs.


    :param dict kwargs: Keyword argument dictionary to validate.

    :returns: Tuple of validated and prepared arguments and ParserNode kwargs.
    """

    # As ParserNode instances can be initialized with metadata alone, make sure
    # we permit it here as well.
    if "metadata" in kwargs:
        kwargs.setdefault("comment", None)
        kwargs.setdefault("filepath", None)

    kwargs.setdefault("dirty", False)
    kwargs.setdefault("metadata", {})

    kwargs = validate_kwargs(kwargs, ["ancestor", "dirty", "filepath", "comment",
                                      "metadata"])

    comment = kwargs.pop("comment")
    return comment, kwargs


def directivenode_kwargs(kwargs):
    """
    Validates keyword arguments for DirectiveNode and BlockNode and sets the
    default values for optional kwargs. This function modifies the kwargs
    dictionary, and hence the returned dictionary should be used instead in the
    caller function instead of the original kwargs.

    :param dict kwargs: Keyword argument dictionary to validate.

    :returns: Tuple of validated and prepared arguments and ParserNode kwargs.
    """

    # As ParserNode instances can be initialized with metadata alone, make sure
    # we permit it here as well.
    if "metadata" in kwargs:
        kwargs.setdefault("name", None)
        kwargs.setdefault("filepath", None)

    kwargs.setdefault("dirty", False)
    kwargs.setdefault("enabled", True)
    kwargs.setdefault("parameters", ())
    kwargs.setdefault("metadata", {})

    kwargs = validate_kwargs(kwargs, ["ancestor", "dirty", "filepath", "name",
                                      "parameters", "enabled", "metadata"])

    name = kwargs.pop("name")
    parameters = kwargs.pop("parameters")
    enabled = kwargs.pop("enabled")
    return name, parameters, enabled, kwargs
