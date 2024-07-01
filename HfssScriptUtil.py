
def changeGlobalVar(oProject, varName, newValStr):
	oProject.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:ProjectVariableTab",
			[
				"NAME:PropServers", 
				"ProjectVariables"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:" + varName,
					"Value:="		, newValStr
				]
			]
		]
	])
        
def createLocalVar(oDesign, varName, valStr):
    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:LocalVariableTab",
                [
                    "NAME:PropServers", 
                    "LocalVariables"
                ],
                [
                    "NAME:NewProps",
                    [
                        "NAME:" + varName,
                        "PropType:="		, "VariableProp",
                        "UserDef:="		, True,
                        "Value:="		, valStr
                    ]
                ]
            ]
        ])
	
def changeLocalVar(oDesign, varName, newValStr):
	oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:" + varName,
					"Value:="		, newValStr
				]
			]
		]
	])
    
def moveGroup(oEditor, grpName, x='0cm', y='0cm', z='0cm'):
    oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, grpName,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, x,
            "TranslateVectorY:="	, y,
            "TranslateVectorZ:="	, z
        ])    

def rotateGroup(oEditor, grpName, axis='Z', angle='0deg'): 
    oEditor.Rotate(
        [
            "NAME:Selections",
            "Selections:="		, grpName,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:RotateParameters",
            "RotateAxis:="		, axis,
            "RotateAngle:="		, angle
        ])

def rotateSelection(oEditor, objList, axis='Z', angle='0deg'):
    # turn the obj list into a plain-old string
    selStr = ''
    frst = True
    for obj in objList:
        if frst:
            frst = False
            selStr = obj
        else:
            selStr = selStr + "," + obj
        
    oEditor.Rotate(
        [
            "NAME:Selections",
            "Selections:="		, selStr,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:RotateParameters",
            "RotateAxis:="		, axis,
            "RotateAngle:="		, angle
        ])
    
def createRelativeCS(oEditor, cordSysName='RelativeCS1', x0='0cm', y0='0cm', z0='0cm',):
    oEditor.CreateRelativeCS(
        [
            "NAME:RelativeCSParameters",
            "Mode:="		, "Axis/Position",
            "OriginX:="		, x0,
            "OriginY:="		, y0,
            "OriginZ:="		, z0,
            "XAxisXvec:="		, "1cm",
            "XAxisYvec:="		, "0cm",
            "XAxisZvec:="		, "0cm",
            "YAxisXvec:="		, "0cm",
            "YAxisYvec:="		, "1cm",
            "YAxisZvec:="		, "0cm"
        ], 
        [
            "NAME:Attributes",
            "Name:="		, cordSysName
        ])
      
def setWorkingCoordniateSystem(oEditor, cordSysName='Global'):      
    oEditor.SetWCS(
        [
            "NAME:SetWCS Parameter",
            "Working Coordinate System:=", cordSysName,
            "RegionDepCSOk:="	, False
        ])
    
def changeGroupName(oEditor,oldName,newName):    
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Attributes",
                [
                    "NAME:PropServers", 
                    oldName
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Name",
                        "Value:="		, newName
                    ]
                ]
            ]
        ])    
    
def importStep3dModel(oEditor, fileName, filePath):
    # "C:\\Users\\kaleor\\Dropbox (University of Michigan)\\UMich\\Research\\Corn Stalk\\Corn Models\\DoY217_3_1_processed.step"
    oEditor.Import(
        [
            "NAME:NativeBodyParameters",
            "HealOption:="		, 0,
            "Options:="		, "-1",
            "FileType:="		, "UnRecognized",
            "MaxStitchTol:="	, -1,
            "ImportFreeSurfaces:="	, False,
            "GroupByAssembly:="	, False,
            "CreateGroup:="		, True,
            "STLFileUnit:="		, "Auto",
            "MergeFacesAngle:="	, 0.02,
            "HealSTL:="		, False,
            "ReduceSTL:="		, False,
            "ReduceMaxError:="	, 0,
            "ReducePercentage:="	, 100,
            "PointCoincidenceTol:="	, 1E-06,
            "CreateLightweightPart:=", False,
            "ImportMaterialNames:="	, False,
            "SeparateDisjointLumps:=", False,
            "SourceFile:="		, filePath + fileName         
        ])
        
def exportNetworkData(solModule,varStr, filePath, fileName):
    solModule.ExportNetworkData(varStr, ["Setup1:Sweep"], 3, filePath + fileName, 
    ["All"], False, 50, "S", -1, 0, 15, True, False, False)
        