class DirectDampingComponent:
    """A DirectDampingComponent object is used to define direct damping over a range of modes.

    Attributes
    ----------
    start: int
        An Int specifying the mode number of the lowest mode of a range.
    end: int
        An Int specifying the mode number of the highest mode of a range.
    fraction: float
        A Float specifying the fraction of critical damping.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].directDamping.components[i]

    """

    # An Int specifying the mode number of the lowest mode of a range.
    start: int = None

    # An Int specifying the mode number of the highest mode of a range.
    end: int = None

    # A Float specifying the fraction of critical damping.
    fraction: float = None
