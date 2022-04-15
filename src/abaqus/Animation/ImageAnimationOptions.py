from abaqusConstants import *


class ImageAnimationOptions:
    """The ImageAnimationOptions object is used to store values and attributes associated with
    saving viewport animations. The ImageAnimationOptions object has no constructor. Abaqus 
    creates the *imageAnimationOptions* member when the animation module is imported. 

    Notes
    -----
    This object can be accessed by:
    
    .. code-block:: python
        
        import animation
        session.imageAnimationOptions

    """

    def setValues(self, frameRate: int = None, timeScale: int = None, vpDecorations: Boolean = ON,
                  vpBackground: Boolean = OFF, compass: Boolean = OFF):
        """This method modifies the ImageAnimationOptions object.
        
        Parameters
        ----------
        frameRate
            An Int specifying the frame rate to record on the saved animation file. The effective 
            frame rate in frames per second will be obtained by dividing the given frame rate by the 
            time scale. 
        timeScale
            An Int specifying the time scale to apply to the frame rate. 
        vpDecorations
            A Boolean specifying whether to capture the viewport border and title. The default value 
            is ON. 
        vpBackground
            A Boolean specifying whether to capture viewport backgrounds. The default value is OFF. 
        compass
            A Boolean specifying whether to capture the view compass. The default value is OFF. 
        """
        pass
