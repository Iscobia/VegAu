#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#########################################
#										#
#   		CUSTOM EXCEPTIONS       	#
#										#
#########################################

class Delay(Exception):
	pass

class ColdSeason(Exception):
	pass

class DrySeason(Exception):
	pass

class NoNutrients(Exception):
	pass

class TenYears(Exception):
	pass

class LastCropsCC(Exception):
	pass


#########################################
#										#
#		KEY OBJECTS OF THE PROGRAMM		#
#										#
#########################################

class x:
	#=======================================================
	#== COMMON VARIABLES:
	results = {}
	dietary_results = {}


	#=======================================================
	#== FROM STEP 1:
	all_crop_parameters_match_the_PRA_ones = True

	TOLERdrought = 0
	TOLERflood	= 0
	edible_Tmin = []
	edibleCropsID = {}
	edibleCropsEN = {}
	edibleCropsFR = {}
	edibleCropsDE = {}


	#=======================================================
	#== FROM STEP2:

	#-------------------------------------------------------
	#-- Selection variables :

	edibleCrops     = []
	edibleCrops_init = []
	edibleCompanionCrops = {}
	laterCrops      = {}
	# --------------------------------------
	indexDelay      = {}	# before : DelayIndex
	indexPnD	= {}	# before : edibleCropsPnD
	indexWR	= {}	# before : edibleCropsWR
	indexNutrients = {}	# before : NutrientsMargin
	# --------------------------------------
	CCwater = {}	# before : CCedibility. Dictionary from ASSESS_Water_CompanionCrop... with the different nutrients margins
					# ---> used if the selected Companion Crop needs more nutrients than the soil can provide.
	# --------------------------------------
	SelectedCrop = None
	SelectedCC = None
	PreviouslySelectedCrop = None


	# -------------------------------------------------------
	# -- Temporal variables
	GSstart = 0
	EndPreviousCrop_earlier = 0
	EndPreviousCrop_later = 0

	#-------------------------------------------------------
	#-- Analytical variables

	# Territorial  repartition
	prodSURFACE = {}
	ActualStand = {}
	mapsPreparation = {}

	# Limiting Factors (lack of nutrients, pests and diseases)
	LimitingFactor = {}
	LimitingFactor_crops = {}
	PestsDiseases_in_rotation = {}
	VERIFprodBOT = {}
	rotation_length = {}

	# Yields
	totalYields = {}

	# Rotations analysis
	rotat = {}
	representativity = {}
	CHOICE = {}
	# --> for each PRA, CHOICE must give back the **list** that has been chosen to chose the Selected Crop
	# It allow to see how the crops choice occurs.
	# The format of an occurence looks like : (dictionnary name, length of the dict)


	#-------------------------------------------------------
	#-- Coordination variables

	LimitingFactorReached = False
	no_delay_because_of_T_or_water = True
	decomposition_month = {}


	#=======================================================
	#== FROM STEP 3: (cf Functions_step3)
	TotalNutrients = {}
	WeeklyResources = {}

