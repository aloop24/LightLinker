import maya.cmds as cmds
import maya.mel as mel
# Delink Everything

def delinkEverything(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    objs = cmds.ls ( geometry = True, lights = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in objs:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        #print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in poly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(b = True,  light = lightStr, object = polyStr)

def linkEverything(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    objs = cmds.ls ( geometry = True, lights = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in objs:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        #print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in poly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(light = lightStr, object = polyStr)

def delinkSelObj(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    objs = cmds.ls ( geometry = True, lights = True)

    #Get all Geometry in scene
    selection = cmds.ls (sl = True)
    selPolyShape = cmds.listRelatives(selection, c = True, type = "mesh")
    selPoly = cmds.listRelatives(selPolyShape, p = True, path = True)
    print("selected Poly:", selPoly)
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in objs:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        #print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in selPoly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(b = True,  light = lightStr, object = polyStr)

def linkSelObj(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    objs = cmds.ls ( geometry = True, lights = True)

    #Get all Geometry in scene
    selection = cmds.ls (sl = True)
    selPolyShape = cmds.listRelatives(selection, c = True, type = "mesh")
    selPoly = cmds.listRelatives(selPolyShape, p = True, path = True)
    print("selected Poly:", selPoly)
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in objs:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        #print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in selPoly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(light = lightStr, object = polyStr)

def delinkSelLight(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    selection = cmds.ls (sl = True)
    selChild = cmds.listRelatives(selection, c = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in selChild:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in poly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(b = True,  light = lightStr, object = polyStr)

def linkSelLight(*args):
    ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    selection = cmds.ls (sl = True)
    selChild = cmds.listRelatives(selection, c = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in selChild:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in poly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(light = lightStr, object = polyStr)
    
def delinkSel(*args):
   ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    selection = cmds.ls (sl = True)
    selChild = cmds.listRelatives(selection, c = True)
    selPolyShape = cmds.listRelatives(selection, c = True, type = "mesh")
    selPoly = cmds.listRelatives(selPolyShape, p = True, path = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in selChild:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in selPoly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(b = True,  light = lightStr, object = polyStr)

def linkSel(*args):
       ###TODO: Simplify into a less roundabout method
    #Get all Objects in scene
    selection = cmds.ls (sl = True)
    selChild = cmds.listRelatives(selection, c = True)
    selPolyShape = cmds.listRelatives(selection, c = True, type = "mesh")
    selPoly = cmds.listRelatives(selPolyShape, p = True, path = True)

    #Get all Geometry in scene
    polygon = cmds.ls (type = "mesh")
    poly = cmds.listRelatives(polygon, p =True, path = True)
    print poly
    #Remove all real Geometry from Objects list to get only lights
    lights = []
    firstTime = False
    for x in selChild:
        print("name: ", x, "Type: ", cmds.objectType(x))
        if "Light" in cmds.objectType(x):
            if firstTime == False:
               lights = [x]
               firstTime = True
            elif firstTime == True:
                lights.append(x)
    lightsParent = cmds.listRelatives(lights, p =True, path = True)
    print lightsParent
    ###ENDTODO    
    lightStr = []
    polyStr = []

        
    for x in lightsParent:
        print("x in lights: ", x)
        xStr = str(x)
        if firstTime == True:
            lightStr = [xStr]
            firstTime = False
        elif firstTime == False:
            lightStr.append(xStr)        
    print("Lights list: ", lightStr)
    for x in selPoly:
        xStr = str(x)
        if firstTime == False:
            polyStr = [xStr]
            firstTime = True
        elif firstTime == True:
            polyStr.append(xStr)
    print(polyStr)    
        
    cmds.lightlink(light = lightStr, object = polyStr)

#When options are collapsed window gets smaller
def optionsCollapse(*args):
    currentHeight = cmds.window(window, query = True, height = True)
    optionsHeight = cmds.frameLayout("options_ui_frameLayout", query = True, height = True)
    newHeight = currentHeight - optionsHeight
    cmds.window(window, e = True, height = newHeight)
    cmds.frameLayout("options_ui_frameLayout", e = True, height = 30)
#When options are expanded window gets larger
def optionsExpand(*args):
    currentHeight = cmds.window(window, query = True, height = True)
    optionsHeight = cmds.frameLayout("options_ui_frameLayout", query = True, height = True)
    newHeight = currentHeight + optionsHeight
    cmds.window(window, e = True, height = newHeight)
#When Light Linker is collapsed window gets smaller
def llCollapse(*args):
    currentHeight = cmds.window(window, query = True, height = True)
    llHeight = cmds.frameLayout("LL_ui_frameLayout", query = True, height = True)
    newHeight = currentHeight - llHeight
    cmds.window(window, e = True, height = newHeight)
#When Light Linker is expanded window gets larger
def llExpand(*args):
    currentHeight = cmds.window(window, query = True, height = True)
    llHeight = 300 #want Light Linker to have height of 300 px
    newHeight = currentHeight + llHeight
    cmds.window(window, e = True, height = newHeight)

# Make the window
if cmds.window("LL_ui_window", exists=True): #If the window exists
    cmds.deleteUI("LL_ui_window") #Delete it
window = cmds.window("LL_ui_window", title="Light Linker")
cmds.frameLayout(p="LL_ui_window", lv= False)
cmds.frameLayout("options_ui_frameLayout", p="LL_ui_window", label ="Options", cll = True, cl = False, collapseCommand = optionsCollapse, expandCommand = optionsExpand)
cmds.columnLayout(adjustableColumn=True, rowSpacing=20)
cmds.button (label = "Delink Everything", command = delinkEverything)
cmds.button (label = "Link Everything", command = linkEverything)
cmds.button (label = "Delink Selected Objects from all lights", command = delinkSelObj)
cmds.button (label = "Link Selected Objects to all lights", command = linkSelObj)
cmds.button (label = "Delink Everything from Selected Lights", command = delinkSelLight)
cmds.button (label = "Link Everything to Selected Lights", command = linkSelLight)
cmds.button (label = "Delink Selected Objects from Selected Lights", command = delinkSel)
cmds.button (label = "Link Selected Objects to Selected Lights", command = linkSel)
# Embed Light Linker
cmds.frameLayout("LL_ui_frameLayout", p="LL_ui_window", label="Light Linking Editor", cll = True, cl = True, collapseCommand = llCollapse, expandCommand = llExpand)
if cmds.scriptedPanel("LL_ui_scriptedPanel", exists=True): #If the scriptel panel already exists
    cmds.deleteUI("LL_ui_scriptedPanel") #Delete it
cmds.scriptedPanel("LL_ui_scriptedPanel", unParent=True, type="relationshipPanel")
cmds.scriptedPanel( "LL_ui_scriptedPanel", e=True, parent="LL_ui_frameLayout") #parent the scripted panel to your frame layout
cmds.window(window, e=True, height = 380) #Want the window to open at this height
cmds.showWindow(window)
