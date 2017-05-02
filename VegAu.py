#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
"""VegAu is a programm to estimate the nutritional yield for a single place
up to a whole country in order to compare it with the Dietical requirement
of the population."""


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

print("Importing modules...")

#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

from inputFR import environment	# dictionnary containing all environmental data
from inputFR import plants		# dictionnary containing all data.plants (biological) data
from inputFR import nutrition	# dictionnary containing dietical properties of each crop from 'plants'

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
from math import ceil

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
	"""Fonction that tests if a PRA is edible or not to grow a crop.
	This function only works with the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	This function tests each crop of 'plants' according to the environmental data from 'environment'."""

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
			print("Edibility assessement for the PRA {}...".format(IDPRA(PRA)))

			for crop in database:
				if crop != 'headers_full' and crop != 'IDXinit' and crop != 'headers_ID':
					print("The current crop is :", crop)

					#=======================================================================================================================================
					# assessement fonctions

					the_selected_crop_is_a_permanent_crop = prodCAT(crop) == 1 or prodCAT(crop) == 2 # fruit/nut tree (1), shrub (2)
					all_crop_parameters_match_the_PRA_ones = True

					while all_crop_parameters_match_the_PRA_ones :

						try :

							if the_selected_crop_is_a_permanent_crop:
								ASSESS_Tmin_germ_forFruits(x, crop, PRA, all_crop_parameters_match_the_PRA_ones)
							else:
								ASSESS_Tmin( crop, x, PRA, all_crop_parameters_match_the_PRA_ones )
							ASSESS_Water( crop, PRA, x, all_crop_parameters_match_the_PRA_ones)
							ASSESS_pH(crop, PRA, x, all_crop_parameters_match_the_PRA_ones)

						except ValueError : # if there is a missing variable in the database
							pass

						print("""This crop is edible for the current PRA ! :D""")	# if the code runs till this line, the crop is edible
																					# because all_crop_parameters_match_the_PRA_ones == True
						print("prodID(crop) = ", prodID(crop), "prod_EN(crop) = ", prod_EN(crop))
						x.edibleCropsID[PRA].append(prodID(crop))
						x.edibleCropsEN[PRA].append(prod_EN(crop))
						x.edibleCropsFR[PRA].append(prod_FR(crop))
						x.edibleCropsDE[PRA].append(prod_DE(crop))

						print("Adding the PRA's surface to the 'prodSURFACE' dictionnary...")
						if crop not in x.prodSURFACE.keys():
							x.prodSURFACE[crop] = 0
						x.prodSURFACE[crop] += PRAsurface(PRA)
						print("	OK")
						# End of the edibility assessement for the current crop --> the loop's boolean is set to False :
						all_crop_parameters_match_the_PRA_ones = False
						print("all_crop_parameters_match_the_PRA_ones = ", all_crop_parameters_match_the_PRA_ones)

						# END while (all_crop_parameters_match_the_PRA_ones)

					#END for (crop in database)

			print( "	There are {} edible crops for this PRA.".format(len(x.edibleCropsID)) )

			#END for (pra in country)
		
		
		
	PriorityAssessement(x, data)# assessing the priority indexes for each crop (PRIORITYgeneral(crop), PRIORITYfruits(crop), PRIORITYtextiles)
	# needs the x.prodSURFACE value to be copied in PRAedibility (cf previous fonction)
		

def ASSESS_PRArotation(x, data):
	"""Fonction that creates an optimal rotation using crops wich
	have previously been selected as "edible".
	This function tests each crop of 'plants' according to the environmental
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

	
	x.RotatMonth = 3
	PreviouslySelectedCrop = None
	x.SelectedCrop = None
	x.SelectedCC = None
	x.EndPreviousCrop_earlier	= 3 # simulation begins in March
	x.EndPreviousCrop_later	= 3 # simulation begins in March
	x.ActualStand	=	{}
	month = {}
		
	country		=	data.environment.keys()
	database 	=	data.plants.keys()
	
	#===========================================================================
	#===========================================================================
	
	for PRA in country:
		if PRA != 'headers_full' and PRA != 'headers_ID':
			print("Building a rotation for PRA n°{}...".format(IDPRA(PRA)))
			#~ PRA = PRArow_ENVIRONMENT(pra)

			x.rotat[PRA] = []
			x.edibleCropsWR	= {}	# dictionnary that will assign each crop index to a Water Resources assessement index
			edibleCropsSN	= {}	# dictionnary that will assign each crop index to a Soil Nutrient assessement index
			x.edibleCropsPnD	= {}	# dictionnary that will assign each crop index to a Pest and Diseases assessement index
			x.WRmargin_moy	= {}

			x.VERIFprodBOT = {}
			PestsDiseases_in_rotation = {}	# dictionnary that will assign each crop index to YIELD depreciating index if it is  subject to Pest and Diseases risks.
			PestsDiseases_total = 0

			x.ActualStand[PRA] = {"N": nmin_med(PRA), "P": P_med(PRA), "K": K_med(PRA), "Na": nao_med(PRA), "Mg": mgo_med(PRA), "Ca": cao_med(PRA), "Mn": mned_med(PRA), "Fe": feed_med(PRA), "Cu": cued_med(PRA), "OM": corgox_med(PRA)}
			NutrientsSufficient = True  # taken into account in ASSESS_NutrientsMargin(crop, PRA, x)()
			the_selected_crop_is_a_permanent_crop = prodCAT(PreviouslySelectedCrop) == 1 # fruit/nut tree, shrub

			x.edibleCompanionCrops	= []

			while NutrientsSufficient :

				#===========================================================================

				if the_selected_crop_is_a_permanent_crop:

					print("The Selected Crop is a permanent crop. Assessing crop impacts for the Current year...")

					#~ CROProw = CROProw_PLANTS(x.SelectedCrop)
					#~ CROPcol = CROPcol_PRAedibility(x.SelectedCrop)
					#~ CROPcol_yields = CROPcol_PRAyields(x.SelectedCrop)

					###########################
					# Assess Companion Crop ? #
					###########################

					x.edibleCrops=[x.SelectedCrop]
					ASSESS_Nutrients(x)
					SelectedCrop_Harvest(PRA, x)
					x.totalYields[x.SelectedCrop] += expYIELD(x.SelectedCrop) * x.WRmargin_moy[x.SelectedCrop]
					print("	OK")


				#===========================================================================

				else:
					x.edibleCrops = list(x.edibleCropsID)
					x.GSstart = {} # key = CROProw, value = first month of the potential growing season

					# selecting the crops according to their planting date:
					FindOptimalSeedingDate(crop, PRA, x)
					# after this function, we have :
					#		* a list 'edibleCrops' with the index of every edible crop for this x.rotation's time according to the sawing/planting date.
					#		* a dictionnary 'GSstart' with: keys = crop's indexes, values = first GS month


					ASSESS_OptimalWaterResources(crop, PRA, x)
					# after this function, we get:
					#		* an updated "x.edibleCrops' list
					#		* an 'edibleCropsWR' dictionnary with :
					#			*	keys = CROProw
					#			*	values = standardized "WaterResources evaluation" (WReval)



					ASSESS_Nutrients(x)
					# after this function, we get:
					#	* an updated "x.edibleCrops' list
					#	* an 'edibleCropsSN' dictionnary ('SN' for 'Soil Nutrients') with:
					#			*	keys = CROProw
					#			*	values = standardized nutrients margin

					# -> All these intermediary functions helps to compare the remaining crops thanks an homogenized Index and the priority Indexes



					ASSESS_PestDiseases(crop, x)
					# returns an updated ediblePnD dictionnary with, for each crop, an index according to the risks of pests and diseases
					# relative to a too short period between several crops of a same botanic family


					x.SelectedCrop = SelectCrop(x)
					# This function selects the best crop according to the previously calculated indexes and the Priority indexes.
					CROProw = x.SelectedCrop # in case there are still some lost CROProw...
					CROPcol = x.SelectedCrop + 6
					CROPcol_yields = x.SelectedCrop + 2



					# indicating the earlier and the later month for the end of this crop for the next one:
					# this is calculated before the next crop to capture the GStot values of this crop and not the next one.
					x.EndPreviousCrop_earlier = int((x.RotatMonth + GSmin(x.SelectedCrop)) % 12)
					x.EndPreviousCrop_later	= ADAPT_EndGS_later(x)


					# assessing if there is possible to mix the x.SelectedCrop with a CompanionCrop
					ASSESS_Water_CompanionCrop_for_SelectedCrop(x)
					ASSESS_Nutrients_CompanionCrop_for_SelectedCrop(x)

					#------------------------------------------------------------------------

					YIELD =  expYIELD(x.SelectedCrop) * x.WRmargin_moy[x.SelectedCrop]	# adapt the yield proportionnaly to the Water Resources quality

					ASSESS_ResiduesDecomposition_of_PreviousCrops(crop, PRA, x)

					SelectedCC_Kill(PRA, x) # the selected Companion Crop is cut at the same time as the Selected Cash Crop is harvested
					SelectedCrop_Harvest(PRA, x)	# updates 'ActualStand'
											# /!\ CAUTION: if there is a x.SelectedCC, SelectedCC_Kill(PRA, x) modifies 'ActualStand' !
											#		----> SelectedCC_Kill(PRA, x) must run BEFORE SelectedCrop_Harvest(PRA, x) !!



					print("Calculating the yield for the Selected Crop...")
					YIELD *= x.edibleCropsPnD[x.SelectedCrop]	# adapt the yield proportionnaly to the Pests and Diseases risks.
					x.totalYields[x.SelectedCrop] += YIELD

					# Notice: Yields are in tons, not in t/ha anymore ! -> preparation for the assessement of the nutritional requirements


					# indicates the earlier and the later month for the end of this crop for the next one:
					# this is calculated before the next crop to capture the GStot values of this crop and not the next one.
					x.EndPreviousCrop_earlier = int((x.RotatMonth + GSmin(x.SelectedCrop)) % 12)
					x.EndPreviousCrop_later	= ADAPT_EndGS_later(x)


					#=======================================================================================================
					# Taking into account the WaterRequirement on the GS and the Next Crop -> adapting x.EndPreviousCrop_later

					print("Adapting the later selected crop's harvest date according to the PRA's water ressources...")

					month = int(x.RotatMonth)
					month_in_GS = ( month <= (x.GSstart[x.SelectedCrop] + GSmax(x.SelectedCrop)) )
					while month_in_GS: # same syntaxe as in the function ASSESS_OptimalWaterResources(crop, PRA, x)
						if ETc_GSmax(crop, month, x, PRA) * x.TOLERdrought(x.SelectedCrop) < WaterResources(month) < ETc_GSmax(crop, month, x, PRA) * x.TOLERflood(x.SelectedCrop):
							pass
						else:
							x.EndPreviousCrop_later = int(month)

					print("	OK")



					#=======================================================================================================
					# yet, we can update VERIFYprodBOT, x.RotatMonth and the cells from PRArotat by adding the prodID of the previously selected crop
					# from the seed_from(PreviouslySelectedCrop) to the seed_from(x.SelectedCrop) non inclusive:

					update_RotatMonth_and_VERIFprodBOT(x)
					# now, x.RotatMonth corresponds to the duration from the begining of the rotation up to x.GSstart[x.SelectedCrop]

					update_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x)
					# This function creates an entry in x.VERIFprodBOT for the newly selected crop if there is no one in the dictionnary
					# and verifies if the minimum return period is respected.
					# 		* If respected : no Pest and Diseases malus
					# 		* If not respected : +1 for this crop in the dict 'PestsDiseases_in_rotation'.
					# In both cases, the 'Duration since previous crop' returns to 0 (because it is yet the 'previous crop' for the potential next ones).()


					#Saving the x.SelectedCrop as "Previously Selected Crop" for the next loop:
					PreviouslySelectedCrop = int(x.SelectedCrop)

				#END while (Nutrient Sufficient)

			x.rotation_length[PRA] = (x.RotatMonth - 2) # because it started in March

			print("Switching to PRA {} (index {})".format(IDPRA(PRA), PRA))

			# END for (pra in country)
		
		
	average_rotation_duration = round(sum(x.rotation_length[PRA]) / len(x.rotation_length[PRA]), 1)
	
	print("The average x.rotation duration is of {} months ({} years)".format(average_rotation_duration, round(average_rotation_duration/12, 1) ) )



if __name__ == '__main__':
	#==================================================================================================================================
	### STEP 1
	### creating the sheets for the edibility and yield assessement and importing the automatic columns creation + associated functions:
	
	print("""===================== STEP 1 =====================
	Assessing edible Crops for each PRA according to Environmental (Climate and Soil) Data and Biological Data""")

	PRAedibilityTest(x, data)
	print("""
				===================== STEP 2 =====================
	Building a typical Crop Rotation for each PRA according to Climate and Soil Data...""")
	#==================================================================================================================================
	### STEP 2
	### creating the sheets for the rotation calculation and importing the automatic columns creation + associated functions:
	
	ASSESS_PRArotation(x, data)


	#==================================================================================================================================
	### STEP 3
	
	#~ print("""
				#~ ===================== STEP 3 =====================
		#~ Calculating the average daily nutritional value per person for the total yield...""")
	#~ 
	#~ 
	#~ ASSESS_FoodNutrients( x )
	#~ # --> It sums the nutrients and vitamins of all products in the appropriate variables (1 variable per nutritional feature)
	#~ # of the dictionnary 'TotalNutrients' (each key corresponds to a nutrient, vitamin or other dietetic feature)
	#~ 
	#~ ASSESS_QTTperPERSON( x )
	#~ # This function updates the 'TotalNutrients' dictionnary by dividing each nutrient amount by the total population
	#~ # and copies the results in the sheet 'NUTRIassess' for each crop in order to keep a friendly interface to oberve the results.
	#~ # OUTPUT:	* updated 'TotalNutrient' dictionnay with the average nutrient quantity per person 
	#~ # 			* fulfilled 'NUTRIassess' sheet
	#~ #			* fulfilled 'Results' sheet
	
	
	#==================================================================================================================================
	### Exporting the data in 'output.ods'
	
	#~ import exporting_in_ODS
	
	
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
#~ from os import *
#~ os.system("pause")# allows the window to stay open to see the results or eventual errors
