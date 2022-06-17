from abaqusConstants import *


class OdbMeshRegionData:
    """The OdbMeshRegionData object defines the external source data of MappedField from an ODB
    file.

    Attributes
    ----------
    stepIndex: int
        An Int specifying the step index. Possible values are 0 ≤≤ **stepIndex** ≤≤ (**numSteps** −
        1). The default value is 0.
    frameIndex: int
        An Int specifying the frame in the specified step. Valid values are 0 ≤≤ **frameIndex** ≤≤
        (**numFramesInStep** − 1). The default value is 0.
    outputPosition: SymbolicConstant
        A SymbolicConstant specifying the position from which to obtain data. Data can be
        obtained only from the position at which they were written to the output database during
        the analysis. This position should be aligned with the field output variable. Possible
        values are:
            - UNDEFINED_POSITION
            - NODAL
            - INTEGRATION_POINT
            - ELEMENT_FACE
            - ELEMENT_NODAL
            - ELEMENT_CENTROID
            - WHOLE_ELEMENT
            - WHOLE_REGION
            - WHOLE_PART_INSTANCE
            - WHOLE_MODEL
            - GENERAL_PARTICLE
        The default value is UNDEFINED_POSITION.
    dataType: SymbolicConstant
        A SymbolicConstant specifying the data type of the field output variable which should be
        aligned with the variable. Currently only SCALAR is supported. Possible values are:
            - ENUMERATION
            - BOOLEAN
            - INTEGER
            - SCALAR
            - VECTOR
            - QUATERNION_2D
            - QUATERNION_3D
            - TENSOR
            - TENSOR_3D_FULL
            - TENSOR_3D_PLANAR
            - TENSOR_3D_SURFACE
            - TENSOR_2D_PLANAR
            - TENSOR_2D_SURFACE
        The default value is SCALAR.
    storageType: SymbolicConstant
        A SymbolicConstant specifying the storage type of the field output variable which should
        be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and BOOLEAN.
        The default value is FLOAT.
    quantityToPlot: SymbolicConstant
        A SymbolicConstant specifying the quantity to plot. Currently only FIELD_OUTPUT is
        supported. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is
        FIELD_OUTPUT.
    averageElementOutput: Boolean
        A Boolean specifying whether to average the element output. The default value is OFF.
    useRegionBoundaries: Boolean
        A Boolean specifying whether to use region boundaries when averaging. The default value
        is OFF.
    regionBoundaries: SymbolicConstant
        A SymbolicConstant specifying the type of averaging region boundaries. Currently only
        NONE and ODB_REGIONS are supported. Possible values are NONE, ODB_REGIONS, ELEMENT_SET,
        and DISPLAY_GROUPS. The default value is NONE.
    includeFeatureBoundaries: Boolean
        A Boolean specifying whether to include additional averaging boundaries for shells and
        membranes based on feature edges. The default value is ON.
    featureAngle: float
        A Float specifying the feature angle to be used when **includeFeatureBoundaries=ON**. The
        default value is 20.0.
    averageOnlyDisplayed: Boolean
        A Boolean specifying whether to average only values on displayed elements. The default
        value is OFF.
    averagingThreshold: float
        A Float specifying the nodal averaging threshold percentage. 0 ≤≤ **averagingThreshold**
        ≤≤100. The default value is 75.0.
    computeOrder: SymbolicConstant
        A SymbolicConstant specifying the order or the computations to be performed on the
        interested field output variable. Possible values are EXTRAPOLATE_AVERAGE_COMPUTE,
        EXTRAPOLATE_COMPUTE_AVERAGE, EXTRAPOLATE_COMPUTE, EXTRAPOLATE_COMPUTE_DISCONTINUITIES,
        and RAW_DATA. The default value is EXTRAPOLATE_COMPUTE_AVERAGE.
    numericForm: SymbolicConstant
        A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
        and COMPLEX_MAG_AT_ANGLE. The default value is REAL.
    complexAngle: float
        A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when *numericForm=COMPLEX_MAG_AT_ANGLE*=COMPLEX_MAG_AT_ANGLE. The
        default value is 0.0.
    odbFileName: str
        A String specifying the name of the output database file (including the .odb extension)
        to be read into as the source data. This String can also be the full path to the output
        database file if it is located in another directory.
    variableLabel: str
        A String specifying the field output variable.
    displayOutputPosition: SymbolicConstant
        A SymbolicConstant specifying the position where the output is displayed in the
        viewport. Possible values
        are:UNDEFINED_POSITIONNODALINTEGRATION_POINTELEMENT_FACEELEMENT_NODALELEMENT_CENTROIDWHOLE_ELEMENTWHOLE_REGIONWHOLE_PART_INSTANCEWHOLE_MODELGENERAL_PARTICLEThe
        default value is UNDEFINED_POSITION.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import field
        mdb.models[name].analyticalFields[name].odbMeshRegionData

    """

    # An Int specifying the step index. Possible values are 0 ≤≤ *stepIndex* ≤≤ (*numSteps* −
    # 1). The default value is 0.
    stepIndex: int = 0

    # An Int specifying the frame in the specified step. Valid values are 0 ≤≤ *frameIndex* ≤≤
    # (*numFramesInStep* − 1). The default value is 0.
    frameIndex: int = 0

    # A SymbolicConstant specifying the position from which to obtain data. Data can be
    # obtained only from the position at which they were written to the output database during
    # the analysis. This position should be aligned with the field output variable. Possible
    # values are:
    # - UNDEFINED_POSITION
    # - NODAL
    # - INTEGRATION_POINT
    # - ELEMENT_FACE
    # - ELEMENT_NODAL
    # - ELEMENT_CENTROID
    # - WHOLE_ELEMENT
    # - WHOLE_REGION
    # - WHOLE_PART_INSTANCE
    # - WHOLE_MODEL
    # - GENERAL_PARTICLE
    # The default value is UNDEFINED_POSITION.
    outputPosition: SymbolicConstant = UNDEFINED_POSITION

    # A SymbolicConstant specifying the data type of the field output variable which should be
    # aligned with the variable. Currently only SCALAR is supported. Possible values are:
    # - ENUMERATION
    # - BOOLEAN
    # - INTEGER
    # - SCALAR
    # - VECTOR
    # - QUATERNION_2D
    # - QUATERNION_3D
    # - TENSOR
    # - TENSOR_3D_FULL
    # - TENSOR_3D_PLANAR
    # - TENSOR_3D_SURFACE
    # - TENSOR_2D_PLANAR
    # - TENSOR_2D_SURFACE
    # The default value is SCALAR.
    dataType: SymbolicConstant = SCALAR

    # A SymbolicConstant specifying the storage type of the field output variable which should
    # be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and BOOLEAN.
    # The default value is FLOAT.
    storageType: SymbolicConstant = FLOAT

    # A SymbolicConstant specifying the quantity to plot. Currently only FIELD_OUTPUT is
    # supported. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is
    # FIELD_OUTPUT.
    quantityToPlot: SymbolicConstant = FIELD_OUTPUT

    # A Boolean specifying whether to average the element output. The default value is OFF.
    averageElementOutput: Boolean = OFF

    # A Boolean specifying whether to use region boundaries when averaging. The default value
    # is OFF.
    useRegionBoundaries: Boolean = OFF

    # A SymbolicConstant specifying the type of averaging region boundaries. Currently only
    # NONE and ODB_REGIONS are supported. Possible values are NONE, ODB_REGIONS, ELEMENT_SET,
    # and DISPLAY_GROUPS. The default value is NONE.
    regionBoundaries: SymbolicConstant = NONE

    # A Boolean specifying whether to include additional averaging boundaries for shells and
    # membranes based on feature edges. The default value is ON.
    includeFeatureBoundaries: Boolean = ON

    # A Float specifying the feature angle to be used when *includeFeatureBoundaries*=ON. The
    # default value is 20.0.
    featureAngle: float = 20

    # A Boolean specifying whether to average only values on displayed elements. The default
    # value is OFF.
    averageOnlyDisplayed: Boolean = OFF

    # A Float specifying the nodal averaging threshold percentage. 0 ≤≤ *averagingThreshold*
    # ≤≤100. The default value is 75.0.
    averagingThreshold: float = 75

    # A SymbolicConstant specifying the order or the computations to be performed on the
    # interested field output variable. Possible values are EXTRAPOLATE_AVERAGE_COMPUTE,
    # EXTRAPOLATE_COMPUTE_AVERAGE, EXTRAPOLATE_COMPUTE, EXTRAPOLATE_COMPUTE_DISCONTINUITIES,
    # and RAW_DATA. The default value is EXTRAPOLATE_COMPUTE_AVERAGE.
    computeOrder: SymbolicConstant = EXTRAPOLATE_COMPUTE_AVERAGE

    # A SymbolicConstant specifying the numeric form in which to display results that contain
    # complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL, IMAGINARY,
    # and COMPLEX_MAG_AT_ANGLE. The default value is REAL.
    numericForm: SymbolicConstant = REAL

    # A Float specifying the angle (in degrees) at which to display results that contain
    # complex numbers when *numericForm=COMPLEX_MAG_AT_ANGLE*=COMPLEX_MAG_AT_ANGLE. The
    # default value is 0.0.
    complexAngle: float = 0

    # A String specifying the name of the output database file (including the .odb extension)
    # to be read into as the source data. This String can also be the full path to the output
    # database file if it is located in another directory.
    odbFileName: str = ""

    # A String specifying the field output variable.
    variableLabel: str = ""

    # A SymbolicConstant specifying the position where the output is displayed in the
    # viewport. Possible values
    # are:UNDEFINED_POSITIONNODALINTEGRATION_POINTELEMENT_FACEELEMENT_NODALELEMENT_CENTROIDWHOLE_ELEMENTWHOLE_REGIONWHOLE_PART_INSTANCEWHOLE_MODELGENERAL_PARTICLEThe
    # default value is UNDEFINED_POSITION.
    displayOutputPosition: SymbolicConstant = UNDEFINED_POSITION

    def __init__(
        self,
        odbFileName: str,
        variableLabel: str,
        stepIndex: int = 0,
        frameIndex: int = 0,
        outputPosition: SymbolicConstant = UNDEFINED_POSITION,
        dataType: SymbolicConstant = SCALAR,
        storageType: SymbolicConstant = FLOAT,
        quantityToPlot: SymbolicConstant = FIELD_OUTPUT,
        averageElementOutput: str = OFF,
        useRegionBoundaries: str = OFF,
        regionBoundaries: SymbolicConstant = NONE,
        includeFeatureBoundaries: str = ON,
        featureAngle: float = 20,
        averageOnlyDisplayed: str = OFF,
        averagingThreshold: float = 75,
        computeOrder: SymbolicConstant = EXTRAPOLATE_COMPUTE_AVERAGE,
        numericForm: SymbolicConstant = REAL,
        complexAngle: float = 0,
        sectionPoint: str = "",
        refinementType: SymbolicConstant = None,
        refinementLabel: str = "",
        displayOutputPosition: SymbolicConstant = None,
    ):
        """This method creates an OdbMeshRegionData object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].analyticalFields[name].OdbMeshRegionData

        Parameters
        ----------
        odbFileName
            A String specifying the name of the output database file (including the .odb extension)
            to be read into as the source data. This String can also be the full path to the output
            database file if it is located in another directory.
        variableLabel
            A String specifying the field output variable.
        stepIndex
            An Int specifying the step index. Possible values are 0 ≤≤ *stepIndex* ≤≤ (*numSteps* −
            1). The default value is 0.
        frameIndex
            An Int specifying the frame in the specified step. Valid values are 0 ≤≤ *frameIndex* ≤≤
            (*numFramesInStep* − 1). The default value is 0.
        outputPosition
            A SymbolicConstant specifying the position where the data is written in the output
            database. Data can be obtained only from the position at which it was written to the
            output database during the analysis. This position should be aligned with the field
            output variable. Possible values are:

            - UNDEFINED_POSITION
            - NODAL
            - INTEGRATION_POINT
            - ELEMENT_FACE
            - ELEMENT_NODAL
            - ELEMENT_CENTROID
            - WHOLE_ELEMENT
            - WHOLE_REGION
            - WHOLE_PART_INSTANCE
            - WHOLE_MODEL
            - GENERAL_PARTICLE
            ​	The default value is UNDEFINED_POSITION.
        dataType
            A SymbolicConstant specifying the data type of the field output variable which should be
            aligned with the variable. Currently only SCALAR is supported. Possible values are:

            - ENUMERATION
            - BOOLEAN
            - INTEGER
            - SCALAR
            - VECTOR
            - QUATERNION_2D
            - QUATERNION_3D
            - TENSOR
            - TENSOR_3D_FULL
            - TENSOR_3D_PLANAR
            - TENSOR_3D_SURFACE
            - TENSOR_2D_PLANAR
            - TENSOR_2D_SURFACE
            The default value is SCALAR.
        storageType
            ​	A SymbolicConstant specifying the storage type of the field output variable which
            should be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and
            BOOLEAN. The default value is FLOAT.
        quantityToPlot
            ​	A SymbolicConstant specifying the quantity to plot. Currently only FIELD_OUTPUT is
            supported. Possible values are FIELD_OUTPUT and DISCONTINUITIES. The default value is
            FIELD_OUTPUT.
        averageElementOutput
            ​	A Boolean specifying whether to average the element output. The default value is OFF.
        useRegionBoundaries
            ​	A Boolean specifying whether to use region boundaries when averaging. The default
            value is OFF.
        regionBoundaries
            ​	A SymbolicConstant specifying the type of averaging region boundaries. Currently only
            NONE and ODB_REGIONS are supported. Possible values are NONE, ODB_REGIONS, ELEMENT_SET,
            and DISPLAY_GROUPS. The default value is NONE.
        includeFeatureBoundaries
            ​	A Boolean specifying whether to include additional averaging boundaries for shells and
            membranes based on feature edges. The default value is ON.
        featureAngle
            ​	A Float specifying the feature angle to be used when *includeFeatureBoundaries*=ON.
            The default value is 20.0.
        averageOnlyDisplayed
            ​	A Boolean specifying whether to average only values on displayed elements. The default
            value is OFF.
        averagingThreshold
            ​	A Float specifying the nodal averaging threshold percentage. 0 ≤≤ *averagingThreshold*
            ≤≤100. The default value is 75.0.
        computeOrder
            ​	A SymbolicConstant specifying the order or the computations to be performed on the
            interested field output variable. Possible values are EXTRAPOLATE_AVERAGE_COMPUTE,
            EXTRAPOLATE_COMPUTE_AVERAGE, EXTRAPOLATE_COMPUTE, EXTRAPOLATE_COMPUTE_DISCONTINUITIES,
            and RAW_DATA. The default value is EXTRAPOLATE_COMPUTE_AVERAGE.
        numericForm
            ​	A SymbolicConstant specifying the numeric form in which to display results that
            contain complex numbers. Possible values are COMPLEX_MAGNITUDE, COMPLEX_PHASE, REAL,
            IMAGINARY, and COMPLEX_MAG_AT_ANGLE. The default value is REAL.
        complexAngle
            ​	A Float specifying the angle (in degrees) at which to display results that contain
            complex numbers when *numericForm=COMPLEX_MAG_AT_ANGLE*=COMPLEX_MAG_AT_ANGLE. The
            default value is 0.0.
        sectionPoint
            ​	A Dictionary with String keys and String values. Each key specifies a region in the
            model; the corresponding value specifies a section point within that region. For
            example:
            sectionPoint={'shell < MAT > < 7 section points >':'SPOS
            (fraction = 1.0)', 'shell < MAT > < 5 section points >':
            'SPOS, (fraction = 1.0)', }
        refinementType
            ​	A SymbolicConstant specifying the type of the FieldOutput object. Possible values for
            the SymbolicConstant are NO_REFINEMENT, INVARIANT and COMPONENT. Default argument is
            NO_REFINEMENT. *refinementType* is mandetory if *variableLabel* has an INVARIANT or a
            COMPONENT.
        refinementLabel
            ​	A String specifying the Label of FieldOutput object. This is required only if the
            *refinementType* is INVARIANT or COMPONENT.
        displayOutputPosition
            ​	A SymbolicConstant specifying the position from which to obtain the data. Possible
            values are NODAL, INTEGRATION_POINT, ELEMENT_FACE, ELEMENT_NODAL, ELEMENT_CENTROID,
            WHOLE_ELEMENT, WHOLE_REGION, WHOLE_PART_INSTANCE, WHOLE_MODEL, and GENERAL_PARTICLE.

        Returns
        -------
            An OdbMeshRegionData object.

        Raises
        ------
            TextException.
        """
        pass

    def setValues(self):
        """This method modifies the OdbMeshRegionData object."""
        pass
