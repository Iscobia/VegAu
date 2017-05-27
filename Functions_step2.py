#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
"""Module containing the functions for :
VegAu, STEP2: Building a typical Crop Rotation for each PRA according to Climate and Soil Data

ATTENTION :
This program only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
The import of this sheet is ensured by the module 'importingODS.py'"""
#########################################
#										#
#		IMPORTING EXTERNAL MODULES		#
#										#
#########################################


#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts
from Functions_step1 import CORRseed_to
from Functions_step1 import CORR_TOLERdf
from Functions_step1 import WaterResources


#########################################
#										#
#			SECUNDARY FUNCTIONS			#
#	(short, just for adapting data)		#
#										#
#########################################


def MonthID(month):
	"""INPUT:
	'month' is the amount of months after the beginning of the computed rotation.

	OUTPUT:
	Returns the month ID composed by the 3 first letters of the month and the amount of years after the beginning
	of the rotation.
	"""
	MonthNum = month % 12
	MonthName = ['dec', 'jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'agu', 'sep', 'oct', 'nov']
	year = int(month//12 + 1)
	if month % 12 == 0:
		return "dec" + str(year - 1)
	else:
		return MonthName[MonthNum] + str(year)

#================================================================================================================


def ETc_GSmax(crop, month, x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	OUTPUT :
	ETc value for each month of the growing season calculated in STEP2 (not STEP1 !!) for the rotation simulation.
	It uses the variable x.EndPreviousCrop and GSmax(crop) to calculate its position in the GS duration.
	"""

	month	= month % 12 - x.EndPreviousCrop_earlier % 12 + 1
	# -> index of the current month of the rotation - index of the month of the begining of the rotation
	# e.g.: x.EndPreviousCrop_earlier = 3 (March) and the current month is 5 (Mai) : we are 5-3+1 = 3nd month of the GSmax(crop) (March + April + Mai).

	maximum_growing_season_duration = GSmax(crop)

	GS1_4	= round(maximum_growing_season_duration * 0.25 )
	GS2_4	= round(maximum_growing_season_duration * 0.50 )
	GS3_4	= round(maximum_growing_season_duration * 0.75 )
	
	if month <= GSmax(crop):
		return Kc4_4(crop)*ETPmoy(month, PRA)			# ETc = Kc (index) ETPmoy (in mm)
	elif month <= GS3_4:
		return Kc3_4(crop)*ETPmoy(month, PRA)
	elif month <= GS2_4 :
		return Kc2_4(crop) * ETPmoy(month, PRA)
	elif month <= GS1_4:
		return Kc1_4(crop) * ETPmoy(month, PRA)


#================================================================================================================


def ETc_GSmin(crop, month, x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	OUTPUT :
	ETc value for each month of the growing season calculated in STEP2 (not STEP1 !!) for the rotation simulation.
	It uses the variable x.EndPreviousCrop_earlier and GSmin(crop) to calculate its position in the GS duration.
	"""

	month	= abs( month - (x.EndPreviousCrop_earlier + 1))
	# -> index of the current month of the rotation - index of the month of the beginning of the rotation
	# e.g.: x.EndPreviousCrop = 3 (March) and the current month is 5 (Mai) : we are 5-3+1 = 3nd month of the GSmin(crop) (March + April + Mai).

	minimum_growing_season_duration = GSmin(crop)
	GS1_4	= round(x.EndPreviousCrop_earlier%12 + minimum_growing_season_duration * 0.25 )
	GS2_4	= round(x.EndPreviousCrop_earlier%12 + minimum_growing_season_duration * 0.50 )
	GS3_4	= round(x.EndPreviousCrop_earlier%12 + minimum_growing_season_duration * 0.75 )

	# BUT DU BREAKPOINT : comprendre pourquoi un "noneType" sort ---> TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
	if month <= GS1_4:
		return Kc1_4(crop) * ETPmoy(month, PRA)  # ETc = Kc (index) ETPmoy (in mm)

	elif month <= GS2_4:
		return Kc2_4(crop) * ETPmoy(month, PRA)

	elif month <= GS3_4:

		return Kc3_4(crop) * ETPmoy(month, PRA)

	else:
		return Kc4_4(crop) * ETPmoy(month, PRA)

#================================================================================================================


def WRmargin_GSmax(crop, month, x, PRA): # inutilisée
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	OUTPUT :
	Proportional margin between the PRA's WaterResources and the most extremes plant's needs/tolerance :
	---> Water Resources / Crops Requirement * Tolerance to Drought
	
	The more the monthly WR are near from this extreme value, the highest
	the margin.
	The Kc values and its appliance to the months of the growing season
	depends on GSmax(crop).
	
	This function is used in ASSESS_OptimalWaterResources(crop, PRA, x) where the
	WRmargin_GSmax(crop, month, x, PRA) values are standardized to get an index from 0 to 1.
	"""

	#~ FUNCTION AS BEFORE  2017.03.22: 
	#~ if WaterResources(month, x.GSstart, PRA, crop, x) < 0.90 * ETc_GSmax(crop, month, x, PRA):
		#~ i = 0.9 - Waterressources(month) / ETc_GSmax(crop, month, x, PRA) # i for Waterressources(month) = ETc_effective
		#~ ETc_effective = (0.9 - i) * ETc_GSmax(crop, month, x, PRA) # i is the % of ETc_GSmax(crop, month, x, PRA)
		#~ return (ETc_effective - ETc_GSmax(crop, month, x, PRA) * TOLERdrought(crop))/(ETc_GSmax(crop, month, x, PRA) * TOLERdrought(crop))
		
		# Function "corrected" (?)
	water_stress_threshold = ETc_GSmax(crop, month, x, PRA) * x.TOLERdrought

	try:
		return_value = 1- (water_stress_threshold / WaterResources(month, x.GSstart[crop], PRA, crop, x))
	except :
		return_value = 1 - (water_stress_threshold / WaterResources(month, x.GSstart, PRA, crop, x))

	return return_value




#================================================================================================================


def WRmargin_GSmin(crop, month, x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	OUTPUT:
	Proportional margin between the PRA's WaterResources and the most extremes plant's needs :
	---> Water Resources / Crops Requirement * Tolerance to Drought
	
	The more the monthly WR are near from this extreme value, the highest
	the margin.
	The Kc values and its appliance to the months of the growing season
	depends on GSmin(crop).
	
	This function is used in ASSESS_OptimalWaterResources(crop, PRA, x) where the
	WRmargin_GSmax(crop, month, x, PRA) values are standardized to get an index from 0 to 1.

	"""

	#~ FUNCTION AS BEFORE  2017.03.22: 
	#~ if WaterResources(month, GSstart, PRA, crop, x) < 0.90 * ETc_GSmin(crop, month, x):
		#~ i = 0.9 - Waterressources(month) / ETc_GSmin(crop, month, x) # i for Waterressources(month) = ETc_effective
		#~ ETc_effective = (0.9 - i) * ETc_GSmin(crop, month, x) # i is the % of ETc_GSmin(crop, month, x)
		#~ return (ETc_effective - ETc_GSmin(crop, month, x) * TOLERdrought(crop))/(ETc_GSmin(crop, month, x) * TOLERdrought(crop))
		
		# Function "corrected" (?)
	water_stress_threshold = ETc_GSmin(crop, month, x, PRA) * x.TOLERdrought
	try:
		return_value = 1- (water_stress_threshold / WaterResources(month, x.GSstart[crop], PRA, crop, x))
	except:
		return_value = 1 - (water_stress_threshold / WaterResources(month, x.GSstart, PRA, crop, x))

	return return_value




#=============================================================================================================
## NOTICE: 'YIELD' is a variable calculated just before the function 'SelectedCrop_Impact()': NOT A LAMBDA !!

HarvWeight	=	lambda prodID: expYIELD(prodID) * 1000 # conversion from tons to kilograms

def StrawWeight(prodID):
	"""Using the crop's % of straw to determine the straw weight.
	If the crop is a cover/companion crop, everything is killed and returned to the ground:
	if ZeroDivisionError occurs, the function returns the expected yield. """
	try:

		return (expSTRAW_rate(prodID) * HarvWeight(prodID)) / (1 - expSTRAW_rate(prodID))

	except ZeroDivisionError:
		return expYIELD(prodID)

#-------------------------------------------------------------------------------------------------------------

fixedN		=	lambda prodID: round ( (HarvWeight(prodID) + StrawWeight(prodID)) * fixN(prodID), 4)


# removedN ---> Amount of removed N according to the harvested wett mass.
#               Fixed N is not removed from the soil because it comes from the atmosphere.
#               The Ndfa values given in the database are supposed to be the percentage of the plant N.
removedN	=	lambda prodID: round ( prodN(prodID) * HarvWeight(prodID) + strawN(prodID) * StrawWeight(prodID) - fixedN(prodID) * (strawN(prodID) * StrawWeight(prodID) + strawN(prodID) * StrawWeight(prodID) * fixN(prodID)), 4)


returnedN	=	lambda prodID: round ( strawN(prodID) * StrawWeight(prodID) + strawN(prodID) * StrawWeight(prodID) * fixN(prodID) * (strawN(prodID) * StrawWeight(prodID) + strawN(prodID) * StrawWeight(prodID)), 4)
				# N that have being fixed in straw (assuming that N fixation is homogeneous: it is false, but no data about it for now)
				# returns to the soil with the crop residues


removedP	= lambda prodID: round (prodP(prodID) * HarvWeight(prodID) + prodP(prodID) * StrawWeight(prodID), 4)
returnedP	= lambda prodID: round (strawP(prodID) * StrawWeight(prodID), 4)

removedK	= lambda prodID: round (prodK(prodID) * HarvWeight(prodID) + prodK(prodID) * StrawWeight(prodID), 4)
returnedK	= lambda prodID: round (strawK(prodID) * StrawWeight(prodID), 4)# does not already exist (no data)

removedNa	= lambda prodID: round (prodNa(prodID) * HarvWeight(prodID), 4)
returnedNa	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

removedMg	= lambda prodID: round( prodMg(prodID) * HarvWeight(prodID) + prodMg(prodID) * StrawWeight(prodID), 4)
returnedMg	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

removedCa	= lambda prodID: round( prodCa(prodID) * HarvWeight(prodID) + prodCa(prodID) * StrawWeight(prodID), 4)
returnedCa	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

removedMn	= lambda prodID: round( prodMn(prodID) * HarvWeight(prodID) + prodMn(prodID) * StrawWeight(prodID), 4)
returnedMn	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

removedFe	= lambda prodID: round( prodFe(prodID) * HarvWeight(prodID) + prodFe(prodID) * StrawWeight(prodID), 4)
returnedFe	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

removedCu	= lambda prodID: round( prodCu(prodID) * HarvWeight(prodID) + prodCu(prodID) * StrawWeight(prodID), 4)
returnedCu	= lambda prodID: round( 0 * StrawWeight(prodID), 4) # does not already exist (no data)

returnedOM	= lambda prodID: round( returnedN(prodID) * CN(prodID), 4)



#================================================================================================================


def mineralizedCPK(crop, month):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)

	FUNCTION:
	Function based on the article of Justes et al. (2009) for the model STICS : https://www.researchgate.net/publication/225690616_Quantifying_and_modelling_C_and_N_mineralization_kinetics_of_catch_crop_residues_in_soil_Parameterization_of_the_residue_decomposition_module_of_STICS_model_for_mature_and_non_mature_residues)
	It returns the mineralized C (OM) in function of time. For the moment, we assume than, because C is not the bacteria's fodder,
	this function can also be applied to P and K. If there is other known functions/parameters for P and K, the code should be updated
	with these new functions/parameters.

	OUTPUT:
	the OM amount returned to the soil after decomposition
	"""
	from math import exp
	
	t = month*30.5 # this function requires days
	R	=	CN(crop)
	a	=	15.4
	b	=	76
	#----------------------------------------------------------------
	Rb	=	a - b/R 	# C:N of zymogeneous bacterial biomass (g/g)
	Rbmin = 7.8
	if Rb < Rbmin:
		Rb = Rbmin
	#----------------------------------------------------------------
	c	=	0.098
	d	=	1.94
	e	=	0.73
	f	=	10.2
	h	=	1 - (e*R) / ( f + R) 	# humification rate of microbial biomass (ndays^-1)
	k = c + d / R					# decomposition rate of plant residues (ndays^-1), value from the article
	# k	=	c + d/R	* 0.98 * 0.74	# decomposition rate of plant residues (ndays^-1), value from the table
	λ	=	0.0076
	Y0	=	0.62		# Assimilation yield residue-C by microbial biomass (g/g)
	Y	=	Y0

	# RESULTS DO NOT CORRESPOND WITH THE ONES OF THE ARTICLE !!! TO TAKE THE ABSOLUTE VALUE IS ONLY A WORKAROUND !!!

	return abs(    (1 - Y*h - (1 + (Y*(k - λ*h)/(λ - k)) *exp(-k*t) + ( (k*Y*(1 - h)/(λ - k))*exp(-λ*t) ) ))   )


#================================================================================================================


def mineralizedN(crop, month):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	month	is the number of the current month (1 for January, 3 for March, 10 for October, etc)

	FUNCTION:
	Function based on the article of Justes et al. (2009) for the model STICS : https://www.researchgate.net/publication/225690616_Quantifying_and_modelling_C_and_N_mineralization_kinetics_of_catch_crop_residues_in_soil_Parameterization_of_the_residue_decomposition_module_of_STICS_model_for_mature_and_non_mature_residues)
	It returns the mineralized N in function of time.

	OUTPUT:
	the amount of N that is returned to the soil after decomposition
	"""
	from math import exp

	t	=	month * 30.5 # this function requires days
	R	=	CN(crop)
	a	=	15.4
	b	=	76
	Rb	=	a + b/R 	# C:N of zymogeneous bacterial biomass (g/g)
	Rbmin = 7.8
	if Rb < Rbmin :
		Rb = Rmin

	c	=	0.098
	d	=	1.94
	e	=	0.73
	f	=	10.2
	h	=	1 - (e*R) / ( f + R) # humification rate of microbial biomass (ndays^-1)
	k	=	c + d/R	* 0.98 * 0.74	# decomposition rate of plant residues (ndays^-1)
	λ	=	0.0076

	Y0	=	0.62	# Assimilation yield residue-C by microbial biomass (g/g)
	Y	=	Y0
	CN_humus	=	9.5
	Wr	=	1/R			# N:C ratio of the plant residues
	Wb	=	1/Rb		# N:C ratio of the newly formed microbial biomass
	Wh	=	1/CN_humus		# N:C ratio of the newly formed humified organic matter
	alpha	=	1 - Wh/Wr * Y * h
	beta	=	1- (k * Wb - λ * h * Wh) * Y/Wr / (k-λ)
	gamma	=	k * Y * (Wb - h * Wh) / Wr / (k - λ)
	
	return (1 - exp(-k * t) - ((Wb * k * Y)/(Wr *( λ - k))) * (exp(-k * t)) - ((Wh * Y * h)/(Wr * (λ - k)))* (exp(-λ*t) - λ * exp(-k*t)) - (Wh/Wr)*Y*h )
	# return (alpha - beta	* exp(-k*t)- gamma * exp(-λ*t) )



#================================================================================================================
#================================================================================================================



#########################################
#										#
#			PRIMARY FUNCTIONS			#
#										#
#########################################


def ASSESS_SeedingDate(PRA, x):
	"""INPUT :
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions

	FUNCTION:
	Fulfil the list 'edibleCrops' by keeping only the x.edible crops (from 'edibleCropsID') for which the
	earliest seeding date is before the latest end of the previous crop's GS.
	
	If no crop can be planted before or while the last month of the previous crop's GS (x.EndPreviousCrop_later),
	the crops are sorted by the time between their seed_from(crop) and the x.EndPreviousCrop_later. Only the 2 shortest
	durations are allowed for the crop to be added in the list 'edibleCrops'.

	OUTPUT:
	'edibleCrops' list with the x.edible crops (from 'edibleCropsID') for which the earliest seeding date
	is before the latest end of the previous crop's GS
	"""

	x.edibleCrops = list(x.edibleCropsID[PRA])
	x.indexDelay = {}

	for crop in x.edibleCropsID[PRA]:
		# assessing if the current crop can be planted before the end of the previous crop's GS.
		# Else, it is deleted from the list 'edibleCrops'.

		# ============================================================================
		earlierPlantingMonth = x.EndPreviousCrop_earlier % 12
		laterPlantingMonth = x.EndPreviousCrop_later % 12
		if earlierPlantingMonth == 0:
			earlierPlantingMonth = 12
		if laterPlantingMonth == 0:
			laterPlantingMonth = 12
		# ----------------------------------------------------------------------------
		if laterPlantingMonth < earlierPlantingMonth:
			no_plantation_delay = earlierPlantingMonth <= seed_from(crop) % 12 <= laterPlantingMonth + 12
		else:
			no_plantation_delay = earlierPlantingMonth <= seed_from(crop) % 12 <= laterPlantingMonth
		# =============================================================================

		seeding_season_starts_before_the_end_of_the_previous_crop = (earlierPlantingMonth) > seed_from(crop)
		ends_after_its_shorter_GS_duration = earlierPlantingMonth <= round(seed_to(crop)) <= laterPlantingMonth

		if no_plantation_delay :
			x.indexDelay[crop] = 1
			if earlierPlantingMonth < seed_from(crop):
				x.GSstart[crop]	= x.EndPreviousCrop_earlier + (seed_from(crop) - earlierPlantingMonth)
			elif earlierPlantingMonth == seed_from(crop):
				x.GSstart[crop]	= x.EndPreviousCrop_earlier + 1

		elif seeding_season_starts_before_the_end_of_the_previous_crop and ends_after_its_shorter_GS_duration :
			x.indexDelay[crop] = 1
			x.GSstart[crop]	= x.EndPreviousCrop_earlier + 1

		else:
			x.edibleCrops = [x for x in x.edibleCrops if x != crop]
	
	#=========================================================================================
	
	
	# If there are no x.edible crops for which the earliest planting date do not match with no one of the earliest
	# and latest end of the previous crop's GS, the 'edibleCrops' list is empty. -> every crop have been deleted.
	
	if x.edibleCrops == [] or len(x.edibleCrops) < 3:
		if x.edibleCrops == [] :
			print("""			No seeding date of any edible crop matches exactly with the end of the previous crop:
				Looking for the shortest delay among seeding dates of the PRA's edible crops...""")
		else:
			print("""			Only {} crops could be planted without a delay ({}).
				Looking for the shortest delay among seeding dates of other PRA's edible crops...""".format(len(x.edibleCrops), x.edibleCrops))

		# restoring the 'edibleCrops' list
		x.laterCrops	=	list(sorted(x.edibleCropsID[PRA]))
		# creating a new dictionary which bounds the crops indexes to the duration btw their earliest seeding date
		# and the earliest end date of the previous crop's GS:
		SelectEarlierPlanting = {}
		for crop in x.laterCrops:
			if seed_from(crop) < laterPlantingMonth:
				SelectEarlierPlanting[crop] =  x.EndPreviousCrop_earlier + ((seed_from(crop) + 12) - laterPlantingMonth)
			else:
				SelectEarlierPlanting[crop] = x.EndPreviousCrop_earlier +  ( seed_from(crop) - laterPlantingMonth )

		# selecting the both earliest planting dates among the crops from the 'SelectEarlierPlanting' dictionary:
		PlantingDate_1 = sorted(list(set(SelectEarlierPlanting.values())))[0]
		PlantingDate_2 = sorted(list(set(SelectEarlierPlanting.values())))[1]

		delay1 = [c for c in x.laterCrops if SelectEarlierPlanting[c] == PlantingDate_1 and c not in x.edibleCrops]
		delay2 = [c for c in x.laterCrops if SelectEarlierPlanting[c] == PlantingDate_2 and c not in x.edibleCrops]

		x.laterCrops = [] # this dict will be used in SELECT_CashCrop --> priority to crops that are not in this dict (no delay).

		for crop in SelectEarlierPlanting.keys():
		# adding ID of the crops for which the earliest planting date are the earliest ones among the other PRA's x.edible crops:
			if len(delay1) + len(x.edibleCrops) > 5:
				x.laterCrops.append( (crop, PlantingDate_1) )
				x.GSstart[crop] = PlantingDate_1
				if PlantingDate_1 > x.EndPreviousCrop_later:
					x.indexDelay[crop] = 1 - ((PlantingDate_1 - x.EndPreviousCrop_later%12) / 12)
				else :
					x.indexDelay[crop] = 1 - ((PlantingDate_1 + 12 - x.EndPreviousCrop_later%12) / 12)

			# if there are less than 5 crops in x.edibleCrops + delay1, we add delay2
			if len(delay2) + len(x.edibleCrops) < 5:
				x.laterCrops.append((crop, PlantingDate_2))
				x.GSstart[crop] = PlantingDate_2
				if PlantingDate_1 > x.EndPreviousCrop_later:
					x.indexDelay[crop] = 1 - ((PlantingDate_2 - x.EndPreviousCrop_later%12) / 12)
				else :
					x.indexDelay[crop] = 1 - ((PlantingDate_2 + 12 - x.EndPreviousCrop_later%12) / 12)

		# if there was no edible crop for this season, we add delayed crops
		if x.edibleCrops == []:
			x.rotat[PRA].append( ('Plantation delay', None, PlantingDate_1) )
			x.edibleCrops = [c for (c, delay) in x.laterCrops]

		# if there was just 1 or 2 crop in x.edibleCrops, we add delayed crops to x.edibleCrops
		else :
			for crop in [c for (c, delay) in x.laterCrops if c not in x.edibleCrops] :
				# 'not in x.edibleCrops' avoids duplicates which create errors in the ASSESS_Nutrient function.
				x.edibleCrops.append(crop)
		print(x.laterCrops)
		print("""			{} edible crops can be planted without any delay : {}""".format(len(x.edibleCrops),
		                                                                                     x.edibleCrops))
		print("""			Next later crops are : {}""".format ([c for (c, delay) in x.laterCrops]))

	else:
		print("""			{} edible crops can be planted without any delay : {}""". format( len(x.edibleCrops), x.edibleCrops))

#================================================================================================================
#================================================================================================================


def ASSESS_WaterResources(PRA, x):
	"""INPUT :
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions
				---> x.edibleCrops (list), x.GSstart[crop] (int), x.GSstart (int), x.TOLERdrought/-flood (int)

	FUNCTION:
	This function compares the quality of the Water Resources provided by the current PRA for each x.edible crop.
	If the PRA's monthly minimum Temperatures are lower than Tmin(crop) while at least one month in GSmin(crop), the crop is eliminated.

	OUTPUT:
	x.indexWR (dict) with a standardized WReval index: the lower the index value, the worse the WaterResources conditions.
	"""

	x.TOLERdrought = 0
	x.TOLERflood = 0
	x.indexWR = {}

	#=============================================================================================================
	# loop for the Tmin(crop) Assessement (deletes all crops for which the PRA's Temperature is too cold for at least one month in GS_min :
	for crop in x.edibleCrops:

		month = int(x.GSstart[crop])
		CORR_TOLERdf(crop, x)  # cf 'Functions_step1.py' --> converting the TOLERdrought(crop)/flood into percentages of ETc
		last_month_of_the_shortest_growing_season = x.GSstart[crop] + GSmin(crop)

		while month <= last_month_of_the_shortest_growing_season: # while the month of rotation is in the potential GS of the current crop

			if TminMOY(month, PRA) < Tmin(crop):
				x.edibleCrops =  [x for x in x.edibleCrops if x != crop]
			month += 1

	if x.edibleCrops == []:
		# updating the earlier and later dates for the begin of a new growing season with a later crop :
		later_dates = [abs(seed_from(c) - x.EndPreviousCrop_later % 12) for c in x.edibleCropsID[PRA] if abs(seed_from(c) - x.EndPreviousCrop_later % 12) != 0]
		delay = sorted(list(set(later_dates)))[0]
		x.EndPreviousCrop_earlier = int(x.EndPreviousCrop_later + delay)
		x.EndPreviousCrop_later = int(x.EndPreviousCrop_earlier + 2)
		x.rotat[PRA].append(('Cold season', None, x.EndPreviousCrop_earlier))
		x.no_delay_because_of_T_or_water = False
		# raise ColdSeason("The rotation must be delayed: Temperature does not match with the edible PRAs.")
	else:
		print("[{}][{}]	The PRA's Tmin matches the crop's one for following crops : {}".format(PRA, x.EndPreviousCrop_later, x.edibleCrops))

		# =============================================================================================================
		# loop for the Water Requirement Assessement :

		for crop in x.edibleCrops:
			month = int(x.GSstart[crop])
			last_month_of_the_shortest_growing_season = x.GSstart[crop] + GSmin(crop)
			x.indexWR[crop] = 0

			while month <= last_month_of_the_shortest_growing_season:  # while the month of rotation is in the potential GS of the current crop

				if round(WRmargin_GSmin(crop, month, x, PRA), 2) >= 0:
					x.indexWR[crop] += round(WRmargin_GSmin(crop, month, x, PRA), 3)  # summing the margins
				else:  # if the PRA's WR are lower than or equal to the drought threshold
					# -> this crop is deleted from the dictionary
					x.edibleCrops = [x for x in x.edibleCrops if x != crop]
					del x.indexWR[crop]
					break  # close the loop for this crop -> back to the 'for-loop' without incrementing 'month'

				month += 1

		# ===============================================================================================================
		# Standardization : dividing all crop's values by this max to get an index between 0 and 1 with 1 = best conditions.
		for crop in x.indexWR:
			x.indexWR[crop] = round(x.indexWR[crop] / max(x.indexWR.values()), 4)

		print("""			Standardization of the Water Resources indices [OK]
					x.indexWR = """, x.indexWR)

		# at the end of these both loops, we get an 'indexWR' dictionary with a "WaterResources evaluation" (WReval)
		# for each edible crop. -> helps to compare, at the end, with the remaining crops.

		print("[{}][{}]	Water Resources verified. Following crops remain : {}.".format(PRA, x.EndPreviousCrop_later, x.edibleCrops))

		if x.edibleCrops == []:
			# resetting the x.edibleCrops list and looking for later crops:
			later_dates = [abs(seed_from(c) - x.EndPreviousCrop_later%12) for c in x.edibleCropsID[PRA]]

			if sorted(list(set(later_dates)))[0] != 0:
				delay = sorted(list(set(later_dates)))[0]
			else:
				delay = sorted(list(set(later_dates)))[1]

			x.EndPreviousCrop_earlier = x.EndPreviousCrop_later + delay # nearest date from the previous 'x.EndPreviousCrop_later'.
			x.EndPreviousCrop_later = int( x.EndPreviousCrop_earlier + 2)
			# there is a hole in the rotation:
			x.rotat[PRA].append( ('Dry season', None, x.EndPreviousCrop_earlier) )
			x.no_delay_because_of_T_or_water = False
			# raise DrySeason("The rotation must be delayed: the season is too dry.")


#================================================================================================================
#================================================================================================================

def VERIF_lastCrops_not_CC(x, PRA, nutrient):
	"""Verifying if the last 4 crops of the rotation (cf x.rotat) are not Cover Crops.
	Else, the rotation is stoped."""

	# If there is already 4 crops in the rotation, if all edible cash crops are removed and
	# the 3 last crops are already cover crops, the limiting factor has been reached :

	if nutrient == None:
		nutrient = 'Last 4 crops are Cover Crops'

	if len(x.rotat[PRA]) > 5:
		last_crops = [c for (c, companion, date) in x.rotat[PRA] if (c != 'start' and c != 'Limiting factor' and c != 'Dry season' and c != 'Plantation delay' and 'season' not in c)]

		if len(last_crops) >= 4:
			i = int(len(last_crops))

			# Selecting the last 4 crops of the rotation :
			last_crops = [ last_crops[i - 4], last_crops[i - 3], last_crops[i - 2], last_crops[i-1] ]

			# if they are all Cover Crops, their "production Category" will be 0, so their average will also be 0:
			last_crops_are_CC = (((prodCAT(last_crops[0]) + prodCAT(last_crops[1]) + prodCAT(
				last_crops[2]) + prodCAT(last_crops[3])) / 4)) == 0

			if last_crops_are_CC:
				# if the only crops in the x.edibleCrops list are CoverCrops, rotation is broken.
				if [c for c in x.edibleCrops if prodCAT(c) != 0] != [] :
					x.rotat[PRA].append(('Limiting factor', nutrient, x.edibleCrops))
					x.LimitingFactorReached = True
				# if the only crops in the x.edibleCrops list are CoverCrops, rotation is broken too.
				# (we assume that only other cover crops will follow)
				else:
					x.rotat[PRA].append(('Limiting factor', 'Last 4 crops are Cover Crops', x.edibleCrops))
					x.LimitingFactorReached = True



#================================================================================================================



def ASSESS_NutrientsMargin(PRA, x):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions


	FUNCTION:
	This function uses the dictionary x.decomposition_month. It contains the nutrient amount which should be released
	to the soil 	after the death of each crop of the rotation. Its keys correspond to the duration (in month) after
	which the nutrients are released, that is to say added to the PRA soil resources. For each month of the rotation,
	the values of each month are switched to the key "month - 1" and the nutrients that was referenced in the key 1
	are added to the PRA soil nutrients.

	It returns a list with the nutrient margin of each crop from x.edibleCrops that have ONLY POSITIVE
	nutrient margins.
	It deletes also from x.edibleCrops every crop that would require more nutrients than the soil can provide.

	OUTPUT:
	*	x.indexNutrients
	*	updated x.edibleCrops (only edible crops)
	"""

	for crop in x.edibleCrops:
		x.indexNutrients[crop] = {}
		removed = {}

		#---------------------------------------------------
		#-- Setting up the dict 'removed' :

		removed = {"N": removedN(crop), "P": removedP(crop), "K": removedK(crop), "Na": removedNa(crop),
				   "Mg": removedMg(crop), "Ca": removedCa(crop), "Mn": removedMn(crop), "Fe": removedFe(crop),
				   "Cu": removedCu(crop)}# Organic Matter ('OM' cannot be removed !)
		nutrients = [x for x in sorted( removed.keys() )]

		#---------------------------------------------------

		for nutrient in nutrients:
			x.indexNutrients[crop][nutrient]=[]

			#-------------------------------------------------------------------------------------------------------------

			monthInGS = 1
			while monthInGS <= GSmin(crop):

				#---------------------------------------------------------------------------------------------------------
				# if the nutrient amount in the PRA's soil is not sufficient while GSmin(crop),
				# the Selected Companion Crop is not considered as x.edible anymore:


				if nutrient == 'N' :
					margin = x.ActualStand[PRA][nutrient] + x.decomposition_month[monthInGS][nutrient] - ((removed[nutrient] - fixedN(crop)) /GSmin(crop) )
				else :
					margin = x.ActualStand[PRA][nutrient] + x.decomposition_month[monthInGS][nutrient] - (removed[nutrient]/GSmin(crop) )

				# ---------------------------------------------------------------------------------------------------------

				if margin < 0 :
					print("			/!\ Not enough {} to grow {}. [DELETED FROM x.edibleCrops]".format(nutrient, prod_EN(crop)))
					if nutrient not in x.LimitingFactor[PRA]:
						x.LimitingFactor[PRA].append(nutrient)
					del x.indexNutrients[crop]
					x.edibleCrops = [x for x in x.edibleCrops if x!= crop]

					if x.edibleCrops == []:
						x.rotat[PRA].append(('Limiting factor', x.LimitingFactor[PRA], x.edibleCrops))
						x.LimitingFactorReached = True
					else:
						# Verifying if the 4 last crops are not cover crops (if they are, the rotation is closed) :
						VERIF_lastCrops_not_CC(x, PRA, nutrient)

					break
					# ---------------------------------------------------------------------------------------------------------

				else:
					# average removed and fixed nutrient for one month of GSmin(crop):
					x.indexNutrients[crop][nutrient].append(margin)

					#END if (margin not negative) --------------------------------------------------------------------------

				monthInGS += 1
				#END while (end of GSmin) ----------------------------------------------------------------------------------

			if crop in x.indexNutrients.keys():
				x.indexNutrients[crop][nutrient] = round( sum(x.indexNutrients[crop][nutrient]) / len(x.indexNutrients[crop][nutrient]), 4)
			else:
				break
			#END for (nutrient in x.indexNutrients[crop].keys())-------------------------------------------------------------

		#END for (crop in x.edibleCrops)--------------------------------------------------------------------------------------

	print("			Nutrient Margin Assessment [OK]")



#================================================================================================================


def ASSESS_Nutrients(x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.

	FUNCTION:
	This function selects the crops for which there is enough nutrients in the PRA (updates the 'edibleCrops' list).
	It updates also the 'edibleCropsSN' dictionary ('SN' for 'Soil Nutrients') with:
		*	keys = prodID
		*	values = standardized nutrients margin: the lower the index value, the less nutrients in the soil after the crop.

	"""
	x.indexNutrients = {}

	ASSESS_NutrientsMargin(PRA, x)
	# after this function, x.indexNutrients contains a key for each crop of edibleCrop for which there is POSITIVE nutrient margins
	# x.edibleCrops is also updated (crops with negative nutrient margins have been deleted.

	# Margin standardization, first step (finding the maximum NutrientMargin for each nutrient
	# -> dividing all by max and get a percentage with 1 the higher value):

	if x.LimitingFactorReached == False :

		MAXvalue = {'N': [], 'P': [], 'K': [], 'Na': [], 'Mg': [], 'Ca': [], 'Mn': [], 'Fe': [], 'Cu': []}

		for crop in x.indexNutrients:
			#----------------------------------------------------------------------------------------------
			for nutrient in MAXvalue.keys():
				MAXvalue[nutrient].append( x.indexNutrients[crop][nutrient] )
			#END for --------------------------------------------------------------------------------------

		for nutrient in MAXvalue.keys():
			MAXvalue[nutrient] = max(MAXvalue[nutrient])


		# Margin standardization, second step (dividing by the MAXvalue to get a percentage):
		for crop in x.indexNutrients:
			#----------------------------------------------------------------------------------------------
			for nutrient in x.indexNutrients[crop].keys():
				x.indexNutrients[crop][nutrient]	/=	MAXvalue[nutrient]
				#END for ----------------------------------------------------------------------------------
			# calculating the average of all standardized nutrient margin to get an index between 0 and 1 :
			x.indexNutrients[crop]	=	round( sum( list(x.indexNutrients[crop].values()) ) / len(x.indexNutrients[crop]), 3)

			#END for --------------------------------------------------------------------------------------
		# END if (x.LimitingFactorReached == False )

#================================================================================================================
#================================================================================================================



def ASSESS_PestDiseases(x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions

	OUTPUT:
	Index according to the risks of pests and diseases relative to a too short period between several crops
	of a same botanic family.
	"""

	x.indexPnD = {} # cleaning up the dict from previous calculations

	for crop in x.edibleCrops:

		if prodBOT(crop) not in x.VERIFprodBOT.keys():
			x.indexPnD[crop] = 1

		elif int(period(crop)) == 0: # if prodBOT == 0, ZeroDivisionError : cover crops and trees have no return period
			x.indexPnD[crop] = 1

		else:
			duration_since_previous_crop	=	x.VERIFprodBOT[prodBOT(crop)]['Duration since previous crop']

			x.indexPnD[crop] = (duration_since_previous_crop / 12) / period(crop)
			# theoritically, if x.indexPnD[prodBOT(crop)] >= 1, no risk -> the highest the ratio, the better the conditions (like the other indexes, important)


	for crop in x.indexPnD:
		if x.indexPnD[crop] != 1: # x.indexPnD[crop] has already been set to 1 because there have no Pests and
										# Diseases risks to rotation occurrence (trees, shrubs and CC: no rotation !)
			try:
				x.indexPnD[crop] = x.indexPnD[crop] / max(x.indexPnD.values())
			except ZeroDivisionError: # if the bigger value of x.indexPnD, it means that there is no risk
				x.indexPnD[crop] = 1

			#the obtained values are yet all comprised between 1 and 0, with 1 the very best one.


#================================================================================================================
#================================================================================================================


def SELECT_CashCrop(x, PRA, data):
	"""INPUT:
	*	x	is the class that contains all self variables used in all VegAu's functions

	FUNCTION :
	Selecting a crop among the 'x.edibleCrops' list according to the indices from the lists :
	' x.indexWR', 'edibleCropsSN' and 'indexPnD'

	OUTPUT :
	*	crop ID of the Selected crop
	*	the list 'x.edibleCompanionCrops' with thoses from the edible crops that are cover crops or companion crops
	"""

	Final_Edibility_Index	= {}
	edibleCashCrops         = []
	x.edibleCompanionCrops  = []
	edibleCoverCrops		= []	# not a self variable because a cover crop is only selected in this function
									# IF the N resources are too low (< 120 kg/ha) AND if there are available cover
									# crops for this season. In this only case, x.edibleCrops becomes edibleCoverCrops.

	# Crossing the Water Requirement, Soil Nutrients and Pest&Diseases indexes (between 0 and 1 with 1 corresponding to the best conditions)
	# Because de Pest&Diseases assessment did not suppress any crop of the list but because it has a critical biological importance,
	# this index is ponderated by 2 against 1 for the others.

	SelectionDone = False

	for crop in x.edibleCrops:

		if prodTYP(crop)=='Companion crop':
			x.edibleCompanionCrops.append(crop)
		if prodTYP(crop)=='Companion crop' or prodTYP(crop)=='Cover crop':
			edibleCoverCrops.append(crop)
		else:
			edibleCashCrops.append(crop)


	#===================================================================================================================
	#== FIRST PART : SELECTING THE TYPE OF CROP ACCORDING TO THE SOIL SUPPLIES IN N AND THEIR OCCURENCE IN THE =========
	#==              ROTATION(S) AT LOCAL AND COUNTRY SCALE ============================================================
	#===================================================================================================================


	if x.ActualStand[PRA]['N'] < 120 and len(edibleCoverCrops) > 0: # if N-ressources are lower than 120 kg/ha
		if edibleCoverCrops != []:
			x.edibleCrops = list(edibleCoverCrops)
		else:
			x.SelectedCrop = edibleCoverCrops[0]
			SelectionDone = True

	#===================================================================================================================
	# Selecting the best(s) crop for following the preceding one:

	else:
		rotation = [c for (c, companion, date) in x.rotat[PRA] if (c != 'start' and c != 'Limiting factor' and 'delay' not in c and 'season' not in c)]
		# Note : 'delay' not in c allows to add further informations about de delay in rotat.
		delay    = [c for (c, delay) in x.laterCrops]
		unusedCrops = [c for c in edibleCashCrops if c not in rotation]
		unusedCrops_countryScale = [c for c in unusedCrops if c not in x.totalYields["TOTAL"] and c not in delay]

		# ------------------------------------------------------------------------------------------

		# if there is only one edible crop left, it is the selected crop
		if len(x.edibleCrops) == 1:
			x.CHOICE[PRA].append(('x.edibleCrops', len(x.edibleCrops))) # Theoretically, ('x.edibleCrops', 1)

			x.SelectedCrop = x.edibleCrops[0]
			SelectionDone = True

		# else, if there are in the selection some unused crops at the local AND country scale (without delay),
		# they have priority
		elif unusedCrops_countryScale != []:
			x.CHOICE[PRA].append(('unusedCrops_countryScale', len(unusedCrops_countryScale)))

			if len(unusedCrops_countryScale) == 1:
				x.SelectedCrop = unusedCrops_countryScale[0]
				SelectionDone = True
			else:
				x.edibleCrops = unusedCrops_countryScale

		# else, if there are some unused crops in the selection, they have priority
		elif unusedCrops != [] :

			# Giving priority to unused crops :
			if len(unusedCrops) == 1:
				x.CHOICE[PRA].append(('unusedCrops', 1))

				x.SelectedCrop = unusedCrops[0]
				SelectionDone = True

			else:
				# x.edibleCrops   = unusedCrops
				unusedCrops_without_delay = [c for c in unusedCrops if c not in delay]
				unusedCrops_countryScale_delay = [c for c in unusedCrops if c not in x.totalYields["TOTAL"]]
				unusedCashCrops = [c for c in edibleCashCrops if c in unusedCrops]

				# if there are unused crops without delay, they have priority
				if unusedCrops_without_delay != []:

					x.CHOICE[PRA].append( ('unusedCrops_without_delay', len(unusedCrops_without_delay)) )

					if len(unusedCrops_without_delay) == 1:
						x.SelectedCrop = unusedCrops_without_delay[0]
						SelectionDone = True
					else:
						x.edibleCrops = unusedCrops_without_delay

				else:
					# if there are no unused crop without delay, delayed crops that have
					# not been used at the country scale have priority:
					if unusedCrops_countryScale_delay != []:
						x.CHOICE[PRA].append( ('unusedCrops_countryScale', len(unusedCrops_countryScale_delay)) )

						if len(unusedCrops_countryScale) == 1:
							x.SelectedCrop = unusedCrops_countryScale_delay[0]
							SelectionDone = True
						else:
							x.edibleCrops = unusedCrops_countryScale_delay

					# if all edible crops have already been used at the country scale,
					# we consider all unused cash crops (at the local scale).
					elif unusedCashCrops != [] :

						x.CHOICE[PRA].append( ('unusedCashCrops', len(unusedCashCrops)) )

						if len(unusedCashCrops) == 1:
							x.SelectedCrop = unusedCashCrops[0]
							SelectionDone = True

						else:
							x.edibleCrops = unusedCashCrops

		# if there is more than one crop in the edible crop list but that they are all already in the rotation
		# cash crops have priority
		elif edibleCashCrops != []:
			x.CHOICE[PRA].append(('edibleCashCrops', len(edibleCashCrops)))

			if len(edibleCashCrops) == 1:
				x.SelectedCrop = edibleCashCrops[0]
				SelectionDone = True

			else:
				x.edibleCrops = edibleCashCrops

		# if all edible crop has already been used and that there is no cash crop, there are only cover crops left.
		else:
			x.CHOICE[PRA].append(('edibleCoverCrops', len(edibleCoverCrops)))

			if len(edibleCoverCrops) == 1:
				x.SelectedCrop = edibleCoverCrops[0]
				SelectionDone = True

			else:
				x.edibleCrops = edibleCoverCrops # theoretically, at this point, x.edibleCrops is already the same as edibleCoverCrops


	#===================================================================================================================
	#= SECOND PART : IF WE HAVE TO CHOSE AMONG SEVERAL CROPS, WE USE THE PREVIOUSLY CALCULATED INDICES =================
	# ==================================================================================================================

	if SelectionDone == False:

		# calculating the representativity index of each edible crop :
		indexRepresent = {}
		CropsUsedAtCountryScale = [x.representativity[c] for c in x.representativity if c in x.edibleCrops]
		if CropsUsedAtCountryScale != [] :
			maxRepresentativity = max([x.representativity[c] for c in x.representativity if c in x.edibleCrops])


		for crop in x.edibleCrops:
			# ----------------------------------------------------------------------------------------------------------
			if crop  in CropsUsedAtCountryScale : # if there is a crop in this list, maxRepresentativity exists
				indexRepresent[crop] = 1 - (x.representativity[crop] / maxRepresentativity)

			else: # for the first study area for example, there is no representativity
				indexRepresent[crop] = 1

			# to be comparable to the other indexes, the higher value must be the better one: the lower the
			# territorial representativity, the bigger the chance for the crop to be chosen
			# ----------------------------------------------------------------------------------------------------------
			Final_Edibility_Index[crop] = round(((x.indexDelay[crop] + 2 * indexRepresent[crop] + x.indexWR[
				crop] + 0.5 * x.indexNutrients[crop] + 2 * x.indexPnD[crop]) / 6.5), 3)
			# ----------------------------------------------------------------------------------------------------------

		FinalSelection = []
		# =======================================================================================================

		for crop in x.edibleCrops:

			if Final_Edibility_Index[crop] == max( Final_Edibility_Index.values() ):
				FinalSelection.append(crop)

		if len(FinalSelection) == 1:
			x.SelectedCrop = FinalSelection[0]
		#-----------------------------------------------
		else: # considering the general priority index :
			priority = [ data.plants[crop]['PRIORITYgeneral'] for crop in FinalSelection ]
			FinalSelection = [x for x in FinalSelection if data.plants[x]['PRIORITYgeneral'] == max(priority)]

			if len(FinalSelection) == 1:
				x.SelectedCrop = FinalSelection[0]
			# -----------------------------------------------
			else: # considering the priority index for fruits :
				priority = [data.plants[crop]['PRIORITYfruits'] for crop in FinalSelection]
				FinalSelection = [x for x in FinalSelection if data.plants[x]['PRIORITYfruits'] == max(priority)]

				if len(FinalSelection) == 1:
					x.SelectedCrop = FinalSelection[0]
				# -----------------------------------------------
				else: # considering the priority index for textiles :
					priority = [data.plants[crop]['PRIORITYtextile'] for crop in FinalSelection]
					FinalSelection = [x for x in FinalSelection if data.plants[x]['PRIORITYtextile'] == max(priority)]

					if len(FinalSelection) == 1:
						x.SelectedCrop = FinalSelection[0]
					# -----------------------------------------------
					else:
						# At least, chosing the crop with the lowest ratioADAPT (crop which have the lesser geographic adaptability in the study area, here France)
						priority = [data.plants[crop]['ratioADAPT'] for crop in FinalSelection]
						FinalSelection = [x for x in FinalSelection if data.plants[x]['ratioADAPT'] == min(priority)]

						x.SelectedCrop = min(FinalSelection)



	print("			The selected crop is : {} ({}).".format(prod_EN(x.SelectedCrop), prodID(x.SelectedCrop)))


	# =========================================================================================================
	# Updating x.GSstart : it becomes an integer and corresponds to the optimal seeding date of the SelectedCrop

	x.GSstart = int( x.GSstart[x.SelectedCrop] )
	if crop not in x.representativity:
		x.representativity[crop] = 1
	else:
		x.representativity[crop] += 1

	# =========================================================================================================
	# == YIELD CALCULATION =====================================================================================

	print("[{}][{}]	Calculating the yield for the Selected Crop...".format(PRA, x.EndPreviousCrop_later))

	# adapting the surface of the study area
	x.YIELD = expYIELD(x.SelectedCrop) * PRAsurface(PRA)

	# adapting the yield proportionnaly to the Water Resources quality
	x.YIELD *= x.indexWR[x.SelectedCrop]

	x.YIELD *= x.indexPnD[x.SelectedCrop]  # adapt the yield proportionnaly to the Pests and Diseases risks (ratio).

	#----------------------------------------------------------------------------------------------------------

	if x.SelectedCrop in x.totalYields[PRA]:
		x.totalYields[PRA][x.SelectedCrop] += round(x.YIELD, 3) # rounding with 3 decimals to lighten the dict
	else:
		x.totalYields[PRA][x.SelectedCrop] = round(x.YIELD, 3)
	# Notice: Yields are in tons, not in t/ha anymore ! -> preparation for the assessment of the nutritional requirements

	#===========================================================================================================
	# ===========================================================================================================
	# UPDATING x.EndPreviousCrop_earlier/later and x.rotat:

	# ----------------------------------------------------------------------------------------------------------
	# indicating the earlier and the later month for the end of this crop for the next one:
	# this is calculated before the next crop to capture the GStot values of this crop and not the next one.
	# (for the next loop, the crop search occurs from the earlier to the later end of the SelectedCrop's GS)
	x.EndPreviousCrop_earlier   = int(x.GSstart + GSmin(x.SelectedCrop))
	x.EndPreviousCrop_later     = int(x.GSstart + GSmax(x.SelectedCrop))


	if x.PreviouslySelectedCrop != None:

		if x.SelectedCrop not in [c for (c, delay) in x.laterCrops]:
			# each time that a crop is selected, the given harvesting date is it's later one because
			# we don't know when the next crop will be planted.
			# ---> Before to add the actual crop's informations, we put right the previous one.
			del x.rotat[PRA][-1]
			x.rotat[PRA].append(
				(x.PreviouslySelectedCrop, x.SelectedCC, x.GSstart - 1))
			# GSstart is the first month of the actual crop's GS, so the previous one ends one month before.
			# Now, we add: (actually selected crop, still no companion crop selected, later end of the GS)
			x.rotat[PRA].append(
			(x.SelectedCrop, None, x.EndPreviousCrop_later))

		else: # If we have a delay to take into account :
			# the later end of its GS stays the later one
			x.rotat[PRA].append((x.PreviouslySelectedCrop, x.SelectedCC, x.EndPreviousCrop_later))
			# the delay is specified:
			x.rotat[PRA].append(('Plantation delay', None, x.GSstart))
			# And than we add the new crop:
			x.rotat[PRA].append(
				(x.SelectedCrop, None, x.EndPreviousCrop_later))

	else:
		x.rotat[PRA].append(('start', None, 3))
		x.rotat[PRA].append( (x.SelectedCrop, None, x.EndPreviousCrop_later) )


	# =======================================================================================================
	# =======================================================================================================
	# Taking into account the WaterRequirement on the GS and the Next Crop -> adapting x.EndPreviousCrop_later

	print("[{}][{}]	Adapting the later selected crop's harvest date (actually {}) according to the PRA's water ressources...".format(PRA, x.EndPreviousCrop_later, MonthID(x.EndPreviousCrop_later)))

	month = int(x.EndPreviousCrop_earlier)
	CORR_TOLERdf(x.SelectedCrop, x)

	while month < x.EndPreviousCrop_later:
		#----------------------------------------------------------------------------------------------------
		water_resources_are_sufficient = ETc_GSmax(x.SelectedCrop, month, x, PRA) * x.TOLERdrought < WaterResources(
			month, x.GSstart, PRA, x.SelectedCrop, x)
		# ----------------------------------------------------------------------------------------------------
		if water_resources_are_sufficient:
			pass
		else:
			x.EndPreviousCrop_later = int(month)
			break
		month += 1

	print("[{}][{}]	The later harvesting date is in {}.".format(PRA, x.EndPreviousCrop_later, MonthID(month)))



#================================================================================================================
#================================================================================================================

def ASSESS_Water_CompanionCrop(x, PRA):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions
	*	data	is the class that contains the original 'plants' and 'environment' data bases
				from 'input[COUNTRY].py' (e.g. 'inputFR.py' for France).

	FUNCTION:
	Assessing if the x.SelectedCrop tolerates a CompanionCrop according to its WaterRequirement and the PRA's WaterResources"""

	if x.edibleCompanionCrops != [] :

		print("[{}][{}]	Looking for an eventual Companion Crop...".format(PRA, x.EndPreviousCrop_later))
		# WaterResources_are_Sufficient = True


		maximum_growing_season_duration = GSmax(x.SelectedCrop)

		GS1_4	= round(maximum_growing_season_duration * 0.25 )
		GS2_4	= round(maximum_growing_season_duration * 0.50 )
		GS3_4	= round(maximum_growing_season_duration * 0.75 )


		# while WaterResources_are_Sufficient:
		if prodCAT(x.SelectedCrop) != 0 or prodCAT(x.SelectedCrop) != 5: # If the Selected Crop is neither a CoverCrop nor a vegetable Legume,

			for crop in x.edibleCompanionCrops:

				CurrentMonth = x.GSstart % 12
				i = 1

				while i <= GSmax(crop):

					#= Determining the current stage of the GS =============================================

					if i	<= GS1_4 :
						# print("Assessing the Water Resources for the 1st quarter of the growing season...")
						ETc					= Kc1_4(crop) * ETPmoy(CurrentMonth, PRA) # ETc = Kc (index) ETPmoy (in mm)
						ETc_SelectedCrop	= Kc1_4(x.SelectedCrop) * ETPmoy(CurrentMonth, PRA)

					elif i	<= GS2_4 :
						ETc					= Kc2_4(crop) * ETPmoy(CurrentMonth, PRA)
						ETc_SelectedCrop	= Kc2_4(x.SelectedCrop) * ETPmoy(CurrentMonth, PRA)
						# print("Assessing the Water Resources for the 2nd quarter of the growing season...")

					elif i	<= GS3_4 :
						ETc					= Kc3_4(crop)*ETPmoy(CurrentMonth, PRA)
						ETc_SelectedCrop	= Kc3_4(x.SelectedCrop) * ETPmoy(CurrentMonth, PRA)
						# print("Assessing the Water Resources for the 3rd quarter of the growing season...")

					else:
						ETc					= Kc4_4(crop)*ETPmoy(CurrentMonth, PRA)
						ETc_SelectedCrop	= Kc4_4(x.SelectedCrop) * ETPmoy(CurrentMonth, PRA)
						# print("Assessing the Water Resources for the 4th quarter of the growing season...")
					#========================================================================================

					# ATTENTION: CompanionCrops with a Cash Crop do not have the same density as if they were alone: 50% * ETc

					CurrentMonth = x.GSstart

					if CurrentMonth % 12 == 0:

						if ETc*0.5 + ETc_SelectedCrop <= WaterResources(12, x.GSstart, PRA, crop, x) :
							pass
						else:
							x.edibleCompanionCrops = [x for x in x.edibleCompanionCrops if x != crop] # deleting the current crop from the list

					elif CurrentMonth % 12 != 0:

						if ETc*0.5 + ETc_SelectedCrop <= WaterResources(CurrentMonth%12, x.GSstart, PRA, crop, x) :
							pass
						else:
							x.edibleCompanionCrops = [x for x in x.edibleCompanionCrops if x != crop] # deleting the current crop from the list

					CurrentMonth += 1
					i += 1

				#END while (i <= GSmax)

			#END for (crop in edibleCompanionCrops)


									# Output at the end of this loop: an updated 'edibleCompanionCrops' list with only the companion Crops
									# that can grow with the x.SelectedCrop
									# ATTENTION: CompanionCrops with a Cash Crop do not have the same density as if they were alone: 50%

		###############################

		month = int(x.GSstart)
		x.indexWR = {}
		WaterResources_acceptable	=	( (ETc_GSmin(x.SelectedCrop, month, x, PRA) * TOLERdrought(x.SelectedCrop)) < WaterResources(month, x.GSstart, PRA, x.SelectedCrop, x) < (ETc_GSmin(x.SelectedCrop, month, x, PRA) * TOLERflood(x.SelectedCrop)) )
		WaterResources_ideal		=	( ETc_GSmin(x.SelectedCrop, month, x, PRA) < WaterResources(month, x.GSstart, PRA, x.SelectedCrop, x) < (ETc_GSmin(x.SelectedCrop, month, x, PRA) * TOLERflood(x.SelectedCrop)) )
		x.CCwater = {}

		if len(x.edibleCompanionCrops) == 1:
			x.SelectedCC = x.edibleCompanionCrops[0]

		# else: #  len(x.edibleCompanionCrops) >= 1 : each "non edible" crop has been deleted while the last loop
		for crop in x.edibleCompanionCrops:
			#~ CROProw = crop
			x.CCwater[crop] = 0
			month = int(x.GSstart)
			end_GSmin_SelectedCrop = month + GSmin(x.SelectedCrop)

			while month <= end_GSmin_SelectedCrop:

				if WaterResources_ideal:
					x.CCwater[crop] += 4

				elif WaterResources_acceptable:

					if WRmargin_GSmin(crop, month, x, PRA) >= 0.8:
						x.CCwater[crop] += 3
					elif WRmargin_GSmin(crop, month, x, PRA) >= 0.5:
						x.CCwater[crop] += 2
					elif WRmargin_GSmin(crop, month, x, PRA) >= 0.2:
						x.CCwater[crop] += 1
					elif WRmargin_GSmin(crop, month, x, PRA) >= 0.0:
						x.CCwater[crop] += 0

				else :
				# the crop's Water Requirements do not match with the PRA's Water Resources
				# -> this crop is deleted from the dictionary
					x.edibleCompanionCrops = [c for c in x.edibleCompanionCrops if c != crop] # removing the crop from 'edibleCompanionCrops'
					if x.edibleCompanionCrops == []:
						x.SelectedCC = None
					break # switch to next crop

				month += 1

			# Standardizing the CCwater indices according to the maximum (indices between 1 and 0, with 1 the better conditions)
			if crop in x.CCwater:
				x.CCwater[crop] = x.CCwater[crop] / round(max( x.CCwater.values() ), 3)

				# END for (crop in x.edibleCompanionCrops)


	else: # if the list x.edibleCompanionCrops is empty
		x.SelectedCC = None


#----------------------------------------------------------------------------------------------------------------

def ASSESS_Nutrients_CompanionCrop(x, PRA):
	"""INPUT :
	*	x		is the class that contains all self variables used in all VegAu's functions

	FUNCTION:
	If the SelectedCrop tolerates a CompanionCrop (acc. to Water Requirement and Resources), cheking if there is enough nutrients for it to grow:
	Nfix(crop) - Nremoved(crop) > x.ActualStand[PRA]['N']

	OUTPUT:
	Average margin for each nutrient and for each 'edibleCrops' and associates this value with indexNutrients[crop][nutrient].
	If a margin is negative while GSmin(x.SelectedCC), this SelectedCC is deleted from the dict 'indexNutrients' and 'edibleCrops'.
	Takes the decomposition of previous crops into account.
	"""

	try:

		print("[{}][{}]	Calculation nutrient margins for edible Companion Crops...".format(PRA, x.EndPreviousCrop_later))

		for crop in x.edibleCompanionCrops :

			x.indexNutrients[crop] = {'N': [], 'P': [], 'K': [], 'Na': [],'Mg': [], 'Ca': [], 'Mn': [], 'Fe': [], 'Cu': []}



			#--------------------------------------
			print("			Testing {}...".format( prod_EN(crop) ))

			# ---------------------------------------------------------------------------------------------------------
			# if the nutrient amount in the PRA's soil is not sufficient while GSmin(crop),
			# the Selected Companion Crop is not considered as x.edible anymore:
			removed = {"N": removedN(crop), "P": removedP(crop),
					   "K": removedK(crop), "Na": removedNa(crop),
					   "Mg": removedMg(crop), "Ca": removedCa(crop),
					   "Mn": removedMn(crop), "Fe": removedFe(crop),
					   "Cu": removedCu(crop)}

			for nutrient in x.indexNutrients[crop].keys():
				x.indexNutrients[crop][nutrient] = []
				monthInGS = 1
				actual_stand = dict(x.ActualStand[PRA])
				end_GSmin = monthInGS + GSmin(crop)

				# -------------------------------------------------------------------------------------------------------------

				while monthInGS <= end_GSmin: # Simulation according to the ActualStand values for each GS month

					if nutrient == 'N': # N can be fixed : separated margin assessment
						margin = (actual_stand[nutrient] + x.decomposition_month[monthInGS][
							nutrient] - ((removed[nutrient] - fixedN(crop)) / GSmin(crop)))

					else:
						margin = (actual_stand[nutrient] + x.decomposition_month[monthInGS][
							nutrient] - (removed[nutrient] / GSmin(crop)))

					# NOTICE :	divison by GSmin assuming that the nutrient absorption is stable while GSmin
					# 			(monthly assessment)
					# ---------------------------------------------------------------------------------------------------------

					if margin < 0 :
						print("			Not enough {} for growing {}...".format(nutrient, prod_EN(crop)))
						x.edibleCompanionCrops = [CC for CC in x.edibleCompanionCrops if CC != crop]
						del x.indexNutrients[crop]

						# breaking the loop to assess the nutrient margins for this new crop :
						assert x.edibleCompanionCrops != []
						# If there are still x.edible Companion Crops, another one is chosen according to its Water Requirements:	#
						# for crop in x.edibleCompanionCrops :																		# state for the function before the replacement
						# 	if x.CCwater[crop] == max(x.CCwater.values()):													# by the next line (we consider all edible ComppanionCrops anyway !...?)
						# 		crop = str(crop)																					#


					else:
						# average removed and fixed nutrient for one month of GSmin(crop):
						x.indexNutrients[crop][nutrient].append(margin)


						# END if (margin negative) -------------------------------------------------------------------------

					monthInGS += 1

					# END while (end of GSmin : x.indexNutrients contains margins for all eventual CC for the whole GSmin)-


				# Standardization of nutrient margins acc. to the amount of remaining edible cover crops :
				x.indexNutrients[crop][nutrient] = sum(x.indexNutrients[crop][nutrient]) / len(x.indexNutrients[crop][nutrient])


				# END for (nutrient) ----------------------------------------------------------------------------------------------------

			x.indexNutrients[crop] = [round(nutrient_amount / max(x.indexNutrients[crop].values()), 3) for
			                           nutrient_amount in x.indexNutrients[crop].values()]
			# END for (crop in x.edibleCompanionCrops)-----------------------------------------------------------------------------------


	except AssertionError:  # crop == None, x.edibleCompanionCrops is empty
		x.SelectedCC = None
		print("			No companion crop available.")
#----------------------------------------------------------------------------------------------------------------

def SELECT_CompanionCrop(x, PRA):

	if prodCAT(x.SelectedCrop) != 0 : # if prodCAT == 0, the Selected crop is already a cover/companion crop !

		#=========================================================================================================

		ASSESS_Water_CompanionCrop(x, PRA)
		# This function gives back a dict x.CCwater with standardized indices for the WR quality
		ASSESS_Nutrients_CompanionCrop(x, PRA)
		# This function updates the x.indexNutrients dict with standardized indices for nutrients availability

		selection = {}

		if x.edibleCompanionCrops != [] or x.SelectedCC != None:
			for crop in x.edibleCompanionCrops:
				selection[crop] = x.CCwater[crop]/x.indexNutrients[crop]
			# Choosing the higher index :
			selection = [crop for crop in x.edibleCompanionCrops if selection[crop] == max(selection)]
			x.SelectedCC = max(selection)

			print("Companion crop selected: {}".format(prod_EN(x.SelectedCC)))


		else:
			print("[{}][{}]	There are no edible Companion Crop for the currently Selected Crop.".format(PRA, x.EndPreviousCrop_later))
			x.SelectedCC = None

	x.rotat[PRA][-1] = (x.rotat[PRA][-1][0], x.SelectedCC, x.rotat[PRA][-1][2])

#================================================================================================================
#================================================================================================================


def APPLY_ResiduesDecomposition_of_PreviousCrops(PRA, x):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions

	OUTPUT:
	Residues that are RETURNED BY THE PREVIOUS CROP while the GS of the newly x.SelectedCrop.
	"""
	
	
	print("[{}][{}]	Calculating the nutrients that are returned by the previous crops...".format(PRA, x.EndPreviousCrop_later))
	monthInGS = 1
	
	
	# Calculated the nutrients that are returned by the previous crop by the GS of the newly x.SelectedCrop:
	while monthInGS <= GSmin(x.SelectedCrop):
		for nutrient in x.ActualStand[PRA].keys():
			if monthInGS not in x.decomposition_month.keys():
				x.decomposition_month[monthInGS] = {}
				x.decomposition_month[monthInGS] = 0
			if monthInGS == 1:								# minerals that still had 1 month delay before mineralization 
				x.ActualStand[PRA][nutrient] += x.decomposition_month[1][nutrient]	# at x.GSstart-1 are yet available to x.SelectedCrop
		monthInGS += 1

	for i in sorted(x.decomposition_month.keys()) :
		try:
			x.decomposition_month[i] = x.decomposition_month[i+1]	# updating mineralization delay: mineralization delay reduces each month by 1 month (while GS)

		except KeyError: # the last month (i) has no following month (i+1)
			# --> rebuilding the dict acc. to the initial NutrientList (allows to add nutrients in the list and be sure
			#     that the change will be taken into account in the whole script
			for nutrient in x.ActualStand:
				x.decomposition_month[i][nutrient] = 0

#================================================================================================================
#================================================================================================================


def APPLY_ResiduesDecomposition_of_CompanionCrop(x):
	"""INPUT :
	*	x		is the class that contains all self variables used in all VegAu's functions

	FUNCTION:
	Calculating the residues that remain after the x.SelectedCC according to the functions from the STICS model
	and the parameter described in Justes et al. (2009).

	OUTPUT:
	updated 'x.decomposition_month' dictionary
	"""


	Residues = {"N": returnedN(x.SelectedCC), "P": returnedP(x.SelectedCC), "K": returnedK(x.SelectedCC), "OM": returnedOM(x.SelectedCC)}

	print("			Simulating the Residues Decomposition for the selected Companion Crop...")

	i = 1
	# to avoid an infinite number of months in the dict 'month', the loop stops automatically after 8 years (96 months):
	while i < 97:
		for nutrient in Residues.keys():
			mineralizedN_amount = mineralizedN(x.SelectedCC, i) - mineralizedN(x.SelectedCC, i - 1)
			mineralizedCPK_amount = mineralizedCPK(x.SelectedCC, i) - mineralizedCPK(x.SelectedCC, i - 1)
			# the functions mineralizedCPK(crop, month) and mineralizedN(crop, month) give the mineralized stuff amount at month[i]
			# to get the mineralized amount while month[i] only --> month[i] - month [i-1]
			while mineralizedN_amount > 0 or mineralizedCKN_amount > 0:

				if nutrient == 'N':
					x.decomposition_month[i][nutrient] += mineralizedN_amount/2 # The density of a CompanionCrop can't be as high as if it were grown alone -> divided by 2
				else:
					x.decomposition_month[i][nutrient] += mineralizedCPK_amount/2
				# decomposition of each nutrient have been assessed for month i

		i += 1 # switching to next month

#----------------------------------------------------------------------------------------------------------------

def APPLY_SelectedCC_Kill(PRA, x):
	"""INPUT :
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions

	OUTPUT:
	Amounts of removed nutrients by the Selected Companion Crop while the current crop's GS.
	It takes into account the decomposition of previous crop thanks the dictionary x.decomposition_month in the
	function APPLY_ResiduesDecomposition_of_CompanionCrop(x).
	"""


	if x.SelectedCC != None:
		monthInGS = 1
		# Calculated the nutrients that are returned by the previous crop by the GS of the newly x.SelectedCC:
		while monthInGS <= GSmin(x.SelectedCC):
			x.ActualStand[PRA]['N'] - removedN(x.SelectedCC)
			x.ActualStand[PRA]['P'] - removedP(x.SelectedCC)
			x.ActualStand[PRA]['K'] -= removedK(x.SelectedCC)
			x.ActualStand[PRA]['Na'] -= removedNa(x.SelectedCC)
			x.ActualStand[PRA]['Mg'] -= removedMg(x.SelectedCC)
			x.ActualStand[PRA]['Ca'] -= removedCa(x.SelectedCC)
			x.ActualStand[PRA]['Mn'] -= removedMn(x.SelectedCC)
			x.ActualStand[PRA]['Fe'] -= removedFe(x.SelectedCC)
			x.ActualStand[PRA]['Cu'] -= removedCu(x.SelectedCC)


		print("[{}][{}]".format(PRA, x.EndPreviousCrop_later), """	Simulating the residues decomposition of the Selected Companion Crop...""")
		APPLY_ResiduesDecomposition_of_CompanionCrop(x)
		print("	OK")
		#END if


#================================================================================================================
#================================================================================================================


def APPLY_ResiduesDecomposition_of_SelectedCrop(x):
	"""INPUT :
	*	x		is the class that contains all self variables used in all VegAu's functions

	OUTPUT:
	Residues that remain after the x.SelectedCrop according to the functions from the STICS model
	and the parameter described in Justes et al. (2009).
	"""

	Residues = {"N": returnedN(x.SelectedCrop), "P": returnedP(x.SelectedCrop), "K": returnedK(x.SelectedCrop), "OM": returnedOM(x.SelectedCrop)}

	# assert len([x for x in Residues.values() if x >= 0]) == len(Residues), """All amounts of returned residues are not positive !
	# ---> Fix the functions returnedXX(crop), with XX the nutrients name.
	# Concerned nutrients are : {}""".format([x for x in Residues.values() if x > 0])

	#~ Dictionnary that contains ALL NUTRIENTS: usable if we have all nutrient amounts for straw
	#~ ReturnedMinerals = {"N": returnedN(x.SelectedCrop), "P": returnedP(x.SelectedCrop), "K": returnedK(x.SelectedCrop), "Na": returnedNa(x.SelectedCrop), "Mg": returnedMg(x.SelectedCrop), "Ca": returnedCa(x.SelectedCrop), "Mn": returnedMn(x.SelectedCrop), "Fe": returnedFe(x.SelectedCrop), "Cu": returnedCu(x.SelectedCrop), "OM": returnedOM(x.SelectedCrop)}
	
	try:
		i = 1
		while i < 97: # to avoid an infinite number of months in the dict 'x.decomposition_month', the loop stops automatically after 8 years
			mineralizedN_percentage = mineralizedN(x.SelectedCrop, i)
			mineralizedN_percentageDiff = mineralizedN(x.SelectedCrop, i) - mineralizedN(x.SelectedCrop, i - 1)
			mineralizedCPK_percentage = mineralizedCPK(x.SelectedCrop, i) - mineralizedCPK(x.SelectedCrop, i - 1)
			# the functions mineralizedCPK(crop, month) and mineralizedN(crop, month) give the mineralized stuff amount at month[i]
			# to get the mineralized amount while x.decomposition_month[i] only --> x.decomposition_month[i] - x.decomposition_month [i-1]

			for nutrient in Residues.keys():

				# if (nutrient == 'N' and mineralizedN_amount > 0) or ( nutrient != 'N' and mineralizedCPK_amount > 0) :
				if nutrient == 'N':
					if mineralizedN_percentageDiff > 0 :
						# The first mineralization amoount may be negative, especially for cereals (bacteria feed on their N to decompose their C)
						x.decomposition_month[i][nutrient] += mineralizedN_percentageDiff * Residues['N']
					else:
						x.decomposition_month[i][nutrient] += mineralizedN_percentage * Residues['N']
				else:
					x.decomposition_month[i][nutrient] += mineralizedCPK_percentage * Residues[nutrient]
				# decomposition of each nutrient have been assessed for month i

			#print(mineralizedCPK_percentage,"	|	", mineralizedN_percentage)
			i += 1 # switching to next month
	except TypeError:
		print("TypeError: 'int' object is not subscriptable")
		print("[{}][{}]".format(PRA, x.EndPreviousCrop_later), """	"Type of :
		x.decomposition_month --> {}""".format(type(x.decomposition_month)))
#----------------------------------------------------------------------------------------------------------------

def APPLY_SelectedCrop_Harvest(PRA, x):
	"""INPUT :
	*	crop 	is the ID of a current crop. It allows to call the related data in the 'plants' dictionary.
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions

	OUTPUT:
	Amounts of removed nutrients while the current crop GS.
	It takes into account the decomposition of previous crop thanks the dictionary x.decomposition_month.
	"""
	

	monthInGS = 1
	end_of_the_shortest_GS = GSmin(x.SelectedCrop)
	# Calculating the nutrients that are REMOVED while the GS of the newly x.SelectedCrop:
	print("			Simulating the nutrient uptakes by the Selected Crop...")
	
	while monthInGS <= end_of_the_shortest_GS:
		x.ActualStand[PRA]['N'] -= removedN(x.SelectedCrop)
		x.ActualStand[PRA]['P'] -= removedP(x.SelectedCrop)
		x.ActualStand[PRA]['K'] -= removedK(x.SelectedCrop)
		x.ActualStand[PRA]['Na'] -= removedNa(x.SelectedCrop)
		x.ActualStand[PRA]['Mg'] -= removedMg(x.SelectedCrop)
		x.ActualStand[PRA]['Ca'] -= removedCa(x.SelectedCrop)
		x.ActualStand[PRA]['Mn'] -= removedMn(x.SelectedCrop)
		x.ActualStand[PRA]['Fe'] -= removedFe(x.SelectedCrop)
		x.ActualStand[PRA]['Cu'] -= removedCu(x.SelectedCrop)
		monthInGS += 1
		
	# The following function calculates the residues that remain after the x.SelectedCrop:
	APPLY_ResiduesDecomposition_of_SelectedCrop(x)


#================================================================================================================
#================================================================================================================


def UPDATE_VERIFprodBOT_and_PestsDiseases_in_rotation(PRA, x):
	"""INPUT :
	*	PRA		is the ID of a current PRA. It allows to call the related data in the 'environment' dictionary.
	*	x		is the class that contains all self variables used in all VegAu's functions


	FUNCTION:
	If there is no one in the dictionary and verifies if the minimum return period is respected.
	If respected : no Pest and Diseases malus
	If not respected : +1 for this crop in the dict 'PestsDiseases_in_rotation'.
	In both cases, the 'Duration since previous crop' returns to 0.

	OUTPUT:
	*	updated 'x.VERIFprodBOT' dictionary
	*	updated 'PestsDiseases_in_rotation' dictionary
	"""

	print("			Verifying if the minimum return period is respected...")


	# ==================================================
	if x.SelectedCrop not in x.VERIFprodBOT :
		x.VERIFprodBOT[prodBOT(x.SelectedCrop)] = {'Duration since previous crop': 0, 'Crops in Rotation': 1}

	elif x.EndPreviousCrop_earlier < x.GSstart < x.EndPreviousCrop_later:
		for BotanicFamily in x.VERIFprodBOT.keys():
			x.VERIFprodBOT[BotanicFamily][
				'Duration since previous crop'] += GSmin(x.SelectedCrop) + x.GSstart - x.EndPreviousCrop_earlier
	elif x.GSstart > x.EndPreviousCrop_later:
		for BotanicFamily in x.VERIFprodBOT.keys():
			x.VERIFprodBOT[BotanicFamily][
				'Duration since previous crop'] += GSmin(x.SelectedCrop) + x.GSstart - x.EndPreviousCrop_later

	else :
		print("ERROR ! Can't increment the VERIFprodBOT dict...")

	# ==================================================


	# x.SelectedCrop is added to the list of the crops added to the rotation :

	if prodBOT(x.SelectedCrop) in x.VERIFprodBOT.keys():

		x.VERIFprodBOT[prodBOT(x.SelectedCrop)]['Crops in Rotation'] += 1	# This variable is unused in the script
																			# but may be interesting to observe as a result

		if x.VERIFprodBOT[prodBOT(x.SelectedCrop)]['Duration since previous crop']//12 < period(x.SelectedCrop):

			# if the minimum return period is not respected:
			#------------------------------------------------------------------------------------
			x.VERIFprodBOT[prodBOT(x.SelectedCrop)]['Duration since previous crop'] = 0

			# adding an entry to the dict 'PestsDiseases_in_rotation' for this crop or incrementing its already existing value:
			if PRA in x.PestsDiseases_in_rotation.keys():
					x.PestsDiseases_in_rotation[PRA] += 1
			else:
				x.PestsDiseases_in_rotation[PRA] = 1

			print("""

			There is already a crop from the same botanic family of the x.SelectedCrop in the rotation...
			Incrementing the 'PestsDiseases_in_rotation' index for the botanic family of this crop (PestsDiseases_in_rotation = {}).""".format(
				x.PestsDiseases_in_rotation[PRA]))


		else:
			x.VERIFprodBOT[prodBOT(x.SelectedCrop)]['Duration since previous crop'] = 0


			#END if (min return period not respected)--------------------------------------------

	else:
		x.VERIFprodBOT[prodBOT(x.SelectedCrop)] = {'Duration since previous crop': 0, 'Crops in Rotation': 1}
		# normally it has already been done in the function SelectCrop(x, PRA)

		# END if (prodBOT(SelectedCrop in VERIFprodBOT)--------------------------------------------


