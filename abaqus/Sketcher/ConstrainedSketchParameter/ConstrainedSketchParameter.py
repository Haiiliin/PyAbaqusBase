class ConstrainedSketchParameter:
    """The ConstrainedSketchParameter object stores the definition of a parameter in the
    sketch. 

    Notes
    -----
        This object can be accessed by:
        
        .. code-block:: python
            
            import sketch
            mdb.models[name].sketches[name].parameters[i]

    """

    # A String specifying the name of the ConstrainedSketchParameter object. 
    name: str = ''

    # A String specifying the path to the ConstrainedSketchDimension that depends on this 
    # ConstrainedSketchParameter. 
    path: str = ''

    # A String specifying an expression or value associated with this 
    # ConstrainedSketchParameter. 
    expression: str = ''

    # A String specifying the name of the ConstrainedSketchParameter that appears before this 
    # one in the ordered list. 
    previousParameter: str = ''

    def Parameter(self, name: str, path: str = '', expression: str = '', previousParameter: str = ''):
        """This method creates a parameter and optionally associates a dimension with this
        parameter.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].sketches[name].ConstrainedSketchParameter
        
        Parameters
        ----------
        name
            A String specifying the name of the ConstrainedSketchParameter object. No two parameters 
            in the same ConstrainedSketch can have the same name. 
        path
            A String specifying the ConstrainedSketchDimension object with which this parameter is 
            associated. 
        expression
            A String specifying the expression or value associated with the 
            ConstrainedSketchParameter. 
        previousParameter
            A String specifying the name of the previous ConstrainedSketchParameter, if it exists. 
            The *previousParameter* argument implies an order among the parameters. No two 
            parameters can reference the same parameter as the previous parameter. 

        Returns
        -------
            A ConstrainedSketchParameter object.
            
        """
        pass
