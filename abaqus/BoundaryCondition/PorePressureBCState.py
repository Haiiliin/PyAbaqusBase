from abaqusConstants import *
from .BoundaryConditionState import BoundaryConditionState


class PorePressureBCState(BoundaryConditionState):
    """The PorePressureBCState object stores the propagating data for a pore pressure boundary
    condition in a step. One instance of this object is created internally by the 
    PorePressureBC object for each step. The instance is also deleted internally by the 
    PorePressureBC object. 
    The PorePressureBCState object has no constructor or methods. 
    The PorePressureBCState object is derived from the BoundaryConditionState object. 

    Attributes
    ----------
    magnitude: float
        A Float specifying the pore pressure magnitude.
    magnitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the pore pressure magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` object. Possible values are:
        NOT_YET_ACTIVE
        CREATED
        PROPAGATED
        MODIFIED
        DEACTIVATED
        NO_LONGER_ACTIVE
        TYPE_NOT_APPLICABLE
        INSTANCE_NOT_APPLICABLE
        PROPAGATED_FROM_BASE_STATE
        MODIFIED_FROM_BASE_STATE
        DEACTIVATED_FROM_BASE_STATE
        BUILT_INTO_MODES
    amplitude: str
        A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    Notes
    -----
        This object can be accessed by:
        - import load
        - mdb.models[name].steps[name].boundaryConditionStates[name]

    Corresponding analysis keywords
    -------------------------------
        - BOUNDARY

    """

    # A Float specifying the pore pressure magnitude. 
    magnitude: float = None

    # A SymbolicConstant specifying the propagation state of the pore pressure magnitude. 
    # Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    magnitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the amplitude reference. Possible 
    # values are UNSET, SET, UNCHANGED, FREED, and MODIFIED. 
    amplitudeState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:
    # NOT_YET_ACTIVE
    # CREATED
    # PROPAGATED
    # MODIFIED
    # DEACTIVATED
    # NO_LONGER_ACTIVE
    # TYPE_NOT_APPLICABLE
    # INSTANCE_NOT_APPLICABLE
    # PROPAGATED_FROM_BASE_STATE
    # MODIFIED_FROM_BASE_STATE
    # DEACTIVATED_FROM_BASE_STATE
    # BUILT_INTO_MODES
    status: SymbolicConstant = None

    # A String specifying the name of the amplitude reference. The String is empty if the 
    # boundary condition has no amplitude reference. 
    amplitude: str = ''
