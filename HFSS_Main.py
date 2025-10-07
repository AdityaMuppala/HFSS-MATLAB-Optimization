import os
import sys
installPath = "C:\Program Files\AnsysEM\\v221\Win64" # Location of HFSS installation
pluginLoc = "C:\Program Files\AnsysEM\\v221\Win64\PythonFiles\DesktopPlugin" # Location of ScriptEnv.py file
sys.path.append(installPath)
sys.path.append(pluginLoc)
import ScriptEnv
import csv
import HfssScriptUtil as hfss

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("USlotPatch_Trial")
oDesign = oProject.SetActiveDesign("Xband_Uslot_Patch_original")
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
					"NAME:SlotW",
					"Value:="		, sys.argv[1] + "mm"
				]
			]
		]
	])
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
					"NAME:SlotL",
					"Value:="		, sys.argv[2] + "mm"
				]
			]
		]
	])
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
					"NAME:SlotY",
					"Value:="		, sys.argv[3] + "mm"
				]
			]
		]
	])
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
					"NAME:SlotThickness",
					"Value:="		, sys.argv[4] + "mm"
				]
			]
		]
	])
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
					"NAME:PatchW",
					"Value:="		, sys.argv[5] + "mm"
				]
			]
		]
	])
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
					"NAME:PatchL",
					"Value:="		, sys.argv[6] + "mm"
				]
			]
		]
	])
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
					"NAME:FeedY",
					"Value:="		, sys.argv[7] + "mm"
				]
			]
		]
	])
oProject.Save()
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("SParams", "C:/Users/mavarma/Dropbox (University of Michigan)/YOUTUBE Tutorials/AntennasAndArrays 01 - U Slot Patch Antenna/MATLAB_Codes_Trial/S11.csv", False)
oDesign.DeleteFullVariation("All", False)


