''' Logic that's specific to this script tool. 
    Keeping this separate from tool.py makes it easier to re-purpose
    in the future, if we need to. 

    https://realpython.com/python-modules-packages/  
''' 

def specialThing():
    '''Basic demo for unit test example. '''
    return "Did a special thing"

def anotherSpecialThing(argument):
    '''Another demo. This accepts an argument and returns its type.'''
    output = type(argument)
    return output

def doComplicatedArcpyAnalysis(in_fc, out_fc, distance, arcpy):
    ''' Invoke arcpy logic. Note that arcpy is passed as an argument. 
        This helps to ensure that arcpy is never loaded more than 
        once, regardless of how many files we reference in tool.py. 

        Passing a module as an argument in this way is a form of 
        dependency injection. https://stackoverflow.com/a/9689381/ 
    '''
    result = arcpy.Buffer_analysis(in_fc, out_fc, distance)
    return result
