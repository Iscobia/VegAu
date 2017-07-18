#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


Canada_Health = {
	'Acide linoléique, n-6 (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Acide linoléique, n-6 (g/jour, AS)' : {
		'Enfants': {'4-8 ans': 10, '1-3 ans': 7},
		'Femmes': {'19-30 ans': 12, '31-50 ans': 12, '9-13 ans': 10, '51-70 ans': 12, '14-18 ans': 11, '> 70 ans': 12},
		'Hommes': {'19-30 ans': 17, '31-50 ans': 17, '9-13 ans': 12, '51-70 ans': 14, '14-18 ans': 16, '> 70 ans': 14},
		'Nourrissons': {'7-12 mois': 4.6, '0-6 mois': 4.4}
		},
	'Acide panthoénique (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Acide panthoénique (AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 3, '1-3 ans': 2},
		'Femmes': {'19-30 ans': 5, '31-50 ans': 5, '9-13 ans': 4, '51-70 ans': 5, '14-18 ans': 5, '> 70 ans': 5},
		'Hommes': {'19-30 ans': 5, '31-50 ans': 5, '9-13 ans': 4, '51-70 ans': 5, '14-18 ans': 5, '> 70 ans': 5},
		'Nourrissons': {'7-12 mois': 1.8, '0-6 mois': 1.7}
		},
	'Acide α-linolénique, n-3 (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Acide α-linolénique, n-3 (g/jour, AS)' : {
		'Enfants': {'4-8 ans': 0.9, '1-3 ans': 0.7},
		'Femmes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 1.0, '51-70 ans': 1.1, '14-18 ans': 1.1, '> 70 ans': 1.1},
		'Hommes': {'19-30 ans': 1.6, '31-50 ans': 1.6, '9-13 ans': 1.2, '51-70 ans': 1.6, '14-18 ans': 1.6, '> 70 ans': 1.6},
		'Nourrissons': {'7-12 mois': 0.5, '0-6 mois': 0.5}
		},
	'Arsenic (N/A, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Arsenic (N/A, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Biotine (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Biotine (AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 12, '1-3 ans': 8},
		'Femmes': {'19-30 ans': 30, '31-50 ans': 30, '9-13 ans': 20, '51-70 ans': 30, '14-18 ans': 25, '> 70 ans': 30},
		'Hommes': {'19-30 ans': 30, '31-50 ans': 30, '9-13 ans': 20, '51-70 ans': 30, '14-18 ans': 25, '> 70 ans': 30},
		'Nourrissons': {'7-12 mois': 6, '0-6 mois': 5}
		},
	'Bore (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 6, '1-3 ans': 3},
		'Femmes': {'19-30 ans': 20, '31-50 ans': 20, '9-13 ans': 11, '51-70 ans': 20, '14-18 ans': 17, '> 70 ans': 20},
		'Hommes': {'19-30 ans': 20, '31-50 ans': 20, '9-13 ans': 11, '51-70 ans': 20, '14-18 ans': 17, '> 70 ans': 20},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Bore (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Calcium (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 2500, '1-3 ans': 2500},
		'Femmes': {'19-30 ans': 2500, '31-50 ans': 2500, '9-13 ans': 3000, '51-70 ans': 2000, '14-18 ans': 3000, '> 70 ans': 2000},
		'Hommes': {'19-30 ans': 2500, '31-50 ans': 2500, '9-13 ans': 3000, '51-70 ans': 2000, '14-18 ans': 3000, '> 70 ans': 2000},
		'Nourrissons': {'7-12 mois': 1500, '0-6 mois': 1000}
		},
	'Calcium (mg/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 1000, '1-3 ans': 700},
		'Femmes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 1300, '51-70 ans': 1200, '14-18 ans': 1300, '> 70 ans': 1200},
		'Hommes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 1300, '51-70 ans': 1000, '14-18 ans': 1300, '> 70 ans': 1200},
		'Nourrissons': {'7-12 mois': 260, '0-6 mois': 200}
		},
	'Calcium (mg/jour, BME)' : {
		'Enfants': {'4-8 ans': 800, '1-3 ans': 500},
		'Femmes': {'19-30 ans': 800, '31-50 ans': 800, '9-13 ans': 1100, '51-70 ans': 1000, '14-18 ans': 1100, '> 70 ans': 1000},
		'Hommes': {'19-30 ans': 800, '31-50 ans': 800, '9-13 ans': 1100, '51-70 ans': 800, '14-18 ans': 1100, '> 70 ans': 1000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Chlore (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 2900, '1-3 ans': 23000},
		'Femmes': {'19-30 ans': 3600, '31-50 ans': 3600, '9-13 ans': 3400, '51-70 ans': 3600, '14-18 ans': 3600, '> 70 ans': 3600},
		'Hommes': {'19-30 ans': 3600, '31-50 ans': 3600, '9-13 ans': 3400, '51-70 ans': 3600, '14-18 ans': 3600, '> 70 ans': 3600},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Chlore (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 1900, '1-3 ans': 1500},
		'Femmes': {'19-30 ans': 2300, '31-50 ans': 2300, '9-13 ans': 2300, '51-70 ans': 2000, '14-18 ans': 2300, '> 70 ans': 1800},
		'Hommes': {'19-30 ans': 2300, '31-50 ans': 2300, '9-13 ans': 2300, '51-70 ans': 2000, '14-18 ans': 2300, '> 70 ans': 1800},
		'Nourrissons': {'7-12 mois': 570, '0-6 mois': 180}
		},
	'Choline (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 1000, '1-3 ans': 1000},
		'Femmes': {'19-30 ans': 3500, '31-50 ans': 3500, '9-13 ans': 2000, '51-70 ans': 3500, '14-18 ans': 3000, '> 70 ans': 3500},
		'Hommes': {'19-30 ans': 3500, '31-50 ans': 3500, '9-13 ans': 2000, '51-70 ans': 3500, '14-18 ans': 3000, '> 70 ans': 3500},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Choline (AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 250, '1-3 ans': 200},
		'Femmes': {'19-30 ans': 425, '31-50 ans': 425, '9-13 ans': 375, '51-70 ans': 425, '14-18 ans': 400, '> 70 ans': 425},
		'Hommes': {'19-30 ans': 550, '31-50 ans': 550, '9-13 ans': 375, '51-70 ans': 550, '14-18 ans': 550, '> 70 ans': 550},
		'Nourrissons': {'7-12 mois': 150, '0-6 mois': 125}
		},
	'Chrome (μg/ jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Chrome (μg/ jour, AS)' : {
		'Enfants': {'4-8 ans': 15, '1-3 ans': 11},
		'Femmes': {'19-30 ans': 25, '31-50 ans': 25, '9-13 ans': 21, '51-70 ans': 20, '14-18 ans': 24, '> 70 ans': 20},
		'Hommes': {'19-30 ans': 35, '31-50 ans': 35, '9-13 ans': 25, '51-70 ans': 30, '14-18 ans': 35, '> 70 ans': 30},
		'Nourrissons': {'7-12 mois': 5.5, '0-6 mois': 0.2}
		},
	'Cuivre (μg/ jour, AMT)' : {
		'Enfants': {'4-8 ans': 3000, '1-3 ans': 1000},
		'Femmes': {'19-30 ans': 10000, '31-50 ans': 10000, '9-13 ans': 5000, '51-70 ans': 10000, '14-18 ans': 8000, '> 70 ans': 10000},
		'Hommes': {'19-30 ans': 10000, '31-50 ans': 10000, '9-13 ans': 5000, '51-70 ans': 10000, '14-18 ans': 8000, '> 70 ans': 10000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Cuivre (μg/ jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 440, '1-3 ans': 340},
		'Femmes': {'19-30 ans': 900, '31-50 ans': 900, '9-13 ans': 700, '51-70 ans': 900, '14-18 ans': 890, '> 70 ans': 900},
		'Hommes': {'19-30 ans': 900, '31-50 ans': 900, '9-13 ans': 700, '51-70 ans': 900, '14-18 ans': 890, '> 70 ans': 900},
		'Nourrissons': {'7-12 mois': 220, '0-6 mois': 200}
		},
	'Cuivre (μg/ jour, BME)' : {
		'Enfants': {'4-8 ans': 340, '1-3 ans': 260},
		'Femmes': {'19-30 ans': 700, '31-50 ans': 700, '9-13 ans': 540, '51-70 ans': 700, '14-18 ans': 685, '> 70 ans': 700},
		'Hommes': {'19-30 ans': 700, '31-50 ans': 700, '9-13 ans': 540, '51-70 ans': 700, '14-18 ans': 685, '> 70 ans': 700},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Eau totale (L/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Eau totale (L/jour, AS)' : {
		'Enfants': {'4-8 ans': 1.7, '1-3 ans': 1.3},
		'Femmes': {'19-30 ans': 2.7, '31-50 ans': 2.7, '9-13 ans': 2.1, '51-70 ans': 2.7, '14-18 ans': 2.3, '> 70 ans': 2.7},
		'Hommes': {'19-30 ans': 3.7, '31-50 ans': 3.7, '9-13 ans': 2.4, '51-70 ans': 3.7, '14-18 ans': 3.3, '> 70 ans': 3.7},
		'Nourrissons': {'7-12 mois': 0.8, '0-6 mois': 0.7}
		},
	'Fer (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 40, '1-3 ans': 40},
		'Femmes': {'19-30 ans': 45, '31-50 ans': 45, '9-13 ans': 40, '51-70 ans': 45, '14-18 ans': 45, '> 70 ans': 45},
		'Hommes': {'19-30 ans': 45, '31-50 ans': 45, '9-13 ans': 40, '51-70 ans': 45, '14-18 ans': 45, '> 70 ans': 45},
		'Nourrissons': {'7-12 mois': 40, '0-6 mois': 40}
		},
	'Fer (mg/jour, ANR/AS' : {
		'Enfants': {'4-8 ans': 10, '1-3 ans': 7},
		'Femmes': {'19-30 ans': 18, '31-50 ans': 18, '9-13 ans': 8, '51-70 ans': 8, '14-18 ans': 15, '> 70 ans': 8},
		'Hommes': {'19-30 ans': 8, '31-50 ans': 8, '9-13 ans': 8, '51-70 ans': 8, '14-18 ans': 11, '> 70 ans': 8},
		'Nourrissons': {'7-12 mois': 11, '0-6 mois': 0.27}
		},
	'Fer (mg/jour, BME)' : {
		'Enfants': {'4-8 ans': 4.1, '1-3 ans': 3.0},
		'Femmes': {'19-30 ans': 8.1, '31-50 ans': 8.1, '9-13 ans': 5.7, '51-70 ans': 5, '14-18 ans': 7.9, '> 70 ans': 5},
		'Hommes': {'19-30 ans': 7.7, '31-50 ans': 7.7, '9-13 ans': 5.9, '51-70 ans': 7.7, '14-18 ans': 7.7, '> 70 ans': 7.7},
		'Nourrissons': {'7-12 mois': 6.9, '0-6 mois': 'ND'}
		},
	'Fibres totales (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Fibres totales(g/jour, AS)' : {
		'Enfants': {'4-8 ans': 25, '1-3 ans': 19},
		'Femmes': {'19-30 ans': 25, '31-50 ans': 25, '9-13 ans': 26, '51-70 ans': 21, '14-18 ans': 26, '> 70 ans': 21},
		'Hommes': {'19-30 ans': 38, '31-50 ans': 38, '9-13 ans': 31, '51-70 ans': 30, '14-18 ans': 38, '> 70 ans': 30},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Fluor (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 2.2, '1-3 ans': 1.3},
		'Femmes': {'19-30 ans': 10, '31-50 ans': 10, '9-13 ans': 10, '51-70 ans': 10, '14-18 ans': 10, '> 70 ans': 10},
		'Hommes': {'19-30 ans': 10, '31-50 ans': 10, '9-13 ans': 10, '51-70 ans': 10, '14-18 ans': 10, '> 70 ans': 10},
		'Nourrissons': {'7-12 mois': 0.9, '0-6 mois': 0.7}
		},
	'Fluor (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 1, '1-3 ans': 0.7},
		'Femmes': {'19-30 ans': 3, '31-50 ans': 3, '9-13 ans': 2, '51-70 ans': 3, '14-18 ans': 3, '> 70 ans': 3},
		'Hommes': {'19-30 ans': 4, '31-50 ans': 4, '9-13 ans': 2, '51-70 ans': 4, '14-18 ans': 3, '> 70 ans': 4},
		'Nourrissons': {'7-12 mois': 0.5, '0-6 mois': 0.01}
		},
	'Folate (AMT, μg/ jour)' : {
		'Enfants': {'4-8 ans': 400, '1-3 ans': 300},
		'Femmes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 600, '51-70 ans': 1000, '14-18 ans': 800, '> 70 ans': 1000},
		'Hommes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 600, '51-70 ans': 1000, '14-18 ans': 800, '> 70 ans': 1000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Folate (ANR/AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 200, '1-3 ans': 150},
		'Femmes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 300, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Hommes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 300, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Nourrissons': {'7-12 mois': 80, '0-6 mois': 65}
		},
	'Folate (BME, μg/ jour)' : {
		'Enfants': {'4-8 ans': 160, '1-3 ans': 120},
		'Femmes': {'19-30 ans': 320, '31-50 ans': 320, '9-13 ans': 250, '51-70 ans': 320, '14-18 ans': 330, '> 70 ans': 320},
		'Hommes': {'19-30 ans': 320, '31-50 ans': 320, '9-13 ans': 250, '51-70 ans': 320, '14-18 ans': 330, '> 70 ans': 320},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Glucides digestibles (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Glucides digestibles (g/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 130, '1-3 ans': 130},
		'Femmes': {'19-30 ans': 130, '31-50 ans': 130, '9-13 ans': 130, '51-70 ans': 130, '14-18 ans': 130, '> 70 ans': 130},
		'Hommes': {'19-30 ans': 130, '31-50 ans': 130, '9-13 ans': 130, '51-70 ans': 130, '14-18 ans': 130, '> 70 ans': 130},
		'Nourrissons': {'7-12 mois': 95, '0-6 mois': 60}
		},
	'Glucides digestibles (g/jour, BME)' : {
		'Enfants': {'4-8 ans': 100, '1-3 ans': 100},
		'Femmes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 100, '51-70 ans': 100, '14-18 ans': 100, '> 70 ans': 100},
		'Hommes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 100, '51-70 ans': 100, '14-18 ans': 100, '> 70 ans': 100},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Iode (μg/ jour, AMT)' : {
		'Enfants': {'4-8 ans': 300, '1-3 ans': 200},
		'Femmes': {'19-30 ans': 1100, '31-50 ans': 1100, '9-13 ans': 600, '51-70 ans': 1100, '14-18 ans': 900, '> 70 ans': 1100},
		'Hommes': {'19-30 ans': 1100, '31-50 ans': 1100, '9-13 ans': 600, '51-70 ans': 1100, '14-18 ans': 900, '> 70 ans': 1100},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Iode (μg/ jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 90, '1-3 ans': 90},
		'Femmes': {'19-30 ans': 150, '31-50 ans': 150, '9-13 ans': 120, '51-70 ans': 150, '14-18 ans': 150, '> 70 ans': 150},
		'Hommes': {'19-30 ans': 150, '31-50 ans': 150, '9-13 ans': 120, '51-70 ans': 150, '14-18 ans': 150, '> 70 ans': 150},
		'Nourrissons': {'7-12 mois': 130, '0-6 mois': 110}
		},
	'Iode (μg/ jour, BME)' : {
		'Enfants': {'4-8 ans': 65, '1-3 ans': 65},
		'Femmes': {'19-30 ans': 95, '31-50 ans': 95, '9-13 ans': 73, '51-70 ans': 95, '14-18 ans': 95, '> 70 ans': 95},
		'Hommes': {'19-30 ans': 95, '31-50 ans': 95, '9-13 ans': 73, '51-70 ans': 95, '14-18 ans': 95, '> 70 ans': 95},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Lipides totaux (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Lipides totaux (g/jour, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 30, '0-6 mois': 31}
		},
	'Magnésium (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 110, '1-3 ans': 65},
		'Femmes': {'19-30 ans': 350, '31-50 ans': 350, '9-13 ans': 350, '51-70 ans': 350, '14-18 ans': 350, '> 70 ans': 350},
		'Hommes': {'19-30 ans': 350, '31-50 ans': 350, '9-13 ans': 350, '51-70 ans': 350, '14-18 ans': 350, '> 70 ans': 350},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Magnésium (mg/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 130, '1-3 ans': 80},
		'Femmes': {'19-30 ans': 310, '31-50 ans': 320, '9-13 ans': 240, '51-70 ans': 320, '14-18 ans': 360, '> 70 ans': 320},
		'Hommes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 240, '51-70 ans': 400, '14-18 ans': 410, '> 70 ans': 400},
		'Nourrissons': {'7-12 mois': 75, '0-6 mois': 30}
		},
	'Magnésium (mg/jour, BME)' : {
		'Enfants': {'4-8 ans': 110, '1-3 ans': 65},
		'Femmes': {'19-30 ans': 255, '31-50 ans': 255, '9-13 ans': 200, '51-70 ans': 255, '14-18 ans': 300, '> 70 ans': 255},
		'Hommes': {'19-30 ans': 330, '31-50 ans': 350, '9-13 ans': 200, '51-70 ans': 350, '14-18 ans': 340, '> 70 ans': 350},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Manganèse (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 3, '1-3 ans': 2},
		'Femmes': {'19-30 ans': 11, '31-50 ans': 11, '9-13 ans': 6, '51-70 ans': 11, '14-18 ans': 9, '> 70 ans': 11},
		'Hommes': {'19-30 ans': 9, '31-50 ans': 9, '9-13 ans': 6, '51-70 ans': 9, '14-18 ans': 9, '> 70 ans': 9},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Manganèse (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 1.5, '1-3 ans': 1.2},
		'Femmes': {'19-30 ans': 1.8, '31-50 ans': 1.8, '9-13 ans': 1.6, '51-70 ans': 1.8, '14-18 ans': 1.6, '> 70 ans': 1.8},
		'Hommes': {'19-30 ans': 2.2, '31-50 ans': 2.2, '9-13 ans': 1.9, '51-70 ans': 2.2, '14-18 ans': 2.2, '> 70 ans': 2.2},
		'Nourrissons': {'7-12 mois': 0.6, '0-6 mois': 0.003}
		},
	'Molybdène (μg/ jour, AMT)' : {
		'Enfants': {'4-8 ans': 600, '1-3 ans': 300},
		'Femmes': {'19-30 ans': 2000, '31-50 ans': 2000, '9-13 ans': 1100, '51-70 ans': 2000, '14-18 ans': 1700, '> 70 ans': 2000},
		'Hommes': {'19-30 ans': 1700, '31-50 ans': 1700, '9-13 ans': 1100, '51-70 ans': 1700, '14-18 ans': 1700, '> 70 ans': 1700},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Molybdène (μg/ jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 22, '1-3 ans': 17},
		'Femmes': {'19-30 ans': 45, '31-50 ans': 45, '9-13 ans': 34, '51-70 ans': 45, '14-18 ans': 43, '> 70 ans': 45},
		'Hommes': {'19-30 ans': 43, '31-50 ans': 43, '9-13 ans': 34, '51-70 ans': 43, '14-18 ans': 43, '> 70 ans': 43},
		'Nourrissons': {'7-12 mois': 3, '0-6 mois': 2}
		},
	'Molybdène (μg/ jour, BME)' : {
		'Enfants': {'4-8 ans': 17, '1-3 ans': 13},
		'Femmes': {'19-30 ans': 34, '31-50 ans': 34, '9-13 ans': 26, '51-70 ans': 34, '14-18 ans': 33, '> 70 ans': 34},
		'Hommes': {'19-30 ans': 33, '31-50 ans': 33, '9-13 ans': 26, '51-70 ans': 33, '14-18 ans': 33, '> 70 ans': 33},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Niacine (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 10, '1-3 ans': 15},
		'Femmes': {'19-30 ans': 35, '31-50 ans': 35, '9-13 ans': 20, '51-70 ans': 35, '14-18 ans': 30, '> 70 ans': 35},
		'Hommes': {'19-30 ans': 35, '31-50 ans': 35, '9-13 ans': 20, '51-70 ans': 35, '14-18 ans': 30, '> 70 ans': 35},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Niacine (ANR/AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 6, '1-3 ans': 8},
		'Femmes': {'19-30 ans': 14, '31-50 ans': 14, '9-13 ans': 12, '51-70 ans': 14, '14-18 ans': 14, '> 70 ans': 14},
		'Hommes': {'19-30 ans': 16, '31-50 ans': 16, '9-13 ans': 12, '51-70 ans': 16, '14-18 ans': 16, '> 70 ans': 16},
		'Nourrissons': {'7-12 mois': 2, '0-6 mois': 4}
		},
	'Niacine (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 5, '1-3 ans': 6},
		'Femmes': {'19-30 ans': 11, '31-50 ans': 11, '9-13 ans': 9, '51-70 ans': 11, '14-18 ans': 11, '> 70 ans': 11},
		'Hommes': {'19-30 ans': 12, '31-50 ans': 12, '9-13 ans': 9, '51-70 ans': 12, '14-18 ans': 12, '> 70 ans': 12},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Nickel (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 0.3, '1-3 ans': 0.2},
		'Femmes': {'19-30 ans': 1, '31-50 ans': 1, '9-13 ans': 0.6, '51-70 ans': 1, '14-18 ans': 1, '> 70 ans': 1},
		'Hommes': {'19-30 ans': 1, '31-50 ans': 1, '9-13 ans': 0.6, '51-70 ans': 1, '14-18 ans': 1, '> 70 ans': 1},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Nickel (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Phosphore (BME)' : {
		'Enfants': {'4-8 ans': 405, '1-3 ans': 380},
		'Femmes': {'19-30 ans': 580, '31-50 ans': 580, '9-13 ans': 1055, '51-70 ans': 580, '14-18 ans': 1055, '> 70 ans': 580},
		'Hommes': {'19-30 ans': 580, '31-50 ans': 580, '9-13 ans': 1055, '51-70 ans': 580, '14-18 ans': 1055, '> 70 ans': 580},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Phosphore (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 3000, '1-3 ans': 3000},
		'Femmes': {'19-30 ans': 4000, '31-50 ans': 4000, '9-13 ans': 4000, '51-70 ans': 4000, '14-18 ans': 4000, '> 70 ans': 4000},
		'Hommes': {'19-30 ans': 4000, '31-50 ans': 4000, '9-13 ans': 4000, '51-70 ans': 4000, '14-18 ans': 4000, '> 70 ans': 4000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Phosphore (mg/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 500, '1-3 ans': 460},
		'Femmes': {'19-30 ans': 700, '31-50 ans': 700, '9-13 ans': 1250, '51-70 ans': 700, '14-18 ans': 1250, '> 70 ans': 700},
		'Hommes': {'19-30 ans': 700, '31-50 ans': 700, '9-13 ans': 1250, '51-70 ans': 700, '14-18 ans': 1250, '> 70 ans': 700},
		'Nourrissons': {'7-12 mois': 275, '0-6 mois': 100}
		},
	'Potassium (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Potassium (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 3800, '1-3 ans': 3000},
		'Femmes': {'19-30 ans': 4700, '31-50 ans': 4700, '9-13 ans': 4500, '51-70 ans': 4700, '14-18 ans': 4700, '> 70 ans': 4700},
		'Hommes': {'19-30 ans': 4700, '31-50 ans': 4700, '9-13 ans': 4500, '51-70 ans': 4700, '14-18 ans': 4700, '> 70 ans': 4700},
		'Nourrissons': {'7-12 mois': 700, '0-6 mois': 400}
		},
	'Protéines totales (g/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Protéines totales (g/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 19, '1-3 ans': 13},
		'Femmes': {'19-30 ans': 46, '31-50 ans': 46, '9-13 ans': 34, '51-70 ans': 46, '14-18 ans': 46, '> 70 ans': 46},
		'Hommes': {'19-30 ans': 56, '31-50 ans': 56, '9-13 ans': 34, '51-70 ans': 56, '14-18 ans': 52, '> 70 ans': 56},
		'Nourrissons': {'7-12 mois': 11, '0-6 mois': 9.1}
		},
	'Protéines totales (g/kg/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 0.95, '1-3 ans': 1.05},
		'Femmes': {'19-30 ans': 0.8, '31-50 ans': 0.8, '9-13 ans': 0.95, '51-70 ans': 0.8, '14-18 ans': 0.85, '> 70 ans': 0.8},
		'Hommes': {'19-30 ans': 0.8, '31-50 ans': 0.8, '9-13 ans': 0.95, '51-70 ans': 0.8, '14-18 ans': 0.85, '> 70 ans': 0.8},
		'Nourrissons': {'7-12 mois': 1.2, '0-6 mois': 1.52}
		},
	'Protéines totales(g/kg/jour, BME)' : {
		'Enfants': {'4-8 ans': 0.76, '1-3 ans': 0.87},
		'Femmes': {'19-30 ans': 0.66, '31-50 ans': 0.66, '9-13 ans': 0.76, '51-70 ans': 0.66, '14-18 ans': 0.71, '> 70 ans': 0.66},
		'Hommes': {'19-30 ans': 0.66, '31-50 ans': 0.66, '9-13 ans': 0.76, '51-70 ans': 0.66, '14-18 ans': 0.73, '> 70 ans': 0.66},
		'Nourrissons': {'7-12 mois': 1, '0-6 mois': 'ND'}
		},
	'Riboflavine (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Riboflavine (ANR/AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 0.5, '1-3 ans': 0.6},
		'Femmes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 0.9, '51-70 ans': 1.1, '14-18 ans': 1.0, '> 70 ans': 1.1},
		'Hommes': {'19-30 ans': 1.3, '31-50 ans': 1.3, '9-13 ans': 0.9, '51-70 ans': 1.3, '14-18 ans': 1.3, '> 70 ans': 1.3},
		'Nourrissons': {'7-12 mois': 0.3, '0-6 mois': 0.4}
		},
	'Riboflavine (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 0.4, '1-3 ans': 0.5},
		'Femmes': {'19-30 ans': 0.9, '31-50 ans': 0.9, '9-13 ans': 0.8, '51-70 ans': 0.9, '14-18 ans': 0.9, '> 70 ans': 0.9},
		'Hommes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 0.8, '51-70 ans': 1.1, '14-18 ans': 1.1, '> 70 ans': 1.1},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Silicium  (N/A, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Silicium (N/A, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Sodium (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 1900, '1-3 ans': 1500},
		'Femmes': {'19-30 ans': 2300, '31-50 ans': 2300, '9-13 ans': 2200, '51-70 ans': 2300, '14-18 ans': 2300, '> 70 ans': 2300},
		'Hommes': {'19-30 ans': 2300, '31-50 ans': 2300, '9-13 ans': 2200, '51-70 ans': 2300, '14-18 ans': 2300, '> 70 ans': 2300},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Sodium (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 1200, '1-3 ans': 1000},
		'Femmes': {'19-30 ans': 1500, '31-50 ans': 1500, '9-13 ans': 1500, '51-70 ans': 1300, '14-18 ans': 1500, '> 70 ans': 1200},
		'Hommes': {'19-30 ans': 1500, '31-50 ans': 1500, '9-13 ans': 1500, '51-70 ans': 1300, '14-18 ans': 1500, '> 70 ans': 1200},
		'Nourrissons': {'7-12 mois': 370, '0-6 mois': 120}
		},
	'Sulfate (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Sulfate (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Sélénium (μg/ jour, AMT)' : {
		'Enfants': {'4-8 ans': 150, '1-3 ans': 90},
		'Femmes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 280, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Hommes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 280, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Nourrissons': {'7-12 mois': 60, '0-6 mois': 45}
		},
	'Sélénium (μg/ jour, ANR/AS),' : {
		'Enfants': {'4-8 ans': 30, '1-3 ans': 20},
		'Femmes': {'19-30 ans': 55, '31-50 ans': 55, '9-13 ans': 40, '51-70 ans': 55, '14-18 ans': 55, '> 70 ans': 55},
		'Hommes': {'19-30 ans': 55, '31-50 ans': 55, '9-13 ans': 40, '51-70 ans': 55, '14-18 ans': 55, '> 70 ans': 55},
		'Nourrissons': {'7-12 mois': 20, '0-6 mois': 15}
		},
	'Sélénium (μg/ jour, BME)' : {
		'Enfants': {'4-8 ans': 23, '1-3 ans': 17},
		'Femmes': {'19-30 ans': 45, '31-50 ans': 45, '9-13 ans': 35, '51-70 ans': 45, '14-18 ans': 45, '> 70 ans': 45},
		'Hommes': {'19-30 ans': 45, '31-50 ans': 45, '9-13 ans': 35, '51-70 ans': 45, '14-18 ans': 45, '> 70 ans': 45},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Thiamine (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Thiamine (ANR/AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 0.5, '1-3 ans': 0.6},
		'Femmes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 0.9, '51-70 ans': 1.1, '14-18 ans': 1.0, '> 70 ans': 1.1},
		'Hommes': {'19-30 ans': 1.2, '31-50 ans': 1.2, '9-13 ans': 0.9, '51-70 ans': 1.2, '14-18 ans': 1.2, '> 70 ans': 1.2},
		'Nourrissons': {'7-12 mois': 0.2, '0-6 mois': 0.3}
		},
	'Thiamine (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 0.4, '1-3 ans': 0.5},
		'Femmes': {'19-30 ans': 0.9, '31-50 ans': 0.9, '9-13 ans': 0.7, '51-70 ans': 0.9, '14-18 ans': 0.9, '> 70 ans': 0.9},
		'Hommes': {'19-30 ans': 1.0, '31-50 ans': 1.0, '9-13 ans': 0.7, '51-70 ans': 1.0, '14-18 ans': 1.0, '> 70 ans': 1.0},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vanadium (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 18, '31-50 ans': 18, '9-13 ans': 'ND', '51-70 ans': 18, '14-18 ans': 'ND', '> 70 ans': 18},
		'Hommes': {'19-30 ans': 18, '31-50 ans': 18, '9-13 ans': 'ND', '51-70 ans': 18, '14-18 ans': 'ND', '> 70 ans': 18},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vanadium (mg/jour, AS)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine A (AMT, IU/ jour)' : {
		'Enfants': {'4-8 ans': 3000, '1-3 ans': 2000},
		'Femmes': {'19-30 ans': 10000, '31-50 ans': 10000, '9-13 ans': 5667, '51-70 ans': 10000, '14-18 ans': 9333, '> 70 ans': 10000},
		'Hommes': {'19-30 ans': 10000, '31-50 ans': 10000, '9-13 ans': 5667, '51-70 ans': 10000, '14-18 ans': 9333, '> 70 ans': 10000},
		'Nourrissons': {'7-12 mois': 2000, '0-6 mois': 2000}
		},
	'Vitamine A (AMT, μg/ jour)' : {
		'Enfants': {'4-8 ans': 900, '1-3 ans': 600},
		'Femmes': {'19-30 ans': 3000, '31-50 ans': 3000, '9-13 ans': 1700, '51-70 ans': 3000, '14-18 ans': 2800, '> 70 ans': 3000},
		'Hommes': {'19-30 ans': 3000, '31-50 ans': 3000, '9-13 ans': 1700, '51-70 ans': 3000, '14-18 ans': 2800, '> 70 ans': 3000},
		'Nourrissons': {'7-12 mois': 600, '0-6 mois': 600}
		},
	'Vitamine A (ANR/AS, IU/ jour)' : {
		'Enfants': {'4-8 ans': 1333, '1-3 ans': 1000},
		'Femmes': {'19-30 ans': 2333, '31-50 ans': 2333, '9-13 ans': 2000, '51-70 ans': 2333, '14-18 ans': 2333, '> 70 ans': 2333},
		'Hommes': {'19-30 ans': 3000, '31-50 ans': 3000, '9-13 ans': 2000, '51-70 ans': 3000, '14-18 ans': 3000, '> 70 ans': 3000},
		'Nourrissons': {'7-12 mois': 1667, '0-6 mois': 1333}
		},
	'Vitamine A (ANR/AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 400, '1-3 ans': 300},
		'Femmes': {'19-30 ans': 700, '31-50 ans': 700, '9-13 ans': 600, '51-70 ans': 700, '14-18 ans': 700, '> 70 ans': 700},
		'Hommes': {'19-30 ans': 900, '31-50 ans': 900, '9-13 ans': 600, '51-70 ans': 900, '14-18 ans': 900, '> 70 ans': 900},
		'Nourrissons': {'7-12 mois': 500, '0-6 mois': 400}
		},
	'Vitamine A (BME, IU/ jour)' : {
		'Enfants': {'4-8 ans': 917, '1-3 ans': 700},
		'Femmes': {'19-30 ans': 1667, '31-50 ans': 1667, '9-13 ans': 1400, '51-70 ans': 1667, '14-18 ans': 1617, '> 70 ans': 1667},
		'Hommes': {'19-30 ans': 2083, '31-50 ans': 2083, '9-13 ans': 1483, '51-70 ans': 2083, '14-18 ans': 2100, '> 70 ans': 2083},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine A (BME, μg/ jour)' : {
		'Enfants': {'4-8 ans': 275, '1-3 ans': 210},
		'Femmes': {'19-30 ans': 500, '31-50 ans': 500, '9-13 ans': 420, '51-70 ans': 500, '14-18 ans': 485, '> 70 ans': 500},
		'Hommes': {'19-30 ans': 625, '31-50 ans': 625, '9-13 ans': 445, '51-70 ans': 625, '14-18 ans': 630, '> 70 ans': 625},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine B12 (AMT, μg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine B12 (ANR/AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 1.2, '1-3 ans': 0.9},
		'Femmes': {'19-30 ans': 2.4, '31-50 ans': 2.4, '9-13 ans': 1.8, '51-70 ans': 2.4, '14-18 ans': 2.4, '> 70 ans': 2.4},
		'Hommes': {'19-30 ans': 2.4, '31-50 ans': 2.4, '9-13 ans': 1.8, '51-70 ans': 2.4, '14-18 ans': 2.4, '> 70 ans': 2.4},
		'Nourrissons': {'7-12 mois': 0.5, '0-6 mois': 0.4}
		},
	'Vitamine B12 (BME, μg/ jour)' : {
		'Enfants': {'4-8 ans': 1.0, '1-3 ans': 0.7},
		'Femmes': {'19-30 ans': 2.0, '31-50 ans': 2.0, '9-13 ans': 1.5, '51-70 ans': 2.0, '14-18 ans': 2.0, '> 70 ans': 2.0},
		'Hommes': {'19-30 ans': 2.0, '31-50 ans': 2.0, '9-13 ans': 1.5, '51-70 ans': 2.0, '14-18 ans': 2.0, '> 70 ans': 2.0},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine B6 (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 30, '1-3 ans': 40},
		'Femmes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 60, '51-70 ans': 100, '14-18 ans': 80, '> 70 ans': 100},
		'Hommes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 60, '51-70 ans': 100, '14-18 ans': 80, '> 70 ans': 100},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine B6 (ANR/AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 0.5, '1-3 ans': 0.6},
		'Femmes': {'19-30 ans': 1.3, '31-50 ans': 1.3, '9-13 ans': 1.0, '51-70 ans': 1.5, '14-18 ans': 1.2, '> 70 ans': 1.5},
		'Hommes': {'19-30 ans': 1.3, '31-50 ans': 1.3, '9-13 ans': 1.0, '51-70 ans': 1.7, '14-18 ans': 1.3, '> 70 ans': 1.7},
		'Nourrissons': {'7-12 mois': 0.1, '0-6 mois': 0.3}
		},
	'Vitamine B6 (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 0.4, '1-3 ans': 0.5},
		'Femmes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 0.8, '51-70 ans': 1.3, '14-18 ans': 1.0, '> 70 ans': 1.3},
		'Hommes': {'19-30 ans': 1.1, '31-50 ans': 1.1, '9-13 ans': 0.8, '51-70 ans': 1.4, '14-18 ans': 1.1, '> 70 ans': 1.4},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine C (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 400, '1-3 ans': 650},
		'Femmes': {'19-30 ans': 2000, '31-50 ans': 2000, '9-13 ans': 1200, '51-70 ans': 2000, '14-18 ans': 1800, '> 70 ans': 2000},
		'Hommes': {'19-30 ans': 2000, '31-50 ans': 2000, '9-13 ans': 1200, '51-70 ans': 2000, '14-18 ans': 1800, '> 70 ans': 2000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine C (ANR/AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 15, '1-3 ans': 25},
		'Femmes': {'19-30 ans': 75, '31-50 ans': 75, '9-13 ans': 45, '51-70 ans': 75, '14-18 ans': 65, '> 70 ans': 75},
		'Hommes': {'19-30 ans': 90, '31-50 ans': 90, '9-13 ans': 45, '51-70 ans': 90, '14-18 ans': 75, '> 70 ans': 90},
		'Nourrissons': {'7-12 mois': 40, '0-6 mois': 50}
		},
	'Vitamine C (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 13, '1-3 ans': 22},
		'Femmes': {'19-30 ans': 60, '31-50 ans': 60, '9-13 ans': 39, '51-70 ans': 60, '14-18 ans': 56, '> 70 ans': 60},
		'Hommes': {'19-30 ans': 75, '31-50 ans': 75, '9-13 ans': 39, '51-70 ans': 75, '14-18 ans': 63, '> 70 ans': 75},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine D (AMT, IU/ jour)' : {
		'Enfants': {'4-8 ans': 3000, '1-3 ans': 2500},
		'Femmes': {'19-30 ans': 4000, '31-50 ans': 4000, '9-13 ans': 4000, '51-70 ans': 4000, '14-18 ans': 4000, '> 70 ans': 4000},
		'Hommes': {'19-30 ans': 4000, '31-50 ans': 4000, '9-13 ans': 4000, '51-70 ans': 4000, '14-18 ans': 4000, '> 70 ans': 4000},
		'Nourrissons': {'7-12 mois': 1500, '0-6 mois': 1000}
		},
	'Vitamine D (AMT, μg/ jour)' : {
		'Enfants': {'4-8 ans': 75, '1-3 ans': 63},
		'Femmes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 100, '51-70 ans': 100, '14-18 ans': 100, '> 70 ans': 100},
		'Hommes': {'19-30 ans': 100, '31-50 ans': 100, '9-13 ans': 100, '51-70 ans': 100, '14-18 ans': 100, '> 70 ans': 100},
		'Nourrissons': {'7-12 mois': 38, '0-6 mois': 25}
		},
	'Vitamine D (ANR/AS, IU/ jour)' : {
		'Enfants': {'4-8 ans': 600, '1-3 ans': 600},
		'Femmes': {'19-30 ans': 600, '31-50 ans': 600, '9-13 ans': 600, '51-70 ans': 600, '14-18 ans': 600, '> 70 ans': 800},
		'Hommes': {'19-30 ans': 600, '31-50 ans': 600, '9-13 ans': 600, '51-70 ans': 600, '14-18 ans': 600, '> 70 ans': 800},
		'Nourrissons': {'7-12 mois': 400, '0-6 mois': 400}
		},
	'Vitamine D (ANR/AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 15, '1-3 ans': 15},
		'Femmes': {'19-30 ans': 15, '31-50 ans': 15, '9-13 ans': 15, '51-70 ans': 15, '14-18 ans': 15, '> 70 ans': 20},
		'Hommes': {'19-30 ans': 15, '31-50 ans': 15, '9-13 ans': 15, '51-70 ans': 15, '14-18 ans': 15, '> 70 ans': 20},
		'Nourrissons': {'7-12 mois': 10, '0-6 mois': 10}
		},
	'Vitamine D (BME, IU/ jour)' : {
		'Enfants': {'4-8 ans': 400, '1-3 ans': 400},
		'Femmes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 400, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Hommes': {'19-30 ans': 400, '31-50 ans': 400, '9-13 ans': 400, '51-70 ans': 400, '14-18 ans': 400, '> 70 ans': 400},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine D (BME, μg/ jour)' : {
		'Enfants': {'4-8 ans': 10, '1-3 ans': 10},
		'Femmes': {'19-30 ans': 10, '31-50 ans': 10, '9-13 ans': 10, '51-70 ans': 10, '14-18 ans': 10, '> 70 ans': 10},
		'Hommes': {'19-30 ans': 10, '31-50 ans': 10, '9-13 ans': 10, '51-70 ans': 10, '14-18 ans': 10, '> 70 ans': 10},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine E (AMT, mg/ jour)' : {
		'Enfants': {'4-8 ans': 300, '1-3 ans': 200},
		'Femmes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 600, '51-70 ans': 1000, '14-18 ans': 800, '> 70 ans': 1000},
		'Hommes': {'19-30 ans': 1000, '31-50 ans': 1000, '9-13 ans': 600, '51-70 ans': 1000, '14-18 ans': 800, '> 70 ans': 1000},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine E (ANR/AS, mg/ jour)' : {
		'Enfants': {'4-8 ans': 7, '1-3 ans': 6},
		'Femmes': {'19-30 ans': 15, '31-50 ans': 15, '9-13 ans': 11, '51-70 ans': 15, '14-18 ans': 15, '> 70 ans': 15},
		'Hommes': {'19-30 ans': 15, '31-50 ans': 15, '9-13 ans': 11, '51-70 ans': 15, '14-18 ans': 15, '> 70 ans': 15},
		'Nourrissons': {'7-12 mois': 5, '0-6 mois': 4}
		},
	'Vitamine E (BME, mg/ jour)' : {
		'Enfants': {'4-8 ans': 6, '1-3 ans': 5},
		'Femmes': {'19-30 ans': 12, '31-50 ans': 12, '9-13 ans': 9, '51-70 ans': 12, '14-18 ans': 12, '> 70 ans': 12},
		'Hommes': {'19-30 ans': 12, '31-50 ans': 12, '9-13 ans': 9, '51-70 ans': 12, '14-18 ans': 12, '> 70 ans': 12},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine K (AMT, μg/ jour)' : {
		'Enfants': {'4-8 ans': 'ND', '1-3 ans': 'ND'},
		'Femmes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Hommes': {'19-30 ans': 'ND', '31-50 ans': 'ND', '9-13 ans': 'ND', '51-70 ans': 'ND', '14-18 ans': 'ND', '> 70 ans': 'ND'},
		'Nourrissons': {'7-12 mois': 'ND', '0-6 mois': 'ND'}
		},
	'Vitamine K (AS, μg/ jour)' : {
		'Enfants': {'4-8 ans': 55, '1-3 ans': 30},
		'Femmes': {'19-30 ans': 90, '31-50 ans': 90, '9-13 ans': 60, '51-70 ans': 90, '14-18 ans': 75, '> 70 ans': 90},
		'Hommes': {'19-30 ans': 120, '31-50 ans': 120, '9-13 ans': 60, '51-70 ans': 120, '14-18 ans': 75, '> 70 ans': 120},
		'Nourrissons': {'7-12 mois': 2.5, '0-6 mois': 2.0}
		},
	'Zinc (mg/jour, AMT)' : {
		'Enfants': {'4-8 ans': 12, '1-3 ans': 7},
		'Femmes': {'19-30 ans': 40, '31-50 ans': 40, '9-13 ans': 23, '51-70 ans': 40, '14-18 ans': 34, '> 70 ans': 40},
		'Hommes': {'19-30 ans': 40, '31-50 ans': 40, '9-13 ans': 23, '51-70 ans': 40, '14-18 ans': 34, '> 70 ans': 40},
		'Nourrissons': {'7-12 mois': 5, '0-6 mois': 4}
		},
	'Zinc (mg/jour, ANR/AS)' : {
		'Enfants': {'4-8 ans': 5, '1-3 ans': 3},
		'Femmes': {'19-30 ans': 11, '31-50 ans': 11, '9-13 ans': 8, '51-70 ans': 11, '14-18 ans': 11, '> 70 ans': 11},
		'Hommes': {'19-30 ans': 8, '31-50 ans': 8, '9-13 ans': 8, '51-70 ans': 8, '14-18 ans': 9, '> 70 ans': 8},
		'Nourrissons': {'7-12 mois': 3, '0-6 mois': 2}
		},
	'Zinc (mg/jour, BME)' : {
		'Enfants': {'4-8 ans': 4, '1-3 ans': 2.5},
		'Femmes': {'19-30 ans': 9.4, '31-50 ans': 9.4, '9-13 ans': 7, '51-70 ans': 9.4, '14-18 ans': 8.5, '> 70 ans': 9.4},
		'Hommes': {'19-30 ans': 6.8, '31-50 ans': 6.8, '9-13 ans': 7, '51-70 ans': 6.8, '14-18 ans': 7.3, '> 70 ans': 6.8},
		'Nourrissons': {'7-12 mois': 2.5, '0-6 mois': 'ND'}
		},
	}

