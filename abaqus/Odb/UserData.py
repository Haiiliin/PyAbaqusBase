from ..Annotation.Annotation import Annotation
from ..UtilityAndView.Repository import Repository
from ..XY.QuantityType import QuantityType
from ..XY.XYData import XYData

class UserData:

    """The UserData object contains user-defined XY data. The UserData object has no 
    constructor; it is created automatically when an Odb object is created. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].userData

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A String specifying the repository key. 
    name: str = ''

    # A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken 
    # from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string. 
    sourceDescription: str = ''

    # A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The 
    # default value is an empty string. 
    contentDescription: str = ''

    # A String specifying additional information about the *X–Y* data (e.g., “for whole 
    # model”). The default value is an empty string. 
    positionDescription: str = ''

    # A String specifying the label for the X-values. This value may be overridden if the 
    # *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
    xValuesLabel: str = ''

    # A String specifying the label for the Y-values. This value may be overridden if the 
    # *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
    yValuesLabel: str = ''

    # A QuantityType object specifying the QuantityType object associated to the X -axis1- 
    # values. 
    axis1QuantityType: QuantityType = None

    # A QuantityType object specifying the QuantityType object associated to the Y -axis2- 
    # values. 
    axis2QuantityType: QuantityType = None

    # A String specifying the label to be used in the legend. The default value is the name of 
    # the XYData object. 
    legendLabel: str = ''

    # A repository of XYData objects. 
    xyDataObjects: Repository[str, XYData] = None

    # A repository of Annotation objects. 
    annotations: Repository[str, Annotation] = None

    # A tuple of pairs of Floats specifying the *X–Y* data pairs. 
    data: float = None

    def XYData(self, name: str, data: tuple, sourceDescription: str = '', contentDescription: str = '', 
               positionDescription: str = '', legendLabel: str = '', xValuesLabel: str = '', 
               yValuesLabel: str = '', axis1QuantityType: QuantityType = None, 
               axis2QuantityType: QuantityType = None):
        """This method creates an XYData object from a sequence of *X–Y* data pairs.

        Path
        ----
            - session.odbs[name].userData.XYData

        Parameters
        ----------
        name
            A String specifying the repository key. 
        data
            A sequence of pairs of Floats specifying the *X–Y* data pairs. 
        sourceDescription
            A String specifying the source of the *X–Y* data (e.g., “Entered from keyboard”, “Taken 
            from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string. 
        contentDescription
            A String specifying the content of the *X–Y* data (e.g., “field 1 vs. field 2”). The 
            default value is an empty string. 
        positionDescription
            A String specifying additional information about the *X–Y* data (e.g., “for whole 
            model”). The default value is an empty string. 
        legendLabel
            A String specifying the label to be used in the legend. The default value is the name of 
            the XYData object. 
        xValuesLabel
            A String specifying the label for the X-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        yValuesLabel
            A String specifying the label for the Y-values. This value may be overridden if the 
            *X–Y* data are combined with other *X–Y* data. The default value is an empty string. 
        axis1QuantityType
            A QuantityType object specifying the QuantityType object associated to the X -axis1- 
            values. 
        axis2QuantityType
            A QuantityType object specifying the QuantityType object associated to the Y -axis2- 
            values. 

        Returns
        -------
            An XYData object. 

        Exceptions
        ----------
            InvalidNameError. 
        """
        pass

