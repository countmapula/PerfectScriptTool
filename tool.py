''' This is the file that's referenced directly by your script tool
    in ArcGIS Pro. 

    Things to do:
    
    - Import other modules that you need
    - Get and set script tool parameters using arcpy.GetParameter...
    - Set other global variables
    - Send messages to the ArcGIS Pro interface with arcpy.Add... 
    - Invoke logic from your other files 
'''


# Imports 
# You don't need to import arcpy - this happens implicitly in script tools 
import sys

# Local imports 
from always_useful import things
import toolLogic 


# Variables 
in_fc = arcpy.GetParameterAsText(0)
out_fc = arcpy.GetParameterAsText(1) 
distance = arcpy.GetParameterAsText(2)


# Logic and error handling 
# Execute logic that's specific to this tool 
arcpy.AddMessage('Doing some complicated arcpy analysis')
try:
    # Using a function from toolLogic.py
    toolLogic.doComplicatedArcpyAnalysis(in_fc, out_fc, distance, arcpy) 
except Exception: 
    e = sys.exc_info()[1]
    # If using this code within a script tool, AddError can be used to return messages 
    # back to a script tool. If not, AddError will have no effect.
    arcpy.AddError(e.args[0])

# Execute one of your always_useful things 
arcpy.AddMessage('Doing routine data management')
try:
    # Using a function from always_useful/things.py
    things.doGeneralThing(out_fc)
except Exception: 
    e = sys.exc_info()[1]
    arcpy.AddError(e.args[0])

arcpy.AddMessage('All done!')
