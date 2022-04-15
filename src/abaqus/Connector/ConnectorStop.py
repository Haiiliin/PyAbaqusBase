from .ConnectorBehaviorOption import ConnectorBehaviorOption


class ConnectorStop(ConnectorBehaviorOption):
    """The ConnectorStop object defines connector stops for one or more components of a
    connector's relative motion. 
    The ConnectorStop object is derived from the ConnectorBehaviorOption object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name].behaviorOptions[i]
        import odbSection
        session.odbs[name].sections[name].behaviorOptions[i]

    The corresponding analysis keywords are:

    - CONNECTOR STOP

    """

    def __init__(self, minMotion: float = None, maxMotion: float = None, components: tuple = ()):
        """This method creates a connector stop behavior option for a ConnectorSection object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            import connectorBehavior
            connectorBehavior.ConnectorStop
            import odbConnectorBehavior
            odbConnectorBehavior.ConnectorStop
        
        Parameters
        ----------
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all 
            specified components, or no lower bound. The default value is None. 
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all 
            specified components, or no upper bound. The default value is None. 
        components
            A sequence of Ints specifying the components of relative motion for which the behavior 
            is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be 
            specified. The default value is an empty sequence. 

        Returns
        -------
            A ConnectorStop object. 

        Raises
        ------
            ValueError and TextError. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ConnectorStop object.

        Raises
        ------
            ValueError. 
        """
        pass
