class Interaction:
    """The Interaction object is the abstract base type for other Interaction objects. The
    Interaction object has no explicit constructor. Each of the Interaction objects has the
    following methods:
    - deactivate
    - move
    - reset
    - resume
    - suppress
    - delete
    The methods are described below.

    Attributes
    ----------
    name: str
        A String specifying the repository key.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    """

    # A String specifying the repository key.
    name: str = ""

    def deactivate(self, stepName: str):
        """This method deactivates the interaction in the specified step and all its subsequent
        steps.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is deactivated.
        """
        pass

    def move(self, fromStepName: str, toStepName: str):
        """This method moves an interaction from one step to another.

        Parameters
        ----------
        fromStepName
            A String specifying the name of the step from which to move the interaction.
        toStepName
            A String specifying the name of the step to which to move the interaction.
        """
        pass

    def reset(self, stepName: str):
        """This method reactivates an interaction that was deactivated previously. The reset method
        is available during the step in which the interaction was deactivated originally.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the interaction is reactivated.
        """
        pass

    def resume(self):
        """This method resumes an interaction that was previously suppressed."""
        pass

    def suppress(self):
        """This method suppresses an interaction."""
        pass

    def delete(self, indices: tuple):
        """This method allows you to delete existing interactions.

        Parameters
        ----------
        indices
            A sequence of Ints specifying the index of each interaction to delete.
        """
        pass
