from abaqusConstants import *

class UniaxialTestData:

    """The UniaxialTestData object provides uniaxial test data (compression and/or tension). 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].hyperelastic.uniaxialTestData
        - mdb.models[name].materials[name].hyperfoam.uniaxialTestData
        - mdb.models[name].materials[name].lowDensityFoam.uniaxialCompressionTestData
        - mdb.models[name].materials[name].lowDensityFoam.uniaxialTensionTestData
        - mdb.models[name].materials[name].mullinsEffect.uniaxialTests[i]
        - import odbMaterial
        - session.odbs[name].materials[name].hyperelastic.uniaxialTestData
        - session.odbs[name].materials[name].hyperfoam.uniaxialTestData
        - session.odbs[name].materials[name].lowDensityFoam.uniaxialCompressionTestData
        - session.odbs[name].materials[name].lowDensityFoam.uniaxialTensionTestData
        - session.odbs[name].materials[name].mullinsEffect.uniaxialTests[i]

    Table Data
    ----------
        For a hyperelastic material model, the table data specify the following:
        - Nominal stress, TU.
        - Nominal strain, ϵU.
        For a hyperfoam material model, the table data specify the following:
        - Nominal stress, TL.
        - Nominal strain, ϵU.
        - Nominal lateral strain, ϵ2=ϵ3. The default value is 0.
        For a low-density foam material model, the table data specify the following:
        - Nominal stress, TU.
        - Nominal strain, ϵU.
        - Nominal strain rate, ϵU˙.

    Corresponding analysis keywords
    -------------------------------
        - UNIAXIAL TEST DATA

    """

    def __init__(self, table: tuple, smoothing: int = None, lateralNominalStrain: Boolean = OFF, 
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a UniaxialTestData object.

        Path
        ----
            - mdb.models[name].materials[name].hyperelastic.UniaxialTestData
            - mdb.models[name].materials[name].hyperfoam.UniaxialTestData
            - mdb.models[name].materials[name].lowDensityFoam.UniaxialTestData
            - mdb.models[name].materials[name].mullinsEffect.UniaxialTestData
            - session.odbs[name].materials[name].hyperelastic.UniaxialTestData
            - session.odbs[name].materials[name].hyperfoam.UniaxialTestData
            - session.odbs[name].materials[name].lowDensityFoam.UniaxialTestData
            - session.odbs[name].materials[name].mullinsEffect.UniaxialTestData

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        smoothing
            None or an Int specifying the value for smoothing. If *smoothing*=None, no smoothing is 
            employed. The default value is None. 
        lateralNominalStrain
            A Boolean specifying whether to include lateral nominal strain. The default value is 
            OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A UniaxialTestData object. 

        Exceptions
        ----------
            None. 
        """
        pass

    def setValues(self):
        """This method modifies the UniaxialTestData object.

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

