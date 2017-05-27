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

from selfVariables import x
from CanadaHealth import Canada_Health	# dictionary containing the Dietary Reference Intakes calculated by Canada Health

from importedVariables import *	# lambda functions to access easier to the data from the abode imported dicts

from inputFR import nutrition

#########################################
#										#
#			PRIMARY FUNCTIONS			#
#										#
#########################################


def MDL_QTTperPERSON(x, nutrition):
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
			* updated 'TotalNutrient' dictionnay with the average nutrient quantity per person
			* fulfilled 'NUTRIassess' sheet
			* fulfilled 'Results' sheet
	"""

	# ==========================================================================================#
	# ==========================================================================================#
	#		STEP 3, PART 1 : updating x.TotalNutrients 											#
	# 						 (calculating the average daily (nutrient) resources per person)	#
	# ==========================================================================================#
	# ==========================================================================================#

	# --> Summing the nutrients and vitamins of all products in the appropriate variables (1 variable per nutritional feature)
	# of the dictionary 'TotalNutrients' (each key corresponds to a nutrient, vitamin or other dietetic feature)


	x.DailyResources = {}
	totalPopulation = 64859599

	for crop in x.totalYields:
		# converting the total Yields from tons to kilogramms
		# total_yield			=	round(float(x.totalYields[crop]) * 1000, 3) # x.totalYields gives bigger amounts than x.totalYields... waiting better results
		total_yield = round(float(x.totalYields[crop]) * 1000, 3)
		productQuantity = float(prodQUANTITY(crop))
		x.DailyResources[crop] = ((total_yield * productQuantity) / 365) / totalPopulation

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
			'Proteins'		:	Proteinses(crop),  # "protéines brutes" (in the Ciqual table)
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
			'vitB5'	:	vitB5,			# pentothénique acid
			'vitB6'	:	vitB6(crop),
			'vitB12':	vitB12(crop),
			'vitB9'	:	vitB9(crop),	# total folates ("Folates totaux")
		}


		x.TotalNutrients[crop] = {}

		for nutrient in CropNutrients.keys():
			if nutrient not in  x.TotalNutrients[crop].keys():
				x.TotalNutrients[nutrient] = 0
			else:
				# adding the nutritional value of the current crop to x.TotalNutrients :
				x.TotalNutrients[nutrient] += (CropNutrients[nutrient] * yearly_Yield) / 365



			# END for (crop in x.totalYields.keys())-------------------------------------------------------------------------------------


	# ==========================================================================================#
	# ==========================================================================================#
	#		STEP 3, PART 2 : dividing each nutrient amount by the total population				#
	# ==========================================================================================#
	# ==========================================================================================#

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
			'>70 ans': 4772705},

		'Hommes': {
			'9-13 ans': 2052720,
			'14-18 ans': 2047672,
			'19-30 ans': 4502265,
			'31-50 ans': 8248735,
			'51-70 ans': 7800488,
			'>70 ans': 3233939}
	}


	NutrientsName = {
		'Mg': 'Magnésium',
		'P'	:	'Phosphore',
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
		'vitB5'	:	'panto', # Acide pantothénique
		'vitB6'	:	'B6',
		'vitB12':	'B12',
		'vitB9'	:	'Folates'
	}

	for gender in PopulationPyramid.keys():
		x.results[gender] = {}

		for age in PopulationPyramid[gender].keys():
			x.results[gender][age] = {}
			for nutrient in x.TotalNutrients.keys():

				for elt in Canada_Health.keys():

					if NutrientsName[nutrient] in elt:
						x.results[gender][age][nutrient] = {}	# this dict will contain the individual percentage of
																# daily recommended intake amounts (min, max and average)
						print(elt)
						if 'BME' in elt :
							if Canada_Health[elt][gender][age] == 'ND':
								x.results[gender][age][nutrient]['pctBME'] = 'ND'
							else:
								x.results[gender][age][nutrient]['pctBME'] = x.TotalNutrients[nutrient] / Canada_Health[elt][gender][age]

						elif 'AS' in elt :
							if Canada_Health[elt][gender][age] == 'ND':
								x.results[gender][age][nutrient]['pctANR_AS'] = 'ND'
							else:
								x.results[gender][age][nutrient]['pctANR_AS'] = x.TotalNutrients[nutrient] / Canada_Health[elt][gender][age]

						elif 'AMT' in elt :
							if Canada_Health[elt][gender][age] == 'ND':
								x.results[gender][age][nutrient]['pctAMT'] = 'ND'
							else:
								x.results[gender][age][nutrient]['pctAMT'] = x.TotalNutrients[nutrient] / Canada_Health[elt][gender][age]

							# END if (NutrientsName[nutrient] in elt)--------------------------------------------------------------------------------

							# END for (elt in Canada_Health)---------------------------------------------------------------------------------------------

				if 'pctBME_sum' not in x.results and 'pctBME_nb' not in x.results:
					x.results['pctBME'] = [0, 0]
				else:
					x.results['pctBME'][0]	+= x.results[gender][age][nutrient]['pctBME']
					x.results['pctBME'][1]	+= 1

				if 'pctANR_AS_sum' not in x.results and 'pctANR_AS_nb' not in x.results:
					x.results['pctANR_AS'] = [0, 0]
				else:
					x.results['pctANR_AS'][0]	+= x.results[gender][age][nutrient]['pctANR_AS']
					x.results['pctANR_AS'][1]	+= 1

				if 'pctAMT_sum' not in x.results and 'pctAMT_nb' not in x.results:
					x.results['pctAMT'] = [0, 0]
				else:
					x.results['pctAMT'][0]	+= x.results[gender][age][nutrient]['pctAMT']
					x.results['pctAMT'][1]	+= 1

				# END for (nutrient)-------------------------------------------------------------------------------------------------------------

				# END for (age)----------------------------------------------------------------------------------------------------------------------

				# END for (gender)-----------------------------------------------------------------------------------------------------------------------


	x.results['pctBME']		=	x.results['pctBME'][0]	/	x.results['pctBME'][1]

	x.results['pctANR_AS']	=	x.results['pctANR_AS'][0 ]/	x.results['pctANR_AS'][1]

	x.results['pctAMT']		=	x.results['pctAMT'][0]	/	x.results['pctAMT'][1]



#~ def ASSESS_QTTperPERSON():
	#~ """This function updates the 'TotalNutrients' dictionary by dividing each nutrient amount by the total population
	#~ and copies the results in the sheet 'NUTRIassess' for each crop in order to keep a friendly interface to oberve the results.
	#~ 
	#~ OUTPUT:
	#~ * updated 'TotalNutrient' dictionnay with the average nutrient quantity per person 
	#~ * fulfilled 'NUTRIassess' sheet
	#~ * fulfilled 'Results' sheet
	#~ """
	#~ 
	#~ 
	#~ DailyIntakeAmount = {}
	#~ totalPopulation = 64859599 # INSEE, estimated population for the 1st of January 2017
	#~ PopulationPyramid = {
		#~ 'Nourrissons' : 714683
		#~ 'Enfants': {'1-3 ans': 2243173, '4-8 ans': 3990871},
		#~ 'Femmes': {
			#~ '9-13 ans' = 1958610,
			#~ '14-18 ans' = 1949007,
			#~ '19-30 ans' = 4493007,
			#~ '31-50 ans' = 8440846,
			#~ '51-70 ans' = 8410878,
			#~ '>70 ans' = 4772705},
#~ 
		#~ 'Hommes':{
			#~ '9-13 ans' = 2052720,
			#~ '14-18 ans' = 2047672,
			#~ '19-30 ans' = 4502265,
			#~ '31-50 ans' = 8248735,
			#~ '51-70 ans' = 7800488,
			#~ '>70 ans' = 3233939}
	#~ }
	#~ 
	#~ 
	#~ for crop in x.TotalNutrients.keys():
		#~ 
		#~ for nutrient in x.TotalNutrients[crop].keys():
			#~ # calculating the prod weight /person/years
			#~ x.TotalNutrients[crop][nutrient] 	/=	totalPopulation
#~ 
			#~ if x.TotalNutrients[nutrient] == 'Yield in kg' and prodQUANTITY(crop) != '':
				#~ # 'prodQUANTITY' is the average fruit/vegetable quantity that corresponds to the yields weight (cf "prod_qtt" column in 'NUTRITION')
				#~ WeeklyResources[crop] = x.TotalNutrients[crop]['Yield in kg'] / prodQUANTITY(crop) / (365/7)
				#~ DailyResources[crop] = x.TotalNutrients[crop]['Yield in kg'] / prodQUANTITY(crop) / 365
				#~ 
			#~ else:	
				#~ if nutrient not in DailyIntakeAmount.keys():
					#~ DailyIntakeAmount[nutrient] = 0
				#~ else:
					#~ DailyIntakeAmount[nutrient] += x.TotalNutrients[crop][nutrient] / 365 # average quantity per day 
			#~ 
			#~ 
		#~ print("This model built x.rotations that would allow the population to get :")
		#~ for nutrient in DailyIntakeAmount.keys() :
			#~ print("	* {} of {}".format( DailyIntakeAmount[nutrient] , nutrient) )
			

