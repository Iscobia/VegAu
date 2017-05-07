#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
"""VegAu is a program to estimate the nutritional yield for a single place
up to a whole country in order to compare it with the Dietical requirement
of the population.

ATTENTION :
This program only works with the imported version of the original file
"inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
The import of this sheet is ensured by the module 'importingODS.py'"""


#########################################
#										#
#		CREATING THE SELF VARIABLES		#
# required by the next imported modules #
#										#
#########################################

from selfVariables import x
 
# if I define the x values here, I risk a circular import error because:
# in VegAu: 				from Functions_step3 import *
# and in Functions_step3:	from VegAu import x

#~ 
	#~ #-- from step 3: (cf Functions_step3)
	#~ RecommendedDailyIntakeAmount = {} # dict with all nutritional feature for which there is a Recommended Daily Intake Amount 
	#~ MinimumDailyIntakeAmount	= {}  # dict taking 15% of each Recommended Daily Intake Amount as the minimum Intake (acc. to European Union Comission)
	#~ DailyResources = {}
	#~ results = {}

#============================
#== For the tests :
from CropRepartition import *
print("Importing modules...")

#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

from inputFR import environment	# dictionary containing all environmental data
from inputFR import plants		# dictionary containing all data.plants (biological) data
from inputFR import nutrition	# dictionary containing dietical properties of each crop from 'plants'

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts

from Functions_step1 import *	# Functions for the step1
from Functions_step2 import *	# Functions for the step2
#~ from Functions_step3 import *	# Functions for the step3


#########################################
#										#
#		IMPORTING EXTERNAL MODULES		#
#										#
#########################################

#~ import os

print("	OK")


#==================================================================================================================================

### importing the data from inputFR.ods (or another file with the same layout) into inputFR.py:
#~ print("Importing the data from 'inputFR.ods'...")
#~ from importingODS import * # importing the dictionnaries that correspond to the inputFR's spreadsheets


#########################################
#										#
#	FUNCTIONS AND VARIABLES DEFINITION	#
#										#
#########################################

class data:
	environment = environment
	plants = plants


def PRAedibilityTest(x, data):
	"""INPUT :
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	data	is the class that contains the original 'plants' and 'environment' data bases
				from 'input[COUNTRY].py' (e.g. 'inputFR.py' for France).
	AIM :
	Testing if a PRA is edible or not to grow a crop.
	This function tests each crop of 'plants' according to the environmental data from 'environment'.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'
	"""

	country		=	sorted(data.environment.keys())
	database	=	sorted(data.plants.keys())


	#===========================================================================
	#===========================================================================

	for PRA in country:
		if PRA != 'headers_full' and PRA != 'headers_ID':
			# =======================================================================================================================================
			# creating new edibility lists for the current PRA
			x.edibleCropsID[PRA] = []
			x.edibleCropsEN[PRA] = []
			x.edibleCropsFR[PRA] = []
			x.edibleCropsDE[PRA] = []
			x.ActualStand[PRA] = {"N": nmin_med(PRA), "P": P_med(PRA), "K": K_med(PRA), "Na": nao_med(PRA),
								  "Mg": mgo_med(PRA), "Ca": cao_med(PRA), "Mn": mned_med(PRA), "Fe": feed_med(PRA),
								  "Cu": cued_med(PRA), "OM": corgox_med(PRA)}
			print("Edibility assessment for the PRA {}...".format(IDPRA(PRA)))

			for crop in database:
				if crop != 'headers_full' and crop != 'IDXinit' and crop != 'headers_ID':
					#print("""--------------------------
					#The current crop is :""", crop)

					#=======================================================================================================================================
					# assessment functions
					x.all_crop_parameters_match_the_PRA_ones = True
					the_selected_crop_is_a_permanent_crop = prodCAT(crop) == 1 or prodCAT(crop) == 2 # fruit/nut tree (1), shrub (2)

					while x.all_crop_parameters_match_the_PRA_ones :

						try :

							if the_selected_crop_is_a_permanent_crop:
								ASSESS_Tmin_germ_forFruits(x, crop, PRA)
							else:
								ASSESS_Tmin( crop, x, PRA)

							# print("x.all_crop_parameters_match_the_PRA_ones = ",  x.all_crop_parameters_match_the_PRA_ones)
							if not x.all_crop_parameters_match_the_PRA_ones :
								break

							ASSESS_Water( crop, PRA, x)
							# print("x.all_crop_parameters_match_the_PRA_ones = ",  x.all_crop_parameters_match_the_PRA_ones)
							if not x.all_crop_parameters_match_the_PRA_ones :
								break
							ASSESS_pH(crop, PRA, x)

						except ValueError : # if there is a missing variable in the database
							pass

						# print("""This crop is edible for the current PRA ! :D""")	# if the code runs till this line, the crop is edible
																					# because x.all_crop_parameters_match_the_PRA_ones == True
						# print("prodID(crop) = ", prodID(crop), "========== prod_EN(crop) = ", prod_EN(crop))
						x.edibleCropsID[PRA].append(prodID(crop))
						x.edibleCropsEN[PRA].append(prod_EN(crop))
						x.edibleCropsFR[PRA].append(prod_FR(crop))
						x.edibleCropsDE[PRA].append(prod_DE(crop))

						# print("Adding the PRA's surface to the 'prodSURFACE' dictionary...")
						if crop not in x.prodSURFACE.keys():
							x.prodSURFACE[crop] = 0
						x.prodSURFACE[crop] += PRAsurface(PRA)
						# print("	OK")
						# End of the edibility assessment for the current crop --> the loop's boolean is set to False :
						x.all_crop_parameters_match_the_PRA_ones = False

						# print("x.all_crop_parameters_match_the_PRA_ones = ", x.all_crop_parameters_match_the_PRA_ones)

						# END while (x.all_crop_parameters_match_the_PRA_ones)

					#END for (crop in database)

			print( "	There are {} edible crops for this PRA : {}.".format(len(x.edibleCropsID[PRA]), x.edibleCropsEN[PRA]) )

			#END for (pra in country)

	#=====================================================================================
	#== EXPORTING THE RESULTS OF THIS FIRST PART =========================================

	# === Enhancing the result's layout before saving ====
	def GoodLookingDict(dict_name):
		result_str = str(sorted(dict_name))
		result = '],\n'.join(result_str.split('],'))
		result = '},\n'.join(result.split('},'))
		return result

	file_name = 'CropRepartition'
	print("Saving the results in  {} ...".format(file_name + '.py'))

	with open(file_name + '.py', 'w') as saves:
		saves.write("CropRepartition_ID = ")
		saves.write(GoodLookingDict(x.edibleCropsID))
		saves.write("""
		""")
		saves.write("CropRepartition_EN = ")
		saves.write(GoodLookingDict(x.edibleCropsEN))
		saves.write("""
		""")
		saves.write("CropRepartition_FR = ")
		saves.write(GoodLookingDict(x.edibleCropsFR))
		saves.write("""
		""")
		saves.write("CropRepartition_DE = ")
		saves.write(GoodLookingDict(x.edibleCropsDE))
		saves.write("""
		""")
		saves.write("prodSURFACE = ")
		saves.write(GoodLookingDict(x.prodSURFACE))

	print("""	OK

	""")


	#=====================================================================================

	PriorityAssessement(x, data)# assessing the priority indexes for each crop (PRIORITYgeneral(crop), PRIORITYfruits(crop), PRIORITYtextiles)
	# needs the x.prodSURFACE value to be copied in PRAedibility (cf previous function)
		

def ASSESS_PRArotation(x, data):
	"""INPUT :
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	data	is the class that contains the original 'plants' and 'environment' data bases
				from 'input[COUNTRY].py' (e.g. 'inputFR.py' for France).

	AIM :
	This function creates an optimal rotation using crops which
	have previously been selected as "edible".
	It tests each crop of 'plants' according to the environmental
	data from 'environment'.
	
	---------------------------------
	
	OUTPUTS :
	*	x.rotat associates a rotation to each PRA. A new crop is
		selected for the rotation until there is not enough nutrient
		anymore to feed one of the 'edibleCrops'
	*	for each crop, gives a totalYields value for whole France:
		these yields are used for the Nutritional Feasibility (last step)
	
	---------------------------------

	NOTICE: Yields take the quality of Water Resources and
			Pests and Diseases into account.
	"""
	#~ from Functions_step2 import *

	x.PreviouslySelectedCrop = None
	x.SelectedCrop = None
	x.SelectedCC = None
	x.EndPreviousCrop_earlier	= 3 # simulation begins in March
	x.EndPreviousCrop_later	= 3 # simulation begins in March
	x.ActualStand	=	{}
	decomposition_month = {}
		
	country		=	sorted(data.environment.keys())
	
	#===========================================================================
	#===========================================================================
	
	for PRA in country:
		if PRA != 'headers_full' and PRA != 'headers_ID':
			print("Building a rotation for PRA n°{}...".format(IDPRA(PRA)))

			#=========================================================================
			#= Setting up each variable

			x.edibleCrops = list(x.edibleCropsID[PRA])
			x.rotat[PRA] = [('start', 3)] # each tuple of 'rotat' gives the name of a crop with the last month of its Growing Season in the rotation
			x.edibleCropsWR	= {}	# dictionary that will assign each crop index to a Water Resources assessment index
			x.edibleCropsPnD	= {}	# dictionary that will assign each crop index to a Pest and Diseases assessment index
			# x.edibleCropsSN	= {}	# dictionary that will assign each crop index to a Soil Nutrient assessment index
										#  REPLACED BY x.NutrientsMargins (it was the same)
			x.NutrientsMargin = {}
			x.WRmargin_moy	= {}

			x.VERIFprodBOT = {}
			PestsDiseases_in_rotation = {}	# dictionary that will assign each crop index to x.YIELD depreciating index if it is  subject to Pest and Diseases risks.
			PestsDiseases_total = 0


			x.ActualStand[PRA] = {"N": nmin_med(PRA), "P": P_med(PRA), "K": K_med(PRA), "Na": nao_med(PRA), "Mg": mgo_med(PRA), "Ca": cao_med(PRA), "Mn": mned_med(PRA), "Fe": feed_med(PRA), "Cu": cued_med(PRA), "OM": corgox_med(PRA)}
			NutrientsSufficient = True  # taken into account in ASSESS_NutrientsMargin(crop, PRA, x)()

			#=========================================================================
			#= Preparing the dict x.decomposion_month :

			i = 1
			# to avoid an infinite number of months in the dict 'month', the loop stops automatically after 8 years (96 months):
			while i < 97:
				x.decomposition_month[i] = {}

				for nutrient in x.ActualStand[PRA]:
					x.decomposition_month[i][nutrient] = 0

				i += 1

			#=========================================================================


			try :
				the_selected_crop_is_a_permanent_crop = prodCAT(x.PreviouslySelectedCrop) == 1 # fruit/nut tree, shrub
			except KeyError: # if there is no "Previously Selected Crop", VegAu has to proceed with the rotation simulation
				the_selected_crop_is_a_permanent_crop = False
			x.edibleCompanionCrops	= []

			while NutrientsSufficient :

				x.edibleCrops = list(x.edibleCropsID[PRA])
				
				# =======================================================================================================
				# =======================================================================================================

				if the_selected_crop_is_a_permanent_crop:

					print("The Selected Crop is a permanent crop. Assessing crop impacts for the Current year (first month of the growing season = {})...".format(MonthID(x.GSstart)))

					#~ CROProw = CROProw_PLANTS(x.SelectedCrop)
					#~ CROPcol = CROPcol_PRAedibility(x.SelectedCrop)
					#~ CROPcol_yields = CROPcol_PRAyields(x.SelectedCrop)

					###########################
					# Assess Companion Crop ? #
					###########################

					x.edibleCrops=[x.SelectedCrop]

					print("Simulating the Nutrients gain and removal...")
					ASSESS_Nutrients(x, PRA)
					SelectedCrop_Harvest(PRA, x)
					
					x.totalYields[x.SelectedCrop] += expYIELD(x.SelectedCrop) * x.WRmargin_moy[x.SelectedCrop]

					# =======================================================================================================
					# yet, we can update VERIFYprodBOT, x.GSstart and the cells from PRArotat by adding the prodID of the previously selected crop
					# from the seed_from(x.PreviouslySelectedCrop) to the seed_from(x.SelectedCrop) non inclusive:

					print("Updating x.GSstart and x.VERIFprodBOT...")
					
					# the SelectedCrop just never changes (tree --> permanent) : the next start
					# of its growing season will be one year later
					x.GSstart += 12 

					UPDATE_EndPreviousCrop_rotat(x)
					# now, x.GSstart corresponds to the duration from the beginning of the rotation up to x.GSstart[x.SelectedCrop]

					print("GSstart = ", x.GSstart)
					print("Updating x.VERIFprodBOT and PestsDiseases_in_rotation...")
					UPDATE_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x)
					print("	OK")


				# =======================================================================================================
				# =======================================================================================================
				
				else:
					try:
						assert type(x.decomposition_month[95]) == dict
						x.GSstart = {} # key = prodID, value = first month of the potential growing season

						print("Looking for the Optimal Seeding Date... (edible crops are : {})". format(x.edibleCrops))

						# selecting the crops according to their planting date:
						ASSESS_SeedingDate(PRA, x)
						# after this function, we have :
						#		* a list 'edibleCrops' with the index of every edible crop for this x.rotation's time according to the sawing/planting date.
						#		* a dictionary 'GSstart' with: keys = crop's indexes, values = first GS month

						# print("Looking for the optimal Water Resources... (edible crops are : {})". format(x.edibleCrops))

						ASSESS_WaterResources(PRA, x)
						# after this function, we get:
						#		* an updated "x.edibleCrops' list
						#		* an 'edibleCropsWR' dictionary with :
						#			*	keys = CROProw
						#			*	values = standardized "WaterResources evaluation" (WReval)

						print("Checking the nutrient requirements for remaining crops... (edible crops are : {})". format(x.edibleCrops))

						ASSESS_Nutrients(x, PRA)
						# after this function, we get:
						#	* an updated "x.edibleCrops' list
						#	* a x.NutrientsMargin dictionary with:
						#			*	keys = CROProw
						#			*	values = standardized nutrients margin

						# -> All these intermediary functions helps to compare the remaining crops thanks an homogenized Index and the priority Indexes

						print("Checking the pests and diseases risks for remaining crops... (edible crops are : {})". format(x.edibleCrops))

						ASSESS_PestDiseases(x)
						# returns an updated ediblePnD dictionary with, for each crop, an index according to the risks of pests and diseases
						# relative to a too short period between several crops of a same botanic family

						print("Selecting the best crop for the {}th month of the Rotation ({})...".format(x.EndPreviousCrop_earlier, MonthID(x.EndPreviousCrop_earlier)))

						SELECT_CashCrop(x, PRA)
						# This function selects the best crop according to the previously calculated indexes and the Priority indexes.


						UPDATE_EndPreviousCrop_rotat(PRA, x)

						print("It will mature until the {}th (earlier : {}) or the {}th (later : {}) month of the rotation.".
							  format(x.EndPreviousCrop_earlier, MonthID(x.EndPreviousCrop_earlier), x.EndPreviousCrop_later, MonthID(x.EndPreviousCrop_later) ))

						# assessing if there is possible to mix the x.SelectedCrop with a CompanionCrop
						SELECT_CompanionCrop(x, PRA)


						#------------------------------------------------------------------------

						APPLY_ResiduesDecomposition_of_PreviousCrops(PRA, x)

						APPLY_SelectedCC_Kill(PRA, x) # the selected Companion Crop is cut at the same time as the Selected Cash Crop is harvested
						APPLY_SelectedCrop_Harvest(PRA, x)	# updates 'ActualStand'
												# /!\ CAUTION: if there is a x.SelectedCC, SelectedCC_Kill(PRA, x) modifies 'ActualStand' !
												#		----> SelectedCC_Kill(PRA, x) must run BEFORE SelectedCrop_Harvest(PRA, x) !!


						UPDATE_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x)
						# This function creates an entry in x.VERIFprodBOT for the newly selected crop if there is no one in the dictionary
						# and verifies if the minimum return period is respected.
						# 		* If respected : no Pest and Diseases malus
						# 		* If not respected : +1 for this crop in the dict 'PestsDiseases_in_rotation'.
						# In both cases, the 'Duration since previous crop' returns to 0 (because it is yet the 'previous crop' for the potential next ones).()


						#Saving the x.SelectedCrop as "Previously Selected Crop" for the next loop:
						x.PreviouslySelectedCrop = str(x.SelectedCrop)

					#END while (Nutrient Sufficient)

					except AssertionError:
						print("""

						STOP !!! THE TYPE OF THE LAST ENTRIES OF x.decomposition_month HAS CHANGED !!!

						""")
						import sys
						sys.exit()

			x.rotation_length[PRA] = (x.GSstart - 2) # because it started in March

			print("Switching to PRA {} (index {})".format(IDPRA(PRA), PRA))

			# END for (pra in country)
		
		
	average_rotation_duration = round(sum(x.rotation_length[PRA]) / len(x.rotation_length[PRA]), 1)
	
	print("The average x.rotation duration is of {} months ({} years)".format(average_rotation_duration, round(average_rotation_duration/12, 1) ) )



if __name__ == '__main__' or __name__ != '__main__': # DEL " or __name__ != '__main__' " WHEN IT WORKS !!
	#==================================================================================================================================
	### STEP 1
	### creating the sheets for the edibility and yield assessment and importing the automatic columns creation + associated functions:
	
	print("""===================== STEP 1 =====================
	Assessing edible Crops for each PRA according to Environmental (Climate and Soil) Data and Biological Data""")

	# PRAedibilityTest(x, data) # complete function

	#----------------------------
	#-- Function for test
	x.edibleCropsID = CropRepartition_ID
	x.edibleCropsEN = CropRepartition_EN
	x.edibleCropsFR = CropRepartition_FR
	x.edibleCropsDE = CropRepartition_DE
	x.prodSURFACE = prodSURFACE

	PriorityAssessement(x, data)

	print("""
				===================== STEP 2 =====================
	Building a typical Crop Rotation for each PRA according to Climate and Soil Data...""")
	#==================================================================================================================================
	### STEP 2
	### creating the sheets for the rotation calculation and importing the automatic columns creation + associated functions:
	
	ASSESS_PRArotation(x, data)


	#==================================================================================================================================
	### STEP 3
	
	print("""
				===================== STEP 3 =====================
		Calculating the average daily nutritional value per person for the total yield...""")


	ASSESS_FoodNutrients( x )
	# --> It sums the nutrients and vitamins of all products in the appropriate variables (1 variable per nutritional feature)
	# of the dictionary 'TotalNutrients' (each key corresponds to a nutrient, vitamin or other dietetic feature)

	ASSESS_QTTperPERSON( x )
	# This function updates the 'TotalNutrients' dictionary by dividing each nutrient amount by the total population
	# and copies the results in the sheet 'NUTRIassess' for each crop in order to keep a friendly interface to oberve the results.
	# OUTPUT:	* updated 'TotalNutrient' dictionnay with the average nutrient quantity per person
	# 			* fulfilled 'NUTRIassess' sheet
	#			* fulfilled 'Results' sheet
	
	
	#==================================================================================================================================
	### Exporting the data in 'output.ods'
	
	import exporting_in_ODS
	
	
	#==================================================================================================================================
	### Showing the results on the screen:
	print("______________________________________________")
	print("|	Crop	|	Daily Product Amount/Person	|")
	
	for crop in x.DailyResources.keys():
		print("|	crop	|		round(x.DailyResources[crop], 2)		|  ")
	print("______________________________________________")
	
	#======================================================================================
	
	print("					_________________________________________________________________________")
	print("					|	Gender	|	Age class	|	Crop	|	% of BME	|	% of ANR/AS	|	% of AMT	|")
	print("__________________________________________________________________________________________")
	
	for gender in x.results.keys():
		for age in x.results['gender'].keys():
			for nutrient in x.results['gender']['age'].keys():
				print("|	{}	|	{}	|		{}		|		{}		|		{}		|		{}		|". format(nutrient, gender, age, x.results[gender][age][nutrient]['pctBME'], x.results[gender][age][nutrient]['pctANR_AS'], x.results[gender][age][nutrient]['pctAMT']))
	print("__________________________________________________________________________________________")

#Code's end
import os
os.system("pause")# allows the window to stay open to see the results or eventual errors
