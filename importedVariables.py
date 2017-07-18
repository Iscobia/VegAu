#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#########################################
#										#
#		IMPORTING INTERNAL MODULES		#
#										#
#########################################

from inputFR import plants
from inputFR import environment
from inputFR import nutrition

#===================================================================
#== INDICES, variables importantes:


#== row index for crops :
# CROProw_PLANTS			= lambda prodID:	plants[prodID]['CROP_index']
# CROProw_NUTRITION		= lambda prodID:	nutrition[prodID]['CROP_index']
# CROProw_NUTRITIONvirgin		= lambda prodID:	NUTRITIONvirgin_dict[prodID]['CROP_index']


#== column index for prodIDs :
# CROPcol_PRAedibility	= lambda prodID:	plants[prodID]['colIndex_PRAedibility']
# CROPcol_PRAyields		= lambda prodID:	plants[prodID]['colIndex_PRAyields']


#== row index for PRAs :
# PRArow_ENVIRONMENT	= lambda pra:	environment[pra]['PRA_index']
# PRArow_PRAvirgin	= lambda pra:	PRAvirgin_dict[pra]['PRA_index']



#############################################
#											#
#	VARIABLES FROM THE DICT 'plants'		#
#											#
#############################################

prodID	= lambda prodID:	plants[prodID][1]
prodBOT	= lambda prodID:	plants[prodID][2]
prodTYP	= lambda prodID:	plants[prodID][3]
prodCAT	= lambda prodID:	plants[prodID][4]
prod_EN	= lambda prodID:	plants[prodID][5]
prod_DE	= lambda prodID:	plants[prodID][6]
prod_FR	= lambda prodID:	plants[prodID][7]
prod_SC	= lambda prodID:	plants[prodID][8]
#~ expYIELD_min	= lambda prodID:	plants[prodID][9]
#~ expYIELD_max	= lambda prodID:	plants[prodID][10]
expYIELD	= lambda prodID:	plants[prodID][10]  # expYIELD_max in the .ods file
# expYIELD	= lambda prodID:	plants[prodID][11]  # expYIELD_av in the .ods file
expSTRAW_rate	= lambda prodID:	plants[prodID][12]
prodN	= lambda prodID:	plants[prodID][13]
prodP	= lambda prodID:	plants[prodID][14]
prodK	= lambda prodID:	plants[prodID][15]
prodNa	= lambda prodID:	plants[prodID][16]
prodMg	= lambda prodID:	plants[prodID][17]
prodCa	= lambda prodID:	plants[prodID][18]
prodMn	= lambda prodID:	plants[prodID][19]
prodFe	= lambda prodID:	plants[prodID][20]
prodCu	= lambda prodID:	plants[prodID][21]
prodZn	= lambda prodID:	plants[prodID][22]
strawN	= lambda prodID:	plants[prodID][23]
fixNmin	= lambda prodID:	plants[prodID][24]
fixNmax	= lambda prodID:	plants[prodID][25]
#~ fixN	= lambda prodID:	plants[prodID][26]
Nstraw_bulck	= lambda prodID:	plants[prodID][27]
fixN	= lambda prodID:	plants[prodID][28]
strawP	= lambda prodID:	plants[prodID][29]
strawK	= lambda prodID:	plants[prodID][30]
CNmin	= lambda prodID:	plants[prodID][31]
CNmax	= lambda prodID:	plants[prodID][32]
CN	= lambda prodID:	plants[prodID][33]
Kc1_4	= lambda prodID:	plants[prodID][34]
Kc2_4	= lambda prodID:	plants[prodID][35]
Kc3_4	= lambda prodID:	plants[prodID][36]
Kc4_4	= lambda prodID:	plants[prodID][37]
rootDEPTH	= lambda prodID:	plants[prodID][38]
pHmin	= lambda prodID:	plants[prodID][39]
pHmax	= lambda prodID:	plants[prodID][40]
Tmin_germ	= lambda prodID:	plants[prodID][41]
Tmin	= lambda prodID:	plants[prodID][42]
period	= lambda prodID:	plants[prodID][43] # periodicity, maximum frequency to avoid pests and diseases
seed_from	= lambda prodID:	plants[prodID][44]
seed_to	= lambda prodID:	plants[prodID][45]
GSmin	= lambda prodID:	round(plants[prodID][46])
GSmax	= lambda prodID:	plants[prodID][47]
#~ GStot_min	= lambda prodID:	plants[prodID][48]
#~ GStot_max	= lambda prodID:	plants[prodID][49]
FSR	= lambda prodID:	plants[prodID][50]
Nscavenge	= lambda prodID:	plants[prodID][51]
DMmin	= lambda prodID:	plants[prodID][52]
DMmax	= lambda prodID:	plants[prodID][53]
RES	= lambda prodID:	plants[prodID][54]
POThumus	= lambda prodID:	plants[prodID][55]
POTinterseed	= lambda prodID:	plants[prodID][56]
TOLERheat = lambda prodID: plants[prodID,57]
TOLERdrought	= lambda prodID:	plants[prodID][58]
TOLERshade	= lambda prodID:	plants[prodID][59]
TOLERflood	= lambda prodID:	plants[prodID][60]
TOLERlf	= lambda prodID:	plants[prodID][61]
ratioADAPT	= lambda prodID:	plants[prodID][62]
PRIORITYgeneral	= lambda prodID:	plants[prodID][63]
PRIORITYfruits	= lambda prodID:	plants[prodID][64]
PRIORITYtextile	= lambda prodID:	plants[prodID][65]



#############################################
#											#
#	VARIABLES FROM THE DICT 'environment'	#
#											#
#############################################


IDDEP	= lambda PRA:	environment[PRA][0]
IDSHOR	= lambda PRA:	environment[PRA][1]
IDPRA	= lambda PRA:	environment[PRA][2]
NAME_PRA	= lambda PRA:	environment[PRA][3]
ID_GEOFLA	= lambda PRA:	environment[PRA][4]
CODE_DEPT	= lambda PRA:	environment[PRA][5]
NOM_DEPT	= lambda PRA:	environment[PRA][6]
CODE_CHF	= lambda PRA:	environment[PRA][7]
NOM_CHF	= lambda PRA:	environment[PRA][8]
X_CHF_LIEU	= lambda PRA:	environment[PRA][9]
Y_CHF_LIEU	= lambda PRA:	environment[PRA][10]
X_CENTROID	= lambda PRA:	environment[PRA][11]
Y_CENTROID	= lambda PRA:	environment[PRA][12]
CODE_REG	= lambda PRA:	environment[PRA][13]
NOM_REG	= lambda PRA:	environment[PRA][14]
PRAsurface	= lambda PRA:	environment[PRA][15]
ntot_med	= lambda PRA:	environment[PRA][16]
ntot_moy	= lambda PRA:	environment[PRA][17]
nmin_med	= lambda PRA:	environment[PRA][18]
nmin_moy	= lambda PRA:	environment[PRA][19]
caact_med	= lambda PRA:	environment[PRA][20]
caact_moy	= lambda PRA:	environment[PRA][21]
cao_med	= lambda PRA:	environment[PRA][22]
cao_moy	= lambda PRA:	environment[PRA][23]
catot_med	= lambda PRA:	environment[PRA][24]
catot_moy	= lambda PRA:	environment[PRA][25]
cecmet_med	= lambda PRA:	environment[PRA][26]
cecmet_moy	= lambda PRA:	environment[PRA][27]
cecrh_med	= lambda PRA:	environment[PRA][28]
cecrh_moy	= lambda PRA:	environment[PRA][29]
corgox_moy	= lambda PRA:	environment[PRA][30]
corgox_med	= lambda PRA:	environment[PRA][31]
corgco_moy	= lambda PRA:	environment[PRA][32]
corgco_med	= lambda PRA:	environment[PRA][33]
corgequiv_moy	= lambda PRA:	environment[PRA][34]
corgequiv_med	= lambda PRA:	environment[PRA][35]
OM_moy	= lambda PRA:	environment[PRA][34]
OM_med	= lambda PRA:	environment[PRA][35]


def OM_retention_capacity(x, PRA):
	"""Returns the retention capacity of the PRA's soil according to its content in Organic Matter. This function
	has been written according to the book "Bodenkundliche Kartierleitung, fünfte Auflage", Ad-hoc-AG Boden Hannover 2005.

	This function uses the dictionary x.ActualStand to take the right OM stand into account while the rotation."""

	soil_type = SoilType_DE(PRA)
	organic_carbon = x.ActualStand[PRA]['OM'] / 10  # given in g/kg --> converting per thousand in percent

	# according to the Hill Laboratory, Organic Matter (%) = Organic Carbon (%) x 1.72
	organic_matter = (organic_carbon * 1.72)

	h2 = organic_matter <= 4  # Very Low (< 2) and Low (2 to 4)
	h3 = 4 <= organic_matter <= 10  # Medium
	h4 = 10 <= organic_matter <= 20  # High
	# h5 = 20 < organic_matter  # Very high

	if environment[PRA][72] != '':
		return int(environment[PRA][72])

	else:
		if soil_type == 'Ss':
			if h2:
				environment[PRA][72] = 1
				return 1

			elif h3:
				environment[PRA][72] = 3
				return 3

			elif h4:
				environment[PRA][72] = 4
				return 4

			else:
				environment[PRA][72] = 5
				return 5

		elif soil_type == 'Sl2':
			if h2:
				environment[PRA][72] = 2
				return 2

			elif h3:
				environment[PRA][72] = 3
				return 3

			elif h4:
				environment[PRA][72] = 4
				return 4

			else:
				environment[PRA][72] = 6
				return 6

		elif soil_type == 'Sl3':
			if h2:
				environment[PRA][72] = 1
				return 1
			elif h3:
				environment[PRA][72] = 3
				return 3

			elif h4:
				environment[PRA][72] = 4
				return 4

			else:
				environment[PRA][72] = 6
				return 6

		elif soil_type == 'Sl4':
			if h2:
				environment[PRA][72] = 2
				return 2
			elif h3:
				environment[PRA][72] = 4
				return 4

			elif h4:
				environment[PRA][72] = 5
				return 5

			else:
				environment[PRA][72] = 6
				return 6

		elif soil_type == 'Slu':
			if h2:
				environment[PRA][72] = 1
				return 1

			elif h3:
				environment[PRA][72] = 2
				return 2

			elif h4:
				environment[PRA][72] = 4
				return 4

			else:
				environment[PRA][72] = 6
				return 6

		elif soil_type == 'St2':
			if h2:
				environment[PRA][72] = 3
				return 3

			elif h3:
				environment[PRA][72] = 4
				return 4

			elif h4:
				environment[PRA][72] = 5
				return 5

			else:
				environment[PRA][72] = 7
				return 7

		elif soil_type == 'St3':
			if h2:
				environment[PRA][72] = 2
				

			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 6
				

			else:
				environment[PRA][72] = 9
				

		elif soil_type == 'Su2':
			if h2:
				environment[PRA][72] = 2
				

			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 4
				

			else:
				environment[PRA][72] = 6
				

		elif soil_type == 'Su3':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 3
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Su4':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 2
				

			elif h4:
				environment[PRA][72] = 3
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Ls2':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 5
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Ls3':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 5
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Ls4':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 6
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Lt2':
			if h2:
				environment[PRA][72] = 3
				
			elif h3:
				environment[PRA][72] = 5
				

			elif h4:
				environment[PRA][72] = 8
				

			else:
				environment[PRA][72] = 10
				

		elif soil_type == 'Lt3':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 8
				

			else:
				environment[PRA][72] = 11
				

		elif soil_type == 'Lts':
			if h2:
				environment[PRA][72] = 3
				
			elif h3:
				environment[PRA][72] = 5
				

			elif h4:
				environment[PRA][72] = 7
				

			else:
				environment[PRA][72] = 9
				

		elif soil_type == 'Lu':
			if h2:
				environment[PRA][72] = 3
				
			elif h3:
				environment[PRA][72] = 5
				

			elif h4:
				environment[PRA][72] = 7
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Uu':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 2
				

			elif h4:
				environment[PRA][72] = 3
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Uls':
			if h2:
				environment[PRA][72] = 3
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 4
				

			else:
				environment[PRA][72] = 7
				

		elif soil_type == 'Us':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 2
				

			elif h4:
				environment[PRA][72] = 3
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Ut2':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 1
				

			elif h4:
				environment[PRA][72] = 2
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Ut3':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 1
				

			elif h4:
				environment[PRA][72] = 2
				

			else:
				environment[PRA][72] = 4
				

		elif soil_type == 'Ut4':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 4
				

			else:
				environment[PRA][72] = 6
				

		elif soil_type == 'Tt':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 5
				

			else:
				environment[PRA][72] = 7
				

		elif soil_type == 'Tl':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 6
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Tu2':
			if h2:
				environment[PRA][72] = 1
				
			elif h3:
				environment[PRA][72] = 3
				

			elif h4:
				environment[PRA][72] = 5
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Tu3':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 7
				

			else:
				environment[PRA][72] = 9
				

		elif soil_type == 'Tu4':
			if h2:
				environment[PRA][72] = 5
				
			elif h3:
				environment[PRA][72] = 5
				

			elif h4:
				environment[PRA][72] = 6
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Ts2':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 6
				

			else:
				environment[PRA][72] = 8
				

		elif soil_type == 'Ts3':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 5
				

			elif h4:
				environment[PRA][72] = 7
				

			else:
				environment[PRA][72] = 9
				

		elif soil_type == 'Ts4':
			if h2:
				environment[PRA][72] = 2
				
			elif h3:
				environment[PRA][72] = 4
				

			elif h4:
				environment[PRA][72] = 7
				

			else:
				environment[PRA][72] = 9

		else:
			print("ERROR : the soil type of the PRA {} cannot be found in the database.".format(PRA, x.EndPreviousCrop_later))
			return 1

		return environment[PRA][72]
		

cued_moy	= lambda PRA:	environment[PRA][36]
cued_med	= lambda PRA:	environment[PRA][37]
feed_med	= lambda PRA:	environment[PRA][38]
feed_moy	= lambda PRA:	environment[PRA][39]
kcec_med	= lambda PRA:	environment[PRA][40]
kcec_moy	= lambda PRA:	environment[PRA][41]
kmg_med	= lambda PRA:	environment[PRA][42]
kmg_moy	= lambda PRA:	environment[PRA][43]
mgcec_med	= lambda PRA:	environment[PRA][44]
mgcec_moy	= lambda PRA:	environment[PRA][45]
mgo_med	= lambda PRA:	environment[PRA][46]
mgo_moy	= lambda PRA:	environment[PRA][47]
mned_med	= lambda PRA:	environment[PRA][48]
mned_moy	= lambda PRA:	environment[PRA][49]
nao_med	= lambda PRA:	environment[PRA][50]
nao_moy	= lambda PRA:	environment[PRA][51]
p2d_med	= lambda PRA:	environment[PRA][52]
p2d_moy	= lambda PRA:	environment[PRA][53]
p2j_med	= lambda PRA:	environment[PRA][54]
p2j_moy	= lambda PRA:	environment[PRA][55]
p2o_med	= lambda PRA:	environment[PRA][56]
p2o_moy	= lambda PRA:	environment[PRA][57]
p2oEQUIV	= lambda PRA:	environment[PRA][295]
#-----------------------------------------------------
def P_med(PRA) :
	"""This function returns the appropriate Phosphorus content in soil accroding to the soil pH of the given PRA.
	Different extraction methods are used for P according to the soil pH:
	*	if the PRA's average pH is acid, we use the P extract. method Dyer (called p2d in the data base)
	*	if the PRA's average pH il neutral of alkaline, the P extract. method Olsen is favoured because (called p2o in the data base)
	*	if no value is available for the Olsen method, then we use the Joret-Hébert method (called p2j in the data base)

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'"""

	if pH(PRA) < 6.5: # if the PRA's average pH is acid, we use the P extract. method Dyer (p2d)
		return p2d_med(PRA)
	else: # else, if the PRA's average pH il neutral of alkaline, the P extract. method Olsen is favoured (p2o, less agressive).
		if p2oEQUIV(PRA) == '':  # If no value for this method is available, then we use the Joret-Hébert method (p2j)
			return p2j_med(PRA)
		else:
			return p2oEQUIV(PRA)
#-----------------------------------------------------
zned_med	= lambda PRA:	environment[PRA][58]
zned_moy	= lambda PRA:	environment[PRA][59]
K_med	= lambda PRA:	environment[PRA][60]
K_moy	= lambda PRA:	environment[PRA][61]
pho_med	= lambda PRA:	environment[PRA][62]
pho_moy	= lambda PRA:	environment[PRA][63]
pH	= lambda PRA:	environment[PRA][63]
BDETM_pH	= lambda PRA:	environment[PRA][64] # gives the pH9000 for the PRA, obviously the more recent of both BDETM variables
#~ BDETM_pH0010	= lambda PRA:	environment[PRA][65]
#~ BDEM_pHmoy	= lambda PRA:	environment[PRA][66]
#~ argile	= lambda PRA:	ENVIRONMENT[PRA][67]
#~ sable	= lambda PRA:	environment[PRA][68]
#~ limon	= lambda PRA:	environment[PRA][69]
SoilType_DE	= lambda PRA:	environment[PRA][70]
AvailableWaterCapacity	= lambda PRA:	environment[PRA][71]
AWC	= lambda PRA:	environment[PRA][71]
# AWC_SoilOnly	= lambda PRA:	environment[PRA][71]

def AWC_SoilOnly(PRA):
	"""Returns the retention capacity of the PRA's soil according to its soil texture. This function
	has been written according to the book "Bodenkundliche Kartierleitung, fünfte Auflage",
	Ad-hoc-AG Boden Hannover 2005, Table 70.

	This function uses the dictionary x.ActualStand to take the right OM stand into account while the rotation."""

	soil_type = SoilType_DE(PRA)

	if soil_type != '' :
		return round(environment[PRA][71])

	else:
		if soil_type == 'Ss':
			environment[PRA][71] = 11
			return 11

		elif soil_type == 'Sl2':
			environment[PRA][71] = 25
			return 25

		elif soil_type == 'Sl3':
			environment[PRA][71] = 27
			return 27

		elif soil_type == 'Sl4':
			environment[PRA][71] = 30
			return 30

		elif soil_type == 'Slu':
			environment[PRA][71] = 33
			return 33

		elif soil_type == 'St2':
			environment[PRA][71] = 22
			return 22

		elif soil_type == 'St3':
			environment[PRA][71] = 30
			return 30

		elif soil_type == 'Su2':
			environment[PRA][71] = 23
			return 23

		elif soil_type == 'Su3':
			environment[PRA][71] = 29
			return 29
		elif soil_type == 'Su4':
			environment[PRA][71] = 32
			return 32
		elif soil_type == 'Ls2':
			environment[PRA][71] = 34
			return 34

		elif soil_type == 'Ls3':
			environment[PRA][71] = 33
			return 33

		elif soil_type == 'Ls4':
			environment[PRA][71] = 32
			return 32
		elif soil_type == 'Lt2':
			environment[PRA][71] = 36
			return 36

		elif soil_type == 'Lt3':
			environment[PRA][71] = 39
			return 39

		elif soil_type == 'Lts':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Lu':
			environment[PRA][71] = 36
			return 36

		elif soil_type == 'Uu':
			environment[PRA][71] = 38
			return 38

		elif soil_type == 'Uls':
			environment[PRA][71] =35
			return 35

		elif soil_type == 'Us':
			environment[PRA][71] = 35
			return 35

		elif soil_type == 'Ut2':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Ut3':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Ut4':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Tt':
			environment[PRA][71] = 43
			return 43

		elif soil_type == 'Tl':
			environment[PRA][71] = 41
			return 41

		elif soil_type == 'Tu2':
			environment[PRA][71] = 42
			return 42

		elif soil_type == 'Tu3':
			environment[PRA][71] = 38
			return 38

		elif soil_type == 'Tu4':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Ts2':
			environment[PRA][71] = 39
			return 39
		elif soil_type == 'Ts3':
			environment[PRA][71] = 37
			return 37

		elif soil_type == 'Ts4':
			environment[PRA][71] = 32
			return 32

# Welkepunkt_pF4,2	= lambda PRA:	environment[PRA][72]
STATalt	= lambda PRA:	environment[PRA][73]
	
def TmaxABS(month, PRA):
	"""TmaxABS = "Temperature maximale absolue" ("maximum absolute Temperature")
	This function returns the highest Temperature recorded in the current PRA for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'"""

	i=0
	if month == 'an':
		return environment[PRA][74+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][74+i]


def TmaxMOY(month, PRA):
	"""TmaxMOY = "Température Maximale Moyenne" ("average highest Temperature")
	This function returns the average highest daily Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'"""

	i=0
	if month == 'an':
		return environment[PRA][87+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][87+i]


def Tmoy(month, PRA):
	"""Tmoy = "Température moyenne" ("average Temperature")
	This function returns the average Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'"""

	i=0
	if month == 'an':
		return environment[PRA][100+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][100+i]


def TminMOY(month, PRA):
	"""TminMOY = "Température minimale moyenne ("average lowest Temperature")
	This function returns the average lowest daily Temperature for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'"""

	i=0
	# print("calculation of TminMOY: month = ", month)
	if month == 'an':
		return environment[PRA][113+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][113+i]


def TminABS(month, PRA):
	"""TminABS = "Température minimale absolue" ("minimum absolute Temperature")
	This function returns the lowest Temperature recorded in the current PRA for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][126+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][126+i]


def JOURS_sup30C(month, PRA):
	"""JOURS_sup30C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 30°C"
	This function returns the average days amount with a maximum Temperature >30°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][139+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][139+i]


def JOURS_sup25C(month, PRA):
	"""JOURS_sup25C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 25°C"
	This function returns the average days amount with a maximum Temperature >25°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][152+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][152+i]


def JOURS_sup0C(month, PRA):
	"""JOURS_sup0C = "Nombre moyen de jours pour lesquels la température maximale est supérieure à 0°C"
	This function returns the average days amount with an maximum Temperature >0°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][165+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][165+i]


def JOURS_TminBelow0C(month, PRA):
	"""JOURS_TminBelow0C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à 0°C"
	This function returns the average days amount with an average minimum Temperature <0°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][178+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][178+i]


def JOURS_TminBelow_Negative_5C(month, PRA):
	"""JOURS_TminBelow_Negative_5C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à -5°C"
	This function returns the average days amount with an average minimum Temperature < -5°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][191+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][191+i]


def JOURS_TminBelow_Negative_10C(month, PRA):
	"""JOURS_TminBelow_Negative_10C = "Nombre moyen de jours pour lesquels la température minimale est inférieure à -10°C"
	This function returns the average days amount with an average minimum Temperature < -10°C for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][204+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][204+i]


def Pmax(month, PRA):
	"""Pmax = "Hauteur de Précipitations quotidiennes maximale"
	This function returns the daily average maximum precipitation (in mm) for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][217+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][217+i]


def Ptot(month, PRA):
	"""Ptot = "Hauteur de Précipitations totales moyenne mensuelle"
	This function returns the average maximum precipitation (in mm) for the selected month.
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][230+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][230+i]


def Tcumul(month, PRA):
	"""Tcumul = "Températures cumulées" (in the original file from MeteoFrance: "Degrés Jours Unifiés")
	This function returns the cumulative temperatures for the selected month (in °C).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][243+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][243+i]


def SOLglobal(month, PRA):
	"""SOLglobal = "Ensoleillement global" (in the original file from MeteoFrance: "Rayonnement global")
	This function returns the average global radiation for the selected month (in J/cm²).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][256+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][256+i]


def SOLmoy(month, PRA):
	"""SOLmoy = "Ensoleillement moyen" (in the original file from MeteoFrance: "Durée d'insolation")
	This function returns the monthly average sunshine duration for the selected month (in hours).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][269+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month == 12:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][269+i]

def SOLmoy_max(month): # unused : only if people from other (shiny !) country use the programm
	"""INPUT:
	*   month is an integer between 1 and 12
	*   month can be 'an' ('year' in French) for a yearly value

	This function calculates the maximum sunshine in the whole country for a given month.
	It allows to do get a sunshine ratio in the assessment of citrus, melons and other exotics trees
	and thus avoid some aberrations (melons and citrus in the northern, couldy regions !)."""


	month = int(month)
	if month == 12:
		i = 11
	else:
		month = month % 12
		i = month - 1

	return max( [ environment[PRA][269 + i] for PRA in environment if type(environment[PRA][269 + i]) != str] )

def SOLmoy_ratio_northernCountries(month, PRA):
	"""INPUT:
	*   month is an integer between 1 and 12
	*   month can be 'an' ('year' in French) for a yearly value

	This function calculates a sunshine ratio according to the monthly maximum sunshine in FRANCE for a given month.
	As South of France is wellknown for its sunny climate, it can be taken as a reference for other temperate climates.

	The output of this function is used in the assessment of citrus, melons and other exotics trees
	and thus avoid some aberrations (melons and citrus in the northern, couldy regions !)."""

	month = int(month)
	if month == 12:
		i = 11
	else:
		month = month % 12
		i = month - 1

	local_sunshine = environment[PRA][269 + i]

	maximum_sunshine_FR = [149.65, 173.8, 238.7, 245.8, 292.9, 333.4, 375.5, 332.7, 259.3, 195.9, 152.5, 136.65]

	return round( local_sunshine / maximum_sunshine_FR[month - 1], 4)


def ETPmoy(month, PRA):
	"""ETPmoy = "Evapotranspiration (potentielle) moyenne mensuelle"
	This function returns the average evapotranspiration for the selected month (ETP Penman in mm).
	'month' can be written as follows: 01, 02, 03, etc; or 1, 2, 3, etc.
	'an' gives the yearly average.

	ATTENTION :
	This function only works with the imported version of the original file "inputFR.ods" or a file with the same layout (sheets, columns in sheets...).
	The import of this sheet is ensured by the module 'importingODS.py'."""

	i=0
	if month == 'an':
		return environment[PRA][282+12]
	else:
		if str(month)[0] == 0:
			month = int(month[1:])
		month = int(month)
		if month % 12 == 0:
			i = 11
		else:
			month = month % 12
			i = month - 1
		return environment[PRA][282+i]




#############################################
#											#
#	VARIABLES FROM THE DICT 'nutrition'		#
#											#
#############################################


#~ nutrition_prodNAME_EN  = lambda crop:  nutrition[crop][ 1 ]
#~ nutrition_prodNAME_DE  = lambda crop:  nutrition[crop][ 2 ]
#~ nutrition_prodNAME_FR  = lambda crop:  nutrition[crop][ 3 ]
#~ nutrition_prodNAME_SC  = lambda crop:  nutrition[crop][ 4 ]
prodQUANTITY	= lambda crop:  nutrition[crop][ 5 ]
#~ prodWEIGHT= lambda crop:  nutrition[crop][ 6 ] # always 1kg
#~ Water = lambda crop:  nutrition[crop][ 7 ] # acc. to 'Plant Science'
#~ Sodium	= lambda crop:  nutrition[crop][ 8 ]
Magnesium  = lambda crop:  nutrition[crop][ 9 ]
Phosphore  = lambda crop:  nutrition[crop][ 10 ]
Potassium  = lambda crop:  nutrition[crop][ 11 ]
Calcium  = lambda crop:  nutrition[crop][ 12 ]
Manganese  = lambda crop:  nutrition[crop][ 13 ]
Fer  = lambda crop:  nutrition[crop][ 14 ]
Cuivre  = lambda crop:  nutrition[crop][ 15 ]
Zinc  = lambda crop:  nutrition[crop][ 16 ]
Selenium  = lambda crop:  nutrition[crop][ 17 ]
Iode  = lambda crop:  nutrition[crop][ 18 ]
#~ Proteinses  = lambda crop:  nutrition[crop][ 19 ]
Proteins  = lambda crop:  nutrition[crop][ 20 ]   # "protéines brutes" (in the Ciqual table)
Glucides  = lambda crop:  nutrition[crop][ 21 ]	# carbohydrates
Sucres  = lambda crop:  nutrition[crop][ 22 ]
energie_kJ  = lambda crop:  nutrition[crop][ 23 ]
energie_kcal  = lambda crop:  nutrition[crop][ 24 ]
#~ amidon  = lambda crop:  nutrition[crop][ 25 ]
#~ Énergie, N x facteur Jones, avec fibres (kJ/1kg)  = lambda crop:  nutrition[crop][ 26 ]
#~ Énergie, N x facteur Jones, avec fibres (kcal/1kg)  = lambda crop:  nutrition[crop][ 27 ]
polyolsTotaux  = lambda crop:  nutrition[crop][ 28 ]
fibres  = lambda crop:  nutrition[crop][ 29 ]
#~ eau  = lambda crop:  nutrition[crop][ 30 ] # water (acc. to Ciqual)
lipides  = lambda crop:  nutrition[crop][ 31 ]
vitA  = lambda crop:  nutrition[crop][ 32 ] # Rétinol
#~ vitA_Beta-Carotène  = lambda crop:  nutrition[crop][ 33 ]
#~ vit-provitA  = lambda crop:  nutrition[crop][ 34 ]
vitD	= lambda crop:  nutrition[crop][ 35 ]
vitE	= lambda crop:  nutrition[crop][ 36 ]
#~ vitK1	= lambda crop:  nutrition[crop][ 37 ]
#~ vitK2	= lambda crop:  nutrition[crop][ 38 ]
vitC	= lambda crop:  nutrition[crop][ 39 ]
vitB1	= lambda crop:  nutrition[crop][ 40 ]	# Thiamine
vitB2	= lambda crop:  nutrition[crop][ 41 ]	# Riboflavine
vitB3	= lambda crop:  nutrition[crop][ 42 ]	# PP or Niacine
vitB5	= lambda crop:  nutrition[crop][ 43 ]	# pentothénique acid
vitB6	= lambda crop:  nutrition[crop][ 44 ]
vitB12	= lambda crop:  nutrition[crop][ 45 ]
vitB9	= lambda crop:  nutrition[crop][ 46 ] 	# total folates ("Folates totaux")
#~ AG saturés  = lambda crop:  nutrition[crop][ 47 ]
#~ AGmonoinsaturés  = lambda crop:  nutrition[crop][ 48 ]
#~ AGpolyinsaturés  = lambda crop:  nutrition[crop][ 49 ]
#~ AGbutyrique  = lambda crop:  nutrition[crop][ 50 ]
#~ AGcaproéque  = lambda crop:  nutrition[crop][ 51 ]
#~ AGcaprylique  = lambda crop:  nutrition[crop][ 52 ]
#~ AGcaprique  = lambda crop:  nutrition[crop][ 53 ]
#~ AGlaurique  = lambda crop:  nutrition[crop][ 54 ]
#~ AGmyristique  = lambda crop:  nutrition[crop][ 55 ]
#~ AGpalmitique  = lambda crop:  nutrition[crop][ 56 ]
#~ AGstéarique  = lambda crop:  nutrition[crop][ 57 ]
#~ AGoléique  = lambda crop:  nutrition[crop][ 58 ]
#~ AGlinoléique  = lambda crop:  nutrition[crop][ 59 ]
#~ AGalpha-linolénique  = lambda crop:  nutrition[crop][ 60 ]
#~ AGarachidonique  = lambda crop:  nutrition[crop][ 61 ]
#~ Alcool  = lambda crop:  nutrition[crop][ 62 ]
#~ Acides organiques  = lambda crop:  nutrition[crop][ 63 ]
#~ Cholestérol  = lambda crop:  nutrition[crop][ 64 ]
