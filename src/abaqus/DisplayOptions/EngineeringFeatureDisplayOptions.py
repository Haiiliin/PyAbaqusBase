from abaqusConstants import *


class EngineeringFeatureDisplayOptions:
    """The EngineeringFeatureDisplayOptions object stores settings that specify how assemblies
    are to be displayed in a particular viewport when
    session.viewports[name].assemblyDisplay.engineeringFeatures=ON
    The EngineeringFeatureDisplayOptions object has no constructor. When you create a new
    viewport, the settings are copied from the current viewport.

    Notes
    -----
    This object can be accessed by:

    .. code-block::

        session.viewports[name].assemblyDisplay.engineeringFeatureOptions
        session.viewports[name].layers[name].assemblyDisplay.engineeringFeatureOptions
        import part
        session.viewports[name].layers[name].partDisplay.engineeringFeatureOptions
        session.viewports[name].partDisplay.engineeringFeatureOptions

    """

    def setValues(
        self,
        pointMassInertia: Boolean = ON,
        nonstructuralMass: Boolean = ON,
        heatCapacitance: Boolean = ON,
        contourIntegral: Boolean = ON,
        springToGround: Boolean = ON,
        twoPointSpring: Boolean = ON,
    ):
        """This method modifies the EngineeringFeatureDisplayOptions object.

        Parameters
        ----------
        pointMassInertia
            A Boolean specifying whether point mass inertia symbols are shown. The default value is
            ON.
        nonstructuralMass
            A Boolean specifying whether nonstructural mass symbols are shown. The default value is
            ON.
        heatCapacitance
            A Boolean specifying whether heat capacitance symbols are shown. The default value is
            ON.
        contourIntegral
            A Boolean specifying whether contour integral symbols are shown. The default value is
            ON.
        springToGround
            A Boolean specifying whether spring-to-ground symbols are shown. The default value is
            ON.
        twoPointSpring
            A Boolean specifying whether two-point spring symbols are shown. The default value is
            ON.

        Raises
        ------
        RangeError
        """
        pass
