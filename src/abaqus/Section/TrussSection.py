from .Section import Section


class TrussSection(Section):
    """The TrussSection object defines the properties of a truss section.
    The TrussSection object is derived from the Section object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name]
        import odbSection
        session.odbs[name].sections[name]

    The corresponding analysis keywords are:

    - SOLID SECTION

    """

    def __init__(self, name: str, material: str, area: float = 1):
        """This method creates a TrussSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].TrussSection
            session.odbs[name].TrussSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        area
            A Float specifying the cross-sectional area for the section. Possible values are *area*
            >> 0. The default value is 1.0.

        Returns
        -------
            A TrussSection object.

        Raises
        ------
            RangeError and InvalidNameError.
        """
        super().__init__()
        pass

    def setValues(self, area: float = 1):
        """This method modifies the TrussSection object.

        Parameters
        ----------
        area
            A Float specifying the cross-sectional area for the section. Possible values are *area*
            >> 0. The default value is 1.0.

        Raises
        ------
        RangeError
        """
        pass
