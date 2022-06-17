from abaqusConstants import *
from .InteractionState import InteractionState


class SelfContactExpState(InteractionState):
    """The SelfContactExpState object stores the propagating data for a SelfContactExp object.
    One instance of this object is created internally by the SelfContactExp object for each
    step. The instance is also deleted internally by the SelfContactExp object.
    The SelfContactExpState object has no constructor or methods.
    The SelfContactExpState object is derived from the InteractionState object.

    Attributes
    ----------
    interactionPropertyState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
        Possible values are UNSET, SET, UNCHANGED, and FREED.
    contactControlsState: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the **contactControls** member.
        Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionProperty: str
        A String specifying the name of the :py:class:`~abaqus.Interaction.ContactProperty.ContactProperty` object associated with this
        interaction.
    contactControls: str
        A String specifying the name of the :py:class:`~abaqus.Interaction.ContactControl.ContactControl` object associated with this
        interaction.
    status: SymbolicConstant
        A SymbolicConstant specifying the propagation state of the :py:class:`~abaqus.Interaction.InteractionState.InteractionState` object.
        Possible values are:
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - BUILT_INTO_BASE_STATE

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].steps[name].interactionStates[name]

    The corresponding analysis keywords are:

    - CONTACT CONTROLS
            - CONTACT PAIR
            - MODEL CHANGE

    """

    # A SymbolicConstant specifying the propagation state of the *interactionProperty* member.
    # Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionPropertyState: SymbolicConstant = None

    # A SymbolicConstant specifying the propagation state of the *contactControls* member.
    # Possible values are UNSET, SET, UNCHANGED, and FREED.
    contactControlsState: SymbolicConstant = None

    # A String specifying the name of the ContactProperty object associated with this
    # interaction.
    interactionProperty: str = ""

    # A String specifying the name of the ContactControl object associated with this
    # interaction.
    contactControls: str = ""

    # A SymbolicConstant specifying the propagation state of the InteractionState object.
    # Possible values are:
    # - NOT_YET_ACTIVE
    # - CREATED
    # - PROPAGATED
    # - MODIFIED
    # - DEACTIVATED
    # - NO_LONGER_ACTIVE
    # - TYPE_NOT_APPLICABLE
    # - INSTANCE_NOT_APPLICABLE
    # - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None
