from abaqusConstants import *
from .Load import Load
from ..Region.Region import Region


class BodyConcentrationFlux(Load):
    """The BodyConcentrationFlux object defines body concentration flux from a region or into a
    region. 
    The BodyConcentrationFlux object is derived from the Load object. 

    Attributes
    ----------
    name: str
        A String specifying the load repository key.
    distributionType: SymbolicConstant
        A SymbolicConstant specifying how the body concentration flux is distributed spatially.
        Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM.
    field: str
        A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType=FIELD**. The default value is an
        empty string.
    region: Region
        A Region object specifying the region to which the load is applied.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].loads[name]

    """

    # A String specifying the load repository key. 
    name: str = ''

    # A SymbolicConstant specifying how the body concentration flux is distributed spatially. 
    # Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
    distributionType: SymbolicConstant = UNIFORM

    # A String specifying the name of the AnalyticalField object associated with this load. 
    # The *field* argument applies only when *distributionType*=FIELD. The default value is an 
    # empty string. 
    field: str = ''

    # A Region object specifying the region to which the load is applied. 
    region: Region = Region()

    def __init__(self, name: str, createStepName: str, region: Region, magnitude: float, field: str = '',
                 distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET):
        """This method creates a BodyConcentrationFlux object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].BodyConcentrationFlux

        Parameters
        ----------
        name
            A String specifying the load repository key. 
        createStepName
            A String specifying the name of the step in which the load is created. 
        region
            A Region object specifying the region to which the load is applied. 
        magnitude
            A Float specifying the body concentration flux magnitude. *magnitude* is optional if 
            *distributionType*=USER_DEFINED. 
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 

        Returns
        -------
            A BodyConcentrationFlux object. . 
        """
        super().__init__()
        pass

    def setValues(self, field: str = '', distributionType: SymbolicConstant = UNIFORM, amplitude: str = UNSET):
        """This method modifies the data for an existing BodyConcentrationFlux object in the step
        where it is created.

        Parameters
        ----------
        field
            A String specifying the name of the AnalyticalField object associated with this load. 
            The *field* argument applies only when *distributionType*=FIELD. The default value is an 
            empty string. 
        distributionType
            A SymbolicConstant specifying how the body concentration flux is distributed spatially. 
            Possible values are UNIFORM, USER_DEFINED, and FIELD. The default value is UNIFORM. 
        amplitude
            A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. 
            UNSET should be used if the load has no amplitude reference. The default value is UNSET. 
            You should provide the *amplitude* argument only if it is valid for the specified step. 
        """
        pass

    def setValuesInStep(self, stepName: str, magnitude: float = None, amplitude: str = ''):
        """This method modifies the propagating data for an existing BodyConcentrationFlux object
        in the specified step.

        Parameters
        ----------
        stepName
            A String specifying the name of the step in which the Body heat flux is modified. 
        magnitude
            A Float specifying the Body concentration flux magnitude. 
        amplitude
            A String or a SymbolicConstant specifying the name of the amplitude reference. Possible 
            values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the 
            amplitude is propagated from the previous analysis step. FREED should be used if the 
            load has no amplitude reference. You should provide the *amplitude* argument only if it 
            is valid for the specified step. 
        """
        pass
