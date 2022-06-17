class MeshStats:
    """The MeshStats object is a query object for holding mesh statistics and is returned by
    the getMeshStats command. The object does not have any methods.

    Attributes
    ----------
    numPointElems: int
        An Int specifying the number of point elements.
    numLineElems: int
        An Int specifying the number of line elements.
    numQuadElems: int
        An Int specifying the number of quadrilateral elements.
    numTriElems: int
        An Int specifying the number of triangular elements.
    numHexElems: int
        An Int specifying the number of hexahedral elements.
    numWedgeElems: int
        An Int specifying the number of wedge elements.
    numTetElems: int
        An Int specifying the number of tetrahedral elements.
    numPyramidElems: int
        An Int specifying the number of pyramid elements.
    numNodes: int
        An Int specifying the number of nodes.
    numMeshedRegions: int
        An Int specifying the number of regions that contain a mesh.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import mesh

    """

    # An Int specifying the number of point elements.
    numPointElems: int = None

    # An Int specifying the number of line elements.
    numLineElems: int = None

    # An Int specifying the number of quadrilateral elements.
    numQuadElems: int = None

    # An Int specifying the number of triangular elements.
    numTriElems: int = None

    # An Int specifying the number of hexahedral elements.
    numHexElems: int = None

    # An Int specifying the number of wedge elements.
    numWedgeElems: int = None

    # An Int specifying the number of tetrahedral elements.
    numTetElems: int = None

    # An Int specifying the number of pyramid elements.
    numPyramidElems: int = None

    # An Int specifying the number of nodes.
    numNodes: int = None

    # An Int specifying the number of regions that contain a mesh.
    numMeshedRegions: int = None
