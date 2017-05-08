#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

class x:
	#-- from step 1:
	all_crop_parameters_match_the_PRA_ones = True

	TOLERdrought = 0
	TOLERflood	= 0
	edible = []
	edible_Tmin = []
	edibleCropsID = {}
	edibleCropsEN = {}
	edibleCropsFR = {}
	edibleCropsDE = {}
	
	#-- from step 2:
	edibleCrops = {}
	edibleCropsPnD	= {}
	WRmargin_moy	= {}
	edibleCropsWR	= {}
	edibleCompanionCrops = {}
	CCedibility = {}	# dictionary from ASSESS_Water_CompanionCrop... with the different nutrients margins
						# ---> used if the selected Companion Crop needs more nutrients than the soil can provide.
	prodSURFACE = {}
	GSstart = 0
	# EndPreviousCrop = 0
	EndPreviousCrop_earlier = 0
	EndPreviousCrop_later = 0
	SelectedCrop =	None
	SelectedCC	=	None
	PreviouslySelectedCrop = None

	LimitingFactorReached = False

	decomposition_month = {}
	ActualStand = {}
	totalYields = {}
	YIELD = 0
	PestsDiseases_in_rotation = {}
	VERIFprodBOT	= {}

	rotation_length = {}
	rotat = {}

	TotalNutrients = {}
	NutrientsMargin = {}

	#-- from step 3: (cf Functions_step3)
	MinimumDailyIntakeAmount	= {}  # dict taking 15% of each Recommended Daily Intake Amount as the minimum Intake (acc. to European Union Comission)
	DailyResources = {}
	results = {}
