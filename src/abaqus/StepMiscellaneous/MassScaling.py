from abaqusConstants import *


class MassScaling:
    """A MassScaling object defines the region and controls that govern mass scaling.

    Attributes
    ----------
    objective: SymbolicConstant
        A SymbolicConstant specifying :py:class:`~.the` objective of :py:class:`~.the` mass scaling definition. Possible
        values are SEMI_AUTOMATIC, AUTOMATIC, and REINITIALIZE. The default value is
        SEMI_AUTOMATIC.
    occurs: SymbolicConstant
        A SymbolicConstant specifying whether mass scaling should be performed at the beginning
        of the step or throughout the step. Possible values are AT_BEGINNING and
        THROUGHOUT_STEP.
    type: SymbolicConstant
        A SymbolicConstant specifying the type of scaling. Possible values are UNIFORM,
        BELOW_MIN, SET_EQUAL_DT, and ROLLING. The default value is BELOW_MIN.
    factor: float
        A Float specifying a scaling factor.
    dt: float
        A Float specifying a target time increment.
    frequency: int
        An Int specifying the frequency at which mass scaling calculations are performed.
    numberInterval: int
        An Int specifying the number of intervals at which mass scaling calculations are
        performed.
    feedRate: float
        A Float specifying the estimated average velocity of the workpiece in the rolling
        direction at steady-state conditions.
    extrudedLength: float
        A Float specifying the average element length in the extruded direction.
    crossSection: int
        An Int specifying the number of nodes in the cross-section of the workpiece.
    direction: SymbolicConstant
        A SymbolicConstant specifying the rolling direction. Possible values are GLOBAL_X,
        GLOBAL_Y, GLOBAL_Z, and GLOBAL_NONE. The default value is GLOBAL_X.
    region: SymbolicConstant
        The SymbolicConstant MODEL or a :py:class:`~abaqus.Region.Region.Region` object specifying where the mass scaling is
        applied. The default value is MODEL.

    Notes
    -----
    This object can be accessed by:
    
    .. code-block:: python
    
        import step
        mdb.models[name].steps[name].massScaling[i]

    """

    # A SymbolicConstant specifying the objective of the mass scaling definition. Possible 
    # values are SEMI_AUTOMATIC, AUTOMATIC, and REINITIALIZE. The default value is 
    # SEMI_AUTOMATIC. 
    objective: SymbolicConstant = SEMI_AUTOMATIC

    # A SymbolicConstant specifying whether mass scaling should be performed at the beginning 
    # of the step or throughout the step. Possible values are AT_BEGINNING and 
    # THROUGHOUT_STEP. 
    occurs: SymbolicConstant = None

    # A SymbolicConstant specifying the type of scaling. Possible values are UNIFORM, 
    # BELOW_MIN, SET_EQUAL_DT, and ROLLING. The default value is BELOW_MIN. 
    type: SymbolicConstant = BELOW_MIN

    # A Float specifying a scaling factor. 
    factor: float = None

    # A Float specifying a target time increment. 
    dt: float = None

    # An Int specifying the frequency at which mass scaling calculations are performed. 
    frequency: int = None

    # An Int specifying the number of intervals at which mass scaling calculations are 
    # performed. 
    numberInterval: int = None

    # A Float specifying the estimated average velocity of the workpiece in the rolling 
    # direction at steady-state conditions. 
    feedRate: float = None

    # A Float specifying the average element length in the extruded direction. 
    extrudedLength: float = None

    # An Int specifying the number of nodes in the cross-section of the workpiece. 
    crossSection: int = None

    # A SymbolicConstant specifying the rolling direction. Possible values are GLOBAL_X, 
    # GLOBAL_Y, GLOBAL_Z, and GLOBAL_NONE. The default value is GLOBAL_X. 
    direction: SymbolicConstant = GLOBAL_X

    # The SymbolicConstant MODEL or a Region object specifying where the mass scaling is 
    # applied. The default value is MODEL. 
    region: SymbolicConstant = MODEL
