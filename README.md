# Sample ArcGIS Pro Script Tool (Pro v2.5)

To use this template, clone or download the entire repository and [add MyToolbox.tbx to your ArcGIS Pro project](https://pro.arcgis.com/en/pro-app/help/projects/connect-to-a-toolbox.htm#GUID-07AA7C42-D833-45B3-973E-2521C0224A9E).

**/always_useful/things.py** represents a package of logic that appears in more than one project. For us, this mainly relates to data management tasks like indexing, domain and subtype maintenance, tile cache generation and map service updates.

When you're designing a new process, consider which parts are broadly useful and might belong here, and which are specific to the task at hand. This separation of concerns makes it possible to apply changes (hopefully improvements) across several tools or processes at once.

**MyToolbox.tbx** is where you'll define your STs and their inputs and outputs, including data types, validation and tool-tips through ArcGIS Pro.

**tool.py** is the bridge between Python and ArcGIS Pro. There are a number of advantages to keeping this file as simple as possible. The first is positive, it aids readability. The second is preventative. The way that this file accesses the parameters you set in your .tbx file is bound to the ST framework. Some of this Python syntax won't work anywhere else.

If you write complex logic here that you want to re-purpose later (for example, by invoking it from a script instead of the ArcGIS Pro ST interface), you will have to cut and paste your code. If your business logic isn't cleanly separated from the getting and setting of parameters, and the reporting of messages to arcpy, this could be a frustrating process for you.

**toolLogic.py** contains logic that's specific to this tool. This might include unique combinations of analysis tools.

**toolTest.py** and **toolTestRunner.py** contain unit tests for your scripts. Writing unit tests is not part of the typical geo skill-set, but it's essential for managing more complex scripts efficiently. If you have ever tried to debug by sticking print statements into the body of your code (I'm guilty), unit tests are the solution that you didn't know you needed. Have a look at [Real Python](https://realpython.com/python-testing/) and [Notes From the Lifeboat](https://notesfromthelifeboat.com/post/testing-arcpy-2/) for deeper reading on unit tests in Python and arcpy.
