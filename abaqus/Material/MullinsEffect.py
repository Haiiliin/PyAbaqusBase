from abaqusConstants import *

class MullinsEffect:

    """The MullinsEffect specifies properties for mullins data. 

    Access
    ------
        - import material
        - mdb.models[name].materials[name].mullinsEffect
        - import odbMaterial
        - session.odbs[name].materials[name].mullinsEffect

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the method of specifying the data. Possible values are 
    # USER, CONSTANTS, and TEST_DATA. The default value is CONSTANTS. 
    definition: SymbolicConstant = CONSTANTS

    # A Boolean specifying whether the data depend on temperature. The default value is OFF. 
    temperatureDependency: Boolean = OFF

    # An Int specifying the number of field variable dependencies. The default value is 0. 
    dependencies: int = 0

    # An Int specifying the number of property values needed as data for the user-defined 
    # hyperelastic material. The default value is 0. 
    properties: int = 0

    # A tuple of tuples of Floats specifying the items described below. The default value is 
    # an empty sequence. 
    table: tuple = ()

    # A UniaxialTestDataArray object. 
    uniaxialTests: UniaxialTestDataArray = None

    # A BiaxialTestDataArray object. 
    biaxialTests: BiaxialTestDataArray = None

    # A PlanarTestDataArray object. 
    planarTests: PlanarTestDataArray = None

