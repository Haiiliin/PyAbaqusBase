from abaqusConstants import *

class MagneticPermeability:

    """The MagneticPermeability object specifies magnetic permeability. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].magneticPermeability
        - import odbMaterial
        - session.odbs[name].materials[name].magneticPermeability

    Table Data
    ----------
        If *type*=ISOTROPIC, the table data specify the following:
        - Magnetic permeability.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ISOTROPIC, and *nonlinearBH*=TRUE, the table data specify the following:
        - Magntitude of the magnetic flux density vector.
        - Magnitude of the magnetic field vector.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ORTHOTROPIC, the table data specify the following:
        - μ11E.
        - μ22E.
        - μ33E.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ORTHOTROPIC, and *nonlinearBH*=TRUE, the table data specify the following:
        - Magntitude of the magnetic flux density vector in the first direction.
        - Magnitude of the magnetic field vector in the second direction.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *type*=ANISOTROPIC, the table data specify the following:
        - μ11E.
        - μ12E.
        - μ22E.
        - μ13E.
        - μ23E.
        - μ33E.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - MAGNETIC PERMEABILITY

    """

    def __init__(self, table: tuple, table2: tuple, table3: tuple, type: SymbolicConstant = ISOTROPIC, 
                 frequencyDependency: Boolean = OFF, temperatureDependency: Boolean = OFF, 
                 dependencies: int = 0, nonlinearBH: Boolean = OFF):
        """This method creates a MagneticPermeability object.

        Path
        ----
            - mdb.models[name].materials[name].MagneticPermeability
            - session.odbs[name].materials[name].MagneticPermeability

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below in “Table data.” 
            If *type*=ORTHOTROPIC and nonlinearBH=ON, the data specified in the *table* is for the 
            first direction and *table2* and *table3* must be specified. 
        table2
            A sequence of sequences of Floats specifying the items described below in “Table data” 
            in the second direction. *table2* must be specified only if *type*=ORTHOTROPIC and 
            nonlinearBH=ON. 
        table3
            A sequence of sequences of Floats specifying the items described below in “Table data” 
            in the third direction. *table3* must be specified only if *type*=ORTHOTROPIC and 
            nonlinearBH=ON. 
        type
            A SymbolicConstant specifying the type of magnetic permeability. Possible values are 
            ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC. 
        frequencyDependency
            A Boolean specifying whether the data depend on frequency. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 
        nonlinearBH
            A Boolean specifying whether the magnetic behavior is nonlinear and available in tabular 
            form of magnetic flux density versus magnetic field values. The default value is OFF. 

        Returns
        -------
            A MagneticPermeability object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the MagneticPermeability object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

