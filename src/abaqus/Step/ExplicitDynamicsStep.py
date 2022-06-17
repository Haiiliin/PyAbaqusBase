from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..Load.LoadCase import LoadCase
from ..Load.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.MassScalingArray import MassScalingArray
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class ExplicitDynamicsStep(AnalysisStep):
    """The ExplicitDynamicsStep object is used to perform a dynamic stress/displacement
    analysis using explicit integration in Abaqus/Explicit.
    The ExplicitDynamicsStep object is derived from the AnalysisStep object.

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    timePeriod: float
        A Float specifying the total time period for the step. The default value is 1.0.
    nlgeom: Boolean
        A Boolean specifying whether geometric nonlinearities should be accounted for during the
        step. The default value is ON.
    adiabatic: Boolean
        A Boolean specifying that an adiabatic stress analysis is to be performed. The default
        value is OFF.
    timeIncrementationMethod: SymbolicConstant
        A SymbolicConstant specifying the time incrementation method to be used. Possible values
        are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
        value is AUTOMATIC_GLOBAL.
    maxIncrement: float
        None or a Float specifying the maximum time increment. If there is no upper limit,
        **maxIncrement=None**. This argument is required only when
        **timeIncrementationMethod=AUTOMATIC_GLOBAL** or AUTOMATIC_EBE. The default value is None.
    scaleFactor: float
        A Float specifying the factor that is used to scale the time increment. This argument is
        required only when **timeIncrementationMethod=AUTOMATIC_GLOBAL**, AUTOMATIC_EBE, or
        FIXED_EBE. The default value is 1.0.
    linearBulkViscosity: float
        A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
    quadBulkViscosity: float
        A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
        1.2.
    userDefinedInc: float
        None or a Float specifying the user-defined time increment. This argument is required
        only when **timeIncrementationMethod=FIXED_USER_DEFINED_INC**. The default value is None.
    improvedDtMethod: Boolean
        A Boolean specifying whether to use the "improved" (**improvedDtMethod=ON**) or
        "conservative" (**improvedDtMethod=OFF**) method to estimate the element stable time
        increment for three-dimensional continuum elements and elements with plane stress
        formulations (shell, membrane, and two-dimensional plane stress elements). The default
        value is ON.
    previous: str
        A String specifying the name of the previous step. The new step appears after this step
        in the list of analysis steps.
    description: str
        A String specifying a description of the new step. The default value is an empty string.
    massScaling: MassScalingArray
        A :py:class:`~abaqus.StepMiscellaneous.MassScalingArray.MassScalingArray` object specifying mass scaling controls. The default value is
        PREVIOUS_STEP.
    explicit: SymbolicConstant
        A SymbolicConstant specifying whether the step has an explicit procedure type
        (**procedureType=ANNEAL**, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    perturbation: Boolean
        A Boolean specifying whether the step has a perturbation procedure type.
    nonmechanical: Boolean
        A Boolean specifying whether the step has a mechanical procedure type.
    procedureType: SymbolicConstant
        A SymbolicConstant specifying the Abaqus procedure. Possible values are:
            - ANNEAL
            - BUCKLE
            - COMPLEX_FREQUENCY
            - COUPLED_TEMP_DISPLACEMENT
            - COUPLED_THERMAL_ELECTRIC
            - DIRECT_CYCLIC
            - DYNAMIC_IMPLICIT
            - DYNAMIC_EXPLICIT
            - DYNAMIC_SUBSPACE
            - DYNAMIC_TEMP_DISPLACEMENT
            - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
            - FREQUENCY
            - GEOSTATIC
            - HEAT_TRANSFER
            - MASS_DIFFUSION
            - MODAL_DYNAMICS
            - RANDOM_RESPONSE
            - RESPONSE_SPECTRUM
            - SOILS
            - STATIC_GENERAL
            - STATIC_LINEAR_PERTURBATION
            - STATIC_RIKS
            - STEADY_STATE_DIRECT
            - STEADY_STATE_MODAL
            - STEADY_STATE_SUBSPACE
            - VISCO
    suppressed: Boolean
        A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    fieldOutputRequestState: dict[str, FieldOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState` objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState` objects.
    diagnosticPrint: DiagnosticPrint
        A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    monitor: Monitor
        A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    restart: Restart
        A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState` objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain` objects.
    control: Control
        A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    solverControl: SolverControl
        A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    boundaryConditionStates: dict[str, BoundaryConditionState]
        A repository of :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` objects.
    interactionStates: int
        A repository of :py:class:`~abaqus.Interaction.InteractionState.InteractionState` objects.
    loadStates: dict[str, LoadState]
        A repository of :py:class:`~abaqus.Load.LoadState.LoadState` objects.
    loadCases: dict[str, LoadCase]
        A repository of :py:class:`~abaqus.Load.LoadCase.LoadCase` objects.
    predefinedFieldStates: dict[str, PredefinedFieldState]
        A repository of :py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name]

    The corresponding analysis keywords are:

    - BULK VISCOSITY
            - DYNAMIC
            - FIXED MASS SCALING
            - STEP
            - VARIABLE MASS SCALING

    """

    # A String specifying the repository key.
    name: str = ""

    # A Float specifying the total time period for the step. The default value is 1.0.
    timePeriod: float = 1

    # A Boolean specifying whether geometric nonlinearities should be accounted for during the
    # step. The default value is ON.
    nlgeom: Boolean = ON

    # A Boolean specifying that an adiabatic stress analysis is to be performed. The default
    # value is OFF.
    adiabatic: Boolean = OFF

    # A SymbolicConstant specifying the time incrementation method to be used. Possible values
    # are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
    # value is AUTOMATIC_GLOBAL.
    timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL

    # None or a Float specifying the maximum time increment. If there is no upper limit,
    # *maxIncrement*=None. This argument is required only when
    # *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
    maxIncrement: float = None

    # A Float specifying the factor that is used to scale the time increment. This argument is
    # required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
    # FIXED_EBE. The default value is 1.0.
    scaleFactor: float = 1

    # A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
    linearBulkViscosity: float = 0

    # A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
    # 1.2.
    quadBulkViscosity: float = 1

    # None or a Float specifying the user-defined time increment. This argument is required
    # only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None.
    userDefinedInc: float = None

    # A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or
    # "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time
    # increment for three-dimensional continuum elements and elements with plane stress
    # formulations (shell, membrane, and two-dimensional plane stress elements). The default
    # value is ON.
    improvedDtMethod: Boolean = ON

    # A String specifying the name of the previous step. The new step appears after this step
    # in the list of analysis steps.
    previous: str = ""

    # A String specifying a description of the new step. The default value is an empty string.
    description: str = ""

    # A MassScalingArray object specifying mass scaling controls. The default value is
    # PREVIOUS_STEP.
    massScaling: MassScalingArray = PREVIOUS_STEP

    # A SymbolicConstant specifying whether the step has an explicit procedure type
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type.
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type.
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are:
    # - ANNEAL
    # - BUCKLE
    # - COMPLEX_FREQUENCY
    # - COUPLED_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRIC
    # - DIRECT_CYCLIC
    # - DYNAMIC_IMPLICIT
    # - DYNAMIC_EXPLICIT
    # - DYNAMIC_SUBSPACE
    # - DYNAMIC_TEMP_DISPLACEMENT
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
    # - FREQUENCY
    # - GEOSTATIC
    # - HEAT_TRANSFER
    # - MASS_DIFFUSION
    # - MODAL_DYNAMICS
    # - RANDOM_RESPONSE
    # - RESPONSE_SPECTRUM
    # - SOILS
    # - STATIC_GENERAL
    # - STATIC_LINEAR_PERTURBATION
    # - STATIC_RIKS
    # - STEADY_STATE_DIRECT
    # - STEADY_STATE_MODAL
    # - STEADY_STATE_SUBSPACE
    # - VISCO
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects.
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[
        str, FieldOutputRequestState
    ]()

    # A repository of HistoryOutputRequestState objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[
        str, HistoryOutputRequestState
    ]()

    # A DiagnosticPrint object.
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object.
    monitor: Monitor = None

    # A Restart object.
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState
    ]()

    # A repository of AdaptiveMeshDomain objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A Control object.
    control: Control = Control()

    # A SolverControl object.
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects.
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[
        str, BoundaryConditionState
    ]()

    # A repository of InteractionState objects.
    interactionStates: int = None

    # A repository of LoadState objects.
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    # A repository of LoadCase objects.
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    # A repository of PredefinedFieldState objects.
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[
        str, PredefinedFieldState
    ]()

    def __init__(
        self,
        name: str,
        previous: str,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = ON,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
        maxIncrement: float = None,
        scaleFactor: float = 1,
        massScaling: MassScalingArray = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        userDefinedInc: float = None,
        maintainAttributes: Boolean = False,
        improvedDtMethod: Boolean = ON,
    ):
        """This method creates an ExplicitDynamicsStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ExplicitDynamicsStep

        Parameters
        ----------
        name
            A String specifying the repository key.
        previous
            A String specifying the name of the previous step. The new step appears after this step
            in the list of analysis steps.
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is ON.
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default
            value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit,
            *maxIncrement*=None. This argument is required only when
            *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        massScaling
            A MassScalingArray object specifying mass scaling controls. The default value is
            PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required
            only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None.
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same
            name. The default value is False.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or
            "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

        Returns
        -------
            An ExplicitDynamicsStep object.

        Raises
        ------
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        description: str = "",
        timePeriod: float = 1,
        nlgeom: Boolean = ON,
        adiabatic: Boolean = OFF,
        timeIncrementationMethod: SymbolicConstant = AUTOMATIC_GLOBAL,
        maxIncrement: float = None,
        scaleFactor: float = 1,
        massScaling: MassScalingArray = PREVIOUS_STEP,
        linearBulkViscosity: float = 0,
        quadBulkViscosity: float = 1,
        userDefinedInc: float = None,
        improvedDtMethod: Boolean = ON,
    ):
        """This method modifies the ExplicitDynamicsStep object.

        Parameters
        ----------
        description
            A String specifying a description of the new step. The default value is an empty string.
        timePeriod
            A Float specifying the total time period for the step. The default value is 1.0.
        nlgeom
            A Boolean specifying whether geometric nonlinearities should be accounted for during the
            step. The default value is ON.
        adiabatic
            A Boolean specifying that an adiabatic stress analysis is to be performed. The default
            value is OFF.
        timeIncrementationMethod
            A SymbolicConstant specifying the time incrementation method to be used. Possible values
            are AUTOMATIC_GLOBAL, AUTOMATIC_EBE, FIXED_USER_DEFINED_INC, and FIXED_EBE. The default
            value is AUTOMATIC_GLOBAL.
        maxIncrement
            None or a Float specifying the maximum time increment. If there is no upper limit,
            *maxIncrement*=None. This argument is required only when
            *timeIncrementationMethod*=AUTOMATIC_GLOBAL or AUTOMATIC_EBE. The default value is None.
        scaleFactor
            A Float specifying the factor that is used to scale the time increment. This argument is
            required only when *timeIncrementationMethod*=AUTOMATIC_GLOBAL, AUTOMATIC_EBE, or
            FIXED_EBE. The default value is 1.0.
        massScaling
            A MassScalingArray object specifying mass scaling controls. The default value is
            PREVIOUS_STEP.
        linearBulkViscosity
            A Float specifying the linear bulk viscosity parameter, b1b1. The default value is 0.06.
        quadBulkViscosity
            A Float specifying the quadratic bulk viscosity parameter, b2b2. The default value is
            1.2.
        userDefinedInc
            None or a Float specifying the user-defined time increment. This argument is required
            only when *timeIncrementationMethod*=FIXED_USER_DEFINED_INC. The default value is None.
        improvedDtMethod
            A Boolean specifying whether to use the "improved" (*improvedDtMethod*=ON) or
            "conservative" (*improvedDtMethod*=OFF) method to estimate the element stable time
            increment for three-dimensional continuum elements and elements with plane stress
            formulations (shell, membrane, and two-dimensional plane stress elements). The default
            value is ON.

        Raises
        ------
        RangeError
        """
        pass
