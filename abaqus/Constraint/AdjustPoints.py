from ..Region.Region import Region
from .Constraint import Constraint
from abaqusConstants import *

class AdjustPoints(Constraint):

    """The AdjustPoints constraint object is used to adjust points (nodes) to a surface. 
    The AdjustPoints object is derived from the Constraint object. 

    Access
    ------
        - import interaction
        - mdb.models[name].constraints[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - ADJUST

    """

    # A Boolean specifying whether the constraint is suppressed or not. The default value is 
    # OFF. 
    suppressed: Boolean = OFF

    def __init__(self, name: str, surface: Region, controlPoints: Region):
        """This method creates an AdjustPoints object.

        Path
        ----
            - mdb.models[name].AdjustPoints

        Parameters
        ----------
        name
            A String specifying the constraint repository key. 
        surface
            A Region object specifying the surface to which the *controlPoints* are adjusted. 
        controlPoints
            A Region object specifying the constraint control points. 

        Returns
        -------
            An AdjustPoints object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the AdjustPoints object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            None. 
        """
        pass

