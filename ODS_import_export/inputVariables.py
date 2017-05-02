#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


#################################
#								#
#		IMPORTING MODULES		#
#								#
#################################
print("Importing modules...")

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

# soffice "--accept=socket,host=0,port=2002;urp;"
# libreoffice5.3 "--accept=socket,host=0,port=2002;urp;"
#~ print("Connecting to pyoo...")
#~ desktop = pyoo.Desktop('localhost', 2002)
#~ print("	OK")


#=== IN WINDOWS =======================================================================
# CAUTION ! THIS IS ONLY A WORK AROUND ! The uno-bridge error is still not solved.
 
#~ import socket
#~ print("Connecting to pyoo...")
#~ desktop = pyoo.Desktop('localhost', 2002)
#~ print("	OK")


#=== FOR BOTH OS ======================================================================

#~Copying input.ods as output.ods :
#~ print("Creating  'output.ods'  from  'input.ods'...")
#~ shutil.copyfile('input.ods', 'output.ods')
#~ print("	OK")

#~ Opening output.ods :
#~ print("Connecting to  'output.ods'...")
#~ doc = desktop.open_spreadsheet("output.ods")
#~ print("	OK")

#~ Associating each output's sheet with its name:
#~ print("Connection to output's spreadsheets...")

#=====Creating an UNO-bridge to input.ods ===============
desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("input.ods")

ENVIRONMENT	=	doc.sheets['ENVIRONMENT']
PLANTS		=	doc.sheets['PLANTS']
NUTRITION	=	doc.sheets['NUTRITION']
PRAvirgin	=	doc.sheets['PRAvirgin']
NUTRITIONvirgin	=	doc.sheets['NUTRITIONvirgin']
NUTRITION_RDA = doc.sheets['NUTRITION_Adequate Intakes']
print("	OK")



#############################################################################
### variables from sheet PLANTS:
CROProw = 2 # Row of the first CROP in the 'PLANTS' sheet -> first value for the loop
prodID	= lambda CROProw:	PLANTS[CROProw,1].value
prodBOT	= lambda CROProw:	PLANTS[CROProw,2].value
prodTYP	= lambda CROProw:	PLANTS[CROProw,3].value
prodCAT	= lambda CROProw:	PLANTS[CROProw,4].value
prod_EN	= lambda CROProw:	PLANTS[CROProw,5].value
prod_DE	= lambda CROProw:	PLANTS[CROProw,6].value
prod_FR	= lambda CROProw:	PLANTS[CROProw,7].value
prod_SC	= lambda CROProw:	PLANTS[CROProw,8].value
#~ expYIELD_min	= lambda CROProw:	PLANTS[CROProw,9].value
#~ expYIELD_max	= lambda CROProw:	PLANTS[CROProw,10].value
expYIELD	= lambda CROProw:	PLANTS[CROProw,11].value  # expYIELD_av in the .ods file
expSTRAW_rate	= lambda CROProw:	PLANTS[CROProw,12].value
prodN	= lambda CROProw:	PLANTS[CROProw,13].value
prodP	= lambda CROProw:	PLANTS[CROProw,14].value
prodK	= lambda CROProw:	PLANTS[CROProw,15].value
prodNa	= lambda CROProw:	PLANTS[CROProw,16].value
prodMg	= lambda CROProw:	PLANTS[CROProw,17].value
prodCa	= lambda CROProw:	PLANTS[CROProw,18].value
prodMn	= lambda CROProw:	PLANTS[CROProw,19].value
prodFe	= lambda CROProw:	PLANTS[CROProw,20].value
prodCu	= lambda CROProw:	PLANTS[CROProw,21].value
prodZn	= lambda CROProw:	PLANTS[CROProw,22].value
strawN	= lambda CROProw:	PLANTS[CROProw,23].value
fixNmin	= lambda CROProw:	PLANTS[CROProw,24].value
fixNmax	= lambda CROProw:	PLANTS[CROProw,25].value
#~ fixN	= lambda CROProw:	PLANTS[CROProw,26].value
Nstraw_bulck	= lambda CROProw:	PLANTS[CROProw,27].value
fixN	= lambda CROProw:	PLANTS[CROProw,28].value
strawP	= lambda CROProw:	PLANTS[CROProw,29].value
strawK	= lambda CROProw:	PLANTS[CROProw,30].value
CNmin	= lambda CROProw:	PLANTS[CROProw,31].value
CNmax	= lambda CROProw:	PLANTS[CROProw,32].value
CN	= lambda CROProw:	PLANTS[CROProw,33].value
Kc1_4	= lambda CROProw:	PLANTS[CROProw,34].value
Kc2_4	= lambda CROProw:	PLANTS[CROProw,35].value
Kc3_4	= lambda CROProw:	PLANTS[CROProw,36].value
Kc4_4	= lambda CROProw:	PLANTS[CROProw,37].value
rootDEPTH	= lambda CROProw:	PLANTS[CROProw,38].value
pHmin	= lambda CROProw:	PLANTS[CROProw,39].value
pHmax	= lambda CROProw:	PLANTS[CROProw,40].value
Tmin_germ	= lambda CROProw:	PLANTS[CROProw,41].value
Tmin	= lambda CROProw:	PLANTS[CROProw,42].value
period	= lambda CROProw:	PLANTS[CROProw,43].value # periodicity, maximum frequency to avoid pests and diseases
seed_from	= lambda CROProw:	PLANTS[CROProw,44].value
seed_to	= lambda CROProw:	PLANTS[CROProw,45].value
GSmin	= lambda CROProw:	PLANTS[CROProw,46].value
GSmax	= lambda CROProw:	PLANTS[CROProw,47].value
#~ GStot_min	= lambda CROProw:	PLANTS[CROProw,48].value
#~ GStot_max	= lambda CROProw:	PLANTS[CROProw,49].value
FSR	= lambda CROProw:	PLANTS[CROProw,50].value
Nscavenge	= lambda CROProw:	PLANTS[CROProw,51].value
DMmin	= lambda CROProw:	PLANTS[CROProw,52].value
DMmax	= lambda CROProw:	PLANTS[CROProw,53].value
RES	= lambda CROProw:	PLANTS[CROProw,54].value
POThumus	= lambda CROProw:	PLANTS[CROProw,55].value
POTinterseed	= lambda CROProw:	PLANTS[CROProw,56].value
TOLERheat = lambda CROProw: PLANTS[CROProw,57].value
TOLERdrought	= lambda CROProw:	PLANTS[CROProw,58].value
TOLERshade	= lambda CROProw:	PLANTS[CROProw,59].value
TOLERflood	= lambda CROProw:	PLANTS[CROProw,60].value
TOLERlf	= lambda CROProw:	PLANTS[CROProw,61].value
ratioADAPT	= lambda CROProw:	PLANTS[CROProw,62].value
PRIORITYgeneral	= lambda CROProw:	PLANTS[CROProw,63].value
PRIORITYfruits	= lambda CROProw:	PLANTS[CROProw,64].value
PRIORITYtextile	= lambda CROProw:	PLANTS[CROProw,65].value

def ratioADAPT_in_PLANTS(CROProw,ratioADAPT):
	PLANTS[CROProw,62].value = ratioADAPT

#############################################################################
### variables from sheet ENVIRONMENT:
PRA = 1 # set the first PRA to be analysed : beginning value for the "PRA edibility-test" loop
IDDEP	= lambda PRA:	ENVIRONMENT[PRA,0].value
IDSHOR	= lambda PRA:	ENVIRONMENT[PRA,1].value
IDPRA	= lambda PRA:	ENVIRONMENT[PRA,2].value
NAME_PRA	= lambda PRA:	ENVIRONMENT[PRA,3].value
ID_GEOFLA	= lambda PRA:	ENVIRONMENT[PRA,4].value
CODE_DEPT	= lambda PRA:	ENVIRONMENT[PRA,5].value
NOM_DEPT	= lambda PRA:	ENVIRONMENT[PRA,6].value
CODE_CHF	= lambda PRA:	ENVIRONMENT[PRA,7].value
NOM_CHF	= lambda PRA:	ENVIRONMENT[PRA,8].value
X_CHF_LIEU	= lambda PRA:	ENVIRONMENT[PRA,9].value
Y_CHF_LIEU	= lambda PRA:	ENVIRONMENT[PRA,10].value
X_CENTROID	= lambda PRA:	ENVIRONMENT[PRA,11].value
Y_CENTROID	= lambda PRA:	ENVIRONMENT[PRA,12].value
CODE_REG	= lambda PRA:	ENVIRONMENT[PRA,13].value
NOM_REG	= lambda PRA:	ENVIRONMENT[PRA,14].value
PRAsurface	= lambda PRA:	ENVIRONMENT[PRA,15].value
ntot_med	= lambda PRA:	ENVIRONMENT[PRA,16].value
ntot_moy	= lambda PRA:	ENVIRONMENT[PRA,17].value
nmin_med	= lambda PRA:	ENVIRONMENT[PRA,18].value
nmin_moy	= lambda PRA:	ENVIRONMENT[PRA,19].value
caact_med	= lambda PRA:	ENVIRONMENT[PRA,20].value
caact_moy	= lambda PRA:	ENVIRONMENT[PRA,21].value
cao_med	= lambda PRA:	ENVIRONMENT[PRA,22].value
cao_moy	= lambda PRA:	ENVIRONMENT[PRA,23].value
catot_med	= lambda PRA:	ENVIRONMENT[PRA,24].value
catot_moy	= lambda PRA:	ENVIRONMENT[PRA,25].value
cecmet_med	= lambda PRA:	ENVIRONMENT[PRA,26].value
cecmet_moy	= lambda PRA:	ENVIRONMENT[PRA,27].value
cecrh_med	= lambda PRA:	ENVIRONMENT[PRA,28].value
cecrh_moy	= lambda PRA:	ENVIRONMENT[PRA,29].value
corgox_moy	= lambda PRA:	ENVIRONMENT[PRA,30].value
corgox_med	= lambda PRA:	ENVIRONMENT[PRA,31].value
corgco_moy	= lambda PRA:	ENVIRONMENT[PRA,32].value
corgco_med	= lambda PRA:	ENVIRONMENT[PRA,33].value
corgequiv_moy	= lambda PRA:	ENVIRONMENT[PRA,34].value
corgequiv_med	= lambda PRA:	ENVIRONMENT[PRA,35].value
OM_moy	= lambda PRA:	ENVIRONMENT[PRA,34].value
OM_med	= lambda PRA:	ENVIRONMENT[PRA,35].value
cued_moy	= lambda PRA:	ENVIRONMENT[PRA,36].value
cued_med	= lambda PRA:	ENVIRONMENT[PRA,37].value
feed_med	= lambda PRA:	ENVIRONMENT[PRA,38].value
feed_moy	= lambda PRA:	ENVIRONMENT[PRA,39].value
kcec_med	= lambda PRA:	ENVIRONMENT[PRA,40].value
kcec_moy	= lambda PRA:	ENVIRONMENT[PRA,41].value
kmg_med	= lambda PRA:	ENVIRONMENT[PRA,42].value
kmg_moy	= lambda PRA:	ENVIRONMENT[PRA,43].value
mgcec_med	= lambda PRA:	ENVIRONMENT[PRA,44].value
mgcec_moy	= lambda PRA:	ENVIRONMENT[PRA,45].value
mgo_med	= lambda PRA:	ENVIRONMENT[PRA,46].value
mgo_moy	= lambda PRA:	ENVIRONMENT[PRA,47].value
mned_med	= lambda PRA:	ENVIRONMENT[PRA,48].value
mned_moy	= lambda PRA:	ENVIRONMENT[PRA,49].value
nao_med	= lambda PRA:	ENVIRONMENT[PRA,50].value
nao_moy	= lambda PRA:	ENVIRONMENT[PRA,51].value
p2d_med	= lambda PRA:	ENVIRONMENT[PRA,52].value
p2d_moy	= lambda PRA:	ENVIRONMENT[PRA,53].value
p2j_med	= lambda PRA:	ENVIRONMENT[PRA,54].value
p2j_moy	= lambda PRA:	ENVIRONMENT[PRA,55].value
p2o_med	= lambda PRA:	ENVIRONMENT[PRA,56].value
p2o_moy	= lambda PRA:	ENVIRONMENT[PRA,57].value
p2oEQUIV	= lambda PRA:	ENVIRONMENT[PRA,295].value
zned_med	= lambda PRA:	ENVIRONMENT[PRA,58].value
zned_moy	= lambda PRA:	ENVIRONMENT[PRA,59].value
K_med	= lambda PRA:	ENVIRONMENT[PRA,60].value
K_moy	= lambda PRA:	ENVIRONMENT[PRA,61].value
pho_med	= lambda PRA:	ENVIRONMENT[PRA,62].value
pho_moy	= lambda PRA:	ENVIRONMENT[PRA,63].value
pH	= lambda PRA:	ENVIRONMENT[PRA,63].value
BDETM_pH	= lambda PRA:	ENVIRONMENT[PRA,64].value # gives the pH9000 for the PRA, obviously the more recent of both BDETM variables
#~ BDETM_pH0010	= lambda PRA:	ENVIRONMENT[PRA,65].value
#~ BDEM_pHmoy	= lambda PRA:	ENVIRONMENT[PRA,66].value
#~ argile	= lambda PRA:	ENVIRONMENT[PRA,67].value
#~ sable	= lambda PRA:	ENVIRONMENT[PRA,68].value
#~ limon	= lambda PRA:	ENVIRONMENT[PRA,69].value
SoilType_DE	= lambda PRA:	ENVIRONMENT[PRA,70].value
AvailableWaterCapacity	= lambda PRA:	ENVIRONMENT[PRA,71].value
AWC	= lambda PRA:	ENVIRONMENT[PRA,71].value
AWC_SoilOnly	= lambda PRA:	ENVIRONMENT[PRA,71].value
# Welkepunkt_pF4,2	= lambda PRA:	ENVIRONMENT[PRA,72].value
STATalt	= lambda PRA:	ENVIRONMENT[PRA,73].value
	
def TmaxABS(month):
	"""TmaxABS = "Temperature maximale absolue" ("maximum absolute Temperature")
	This function returns the highest Temperature recorded in the current PRA for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,74+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,74+i].value


def TmaxMOY(month):
	"""TmaxMOY = "Température Maximale Moyenne" ("average highest Temperature")
	This function returns the average highest daily Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,87+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,87+i].value


def Tmoy(month):
	"""Tmoy = "Température moyenne" ("average Temperature")
	This function returns the average Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,100+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,100+i].value


def TminMOY(month):
	"""TminMOY = "Température minimale moyenne ("average lowest Temperature")
	This function returns the average lowest daily Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,113+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,113+i].value


def TminABS(month):
	"""TminABS = "Température minimale absolue" ("minimum absolute Temperature")
	This function returns the lowest Temperature recorded in the current PRA for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,126+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,126+i].value


def JOURS_sup30C(month):
	"""JOURS_sup30C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 30°C"
	This function returns the average days amount with a maximum Temperature >30°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,139+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,139+i].value


def JOURS_sup25C(month):
	"""JOURS_sup25C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 25°C"
	This function returns the average days amount with a maximum Temperature >25°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,152+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,152+i].value


def JOURS_sup0C(month):
	"""JOURS_sup0C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 0°C"
	This function returns the average days amount with an maximum Temperature >0°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,165+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,165+i].value


def JOURS_TminBelow0C(month):
	"""JOURS_TminBelow0C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à 0°C"
	This function returns the average days amount with an average minimum Temperature <0°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,178+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,178+i].value


def JOURS_TminBelow_Negative_5C(month):
	"""JOURS_TminBelow_Negative_5C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à -5°C"
	This function returns the average days amount with an average minimum Temperature < -5°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,191+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,191+i].value


def JOURS_TminBelow_Negative_10C(month):
	"""JOURS_TminBelow_Negative_10C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à -10°C"
	This function returns the average days amount with an average minimum Temperature < -10°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,204+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,204+i].value


def Pmax(month):
	"""Pmax = "Hauteur de Précipitations quotidiennes maximale"
	This function returns the daily average maximum precipitation (in mm) for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,217+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,217+i].value


def Ptot(month):
	"""Ptot = "Hauteur de Précipitations totales moyenne mensuelle"
	This function returns the average maximum precipitation (in mm) for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,230+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,230+i].value


def Tcumul(month):
	"""Tcumul = "Températures cumulées" (in the original file from MeteoFrance: "Degrés Jours Unifiés")
	This function returns the cumulative temperatures for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,243+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,243+i].value


def SOLglobal(month):
	"""SOLglobal = "Ensoleillement global" (in the original file from MeteoFrance: "Rayonnement global")
	This function returns the average global radiation for the selected month (in J/cm²).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,256+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,256+i].value


def SOLmoy(month):
	"""SOLmoy = "Ensoleillement moyen" (in the original file from MeteoFrance: "Durée d'insolation")
	This function returns the monthly average sunshine duration for the selected month (in hours).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,269+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,269+i].value


def ETPmoy(month):
	"""ETPmoy = "Evapotranspiration (potentielle) moyenne mensuelle"
	This function returns the average evapotranspiration for the selected month (ETP Penman in mm).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average."""
	i=0
	if month == 'an':
		return ENVIRONMENT[PRA,282+12].value
	elif type(month) != int:
		month=int(month[1:])
	month = month % 12
	while month != 1+i:
		i+=1
	if month == 1+i:
		return ENVIRONMENT[PRA,282+i].value



###########################################################################################################################################
##################################### /!\ ASK FOR HELP FOR WATER RESSOURCES FORMULA !! ####################################################
###########################################################################################################################################
	
def WaterRessources(month):
	return Ptot(month)
	#~ return WaterRessources = Ptot(CurrentMonth) * AvailableWaterCapacity	# (precipitation (in mm) * available water capacity (in %))
