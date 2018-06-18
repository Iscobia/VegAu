#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#################################
#								#
#		IMPORTING MODULES		#
#								#
#################################

# inputVariables imports the modules pyoo and shutil

import os
import pyoo
#~ import subprocess 
#~ subprocess.call(["""soffice "--accept=socket,host=0,port=2002;urp;""""])
#~ os.popen("""" soffice "--accept=socket,host=0,port=2002;urp;" """)
#~ from importedVariables import *

#####################################################################	
#																	#
#		CONNECTION TO THE SPREADSHEETS IN ORDER TO WORK WITH		#
#							OR										#
#	IMPORTING DATA INTO A PYTHON FILE TO WORK WITHOUT UNO-BRIDGE	#
#																	#
#####################################################################

#======================================================================================
#~ # OPTION 1 : WORKING WITH AN ODS FILE ---> COPY INPUT.ODS AS OUTPUT.ODS AND OPEN OUTPUT.
#										-> JUST IMPORT  inputVariables.py

#~ print("Importing 'inputVariables'...") 
#~ from inputVariables import *
#~ print("	OK")



#======================================================================================
#OPTION 2 : JUST IMPORTING THE DATA FROM INPUT.ODS AND SAVE IT IN A PYTHON FILE

#~ print("Importing 'inputVariables'...") 
#~ from inputVariables import *
#~ print("	OK")


#################################
#								#
#			FUNCTION			#
#								#
#################################

desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("input.ods")
prodID	= lambda CROProw:	doc.sheets['PLANTS'][CROProw,1].value
IDPRA	= lambda PRA:	doc.sheets['ENVIRONMENT'][PRA,2].value

#=== Enhancing the result's layout before saving ====
def GoodLookingDict(dict_name):
	result_str	=	str(dict_name)
	result		=	'],\n'.join(result_str.split('],'))
	result		=	'},\n'.join(result.split('},'))
	return result


#################################
#								#
#		IMPORTING DATA			#
#								#
#################################

#======================================================================================
# Setting up the name of the file to extract (the python file will have the same name):
file_name = 'input'

dicts = {
	#~ 'ENVIRONMENT': 'environment',
	'PLANTS': 'plants',
	'NUTRITION': 'nutrition',
	#~ 'PRAvirgin': 'PRAvirgin_dict',
	#~ 'NUTRITIONvirgin': 'NUTRITIONvirgin_dict'
		}

#======================================================================================
# Clearing the output file if it already exists:

if os.path.exists( file_name + '.py' ):
		with open( file_name + '.py' , 'w') as saves:
			saves.write('# IMPORTED DATA FROM {}.ods'.format(file_name))


for sheet in dicts.keys():
	sheet_name = str(sheet)
	sheet = doc.sheets[sheet_name]
	print("Loading data from the '{}' sheet in to the dictionary '{}'...".format(sheet_name, dicts[sheet_name]))
	
	
	imported_data = {}
	row = 0
	
	while sheet[row, 0].value != '':			# while each line has not been copied
		col = 0
		
		
		#==================================================================================
		# Determining the keys ID:
		
		if sheet_name == 'PRAvirgin': # PRAvirgin is the only sheet to have only 1 row with headers
			if row == 0 :
				key = 'headers_ID'
				imported_data[key] = []
				print("Importing the headers' ID...")	
				
			else:
				if row == 1:
					print("Importing data from input.ods (sheet '{}') into '{}'...".format(sheet_name, dicts[sheet_name]) )
				try:
					key = int(doc.sheets['PRAvirgin'][row,1].value)
				except:
					key = doc.sheets['PRAvirgin'][row,1].value	# the Corsica Island has specific IDs with a letter (no conversion possible)  
				#~ print("Importing the PRA n°{} (row {})...".format(IDPRA(row), row) )
				imported_data[key] = {}
				imported_data[key]['PRA_index']	= row		# = PRA
		
		else:						# for all other sheets that have 2 rows with headers (full headers and headers ID)
			if row == 0 :
				key = 'headers_full'
				imported_data[key] = []
				print("Importing the full headers...")
				
			elif row == 1 :
				key = 'headers_ID'
				imported_data[key] = []
				print("Importing the headers' ID...")
				
				
			else:
				if row == 2:
					print("Importing data from input.ods (sheet '{}') into '{}'...".format(sheet_name, dicts[sheet_name]) )
				if sheet_name == 'ENVIRONMENT':
					key = IDPRA(row)
					#~ print("Importing the PRA n°{} (row {})...".format(IDPRA(row), row) )
					imported_data[key] = {}

								
				if sheet_name == 'PLANTS':
					key = doc.sheets['PLANTS'][row,1].value
					imported_data[key] = {}
					
					#Preparing the keys for the Priority Indexes (avoid KeyError by preparing the orresponding lamdba function)
					imported_data[key]['PRIORITYgeneral']	= 0
					imported_data[key]['PRIORITYfruits']	= 0
					imported_data[key]['PRIORITYtextile']	= 0					


				if sheet_name == 'NUTRITION' or sheet_name == 'NUTRITION_virgin':
					key = sheet[row, 0].value		# = prodID
					imported_data[key] = {}
			
			
		#==================================================================================
		# Enumerating the columns:
		
		while sheet[0, col].value != '':		# while each field/column has not been copied
			#~ print("row {}: Importing data from the column {} (field: '{}')".format(row, col, str(sheet[0, col])[1] ))
			if sheet_name == 'PRAvirgin':
				if row <= 0:
					imported_data[key].append(sheet[row, col].value)
				else:
					imported_data[key][col] = sheet[row, col].value
					
			else:			
				if row <= 1:
					imported_data[key].append(sheet[row, col].value)
				else:
					if '.' in str(sheet[row, col].value):							# if the cell value contain a point, it may be a float
						try:
							imported_data[key][col] = float(sheet[row, col].value)
						except :
							imported_data[key][col] = sheet[row, col].value			# for IDs from 'NUTRITION' that have points without being floats
					else:															# else, it is either an interger or a string
						try :
							imported_data[key][col] = int(sheet[row, col].value)	# if it can't be converted into an integer, it is a string
						except:
							imported_data[key][col] = sheet[row, col].value
			
			col += 1
			# END while (columns)
			
		row += 1
		# END while (lines)
	
	print("""	'{}' has been successfully created, it contains {} entries.""".format( dicts[sheet_name], len(imported_data.keys()) ) )
	
	
	
	#==== Saving the results...====
	print("Saving '{}' in  {} ...".format(dicts[sheet_name], file_name + '.py'))
	

	with open( file_name + '.py' , 'a') as saves:
		saves.write("""\n\n\n {} = {}\n""".format(dicts[sheet_name], '{'))
		for i, row in enumerate(imported_data.keys()):
			
			try:
				rowCORR = str(int(row))
				
				if len(rowCORR) < 5 :
					CORRrow = '0' + str(rowCORR)
				else:
					CORRrow = str(rowCORR)
			except ValueError:
				rowCORR = str(row)
				
			if (i+1) != len(imported_data):
				saves.write("	'{}': {},\n".format(rowCORR, imported_data[row]))
			else:
				saves.write("	'{}': {}\n {}".format(rowCORR, imported_data[row], '}'))
		#~ saves.write( GoodLookingDict(imported_data) )

	
	print("""	OK
	
	""") 

