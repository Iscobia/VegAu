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
	#~ WeeklyResources = {}
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


def MDL_EdibilityTest(x, data):
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

	country		    =	[pra for pra in sorted(data.environment.keys()) if pra != 'headers_full' and pra != 'headers_ID']
	database	    =	[crop for crop in sorted(data.plants.keys()) if crop != 'headers_full' and crop != 'IDXinit' and crop != 'headers_ID']

	#===========================================================================
	#===========================================================================

	for PRA in country:

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

					ASSESS_Tmin( crop, x, PRA)

					assert x.all_crop_parameters_match_the_PRA_ones

					#------------------------------------------------------

					ASSESS_Sunshine(crop, PRA, x)
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


		print("[{}]	There are {} edible crops for this PRA : {}.".format(PRA, len(x.edibleCropsID[PRA]),
																				x.edibleCropsEN[PRA]))
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
	
	# Saves in a Python file :
	
	print("Saving the results in  {} ...".format(file_name + '.py'))

	dicts = [("CropRepartition_ID", x.edibleCropsID), ("CropRepartition_EN", x.edibleCropsEN),
	         ("CropRepartition_FR", x.edibleCropsFR), ("CropRepartition_DE", x.edibleCropsDE), ("prodSURFACE", x.prodSURFACE)]

	with open(file_name + '.py', 'w') as saves:
		for i, d in enumerate(dicts) :
			saves.write("""{} = {}
""".format(dicts[i][0], "{"))
			for entry in dicts[i][1]:
				saves.write(""",\n	'{}': {}
""".format(entry, dicts[i][1][entry]))
			saves.write(""",\n	}
""")
		
	#====================================================================
	# Saves in a .csv file :

	print("Saving the results in  {} ...".format(file_name + '.csv'))

	with open(file_name + '.csv', 'w') as saves:
		saves.write("PRA; Edible crops (ID) ; Edible crops (EN); Edible crops (FR); Edible crops (DE) ; {}".format("; ".join(sorted(list(x.prodSURFACE.keys())))))

		for entry in sorted(x.edibleCropsID):

			saves.write("{}; {}; {}; {}; {}; {}\n".format(str(entry), ", ".join(x.edibleCropsID[entry]), ", ".join(x.edibleCropsEN[entry]),
			            ", ".join(x.edibleCropsFR[entry]), ", ".join(x.edibleCropsDE[entry]),
			            "; ".join([ str(len([ cr for cr in x.edibleCropsID[entry] if cr == c])) for c in sorted(list(x.prodSURFACE.keys())) if c in x.edibleCropsID[entry]])))

		# ------------------------------------------------------------------
		saves.write("{0}; {1}; {1}; {1}; {1}; {2}".format("Total potential surface (ha)", "-",
		                                            "; ".join( [ str(x.prodSURFACE[c]) for c in sorted(list(x.prodSURFACE.keys()))])))


	#=====================================================================================

	ASSESS_Priority(x, data)# assessing the priority indexes for each crop (PRIORITYgeneral(crop), PRIORITYfruits(crop), PRIORITYtextiles)
	# needs the x.prodSURFACE value to be copied in PRAedibility (cf previous function)
		

def MDL_Rotation(x, data):
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


	# country		=	sorted( [PRA for PRA in list(data.environment.keys()) if PRA != 'headers_full' and PRA != 'headers_ID'] )
	country = [PRA for PRA in list(data.environment.keys()) if PRA != 'headers_full' and PRA != 'headers_ID' and PRAsurface(PRA) >= 0 ]

	x.totalYields["TOTAL"] = {}

	#===========================================================================
	#===========================================================================
	
	for PRAcursor, PRA in enumerate(country):

		print("""Building a rotation for the PRA {} [{}%]
						  """.format(PRA, round(( (PRAcursor+1) / (len(environment))) * 100, 3)))

		#============================================================================
		#= Re-Setting up each variables for each PRA to start with the same variables

		x.CHOICE[PRA] = []

		x.PreviouslySelectedCrop = None
		x.SelectedCrop = None
		x.SelectedCC = None
		x.EndPreviousCrop_earlier = 3  # simulation begins in March
		x.EndPreviousCrop_later = 3  # simulation begins in March
		x.decomposition_month = {}
		x.edibleCrops = [c for c in x.edibleCropsID[PRA] if c != 'RBRB' and c != 'CC_GRASSorchard']
		x.edibleCompanionCrops = []
		x.rotat[PRA] = [] # each tuple of 'rotat' gives the name of a crop with the last month of its Growing Season in the rotation
		x.indexWR	= {}	# dictionary that will assign each crop index to a Water Resources assessment index
		x.indexPnD	= {}	# dictionary that will assign each crop index to a Pest and Diseases assessment index
		x.indexNutrients = {}

		x.LimitingFactor[PRA] = []
		x.VERIFprodBOT = {}
		x.PestsDiseases_in_rotation = {}	# dictionary that will assign each crop index to YIELD depreciating index if it is  subject to Pest and Diseases risks.


		x.ActualStand[PRA] = {"N": nmin_med(PRA), "P": P_med(PRA), "K": K_med(PRA), "Na": nao_med(PRA), "Mg": mgo_med(PRA), "Ca": cao_med(PRA), "Mn": mned_med(PRA), "Fe": feed_med(PRA), "Cu": cued_med(PRA), "OM": corgox_med(PRA)}
		x.totalYields[PRA] = {}
		x.LimitingFactorReached = False
		x.no_delay_because_of_T_or_water = True
		the_selected_crop_is_a_permanent_crop = False

		#=========================================================================
		#= Preparing the dict x.decomposion_month :
		i = 1
		# to avoid an infinite number of months in the dict 'month', the loop stops automatically after 8 years (96 months):
		while i < 97:
			x.decomposition_month[i] = {}

			for nutrient in x.ActualStand[PRA].keys():
				x.decomposition_month[i][nutrient] = 0

			i += 1


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


						if x.SelectedCrop != None:
							the_selected_crop_is_a_permanent_crop = prodCAT(x.SelectedCrop) == 1 or prodCAT(
								x.SelectedCrop) == 2  # fruit/nut tree, shrub

						if the_selected_crop_is_a_permanent_crop:

							print("[{}][{}]	The Selected Crop is a permanent crop. Assessing crop impacts for the Current year (first month of the growing season = {})...".format(PRA, x.EndPreviousCrop_later, MonthID(x.GSstart)))

							###########################
							# Assess Companion Crop ? #
							###########################

							x.edibleCrops=[x.SelectedCrop]

							print("[{}][{}]	Simulating the Nutrients gain and removal...".format(PRA, x.EndPreviousCrop_later))
							ASSESS_Nutrients(x, PRA)

							if x.LimitingFactorReached == False:

								APPLY_SelectedCrop_Harvest(PRA, x)

								# =======================================================================================================
								# yet, we can update VERIFYprodBOT, x.GSstart and the cells from PRArotat by adding the prodID of the previously selected crop
								# from the seed_from(x.PreviouslySelectedCrop) to the seed_from(x.SelectedCrop) non inclusive:

								print("[{}][{}]	Updating x.GSstart and x.VERIFprodBOT...".format(PRA, x.EndPreviousCrop_later))

								# the SelectedCrop just never changes (tree --> permanent) : the next start
								# of its growing season will be one year later
								x.GSstart += 12
								# now, x.GSstart corresponds to the duration from the beginning of the rotation up to x.GSstart[x.SelectedCrop]

								print("[{}][{}]	GSstart = {}".format(PRA, x.EndPreviousCrop_later,x.GSstart))
								print("[{}][{}]	Updating x.VERIFprodBOT and x.PestsDiseases_in_rotation...".format(PRA, x.EndPreviousCrop_later))

								UPDATE_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x)

								x.EndPreviousCrop_earlier += 12
								x.EndPreviousCrop_later += 12


							else:
								raise NoNutrients

						# =======================================================================================================
						# =======================================================================================================

						else:
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
							#		* an 'indexWR' dictionary with :
							#			*	keys = CROProw
							#			*	values = standardized "WaterResources evaluation" (WReval)

							if x.no_delay_because_of_T_or_water == True:

								print("""
[{}][{}]	Checking the nutrient requirements for remaining crops...""". format(PRA, x.EndPreviousCrop_later))

								ASSESS_Nutrients(x, PRA)
								# after this function, we get:
								#	* an updated "x.edibleCrops' list
								#	* a x.indexNutrients dictionary with:
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


			# END while (x.LimitingFactorReached == False or x.EndPreviousCrop_later <= 120)-------------------------

			# The following variable exists to inform the user in the last print AND for a x.results[PRA] entry.
			rotation_crops = [crop for (crop, companion, last_month) in x.rotat[PRA] if (
			crop != 'start' and crop != 'Limiting factor' and 'delay' not in crop and 'season' not in crop)]

			if x.LimitingFactorReached == True:
				print("""
[{}][{}]	END OF THE ROTATION : Nutrients are not sufficient (Limiting factor is {}).

{} different crops out of {} succeeded until {}: {}

					""".format(PRA, x.EndPreviousCrop_later, x.rotat[PRA][-1][1], len(list(set(rotation_crops))),
				               len(rotation_crops), MonthID(x.EndPreviousCrop_later), rotation_crops))

			elif x.EndPreviousCrop_later > 120:
				print("""
[{}][{}]	END OF THE ROTATION : The rotation reached 10 years --> switching to next PRA

{} different crops out of {} succeeded until {}: {}
									""".format(PRA, x.EndPreviousCrop_later, len(list(set(rotation_crops))),
				                               len(rotation_crops), MonthID(x.EndPreviousCrop_later),
				                               rotation_crops))
			else:
				print("""
[{}][{}]	END OF THE ROTATION : An error has been raised, the while loop is broken ("break")

{} different crops out of {} succeeded until {}: {}
													""".format(PRA, x.EndPreviousCrop_later,
				                                               len(list(set(rotation_crops))),
				                                               len(rotation_crops),
				                                               MonthID(x.EndPreviousCrop_later),
				                                               rotation_crops))

		x.rotation_length[PRA] = (x.EndPreviousCrop_later - 2)  # because it started in March


		average_rotation_duration = round(sum(x.rotation_length.values()) / len(x.rotation_length), 1)

		print("""At {}% of the database, the average rotation duration is of {} months ({} years)

		=============================================================================
			  """.format(round(((PRAcursor+1)/( len(country)) ) *100, 2), average_rotation_duration, round(average_rotation_duration/12, 1) ) )

		permanent_crops = [c for c in rotation_crops if (prodCAT(c) == 1 or prodCAT(c) == 2)]

		x.results[PRA]  = [x.rotation_length[PRA], len(list(set(rotation_crops))) ,len(rotation_crops), ", ".join(list(set(rotation_crops))), ", ".join(rotation_crops), len(permanent_crops), ", ".join(permanent_crops), ", ".join(x.LimitingFactor[PRA])]

		for crop in x.totalYields[PRA] :
			if x.rotation_length[PRA] > 0 :
				x.totalYields[PRA][crop] = round(x.totalYields[PRA][crop]/(x.rotation_length[PRA]/12), 3)

			if 'CC' not in crop : # excuding Cover Crops from the total
				if crop not in x.totalYields["TOTAL"].keys():
					x.totalYields["TOTAL"][crop]  = round(x.totalYields[PRA][crop], 3)
				else:
					x.totalYields["TOTAL"][crop] += round(x.totalYields[PRA][crop], 3)



		# END for (pra in country)-----------------------------------------------------------------------------------

	x.mapsPreparation = {'headers':[], 'totalYields' : []}

	for crop in sorted(x.totalYields["TOTAL"]):
		x.mapsPreparation['headers'].append("{} ({})".format(prod_EN(crop), crop))

		for PRA in country:

			if PRA not in x.mapsPreparation:
				x.mapsPreparation[PRA] = []

			x.mapsPreparation[PRA].append( len( [c for c in x.results[PRA][4] if c == crop] ) )

		x.mapsPreparation['totalYields'].append(x.totalYields["TOTAL"][crop])





if __name__ == '__main__' or __name__ != '__main__': # DEL " or __name__ != '__main__' " WHEN IT WORKS !!
	#==================================================================================================================================
	### STEP 1
	### creating the sheets for the edibility and yield assessment and importing the automatic columns creation + associated functions:
	
	print("""===================== STEP 1 =====================
	Assessing edible Crops for each PRA according to Environmental (Climate and Soil) Data and Biological Data""")

	# ²MDL_EdibilityTest(x, data) # complete function

	#---------------------------------------------------------------------------------------
	#-- FOR TESTS
	x.edibleCropsID = CropRepartition_ID
	x.edibleCropsEN = CropRepartition_EN
	x.edibleCropsFR = CropRepartition_FR
	x.edibleCropsDE = CropRepartition_DE
	x.prodSURFACE = prodSURFACE

	ASSESS_Priority(x, data)

	# ---------------------------------------------------------------------------------------

	print("""
				===================== STEP 2 =====================
	Building a typical Crop Rotation for each PRA according to Climate and Soil Data...""")
	#==================================================================================================================================
	### STEP 2
	### creating the sheets for the rotation calculation and importing the automatic columns creation + associated functions:
	
	MDL_Rotation(x, data)


	#==================================================================================================================================
	#== Saving the results :


	# ===============================================================================================
	# Exporting the results in a new python file                                                    #
	# ===============================================================================================

	x.results["headers"] = ["Rotation length", "Different crops in the rotation (amount)",
							"Total amount of crops in the rotation", "Different crops in the rotation (ID)",
							"Crops in the rotation (ID)", "Permanent crop ?", "Permanent crop ID",
							"Limiting Factor(s)"]

	#================================
	# Rotation analysis (x.results) #
	#================================

	# -----------------------------------------------------------------------------------------------
	# Exporting the results in a new python file
	fileName = 'results_RotationAnalysis'
	precision = '_1'

	with open('{}{}.py'.format(fileName, precision), 'a') as saves:
		pass # makes sure that the file exists : if there is no file with this name, its creates it

	with open('{}{}.py'.format(fileName, precision), 'w') as saves:
		saves.write("""results = {\n """)
		for entry in sorted(x.results.keys()):
		# for each PRA :
			saves.write("""	'{}': {},\n """.format(entry, x.results[entry]))
		saves.write("""	{}""".format('}'))

	#-----------------------------------------------------------------------------------------------
	# Exporting the results in two a .csv file (one with "x.results", and the other one for mapping):

	with open('{}{}.csv'.format(fileName, precision), 'a') as saves:
		pass # makes sure that the file exists : if there is no file with this name, its creates it


	with open('{}{}.csv'.format(fileName, precision), 'w') as saves:
		saves.write("'AoI'; " + "; ".join(x.results["headers"]) + '\n')
		for entry in sorted(x.results.keys()):
			saves.write("'{}'; {}\n".format(str(entry), str(
				"; ".join([str(v) for v in x.results[entry]]))))

	#===========================================#
	# Mapping informations (x.mapsPreparation)  #
	# ==========================================#

	fileName = "results_Mapping"
	# precision = "1"

	# -----------------------------------------------------------------------------------------------
	# Exporting the results in a .csv file :

	with open('{}{}.csv'.format(fileName, precision), 'a') as saves:
		pass  # makes sure that the file exists : if there is no file with this name, its creates it

	with open('{}{}.csv'.format(fileName, precision), 'w') as saves:
		saves.write("'AoI'; " + "; ".join(x.mapsPreparation["headers"])+'\n')
		for entry in sorted(x.results.keys()):

			saves.write("'{}'; {}\n".format( str(entry), str("; ".join([str(v) for v in x.mapsPreparation[entry]])) ))

		# Pour les yields de x.mapsPreparation :
		saves.write("'{}'; {}\n".format("total Yields", str(
			"; ".join(["-" for v in x.results["headers"]] + [str(v) for v in x.mapsPreparation['totalYields']]))))

	print("Saves done.")



	#==================================================================================================================================
	### STEP 3
	
	print("""
				===================== STEP 3 =====================
		Calculating the average daily nutritional value per person for the total yield...""")


	MDL_QTTperPERSON( x, nutrition )
	# This function updates the 'TotalNutrients' dictionary by dividing each nutrient amount by the total population
	# and copies the results in the sheet 'NUTRIassess' for each crop in order to keep a friendly interface to oberve the results.
	# OUTPUT:	* updated 'TotalNutrient' dictionnay with the average nutrient quantity per person
	# 			* fulfilled 'NUTRIassess' sheet
	#			* fulfilled 'Results' sheet
	
	
	#==================================================================================================================================
	### Exporting the data in a csv file


	NutrientsName = ['Ca', 'Cu', 'Fe', 'I', 'K', 'Mg', 'Mn', 'P', 'Proteins', 'Se', 'Zn', 'carbohydrates', 'lipids', 'vitA',
	             'vitB1', 'vitB12', 'vitB2', 'vitB3', 'vitB5', 'vitB6', 'vitB9', 'vitC', 'vitD']
	Percentages = ['pctBME', 'pctANR_AS', 'pctAMT']


	with open('dietary_results.csv', 'a') as saves:
		pass  # makes sure that the file exists : if there is no file with this name, its creates it
	
	with open('dietary_results.csv', 'w') as saves:
		saves.write('dietary_results = { '+'\n')

		#-------------------------------------------------------------
		# First, upper table with the nutrients percentages

		for nutrient in NutrientsName:
			saves.write("; ".join(x.dietary_results[nutrient]) +', \n')
			saves.write(" Global average ;" + "; ".join([ str(x.dietary_results[pct]) for pct in Percentages ]) + ', \n \n')

		# -------------------------------------------------------------
		# Second table with the daily amount of fruits and vegetables

		saves.write("Crop ; Daily Product Amount per Person ; Weekly Product Amount per Person" + '\n')
		for crop in x.WeeklyResources.keys():
			saves.write("{};{} \n".format(crop, round(x.WeeklyResources[crop], 2), round(x.WeeklyResources[crop]*7, 2)))



#Code's end
print("VegAu is done !")