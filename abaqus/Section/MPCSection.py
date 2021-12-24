from .Section import Section
from abaqusConstants import *

class MPCSection(Section):

    """The MPCSection object defines the properties of a multi-point constraint section. 
    The MPCSection object is derived from the Section object. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name]
        - import odbSection
        - session.odbs[name].sections[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------
        - MPC

    """

    def __init__(self, name: str, mpcType: SymbolicConstant, userMode: SymbolicConstant = DOF_MODE, 
                 userType: int = 0):
        """This method creates a MPCSection object.

        Path
        ----
            - mdb.models[name].MPCSection
            - session.odbs[name].MPCSection

        Parameters
        ----------
        name
            A String specifying the repository key. 
        mpcType
            A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC, 
            ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED. 
        userMode
            A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible 
            values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The *userMode* argument 
            applies only when *mpcType*=USER_DEFINED. 
        userType
            An Int specifying to differentiate between different constraint types in a user-defined 
            MPCSection. The default value is 0.The *userType* argument applies only when 
            *mpcType*=USER_DEFINED. 

        Returns
        -------
            A MPCSection object. 

        Exceptions
        ----------
            RangeError and InvalidNameError. 
        """
        super().__init__()
        pass

