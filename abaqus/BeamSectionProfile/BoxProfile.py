from abaqusConstants import *
from .Profile import Profile


class BoxProfile(Profile):

    """The BoxProfile object defines the properties of a box profile. 
    The BoxProfile object is derived from the Profile object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].profiles[name]
        import odbSection
        session.odbs[name].profiles[name]

        The corresponding analysis keywords are:
            - BEAM SECTION

    """

    def __init__(self, name: str, a: float, b: float, uniformThickness: Boolean, t1: float, t2: float = 0, 
                 t3: float = 0, t4: float = 0):
        """This method creates a BoxProfile object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].BoxProfile
            session.odbs[name].BoxProfile
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        a
            A Float specifying the *a* dimension of the box profile. For more information, see [Beam 
            cross-section 
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all). 
        b
            A Float specifying the *b* dimension of the box profile. 
        uniformThickness
            A Boolean specifying whether the thickness is uniform. 
        t1
            A Float specifying the uniform wall thickness if *uniformThickness*=ON, and the wall 
            thickness of the first segment if *uniformThickness*=OFF. 
        t2
            A Float specifying the wall thickness of the second segment. *t2* is required only when 
            *uniformThickness*=OFF. The default value is 0.0. 
        t3
            A Float specifying the wall thickness of the third segment. *t3* is required only when 
            *uniformThickness*=OFF. The default value is 0.0. 
        t4
            A Float specifying the wall thickness of the fourth segment. *t4* is required only when 
            *uniformThickness*=OFF. The default value is 0.0. 

        Returns
        -------
            A BoxProfile object. 

        Raises
        ------
        RangeError
            
        """
        super().__init__()
        pass

    def setValues(self, t2: float = 0, t3: float = 0, t4: float = 0):
        """This method modifies the BoxProfile object.
        
        Parameters
        ----------
        t2
            A Float specifying the wall thickness of the second segment. *t2* is required only when 
            *uniformThickness*=OFF. The default value is 0.0. 
        t3
            A Float specifying the wall thickness of the third segment. *t3* is required only when 
            *uniformThickness*=OFF. The default value is 0.0. 
        t4
            A Float specifying the wall thickness of the fourth segment. *t4* is required only when 
            *uniformThickness*=OFF. The default value is 0.0.

        Raises
        ------
        RangeError
            
        """
        pass

