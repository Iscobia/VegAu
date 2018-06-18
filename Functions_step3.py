#!/usr/bin/python3.4
# -*-coding:Utf-8 -* 
"""Module containing the functions for :
VegAu, STEP3: Building a typical Crop Rotation for each PRA according to Climate and Soil Data

ATTENTION :
This program only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
The import of this sheet is ensured by the module 'importingODS.py'"""

#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

# Notice: Variables from the 'nutrition' dictionary are in importedVariables.

from CanadaHealth import Canada_Health	# dictionary containing the Dietary Reference Intakes calculated by Canada Health

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts

from inputFR import nutrition



#########################################
#										#
#			PRIMARY FUNCTIONS			#
#										#
#########################################


def MDL_QTTperPerson(x, nutrition):
	"""INPUT :
	*	x			is the class that contains all self variables used in all VegAu's functions
	*	nutrition	is the dictionary that has been imported from 'input[COUNTRY].py'
					(e.g. 'inputFR.py' for France).

	--------------------------------------------------------------

	FUNCTION:
		* FIRST PART :
			It sums the nutrients and vitamins of all products in the appropriate variables (1 variable
			per nutritional feature) of the dictionary 'TotalNutrients' (each key corresponds to a
			nutrient, a vitamin or another dietetic feature)

		* SECOND PART :
			This function updates the 'TotalNutrients' dictionary by dividing each nutrient amount by the total population.

	--------------------------------------------------------------

	OUTPUT:
		* FISRT PART :
			* the dictionary x.TotalNutrients with the average daily resources
		* SECOND PART :
			* updated 'TotalNutrient' dictionary with the average nutrient quantity per person
	"""

	# ==========================================================================================#
	# ==========================================================================================#
	#		STEP 3, PART 1 : updating x.TotalNutrients 											#
	# 						 (calculating the average daily (nutrient) resources per person)	#
	# ==========================================================================================#
	# ==========================================================================================#

	# --> Summing the nutrients and vitamins of all products in the appropriate variables (1 variable per nutritional feature)
	# of the dictionary 'TotalNutrients' (each key corresponds to a nutrient, vitamin or other dietetic feature)

	print("""			Calculating the daily amount of each product per person and the total intake of each
			nutrient for the total population...""")
	
	x.dietary_results   = {}
	x.TotalNutrients    = {}
	
	x.totalYields = x.totalYields["TOTAL"]

	x.WeeklyResources = {}
	totalPopulation = 64859599

	for crop in x.totalYields:

		if crop == "FBRflx":
			# for fibre flax, yields are given for the fibre : for a fibre yield of 4.94 t/ha, there are 1 t/ha of seeds.

			# converting the total Yields from tons to kilograms
			total_yield = round( float(x.totalYields[crop])/4.94 * 1000,  3)

		else:
			# converting the total Yields from tons to kilograms
			total_yield = round(float(x.totalYields[crop]) * 1000, 3)

		productQuantity     = float(prodQUANTITY(crop))

		x.WeeklyResources[crop]  = (((total_yield * productQuantity) / 365) * 7) / totalPopulation

		print("{} : {} piece per week ({} kg, so {} kg in one year)".format(prod_EN(crop), x.WeeklyResources[crop], total_yield/365*7, total_yield))

		# -------------------------------------------------------------------------------------------------------------------------
		CropNutrients = {
			'Mg': Magnesium(crop),
			'P'	:	Phosphore(crop),
			'K'		:	Potassium(crop),
			'Ca'	:	Calcium(crop),
			'Mn'	:	Manganese(crop),
			'Fe'	:	Fer(crop),
			'Cu'	:	Cuivre(crop),
			'Zn'	:	Zinc(crop),
			'Se'	:	Selenium(crop),
			'I'		:	Iode(crop),
			'Proteins'		:	Proteins(crop),  # "protéines brutes" (in the Ciqual table)
			'carbohydrates'	:	Glucides(crop), # "Glucides" in the Cequal table
			'sugar'			:	Sucres(crop),
			'energy_kJ'		:	energie_kJ(crop), # calculated according to the "Réglement UE Né 1169/2011"'	:	do not take fibres into account
			'energy_kcal'	:	energie_kcal(crop), # calculated according to the "Réglement UE Né 1169/2011"'	:	do not take fibres into account
			'lipids'		:	lipides(crop),
			'vitA'	:	vitA(crop),
			'vitD'	:	vitD(crop),
			'vitE'	:	vitE(crop),
			'vitC'	:	vitC(crop),
			'vitB1'	:	vitB1(crop),	# Thiamine
			'vitB2'	:	vitB2(crop),	# Riboflavine
			'vitB3'	:	vitB3(crop),	# PP or Niacine
			'vitB5'	:	vitB5(crop),	# pentothénique acid
			'vitB6'	:	vitB6(crop),
			'vitB12':	vitB12(crop),
			'vitB9'	:	vitB9(crop),	# total folates ("Folates totaux")
		}


		x.TotalNutrients[crop] = dict(CropNutrients)

		for nutrient in x.TotalNutrients[crop].keys():
			#===========================================================================================================
			# Calculating the nutrients for each crop (to get an idea of how it contributes to the total nutrients intake):
			# Updating the total nutrients amount that the crop can give each day acc. to its average yearly yield:
			try:
				x.TotalNutrients[crop][nutrient] *= total_yield / 365
			except TypeError:
				# the value for x.TotalNutrients[crop][nutrient] (from the original database) may be '':
				x.TotalNutrients[crop][nutrient] = 0

			# ===========================================================================================================
			# For calculating the total nutrients intake
			# adding the nutritional value of the current crop to x.TotalNutrients :

			if nutrient not in x.TotalNutrients:
				x.TotalNutrients[nutrient] = x.TotalNutrients[crop][nutrient]
			else :
				x.TotalNutrients[nutrient] += x.TotalNutrients[crop][nutrient]

			# END for (crop in x.totalYields.keys())-------------------------------------------------------------------------------------



	# ==========================================================================================#
	# ==========================================================================================#
	#		STEP 3, PART 2 : dividing each nutrient amount by the total population				#
	# ==========================================================================================#
	# ==========================================================================================#

	print("""			Calculating the average daily intake amount per person...""")

	# totalPopulation = 64859599  # INSEE, estimated population for the 1st of January 2017
	PopulationPyramid = {
		'Nourrissons': {'0-6 mois': 714683 / 2, '7-12 mois': 714683 / 2},
		'Enfants': {'1-3 ans': 2243173, '4-8 ans': 3990871},
		'Femmes': {
			'9-13 ans': 1958610,
			'14-18 ans': 1949007,
			'19-30 ans': 4493007,
			'31-50 ans': 8440846,
			'51-70 ans': 8410878,
			'> 70 ans': 4772705},

		'Hommes': {
			'9-13 ans': 2052720,
			'14-18 ans': 2047672,
			'19-30 ans': 4502265,
			'31-50 ans': 8248735,
			'51-70 ans': 7800488,
			'> 70 ans': 3233939}
	}


	NutrientsName = {
		'Mg'    : 'Magnésium',
		'P'	    :	'Phosphore',
		'K'		:	'Potassium',
		'Ca'	:	'Calcium',
		'Mn'	:	'Manganèse',
		'Fe'	:	'Fer',
		'Cu'	:	'Cuivre',
		'Zn'	:	'Zinc',
		'Se'	:	'Sélénium',
		'I'		:	'Iode',
		'Proteins'		:	'Protéines totales (g/jour',
		'carbohydrates'	:	'Glucides digestibles',
		# ~ 'sugar'			:
		# ~ 'energy_kJ'		:
		# ~ 'energy_kcal'	:
		'lipids'		:	'Lipides totaux',
		'vitA'	:	'Vitamine A',
		'vitD'	:	'Vitamine D',
		# ~ 'vitE'	:	'Vitamine E'  # do not exists in Canada_Health
		'vitC'	:	'Vitamine C',
		'vitB1'	:	'Thiamine',
		'vitB2'	:	'Riboflavine',
		'vitB3'	:	'Niacine',
		'vitB5'	:	'Acide panthoénique',
		'vitB6'	:	'B6',
		'vitB12':	'B12',
		'vitB9'	:	'Folate'
	}

	IntakeThreshold = [('BME', 'sumBME', 'pctBME'), ('AS', 'sumANR_AS', 'pctANR_AS'), ('AMT', 'sumAMT', 'pctAMT')]
	
	for gender in sorted(PopulationPyramid):

		for age in sorted(PopulationPyramid[gender]):

			for nutrient in sorted(NutrientsName) :

				if nutrient not in x.dietary_results :
					x.dietary_results[nutrient] = {}

				for elt in sorted( Canada_Health.keys() ):

					#---------------------------------------------------------------------------------------------------

					if NutrientsName[nutrient] in elt and "IU /jour" not in elt: # Interantional Units are not given in the Ciqual database

						for i, threshold in enumerate(IntakeThreshold):

							if IntakeThreshold[i][0] in elt:
								if Canada_Health[elt][gender][age] == 'ND':
									pass

								else:
									if IntakeThreshold[i][1] in x.dietary_results[nutrient]:
										x.dietary_results[nutrient][IntakeThreshold[i][1]] += Canada_Health[elt][gender][age] * PopulationPyramid[gender][age]
									else:
										x.dietary_results[nutrient][  IntakeThreshold[i][1]  ] = Canada_Health[elt][gender][age] * PopulationPyramid[gender][age]


						# END if (NutrientsName[nutrient] in elt)-------------------------------------------------------

					# END for (elt in Canada_Health)--------------------------------------------------------------------

				# END for (nutrient)------------------------------------------------------------------------------------

			# END for (age)---------------------------------------------------------------------------------------------

		# END for (gender)----------------------------------------------------------------------------------------------


	for nutrient in sorted(NutrientsName):

		for i, threshold in enumerate(IntakeThreshold):

			if IntakeThreshold[i][1] in x.dietary_results[nutrient]:
				# if the threshold value was 'NB' in the CanadaHealth database, there is no value
				x.dietary_results[nutrient][IntakeThreshold[i][2]] = x.TotalNutrients[
																		 nutrient] / x.dietary_results[nutrient][
																		 IntakeThreshold[i][1]]
				# del x.dietary_results[nutrient][IntakeThreshold[i][1]]

	#===================================================================================================================
	print("""			Summarizing values to get global averages...""")
	# Calculating an average value for all nutrients together to get an overview :
	for nutrient in NutrientsName:
		
		#-----------------------------------------------------------------------------------------------------

		# 1 -- summing all percentages (for all nutrients) and taking h*the amount of data into account:
		# (not always the same acc. to the amount of 'NA' in the CanadaHealth database)
		for pctThreshold in x.dietary_results[nutrient]:

			if pctThreshold not in x.dietary_results:

				x.dietary_results[pctThreshold] = [0, 0]

				x.dietary_results[pctThreshold][0] += x.dietary_results[nutrient][pctThreshold]
				x.dietary_results[pctThreshold][1] += 1

			else:
				x.dietary_results[pctThreshold][0] += x.dietary_results[nutrient][pctThreshold]
				x.dietary_results[pctThreshold][1] += 1

		# -----------------------------------------------------------------------------------------------------

		# 2 -- calculating the average for all threshold type :

	for i, threshold in enumerate(IntakeThreshold):
		# IntakeThreshold[i][2] corresponds to "pctThreshold"
		
		x.dietary_results[ IntakeThreshold[i][1] ]  = x.dietary_results[IntakeThreshold[i][1]][0] / x.dietary_results[IntakeThreshold[i][1]][1]
		x.dietary_results[ IntakeThreshold[i][2] ]	= x.dietary_results[ IntakeThreshold[i][2] ][0]	/	x.dietary_results[ IntakeThreshold[i][2] ][1]



	