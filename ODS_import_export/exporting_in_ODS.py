#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
#~ 
#~ 
#################################
#								#
#		IMPORTING MODULES		#
#								#
#################################
print("Importing modules...")

import os
import pyoo
import shutil

print("	OK")


#####################################
#									#
#	CONNECTING TO THE SPREADSHEET	#
#									#
#####################################

#==== IN LINUX ========================================================================
#in a terminal, run the following command for LibreOffice to connect to the right host:

#~ os.popen("""" soffice "--accept=socket,host=0,port=2002;urp;" """)
# libreoffice5.3 "--accept=socket,host=0,port=2002;urp;"
print("Connecting to pyoo...")
desktop = pyoo.Desktop('localhost', 2002)
print("	OK")


#=== IN WINDOWS =======================================================================
# CAUTION ! THIS IS ONLY A WORK AROUND ! The uno-bridge error is still not solved.
 
#~ # import socket
#~ # print("Connecting to pyoo...")
#~ # desktop = pyoo.Desktop('localhost', 2002)
#~ # print("	OK")


#=== FOR BOTH OS ======================================================================

#  Copying input.ods as output.ods :
print("Creating  'output.ods'  from  'input.ods'...")
shutil.copyfile('input.ods', 'output.ods')
print("	OK")

#  Opening output.ods :
print("Connecting to  'output.ods'...")
doc = desktop.open_spreadsheet("output.ods")
print("	OK")

#  Associating each output's sheet with its name:
print("Connection to output's spreadsheets...")
ENVIRONMENT	=	doc.sheets['ENVIRONMENT']
PLANTS		=	doc.sheets['PLANTS']
NUTRITION	=	doc.sheets['NUTRITION']
PRAvirgin	=	doc.sheets['PRAvirgin']
NUTRITIONvirgin	=	doc.sheets['NUTRITIONvirgin']
NUTRITION_RDA = doc.sheets['NUTRITION_Adequate Intakes']



#########################################
#										#
#	IMPORTING LAMBDAS FOR A CLEARER 	#
#			EXPORT SCRIPT				#
#										#
#########################################

#~ useless ?... je les laisse là pour le test: supression si inutiles
#~ print("Importing inputVariables.py...")
#~ from inputVariables import *
#~ print("	OK")

print("Importing the dictionnaries 'environment'and 'plants'...")
#~ utile ? 
from input import plants
from input import environment

#~ useless ?... je les laisse là pour le test: supression si inutiles
#~ #== row index for crops (key= prodID):
#~ from importedVariables import CROProw_PLANTS	
#~ from importedVariables import CROProw_NUTRITION	
#~ from importedVariables import CROProw_NUTRITIONvirgin
#~ 
#~ 
#~ #== column index for prodIDs (key = prodID):
#~ from importedVariables import CROPcol_PRAedibility	
#~ from importedVariables import CROPcol_PRAyields	
#~ 
#~ 
#~ #== row index for PRAs (key = PRA):
#~ from importedVariables import PRArow_ENVIRONMENT	
#~ from importedVariables import PRArow_PRAvirgin	
#~ 
#~ #== specific priority indices:
#~ ratioADAPT	= lambda prodID:	plants[prodID][62]
#~ from importedVariables import PRIORITYgeneral
#~ from importedVariables import PRIORITYfruits
#~ from importedVariables import PRIORITYtextile

print("	OK")


#############################################
#											#
#	  EXPORTING DATA TO 'PRAedibility'		#
#											#
#############################################

#=======================================================
#=== Creating the spreadsheet PRAedibility from PRAvirgin


print("Creating new sheet: PRAedibility...")

doc.sheets.copy('PRAvirgin', 'PRAedibility',3)
PRAedibility =	doc.sheets['PRAedibility']

print("	OK")

#=================================================================================================
#=================================================================================================


#== New columns in the sheet 'PRAedibility':

## total amount of edible crops for the current PRA  + lambda to call the variable from the table:
PRAedibility[0,2].value =	'edibleCropsNBR'
PRAedibility[0,3].value	=	'edibleCropsID'
PRAedibility[0,4].value	=	'edibleCropsEN'
PRAedibility[0,5].value	=	'edibleCropsFR'
PRAedibility[0,6].value	=	'edibleCropsDE'

#=====================================================================	


#== New rows in the sheet 'PRAedibility':
#	* 'prodSURFACE' gives the potential total surface covered by the selected crop
#	* 'ratioADAPT', 'PRIORITYgeneral', 'PRIORITYfruits' and 'PRIORITYtextile' give the different priority indices

# ATTENTION, function SIMPLIFIÉE LE  19 MARS 2017: SI PROBLÈMES, REPRENDRE L'ANCIENNE:
SURFrow = len(PRAvirgin_dict.keys())
PRAedibility[SURFrow,2].value = 'prodSURFACE'

SURFrow + 1 = adapt
SURFrow + 2 = general
SURFrow + 3 = fruits
SURFrow + 4 = textile

PRAedibility[ adapt,	1].value	= 'ratioADAPT'
PRAedibility[ general,	1].value	= 'PRIORITYgeneral'
PRAedibility[ fruits,	1].value	= 'PRIORITYfruits'
PRAedibility[ textile,	1].value	= 'PRIORITYtextile'	

#=====================================================================	
#== Exporting data in PRAedibility :

print("Exporting rotations in PRArotat... ")

for PRA in x.rotat.keys():
	col = 2
	PRArow = PRArow_PRAvirgin(PRA)
	
	PRAedibility[PRArow,2].value	=	edibleCropsNBR[PRA]
	PRAedibility[PRArow,3].value	=	edibleCropsID[PRA]
	PRAedibility[PRArow,4].value	=	edibleCropsEN[PRA]
	PRAedibility[PRArow,5].value	=	edibleCropsFR[PRA]
	PRAedibility[PRArow,6].value	=	edibleCropsDE[PRA]	
	
	#------------------------------------------
	
	for crop in plants.keys():
		col = CROPcol_PRAedibility(crop)
		
		PRAedibility[0,col].value		=	crop
		PRAedibility[PRArow,col].value	=	'edible'

		PRAedibility[SURFrow,col].value =	prodSURFACE[crop]
				
		PRAedibility[general,col].value	=	PRIORITYgeneral(crop)
		PRAedibility[fruits,col].value	=	PRIORITYfruits(crop)
		PRAedibility[textile,col].value =	PRIORITYtextile(crop)	

			
		#END for (crops in the rotation)
		
	#END for (PRA in rotat)
	
print("	OK")
	




prodSURFACE = lambda SURFrow,CROPcol: PRAedibility[SURFrow,CROPcol].value

#############################################
#											#
#		EXPORTING DATA TO 'PRArotat'		#
#											#
#############################################

#=======================================================
#=== Creating the spreadsheet PRArotat from PRAvirgin	

print("Creating new sheet: PRArotat...")
doc.sheets.copy('PRAvirgin', 'PRArotat',3)
PRArotat	=	doc.sheets['PRArotat']

print("	OK")



#=======================================================
#=== Functions relative to PRArotat:


def MonthID():
	global RotatMonth
	year = str( (RotatMonth//12)+1 )
	if RotatMonth % 12 == 1:
		return "jan"+year
	if RotatMonth % 12 == 2:
		return "fev"+year
	if RotatMonth % 12 == 3:
		return "mar"+year
	if RotatMonth % 12 == 4:
		return "avr"+year
	if RotatMonth % 12 == 5:
		return "mai"+year
	if RotatMonth % 12 == 6:
		return "jun"+year
	if RotatMonth % 12 == 7:
		return "jul"+year
	if RotatMonth % 12 == 8:
		return "aout"+year
	if RotatMonth % 12 == 9:
		return "sep"+year
	if RotatMonth % 12 == 10:
		return "oct"+year
	if RotatMonth % 12 == 11:
		return "nov"+year
	if RotatMonth % 12 == 12:
		return "dec"+year
		


#=======================================================
#===  Exporting data in PRArotat

print("Exporting rotations in PRArotat... ")

for PRA in x.rotat.keys():
	PRArow = PRArow_PRAvirgin(PRA)
	
	#-------------------------------------------------------------------------------------------------------------
	crops_list = [ i for i, tuple in enumerate(rotat[PRA]) ] # gives the list of crops in the rotation
	PRArotat[PRArow, 2].value	=	crops_list
	PRArotat[0, 3].value 		=  'Pests and Diseases'
	PRArotat[PRArow, 3].value	=	x.PestsDiseases_in_rotation[PRA] # give a integer that corresponds to the crops that may have been affected by pests or diseasess
	PRArow = rotat[PRA]['PRA row in PRAvirgin']
	#-------------------------------------------------------------------------------------------------------------
	
	col = 4
	RotatMonth = 3
	
	#------------------------------------------
	
	for crop in crops_list: # crops_list is actually the index list of all tuples (cropID, GSlenght) of rotat 
		month = 1
		cropID = rotat[PRA][crop][0]
		GSlength = rotat[PRA][crop][1]
		
		#--------------------------------------
		while month <= GSlength:
			PRArotat[0, col].value		= MonthID(RotatMonth)
			PRArotat[PRArow, col].value = cropID
			col += 1
			month += 1
			#END while (month in GS)
			
		#END for (crops in the rotation)
		
	#END for (PRA in rotat)
	
print("	OK")
	

#############################################
#											#
#		EXPORTING DATA TO 'PRAyields'		#
#											#
#############################################

#= New line :
totalYIELDS_row	=	len(yields) + 1 # +1 for the heading's row
PRAyields[totalYIELDS_row,1].value = 'Total Yield in the whole country'

#======================================================================

for PRA in yields.keys():
	PRArow = PRArow_PRAvirgin(PRA)
	
	for crop in yields[PRA].values():
		yield_in_PRA = yields[PRA][crop]
		totalYIELD = totalYields[crop]
		col = CROPcol_PRAyields(crop)
		PRAyields[ 0, col].value		=	prodID(crop)
		PRAyields[ PRA, col].value		=	yield_in_PRA
		PRAyields[ totalYIELDS_row, col].value	=	totalYIELD
		
		#END for (crop in 'yields')
	
	#END for (PRA in 'yields')


#############################################
#											#
#		EXPORTING DATA TO 'Results'			#
#											#
#############################################

#~ NUTRIassess[crop, 9 ].value = TotalNutrients[crop]['Mg'] / (365/7) # average quantity per week 
#~ NUTRIassess[crop, 10 ].value = TotalNutrients[crop]['P'] / (365/7)
#~ NUTRIassess[crop, 11 ].value = TotalNutrients[crop]['K'] / (365/7)
#~ NUTRIassess[crop, 12 ].value = TotalNutrients[crop]['Ca'] / (365/7)
#~ NUTRIassess[crop, 13 ].value = TotalNutrients[crop]['Mn'] / (365/7)
#~ NUTRIassess[crop, 14 ].value = TotalNutrients[crop]['Fe'] / (365/7)
#~ NUTRIassess[crop, 15 ].value = TotalNutrients[crop]['Cu'] / (365/7)
#~ NUTRIassess[crop, 16 ].value = TotalNutrients[crop]['Zn'] / (365/7)
#~ NUTRIassess[crop, 17 ].value = TotalNutrients[crop]['Se'] / (365/7)
#~ NUTRIassess[crop, 18 ].value = TotalNutrients[crop]['I'] / (365/7)
#~ NUTRIassess[crop, 20 ].value = TotalNutrients[crop]['Proteins'] / (365/7)
#~ NUTRIassess[crop, 21 ].value = TotalNutrients[crop]['carbohydrates'] / (365/7)
#~ NUTRIassess[crop, 22 ].value = TotalNutrients[crop]['sugar'] / (365/7)
#~ NUTRIassess[crop, 23 ].value = TotalNutrients[crop]['energy_kJ'] / (365/7)
#~ NUTRIassess[crop, 24 ].value = TotalNutrients[crop]['energy_kcal'] / (365/7)
#~ NUTRIassess[crop, 31 ].value = TotalNutrients[crop]['lipids'] / (365/7)
#~ NUTRIassess[crop, 32 ].value = TotalNutrients[crop]['vitA'] / (365/7)
#~ NUTRIassess[crop, 35 ].value = TotalNutrients[crop]['vitD'] / (365/7)
#~ NUTRIassess[crop, 36 ].value = TotalNutrients[crop]['vitE'] / (365/7)
#~ NUTRIassess[crop, 39 ].value = TotalNutrients[crop]['vitC'] / (365/7)
#~ NUTRIassess[crop, 40 ].value = TotalNutrients[crop]['vitB1'] / (365/7)
#~ NUTRIassess[crop, 41 ].value = TotalNutrients[crop]['vitB2'] / (365/7)
#~ NUTRIassess[crop, 42 ].value = TotalNutrients[crop]['vitB3'] / (365/7)
#~ NUTRIassess[crop, 43 ].value = TotalNutrients[crop]['vitB5'] / (365/7)
#~ NUTRIassess[crop, 44 ].value = TotalNutrients[crop]['vitB6'] / (365/7)
#~ NUTRIassess[crop, 45 ].value = TotalNutrients[crop]['vitB12'] / (365/7)
#~ NUTRIassess[crop, 46 ].value = TotalNutrients[crop]['vitB9'] / (365/7)
#~ 
#~ 
#~ # copying the individual nutrient/vitamin amounts per day in the 'Results' spreadsheet:
#~ Results[ 4 , 3 ].value = TotalNutrients['Sum'][' Mg '] / 365
#~ Results[ 5 , 3 ].value = TotalNutrients['Sum'][' P '] / 365
#~ Results[ 6 , 3 ].value = TotalNutrients['Sum'][' K '] / 365
#~ Results[ 7 , 3 ].value = TotalNutrients['Sum'][' Ca '] / 365
#~ Results[ 8 , 3 ].value = TotalNutrients['Sum'][' Mn '] / 365
#~ Results[ 9 , 3 ].value = TotalNutrients['Sum'][' Fe '] / 365
#~ Results[ 10 , 3 ].value = TotalNutrients['Sum'][' Cu '] / 365
#~ Results[ 11 , 3 ].value = TotalNutrients['Sum'][' Zn '] / 365
#~ Results[ 12 , 3 ].value = TotalNutrients['Sum'][' Se '] / 365
#~ Results[ 13 , 3 ].value = TotalNutrients['Sum'][' I '] / 365
#~ Results[ 15 , 3 ].value = TotalNutrients['Sum'][' Proteins '] / 365
#~ Results[ 16 , 3 ].value = TotalNutrients['Sum'][' carbohydrates '] / 365
#~ Results[ 17 , 3 ].value = TotalNutrients['Sum'][' sugar '] / 365
#~ Results[ 18 , 3 ].value = TotalNutrients['Sum'][' energy_kJ '] / 365
#~ Results[ 19 , 3 ].value = TotalNutrients['Sum'][' energy_kcal '] / 365
#~ Results[ 26 , 3 ].value = TotalNutrients['Sum'][' lipids '] / 365
#~ Results[ 27 , 3 ].value = TotalNutrients['Sum'][' vitA ']   / 365
#~ Results[ 30 , 3 ].value = TotalNutrients['Sum'][' vitD '] / 365
#~ Results[ 31 , 3 ].value = TotalNutrients['Sum'][' vitE '] / 365
#~ Results[ 34 , 3 ].value = TotalNutrients['Sum'][' vitC '] / 365
#~ Results[ 35 , 3 ].value = TotalNutrients['Sum'][' vitB1 '] / 365
#~ Results[ 36 , 3 ].value = TotalNutrients['Sum'][' vitB2 '] / 365
#~ Results[ 37 , 3 ].value = TotalNutrients['Sum'][' vitB3 '] / 365
#~ Results[ 38 , 3 ].value = TotalNutrients['Sum'][' vitB5 '] / 365
#~ Results[ 39 , 3 ].value = TotalNutrients['Sum'][' vitB6 '] / 365
#~ Results[ 40 , 3 ].value = TotalNutrients['Sum'][' vitB12 '] / 365
#~ Results[ 41 , 3 ].value = TotalNutrients['Sum'][' vitB9 '] / 365
