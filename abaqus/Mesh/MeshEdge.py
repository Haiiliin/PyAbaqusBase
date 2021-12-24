from .MeshElementArray import MeshElementArray

class MeshEdge:

    """The MeshEdge object refers to an element edge. It has no constructor or members. A 
    MeshEdge object can be accessed via a MeshEdgeArray or a repository on a part or part 
    instance. 

    Access
    ------
        - import part
        - mdb.models[name].parts[name].elemEdges[i]
        - mdb.models[name].parts[name].elementEdges[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].elemEdges[i]
        - mdb.models[name].rootAssembly.allInstances[name].elementEdges[i]
        - mdb.models[name].rootAssembly.instances[name].elemEdges[i]
        - mdb.models[name].rootAssembly.instances[name].elementEdges[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def getElements(self):
        """This method returns a tuple of elements that share the element edge.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshElement objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElementsViaTopology(self, domain: MeshElementArray = None):
        """This method returns an array of MeshElement objects that are obtained by recursively
        finding adjacent elements via topology.

        Parameters
        ----------
        domain
            A MeshElementArray object specifying the domain to include in the search. By default, 
            all elements in the mesh are included. 

        Returns
        -------
            A MeshElementArray object, which is a sequence of MeshElement objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getNodesViaTopology(self, domain: MeshElementArray = None):
        """This method returns an array of MeshNode objects that lie along element edges
        topologically in line with the element edge.

        Parameters
        ----------
        domain
            A MeshElementArray object specifying the domain to include in the search. By default, 
            all elements in the mesh are included. 

        Returns
        -------
            A MeshNodeArray object, which is a sequence of MeshNode objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getElemFaces(self):
        """This method returns a tuple of unique MeshFace objects that share the element edge.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshFace objects. 

        Exceptions
        ----------
            None. 
        """
        pass

    def getNodes(self):
        """This method returns a tuple of nodes on the element edge.

        Parameters
        ----------

        Returns
        -------
            A tuple of MeshNode objects. 

        Exceptions
        ----------
            None. 
        """
        pass

