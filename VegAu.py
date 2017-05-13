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
#		IMPORTING EXTERNAL MODULES		#
#										#
#########################################

import os
import sys          # Used for AssetionErrors to get the line and file here the error comes from
import traceback    # Used for AssetionErrors to get the line and file here the error comes from

#########################################
#										#
#		CREATING THE SELF VARIABLES		#
# required by the next imported modules #
#										#
#########################################

from selfVariables import *
 
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
from inputFR import nutrition	# dictionary containing dietical properties of each crop from 'nutrition'

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts

from Functions_step1 import *	# Functions for the step1
from Functions_step2 import *	# Functions for the step2
from Functions_step3 import *	# Functions for the step3


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

	country		    =	sorted(data.environment.keys())
	database	    =	sorted(data.plants.keys())

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


					while x.all_crop_parameters_match_the_PRA_ones :

						x.all_crop_parameters_match_the_PRA_ones = True
						the_selected_crop_is_a_permanent_crop = prodCAT(crop) == 1 or prodCAT(
							crop) == 2  # fruit/nut tree (1), shrub (2)

						try :

							if the_selected_crop_is_a_permanent_crop:
								ASSESS_Tmin_germ_forFruits(x, crop, PRA)
							else:
								ASSESS_Tmin( crop, x, PRA)
							assert x.all_crop_parameters_match_the_PRA_ones

							#------------------------------------------------------

							ASSESS_sunshine(crop, PRA, x)
							assert x.all_crop_parameters_match_the_PRA_ones

							# ------------------------------------------------------

							# print("x.all_crop_parameters_match_the_PRA_ones = ",  x.all_crop_parameters_match_the_PRA_ones)
							assert x.all_crop_parameters_match_the_PRA_ones

							# ------------------------------------------------------

							ASSESS_Water( crop, PRA, x)
							# print("x.all_crop_parameters_match_the_PRA_ones = ",  x.all_crop_parameters_match_the_PRA_ones)
							assert x.all_crop_parameters_match_the_PRA_ones

							# ------------------------------------------------------

							ASSESS_pH(crop, PRA, x)

						except ValueError : # if there is a missing variable in the database
							pass
						except AssertionError:
							break

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

			print( "[{}]	There are {} edible crops for this PRA : {}.".format(PRA, len(x.edibleCropsID[PRA]), x.edibleCropsEN[PRA]) )

			#END for (pra in country)

	#=====================================================================================
	#== EXPORTING THE RESULTS OF THIS FIRST PART =========================================

	# === Enhancing the result's layout before saving ====
	# def GoodLookingDict(dict_name):
	# 	result_str = str(sorted(dict_name))
	# 	result = '],\n'.join(result_str.split('],'))
	# 	result = '},\n'.join(result.split('},'))
	# 	return result

	file_name = 'CropRepartition'
	print("Saving the results in  {} ...".format(file_name + '.py'))

	with open(file_name + '.py', 'w') as saves:
		saves.write("""CropRepartition_ID = {
""")
		# saves.write(GoodLookingDict(x.edibleCropsID))
		for entry in x.edibleCropsID:
			saves.write("""	'{}': {},
""".format(entry, x.edibleCropsID[entry]))
		saves.write("""	}
""")
		#------------------------------------------------------------------
		saves.write("""CropRepartition_EN = {
""")
		# saves.write(GoodLookingDict(x.edibleCropsEN))
		for entry in x.edibleCropsEN:
			saves.write("""	'{}': {},
""".format(entry, x.edibleCropsEN[entry]))
		saves.write("""	}
""")
		# ------------------------------------------------------------------
		saves.write("""CropRepartition_FR = {
""")
		# saves.write(GoodLookingDict(x.edibleCropsFR))
		for entry in x.edibleCropsFR:
			saves.write("""	'{}': {},
""".format(entry, x.edibleCropsFR[entry]))
		saves.write("""	}
""")
		# ------------------------------------------------------------------
		saves.write("""CropRepartition_DE = {
""")
		# saves.write(GoodLookingDict(x.edibleCropsDE))
		for entry in x.edibleCropsDE:
			saves.write("""	'{}': {},
""".format(entry, x.edibleCropsDE[entry]))
		saves.write("""	}
""")
		# ------------------------------------------------------------------
		saves.write("""prodSURFACE = {
""")
		# saves.write(GoodLookingDict(x.prodSURFACE))
		for entry in x.prodSURFACE:
			saves.write("""	'{}': {},
""".format(entry, x.prodSURFACE[entry]))
		saves.write("""	}
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


	country		=	sorted( [PRA for PRA in list(data.environment.keys()) if PRA != 'headers_full' and PRA != 'headers_ID'] )
	
	#===========================================================================
	#===========================================================================
	
	for PRAcursor, PRA in enumerate(country):

		print("""Building a rotation for the PRA {} [{}%]
					      """.format(PRA, round((PRAcursor / (len(environment))) * 100, 3)))

		#============================================================================
		#= Re-Setting up each variables for each PRA to start with the same variables

		x.PreviouslySelectedCrop = None
		x.SelectedCrop = None
		x.SelectedCC = None
		x.EndPreviousCrop_earlier = 3  # simulation begins in March
		x.EndPreviousCrop_later = 3  # simulation begins in March
		x.decomposition_month = {}
		x.edibleCrops = list(x.edibleCropsID[PRA])
		x.rotat[PRA] = [] # each tuple of 'rotat' gives the name of a crop with the last month of its Growing Season in the rotation
		x.edibleCropsWR	= {}	# dictionary that will assign each crop index to a Water Resources assessment index
		x.edibleCropsPnD	= {}	# dictionary that will assign each crop index to a Pest and Diseases assessment index

		x.NutrientsMargin = {}
		x.WRmargin_moy	= {}

		x.VERIFprodBOT = {}
		x.PestsDiseases_in_rotation = {}	# dictionary that will assign each crop index to x.YIELD depreciating index if it is  subject to Pest and Diseases risks.


		x.ActualStand[PRA] = {"N": nmin_med(PRA), "P": P_med(PRA), "K": K_med(PRA), "Na": nao_med(PRA), "Mg": mgo_med(PRA), "Ca": cao_med(PRA), "Mn": mned_med(PRA), "Fe": feed_med(PRA), "Cu": cued_med(PRA), "OM": corgox_med(PRA)}
		x.totalYields_year[PRA] = {}
		x.LimitingFactorReached = False
		x.no_delay_because_of_T_or_water = True

		#=========================================================================
		#= Preparing the dict x.decomposion_month :
		i = 1
		# to avoid an infinite number of months in the dict 'month', the loop stops automatically after 8 years (96 months):
		while i < 97:
			x.decomposition_month[i] = {}

			for nutrient in x.ActualStand[PRA].keys():
				x.decomposition_month[i][nutrient] = 0

			i += 1

		#=========================================================================

		the_selected_crop_is_a_permanent_crop = False
		x.edibleCompanionCrops	= []

		# =========================================================================
		# =========================================================================


		# while there is enough nutrients in the soil :
		while x.LimitingFactorReached == False or x.EndPreviousCrop_later <= 120 : # Simulation stops automatically after 10 years

			try:
				#=======================================================================================================

				if x.LimitingFactorReached == True:

					raise NoNutrients("Breaking the rotation --> Next PRA")

				x.no_delay_because_of_T_or_water = True

				# =======================================================================================================

				while x.no_delay_because_of_T_or_water == True :

					try:    # ---> assert x.LimitingFactorReached == False after the function ASSESS_Nutrients.
							# ---> assert x.EndPreviousCrop_Later >= 120 after the UPDATE function
							# The while loop seemed not to be enough...

						if x.PreviouslySelectedCrop != None :
							the_selected_crop_is_a_permanent_crop = prodCAT(x.PreviouslySelectedCrop) == 1  # fruit/nut tree, shrub
						else:
							pass
						# except KeyError:  # if there is no "Previously Selected Crop", VegAu has to proceed with the rotation simulation

						# =======================================================================================================
						# =======================================================================================================

						if the_selected_crop_is_a_permanent_crop:

							print("[{}][{}]	The Selected Crop is a permanent crop. Assessing crop impacts for the Current year (first month of the growing season = {})...".format(PRA, x.EndPreviousCrop_later, MonthID(x.GSstart)))

							#~ CROProw = CROProw_PLANTS(x.SelectedCrop)
							#~ CROPcol = CROPcol_PRAedibility(x.SelectedCrop)
							#~ CROPcol_yields = CROPcol_PRAyields(x.SelectedCrop)

							###########################
							# Assess Companion Crop ? #
							###########################

							x.edibleCrops=[x.PreviouslySelectedCrop]
							x.SelectedCrop = x.PreviouslySelectedCrop

							print("[{}][{}]	Simulating the Nutrients gain and removal...".format(PRA, x.EndPreviousCrop_later))
							ASSESS_Nutrients(x, PRA)

							if x.LimitingFactorReached == False:

								APPLY_SelectedCrop_Harvest(PRA, x)

								x.totalYields[x.SelectedCrop] += expYIELD(x.SelectedCrop) * x.WRmargin_moy[x.SelectedCrop]

								# =======================================================================================================
								# yet, we can update VERIFYprodBOT, x.GSstart and the cells from PRArotat by adding the prodID of the previously selected crop
								# from the seed_from(x.PreviouslySelectedCrop) to the seed_from(x.SelectedCrop) non inclusive:

								print("[{}][{}]	Updating x.GSstart and x.VERIFprodBOT...".format(PRA, x.EndPreviousCrop_later))

								# the SelectedCrop just never changes (tree --> permanent) : the next start
								# of its growing season will be one year later
								x.GSstart += 12

								UPDATE_EndPreviousCrop_rotat(PRA,x)
								# now, x.GSstart corresponds to the duration from the beginning of the rotation up to x.GSstart[x.SelectedCrop]

								print("[{}][{}]	GSstart = {}".format(PRA, x.EndPreviousCrop_later,x.GSstart))
								print("[{}][{}]	Updating x.VERIFprodBOT and x.PestsDiseases_in_rotation...".format(PRA, x.EndPreviousCrop_later))
								UPDATE_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x)

							else:
								raise NoNutrients

						# =======================================================================================================
						# =======================================================================================================

						else:
							x.edibleCrops = list(x.edibleCropsID[PRA])

							x.edibleCrops = [c for c in x.edibleCrops if c != 'CC-GRASSorchard'] # excluding orchard grass from edible crops
							x.GSstart = {} # key = prodID, value = first month of the potential growing season

							print("[{}][{}]	Looking for the Optimal Seeding Date... (edible crops are : {})".format(PRA, x.EndPreviousCrop_later, x.edibleCrops))

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

							if x.no_delay_because_of_T_or_water == True:

								print("""
	[{}][{}]	Checking the nutrient requirements for remaining crops...""". format(PRA, x.EndPreviousCrop_later))

								ASSESS_Nutrients(x, PRA)
								# after this function, we get:
								#	* an updated "x.edibleCrops' list
								#	* a x.NutrientsMargin dictionary with:
								#			*	keys = CROProw
								#			*	values = standardized nutrients margin

								if x.LimitingFactorReached == False:

									# -> All these intermediary functions helps to compare the remaining crops thanks an homogenized Index and the priority Indexes

									print("			Checking the pests and diseases risks for remaining crops... (edible crops are : {})". format(x.edibleCrops))

									ASSESS_PestDiseases(x, PRA)
									# returns an updated ediblePnD dictionary with, for each crop, an index according to the risks of pests and diseases
									# relative to a too short period between several crops of a same botanic family

									print("			Selecting the best crop for the {}th month of the Rotation ({})...".format(x.EndPreviousCrop_earlier, MonthID(x.EndPreviousCrop_earlier)))
									#
									# VERIF_lastCrops_not_CC(x, PRA, None)
									# if x.LimitingFactorReached == False:
									# 	raise


									SELECT_CashCrop(x, PRA, data)
									# This function selects the best crop according to the previously calculated indexes and the Priority indexes.


									UPDATE_EndPreviousCrop_rotat(PRA, x)


									print("[{}][{}]	It will mature until the {}th (earlier : {}) or the {}th (later : {}) month of the rotation.".
										  format(PRA, x.EndPreviousCrop_later, int(x.EndPreviousCrop_earlier), MonthID(x.EndPreviousCrop_earlier), x.EndPreviousCrop_later, MonthID(x.EndPreviousCrop_later) ))

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


								else:
									raise NoNutrients("Limiting Factor has been reached")

									# END if (x.LimitingFactorReached == False)

							else:
								# # updating the earlier and later dates for the begin of a new growing season with a later crop :
								# later_dates = [abs(seed_from(c) - x.EndPreviousCrop_later % 12) for c in
								#                x.edibleCropsID[PRA] if
								#                abs(seed_from(c) - x.EndPreviousCrop_later % 12) != 0]
								# delay = sorted(list(set(later_dates)))[0]
								#
								# x.EndPreviousCrop_earlier = x.EndPreviousCrop_later + delay
								# x.EndPreviousCrop_later = x.EndPreviousCrop_earlier + 2

								raise Delay("DELAY : no edible crops")

							# END if (x.no_delay_because_of_T_or_water == True)

 						#END if (the_selected_crop_is_a_permanent_crop)

						if x.EndPreviousCrop_later > 120:
							raise TenYears

					except Delay:
						print("DELAY : no edible crops")
						break
					except ColdSeason:
						print("DELAY : cold season")
						break
					except DrySeason:
						print("DELAY : dry season")
						break
					except NoNutrients:
						print("Not enough nutrients")
						break

			except LastCropsCC:
				print("STOP : last crops are only cover crops")
				break
			except TenYears:
				print("STOP : rotation over ten years")
				break
			except NoNutrients:
				print("Not enough nutrients")
				break

			if x.PreviouslySelectedCrop != None :
				# x.rotat[PRA].append((x.PreviouslySelectedCrop, x.SelectedCC, x.EndPreviousCrop_later))
				lastEntry = tuple(x.rotat[PRA][-1])
				del x.rotat[PRA][-1]
				x.rotat[PRA].append((x.PreviouslySelectedCrop, x.SelectedCC, x.EndPreviousCrop_later))
				x.rotat[PRA].append(lastEntry)


			# The following variable exists only to inform the user in the last print.
			rotation_crops = [crop for (crop, companion, last_month) in x.rotat[PRA] if (crop != 'start' and crop != 'Limiting factor' and 'delay' not in crop and 'season' not in crop)]

			if x.LimitingFactorReached == True :
				print("""
	[{}][{}]	END OF THE ROTATION : Nutrients are not sufficient (Limiting factor is {}).

	{} different crops out of {} succeeded until {}: {}

				""".format( PRA, x.EndPreviousCrop_later, x.rotat[PRA][-1][1], len(list(set(rotation_crops))), len(rotation_crops), MonthID(x.EndPreviousCrop_later), rotation_crops ))

			else:
				print("""
	[{}][{}]	END OF THE ROTATION : The rotation reached 10 years --> switching to next PRA

	{} different crops out of {} succeeded until {}: {}
								""".format(PRA, x.EndPreviousCrop_later, len(list(set(rotation_crops))) ,len(rotation_crops), MonthID(x.EndPreviousCrop_later),
				                           rotation_crops))

			x.rotation_length[PRA] = (x.EndPreviousCrop_later - 2)  # because it started in March


			average_rotation_duration = round(sum(x.rotation_length.values()) / len(x.rotation_length), 1)
			print("""At {}% of the database, the average rotation duration is of {} months ({} years)

			=============================================================================
			      """.format(round((PRAcursor/( len(country)) ) *100, 2), average_rotation_duration, round(average_rotation_duration/12, 1) ) )

			for crop in x.totalYields_year[PRA] :
				if x.rotation_length[PRA] <= 1 :
					x.totalYields_year[PRA][crop] = 0
				else :
					x.totalYields_year[PRA][crop] = round(x.totalYields_year[PRA][crop]/x.rotation_length[PRA], 3)

			permanent_crops = [c for c in rotation_crops if prodCAT(c) == 1]

			# Calculation of Limiting factors :
			x.LimitingFactor[PRA] = [i for i in x.rotat[PRA] if x.rotat[PRA][0] == 'Limiting factor']
			x.LimitingFactor[PRA] = list(set( [j for (i, j, k) in x.rotat[PRA] if j != None]))

			x.results[PRA] = [x.rotation_length[PRA], len(list(set(rotation_crops))) ,len(rotation_crops), list(set(rotation_crops)), rotation_crops, len(permanent_crops), permanent_crops, x.LimitingFactor[PRA]]

		# END for (pra in country)

	x.totalYields_year["TOTAL"] = {}

	for PRA in x.totalYields_year.keys():
		for crop in x.totalYields_year[PRA].keys():
			if 'CC' not in crop : # excuding Cover Crops from the total

				if crop not in x.totalYields_year["TOTAL"]:
					x.totalYields_year["TOTAL"][crop]  = x.totalYields_year[PRA][crop]
				else:
					x.totalYields_year["TOTAL"][crop] += x.totalYields_year[PRA][crop]

	x.totalYields_year = x.totalYields_year["TOTAL"]

	print("END STEP 2")




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
	#== Saving the results :

	x.results["headers"] = ["Rotation length", "Different crops in the rotation (amount)",
	                        "Total amount of crops in the rotation", "Different crops in the rotation (ID)",
	                        "Crops in the rotation (ID)", "Permanent crop ?", "Permanent crop ID",
	                        "Limiting Factor(s)"]

	with open('first_results.py', 'a') as saves:
		pass # makes sure that the file exists : if there is no file with this name, its creates it

	with open('first_results.py', 'w') as saves:
		saves.write("""results = {\n """)
		for entry in sorted(x.results.keys()):
			saves.write("""	'{}': {},\n """.format(entry, x.results[entry]))
	#-----------------------------------------------------------------------------------------------
	with open('first_results.csv', 'a') as saves:
		pass # makes sure that the file exists : if there is no file with this name, its creates it

	with open('first_results.csv', 'w') as saves:
		saves.write("'';"+";".join(x.results["headers"])+'\n')
		for entry in sorted(x.results.keys()):

			saves.write("	'{}'; {}\n".format( str(entry), str(";".join(x.results[entry])) ))


	#==================================================================================================================================
	### STEP 3
	
	print("""
				===================== STEP 3 =====================
		Calculating the average daily nutritional value per person for the total yield...""")


	ASSESS_FoodNutrients( x, nutrition )
	# --> It sums the nutrients and vitamins of all products in the appropriate variables (1 variable per nutritional feature)
	# of the dictionary 'TotalNutrients' (each key corresponds to a nutrient, vitamin or other dietetic feature)

	ASSESS_QTTperPERSON( x, nutrition )
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
		print("|	{}	|		{}		|  ".format(crop, round(x.DailyResources[crop], 2)))
	print("______________________________________________")
	
	#======================================================================================
	
	print("				_________________________________________________________________________")
	print("				|	Gender	|	Age class	|	Crop	|	% of BME	|	% of ANR/AS	|	% of AMT	|")
	print("__________________________________________________________________________________________")

	# ==================================================================================================================================
	#
	
	genders = [i for i in x.results.keys() if i == 'Nourrisson' or i == 'Enfants' or i == 'Femmes' or i == 'Hommes']
	
	for gender in genders:
		for age in x.results[gender].keys():
			for nutrient in x.results[gender][age].keys():
				print("|	{}	|	{}	|		{}		|		{}		|		{}		|		{}		|". format(nutrient, gender, age, x.results[gender][age][nutrient]['pctBME'], x.results[gender][age][nutrient]['pctANR_AS'], x.results[gender][age][nutrient]['pctAMT']))
	print("__________________________________________________________________________________________")

	with open('dietary_results.py', 'a') as saves:
		pass  # makes sure that the file exists : if there is no file with this name, its creates it
	
	with open('dietary_results.py', 'w') as saves:
		saves.write('results = { '+'\n')
		for entry in genders:
			saves.write(str(genders[entry]) +', \n')
	# -----------------------------------------------------------------------------------------------
	with open('dietary_results.csv', 'a') as saves:
		pass  # makes sure that the file exists : if there is no file with this name, its creates it
	
	with open('dietary_results.csv', 'w') as saves:
		saves.write("Crop ; Daily Product Amount/Person" + '\n')
		for crop in x.DailyResources.keys():
			saves.write("{};{} \n".format(crop, round(x.DailyResources[crop], 2)))

		saves.write( '\n' * 2 + ";".join(genders["headers"]) + '\n')
		for entry in genders:
			saves.write(";".join(genders[entry]) + '\n')

#Code's end
os.system("pause")# allows the window to stay open to see the results or eventual errors
