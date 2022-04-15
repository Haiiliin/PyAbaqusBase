class OdbMeshNode:
    """OdbMeshNode objects are created with the part.addNodes method.

    Attributes
    ----------
    label: int
        An Int specifying the node label.
    coordinates: float
        A tuple of Floats specifying the nodal coordinates in the global Cartesian coordinate
        system.

    Notes
    -----
    This object can be accessed by:
    
    .. code-block:: python
        
        import odbAccess
        session.odbs[name].parts[name].nodes[i]
        session.odbs[name].parts[name].nodeSets[name].nodes[i]
        session.odbs[name].parts[name].surfaces[name].nodes[i]
        session.odbs[name].rootAssembly.instances[name].nodes[i]
        session.odbs[name].rootAssembly.instances[name].nodeSets[name].nodes[i]
        session.odbs[name].rootAssembly.instances[name].surfaces[name].nodes[i]
        session.odbs[name].rootAssembly.nodes[i]
        session.odbs[name].rootAssembly.nodeSets[name].nodes[i]
        session.odbs[name].rootAssembly.surfaces[name].nodes[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodes[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].nodes[i]
        session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].nodes[i]

    """

    # An Int specifying the node label. 
    label: int = None

    # A tuple of Floats specifying the nodal coordinates in the global Cartesian coordinate 
    # system. 
    coordinates: float = None
