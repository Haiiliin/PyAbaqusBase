from abaqusConstants import *


class InteractionDisplayOptions:
    """The InteractionDisplayOptions object stores settings that specify how assemblies are to
    be displayed in a particular viewport when 
    session.viewports[name].assemblyDisplay.interactions=ON 
    The InteractionDisplayOptions object has no constructor. When you create a new viewport, 
    the settings are copied from the current viewport. 

    Notes
    -----
    This object can be accessed by:

    .. code-block::
    
        session.viewports[name].assemblyDisplay.interactionOptions
        session.viewports[name].layers[name].assemblyDisplay.interactionOptions

    """

    def setValues(self, surfaceContact: Boolean = ON, selfContact: Boolean = ON,
                  elasticFoundation: Boolean = ON, actuatorSensor: Boolean = ON,
                  radiationAmbient: Boolean = ON, filmCondition: Boolean = ON,
                  concentratedRadiationToAmbient: Boolean = ON, concentratedFilmCondition: Boolean = ON):
        """This method modifies the InteractionDisplayOptions object.
        
        Parameters
        ----------
        surfaceContact
            A Boolean specifying whether surface contact symbols are shown. The default value is ON. 
        selfContact
            A Boolean specifying whether self contact symbols are shown. The default value is ON. 
        elasticFoundation
            A Boolean specifying whether elastic foundation symbols are shown. The default value is 
            ON. 
        actuatorSensor
            A Boolean specifying whether actuator/sensor symbols are shown. The default value is ON. 
        radiationAmbient
            A Boolean specifying whether surface radiation-to-ambient symbols are shown. The default 
            value is ON. 
        filmCondition
            A Boolean specifying whether surface film condition symbols are shown. The default value 
            is ON. 
        concentratedRadiationToAmbient
            A Boolean specifying whether concentrated radiation-to-ambient symbols are shown. The 
            default value is ON. 
        concentratedFilmCondition
            A Boolean specifying whether concentrated film condition symbols are shown. The default 
            value is ON.

        Raises
        ------
        RangeError
        """
        pass
