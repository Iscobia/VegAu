#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
""" Module containing the functions for :
VegAu, STEP1: Assessing edible Crops for each PRA according to Environmental (Climate and Soil) Data and Biological Data

ATTENTION :
This program only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
The import of this sheet is ensured by the module 'importingODS.py'"""


#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

# importing databases :
from inputFR import environment
from inputFR import plants

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts

#########################################
#										#
#			SECUNDARY FUNCTIONS			#
#										#
#########################################

#================================================================================================================

def WaterResources(month, PRA):
	return Ptot(month, PRA)


def CORRseed_to(crop):
	"""INPUT:
	crop is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.

	FUNCTION:
	Makes sure that seed_from(crop) < seed_to(crop) in case of a seeding period in winter.
	"""

	if seed_from(crop) < seed_to(crop):
		return seed_to(crop) + 12


#================================================================================================================

def GSmax_for_CurrentCrop(crop):
	"""INPUT:
	crop is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.

	FUNCTION:
	Setting up the longest growing season possibility (GSmax(crop)) for the current crop.
	Gives the amounts of months from seed_from(crop) to seed_to(crop)."""


	#================================================================================================================
	#~ Note : fonction corrigée le 19 mars 2017 en supprimant les globales et en ajoutant CORRseed_to(crop)		#
	#~ Une partie de la fonction a été supprimée parce que jugée inutile -> reprendre l'ancienne en cas de bugs		#
	#================================================================================================================


	seed_to = CORRseed_to(crop) # seed_to > seed_from

	if seed_to == seed_from(crop):
		seedingTime = 1 # it can mean that seed_from is early in the month and seed_to at the end of the month
	else:
		seedingTime = seed_to - seed_from(crop) + 1 # + 1 because the 'seed_from(crop)'-month in included in the seeding time duration
	GSmax_crop = seedingTime+GSmax(crop)
	return int(GSmax_crop)



def CORR_TOLERdf(crop, x):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.

	FUNCTION:
	Converts the 'TOLERdrought(crop)' and 'TOLERflood(crop)' indexes into percentages of the ETC
	"""

	#=======================================================================
    #=== Converting the "Tolerance to Drought" index to a percentage of ETc
	if TOLERdrought(crop) == 10:
		x.TOLERdrought = 0.10
	elif TOLERdrought(crop) == 9:
		x.TOLERdrought = 0.15
	else:
		x.TOLERdrought = (10 - TOLERdrought(crop)) / 10 # for instance, if TOLERdrought(crop) index = 8, we assume that the crop needs at least 20% of its ETc to grow.



	#======================================================================
    #=== Converting the "Tolerance to Flood" intex to a percentage of ETc
	x.TOLERflood = 1+ (TOLERflood(crop) / 10)			# for instance, if TOLERflood(crop) index = 8, we assume that the crop can grow with up to 180% of its ETc to grow.





#########################################
#										#
#			PRIMARY FUNCTIONS			#
#										#
#########################################


def ASSESS_Tmin_germ_forFruits(x, crop, PRA):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	FUNCTION:
	If the current crop is a fruit crop, Tmin(crop) germination must be considered before the other edibility assessement:
	if Tmin_germ(crop) > TminMOY(PRA) while the whole winter, the buds just never open !
	TminMOY(PRA) must be lower than Tmin_germ(crop) at least one month in the winter."""

	x.edible_Tmin_germ = []
	edibTest = 0

	#~ CROProw = CROProw_PLANTS(crop)
	#~ CROPcol = CROPcol_PRAedibility(crop)
	#~ CROPcol_yields = CROPcol_PRAyields(crop)

	#======================================================================


	if prodCAT(crop) == 1 or prodCAT(crop) == 2 : #if the crop is a fruit tree crop
		print("The current crop is a tree/shrub: verifying if winter is cold enough...")
		CurrentMonth = 11
		GSmax = 5 # in this case, only winter is considered to see if the minimal Tgermination for fruit trees is reached at least one month in winter
		i = 1
		while i <= GSmax:
			if CurrentMonth % 12 == 0:
				if Tmin_germ(crop) <= TminMOY(12, PRA):
					x.edible_Tmin.append(False)
				else:
					x.edible_Tmin.append(True)
			elif CurrentMonth % 12 != 0:
				if Tmin_germ(crop) <= TminMOY(CurrentMonth%12, PRA):
					x.edible_Tmin.append(False)
				else:
					x.edible_Tmin.append(True)
			CurrentMonth += 1
			i += 1

		# --------------------------------------

		if True not in x.edible_Tmin:
			x.all_crop_parameters_match_the_PRA_ones = False

		print("	OK")


def ASSESS_Tmin(crop, x, PRA):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	FUNCTION:
	Minimum Temperature assessement: is Tmin (crop) < TminMOY (PRA) ?
	Notice: not "<=" because TminMOY is an average value: it would average that, some days, the coldest T is
	lower than Tmin(crop) (crop) !

	OUTPUT:
	It just verifies if x.all_crop_parameters_match_the_PRA_ones remains True or not. If the PRA minimum Temperature
	is lower than the one supported by the crop for a duration that is longer than or equal to the minimum growing
	season duration (GSmin)"""

	x.edible_Tmin = []
	GrowingMonth = 1
	CurrentMonth = int(seed_from(crop))
	maximum_growing_season_duration = int(GSmax(crop))

	while GrowingMonth <= maximum_growing_season_duration:
		if CurrentMonth % 12 == 0:
			if Tmin(crop) < TminMOY(12, PRA):
				x.edible_Tmin.append(True)
			else:
				x.edible_Tmin.append(False)
		elif CurrentMonth % 12 != 0:
			if Tmin(crop) < TminMOY(CurrentMonth%12, PRA):
				x.edible_Tmin.append(True)
			else:
				x.edible_Tmin.append(False)
		CurrentMonth += 1
		GrowingMonth += 1
	
		PRAedibTest = []
		count = 0

		for MonthIndex, Tmin_edibility in enumerate(x.edible_Tmin):
			if MonthIndex < (len(x.edible_Tmin) - 1) : # indexes begin with 0, so the last index will be the list length - 1
				if Tmin_edibility == True:
					if x.edible_Tmin[MonthIndex - 1] == Tmin_edibility:
						count += 1
					else:
						PRAedibTest.append(count)
						count = 1
			else:								# for the last entry in the list 'x.edible_Tmin' :
												# else, if the list does not end with 'False',
												# the count of consecutive 'True' would not be added to the list
				if Tmin_edibility == True:
					PRAedibTest.append(count)

		# --------------------------------------

		if max(PRAedibTest) <= GSmin(crop):
			x.all_crop_parameters_match_the_PRA_ones = False


def ASSESS_Water(crop, PRA, x):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	FUNCTION:
	Water requirement assessement: Are pecipitations and field capacity sufficient to store enough water to fulfil
	the water requirement (ETc) for each ¼ of the (maximal !) total growing stage?

	OUTPUT:
	It just verifies if x.all_crop_parameters_match_the_PRA_ones remains True or not. If the PRA Water Ressources
	cover the crop's Water Requirement (ETc) for a duration that is longer than or equal to the minimum growing
	season duration (GSmin), it becomes False and the crop is skipped."""


	#~ from selfVariables import x.TOLERdrought
	#~ from selfVariables import x.TOLERflood
	from math import ceil

	# /!\ AvailableWaterCapacity(PRA) (from 'environment') must be recalculated TAKING THE ORGANIC MATTER CONTENT INTO ACCOUNT !
	# ~ an error occurs with the following line (TypeError: can't multiply sequence by non-int of type 'float') : problem by calling values from the 'plants' ?
	#~ WaterDepthMax_in_Soil = (int(rootDEPTH(crop)) * 10) * AvailableWaterCapacity(PRA)	# maximum depth of water that the soil can hold WITHOUT TAKING INFILTRATION INTO ACCOUNT
																	# -> rootDEPTH(crop) (from cm to mm) * AvailableWaterCapacity(PRA)

	#~ x.TOLERdrought = 0
	#~ x.TOLFERflood  = 0

	CORR_TOLERdf(crop, x) # these function updates x.TOLERflood and x.TOLERdrought --> calculates % from the indices TOLERflood(crop) and TOLERdrought(crop)
	edible_WaterRqt = []
	maximum_growing_season_duration = GSmax(crop)
	GS1_4	= round(maximum_growing_season_duration * 0.25 )
	GS2_4	= round(maximum_growing_season_duration * 0.50 )
	GS3_4	= round(maximum_growing_season_duration * 0.75 )

	GrowingMonth = 1
	CurrentMonth = seed_from(crop)

	while GrowingMonth <= maximum_growing_season_duration:
		#= Determining the current stage of the GS =============================================
		if GrowingMonth <= GS1_4 :
			ETc = Kc1_4(crop) * ETPmoy(CurrentMonth, PRA)
			print("Kc1_4(crop) =", Kc1_4(crop))
			print("ETPmoy(CurrentMonth,PRA) =",ETPmoy(CurrentMonth, PRA))
			print("Assessing the Water Resources for the 1st quarter of the growing season...")


		elif GrowingMonth <= GS2_4 :
			ETc		= Kc2_4(crop) * ETPmoy(CurrentMonth, PRA)
			print("Assessing the Water Resources for the 2nd quarter of the growing season...")

		elif GrowingMonth <= GS3_4 :
			ETc= Kc3_4(crop)*ETPmoy(CurrentMonth, PRA)
			print("Assessing the Water Resources for the 3rd quarter of the growing season...")

		else:
			ETc= Kc4_4(crop)*ETPmoy(CurrentMonth, PRA)
			print("Assessing the Water Resources for the 4th quarter of the growing season...")
		#========================================================================================

		if CurrentMonth % 12 == 0:
			#--------------------------------------
			if x.TOLERdrought * ETc <= WaterResources(12, PRA) <= ETc * x.TOLERflood:
				edible_WaterRqt.append(True)
			else:
				edible_WaterRqt.append(False)
			#--------------------------------------

		else:
			#--------------------------------------
			if x.TOLERdrought * ETc <= WaterResources(CurrentMonth%12, PRA) <= ETc * x.TOLERflood:
				edible_WaterRqt.append(True)
			else:
				edible_WaterRqt.append(False)
			#--------------------------------------
		CurrentMonth += 1
		GrowingMonth += 1


		#END while-------------------------------------------------------------------------------


	#========================================================
    #=== ELIBILTY OF THE PRA concerning the Water Resources:

	print("Verifying if the Water Resources match with the Tmin supported by the crop...")
	print("x.edible_Tmin = ",x.edible_Tmin)
	print("edible_WaterRqt = ", edible_WaterRqt)

	PRAedibTest = 0
	the_selected_crop_is_a_permanent_crop = prodCAT(crop) == 1 or prodCAT(crop) == 2  # fruit/nut tree (1), shrub (2)

	if the_selected_crop_is_a_permanent_crop :
		pass
	else:
		PRAedibTest = []
		count = 0

		for MonthIndex, Tmin_edibility in enumerate(x.edible_Tmin):
			if edible_WaterRqt[MonthIndex] == True and Tmin_edibility == True:
				if edible_WaterRqt[MonthIndex - 1] == edible_WaterRqt[MonthIndex] and x.edible_Tmin[MonthIndex - 1] == Tmin_edibility:
					count += 1
				else:
					PRAedibTest.append(count)
					count = 1

		# --------------------------------------

		if max(PRAedibTest) <= GSmin(crop):
			x.all_crop_parameters_match_the_PRA_ones = False




def ASSESS_pH(crop, PRA, x):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	FUNCTION:
	pH(PRA) requirement assessement: the median pH(PRA) value of the current PRA must be included in the range
	[pHmin(crop):pHmax(crop)] of the current crop.

	OUTPUT:
	It just verifies if x.all_crop_parameters_match_the_PRA_ones remains True or not. If the PRA's soil pH does not
	match with the crop's pH window, it becomes False and the crop is skipped."""


	if pHmin(crop) >= pH(PRA) >= pHmax(crop):
		x.all_crop_parameters_match_the_PRA_ones = False
		print("The soil pH of this PRA does not match to the crop requirements.")

	print("The soil pH of this PRA matches to the crop requirements !")



def PriorityAssessement(x, data):
	"""INPUT:
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	data	is the class that contains the original 'plants' and 'environment' data bases
				from 'input[COUNTRY].py' (e.g. 'inputFR.py' for France).

	FUNCTION:
	This function calculates a priority indexes: PRIORITYgeneral, PRIORITYfruits and PRIORITYtextiles.
	While compiling the crop rotation, in case there are several edible crops to continue the rotation,
	these indexes will allow to chose a crop that have a higher geo-political importance than the others.
	PRIORITYgeneral is from 1 to 3
	PRIORITYfruits is from 1 to 5
	PRIORITYtextile is from 1 to 3
	the lower the index, the bigger the geo-political importance

	OUTPUT:
	an updated 'plants' dictionary with the new entries (keys) :
	*	'ratioADAPT'
	*	'PRIORITYgeneral'
	*	'PRIORITYfruits'
	*	'PRIORITYtextiles'
	"""


	#==============================================================================================================
	#== Calculating the NATIONAL AGRICULTURAL SURFACE + QUANTITY PER INHABITANT (kg/week)


	#=== Total agricultural surface:
	TotalAgriSurface = 0
	country = data.environment.keys()

	#=== Calculating the average quantity per inhabitant (don't take the age into account):
	Population = 714683  # Source: INSEE, estimation of the French population the 1st of January 2017)
	WeeksInYear = 365 / 7


	for PRA in country:
		if PRA != 'headers_full' and PRA != 'headers_ID':
			TotalAgriSurface += PRAsurface(PRA)


	#==============================================================================================================


	for crop in data.plants.keys():
		#~ CROProw = CROProw_PLANTS(crop)
		#~ CROPcol = CROPcol_PRAedibility(crop)

		if crop != 'headers_full' and crop != 'IDXinit' and crop != 'headers_ID':

			#======================================================================================

			# calculating the quantity per Inhabitant in kg from the Yields in tons :
			QttPerInhabitant = ((expYIELD(crop) * 1000 * x.prodSURFACE[crop])/Population)/WeeksInYear


			#======================================================================================
			#=== Calculating the "adaptation ratio" for the current CROP

			### calculating the "ratio of adaptability" for EACH CROP to give priority to crops which have the lowest ratio:
			### surface of the territory where the crop could grow/total agricultural surface in France :
			print("Calculating the 'ratio of adaptability' of {} (index = {})...".format( prod_EN(crop) ), crop)

			ratioADAPT = x.prodSURFACE[crop] / TotalAgriSurface
			data.plants[crop]['ratioADAPT'] = ratioADAPT

			print("	ratioADAPT =", ratioADAPT)


			#======================================
			#=== FRUIT TREES

			if prodCAT(crop) == 1:
				print("""The current crop is a tree or shrub.
				Calculating the priority indices...""")

				if ratioADAPT <= 0.6:
					# 'PRIORITYgeneral' = high priority
					data.plants[crop]['PRIORITYgeneral'] = 1
					print("	'PRIORITYgeneral' = ", 1)

				elif 0.6 <= ratioADAPT <= 0.8 :
					 # 'PRIORITYgeneral' = mid priority
					data.plants[crop]['PRIORITYgeneral'] = 2
					print("	'PRIORITYgeneral' = ", 2)

				else:
					# 'PRIORITYgeneral' = low priority
					data.plants[crop]['PRIORITYgeneral'] = 3
					print("	'PRIORITYgeneral' = ", 3)

				#END if (priority general acc. to ratioADAPT


				# 'PRIORITYfruits' assessement :
				if prodTYP(crop) is 'Fruit tree':
					if QttPerInhabitant < 1:
						data.plants[crop]['PRIORITYfruits'] = 1
						print("	'PRIORITYfruits' = ", 1)

					else:
						if 1 < QttPerInhabitant < 2:
							data.plants[crop]['PRIORITYfruits'] = 2
							print("	'PRIORITYfruits' = ", 2)

						elif 2 < QttPerInhabitant < 3:
							data.plants[crop]['PRIORITYfruits'] = 3
							print("	'PRIORITYfruits' = ", 3)

						elif 3 < QttPerInhabitant < 4:
							data.plants[crop]['PRIORITYfruits'] = 4
							print("	'PRIORITYfruits' = ", 4)

						else: # if more than 4kg/person/week
							data.plants[crop]['PRIORITYfruits'] = 5
							print("	'PRIORITYfruits' = ", 5)
							#END if (fruit trees, PRIORITYfruits)

				elif prodTYP(crop) is 'Berry':
					if QttPerInhabitant < 0.1:
						data.plants[crop]['PRIORITYfruits'] = 1
						print("	'PRIORITYfruits' = ", 1)

					else:
						if  0.1 < QttPerInhabitant < 0.2:
							data.plants[crop]['PRIORITYfruits'] = 2
							print("	'PRIORITYfruits' = ", 2)

						elif 0.2 < QttPerInhabitant < 0.3:
							data.plants[crop]['PRIORITYfruits'] = 3
							print("	'PRIORITYfruits' = ", 3)

						elif 0.3 < QttPerInhabitant < 0.4:
							data.plants[crop]['PRIORITYfruits'] = 4
							print("	'PRIORITYfruits' = ", 4)

						elif 0.4 < QttPerInhabitant:
							data.plants[crop]['PRIORITYfruits'] = 5
							print("	'PRIORITYfruits' = ", 5)

						#END if (Berries, PRIORITYfruits)

				data.plants[crop]['PRIORITYtextile'] = 0 # not a textile
				#END if ('PRIORITYfruits' assessement)


			#======================================
			#=== TEXTILE FIBRES

			elif prodTYP(crop) == 'Fiber crop':

				print("""The current crop is a fibre crop.
				Calculating the priority indices...""")

				# PRIORITYgeneral assessement:
				if ratioADAPT <= 0.6:
					data.plants[crop]['PRIORITYgeneral'] = 1
					print("	PRIORITYgeneral = ", 1)

				elif 0.6 <= ratioADAPT <= 0.8 :
					data.plants[crop]['PRIORITYgeneral'] = 2
					print("	PRIORITYgeneral = ", 2)

				else:
					data.plants[crop]['PRIORITYgeneral'] = 3
					print("	PRIORITYgeneral = ", 3)

				# PRIORITYtextile assessement:
				if prodID(crop) is FBRcott:
					data.plants[crop]['PRIORITYtextile'] = 1
					print("	PRIORITYtextile = ", 1)

				if prodID(crop) is FBRflx:
					data.plants[crop]['PRIORITYtextile'] = 2
					print("	PRIORITYtextile = ", 2)

				else:
					data.plants[crop]['PRIORITYtextile'] = 3
					print("	PRIORITYtextile = ", 3)

				data.plants[crop]['PRIORITYfruits']	= 0 # not a fruit/nut tree
				#END if ('PRIORITYtextile' assessement)


			#======================================
			#===  OTHER CROPS
			else:
				print("""The current crop is current cash crop.
					PRIORITYgeneral = 3""")
				data.plants[crop]['PRIORITYgeneral'] = 3 # low priority
				data.plants[crop]['PRIORITYfruits']	= 0 # not a fruit/nut tree
				data.plants[crop]['PRIORITYtextile'] = 0 # not a textile


