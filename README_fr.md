## VegAu : modéliser une autosuffisante théorique d'après des données climatiques, pédologiques et biologiques

Python 3.4
Projet en alpha

### Dépendances (au 13 mars 2017):
* **pyoo** (LibreOffice),
* **pyshp** (gestion des shapefile)

### Données d'entrée et temporaire dépendance à LibreOffice/OpenOffice
Étant **totalement débutante en Python** et souhaitant pouvoir offrir un **support visuel** à d'autres utilisateurs en attendant d'avoir un GUI, j'ai stocké mes données dans un fichier LibrOffice Calc. Pour établir le pont UNO, il est nécessaire d'avoir une **instance de LibreOffice ouverte** (sur Linux, entrer `soffice "--accept=socket,host=0,port=2002;urp;"` dans un terminal). Je n'ai pas encore réussi à établir le UNO-bridge sous Windows (W10), mais certains parviennent à contourner le bug de connexion en important le module `socket`.
Les **résultats** sont également **copiés vers un tableur "output.ods"** tant qu'aucun GUI ne sera en mesure de les montrer à l'utilisateur et de lui en permettre l'importation.

### Que lancer dans quel ordre:
* Lancer OpenOffice/LibreOffice en mode écoute : sous Linux, lancer la commande `soffice "--accept=socket,host=0,port=2002;urp;"` dans un terminal 
* **Vegau.py contient tous les fichiers dont il a besoin:**
   1. il importe les modules pyoo, shutil et ceil (de math)
   2. il crée et lance une copie de input.ods (nommée output.ods)
   3. il importe les fonctions contenues dans inputVariables.py (qui facilitent l'appel des données du tableur)
   4. il importe et lance progressivement les fonctions des autres fichiers python dans l'ordre suivant:
      1. **importation: inputVariables.py**
      2. **importation: PRAedibility.py** : crée la la feuille de calcul "PRAedibility" et y gère la création et lecture des colonnes, lignes et données
      3. **importation: PRAyields.py** : crée la la feuille de calcul "PRAyields" et y gère la création et lecture des colonnes, lignes et données
      4. **importation: step1.py**
      5. **fonction: `PRAedibilityTest()` (step1)**: Soumission de chaque culture à un **test d'éligibilité pour chaque PRA** pour le temps de sa période de gestation
      6. **fonction: `ASSESS_Priority()` (step1)**: pour chaque culture, **calcul d'indices "d'adaptabilité" et de priorité**
      7. **importation: PRArotat.py** -> crée la la feuille de calcul "PRAedibility" et y gère la création et lecture des colonnes, lignes et données
      8. **importation: PRAsimul.py** -> crée la la feuille de calcul "PRAsimul" et y gère la création et lecture des colonnes et données
      9. **importation: step2.py**
      10. **fonction: `PRArotation()` (step2)**: Élaboration d'une **rotation culturale jusqu'à épuisement des ressources du sol** et calcule d'un** indice compris entre 0 et 1 pour estimer la qualité de la ressource** par rapport aux exigences de la chaque culture.
      11. **importation: step3.py**
      12. **fonction: `ASSESS_Nutritional_feasibility()` (step3)**: Détermination de la quantité d'éléments nutritionnels obtenus d'après les rendements calculés par `PRArotation()` et comparaison avec les apports recommandés pour la population.



### Fonctions annexes:
À l'origine, les données d'entrée de l'onglet "ENVIRONMENT" n'étaient sont pas disponibles pour toutes les PRAs ni toutes les variables. Les fonctions comprises dans le fichier shapefile_homogenize.py doivent estimer les valeurs manquantes pour chaque variable en faisant la moyenne des valeurs disponible  dans les unités spatiales adjacentes (ici, des PRA). Cette fonction ne fait pas partie de VegAu à proprement parler, bien qu'elle puisse être utile à des utilisateurs futurs.
* **Dépendances:** les modules:
   * **shapefile** (pyshp, pour importer les données comprises dans le sapefile)
   * et **pyoo** (pour compléter le tableur de façon visuelle: les valeurs estimées apparaissent en gras et rouge).
Le fichier input.ods a déjà subit ce script et peut par conséquent être traité par VegAu directement. 


### Hiérarchie des fonctions de VegAu
VegAu se compose de trois parties:
1. **Étape 1**: `PRAedibilityTest()`. Soumission de chaque culture à un test d'éligibilité pour chaque PRA pour le temps de sa période de gestation
   1. `ASSESS_Tmin_germ(CROProw)_forFruits()`: **Arbres fruitiers** uniquement: vérification que la **température minimum** est bien en-dessous de la température nécessaire à la **fin de l'hivernage** des arbres fruitiers au moins une fois pendant l'hiver;
   2. `ASSESS_Tmin()`: On vérifie que la **température minimum** ne descende pas en dessous de celle supporté par la culture;
   3. `ASSESS_Water()`: On vérifie que les** besoins en eau** de la culture sont couverts par les précipitations;
   4. `ASSESS_pH()`: On vérifie que le** pH du sol** est bien compris dans la fenêtre de pH supportée par la culture.
   5.`ASSESS_PRAedibility()`:  **Synthèse des tests précédents** pour aboutir à un dictionnaire de cultures qui répondent à tous ces critères pour la PRA courante.
2. `ASSESS_Priority()`: Calcul d'**indices "d''adaptabilité" et de priorité** devant **aider au choix des cultures** lors de l'élaboration de la **rotation**. Cette fonction fait partie du "step1(.py)"
3. **Étape 2** : `PRArotation()`. Élaboration d'une **rotation culturale jusqu'à épuisement des ressources du sol**: si plus aucune culture ne peut pousser par manque d'éléments nutritifs, la rotation est terminée. **Pour chaque test** précédent le choix de la culture suivante, on calcule un** indice compris entre 0 et 1 pour estimer la qualité de la ressource** par rapport aux exigences de la plante (plus l'indice est haut, meilleure est la ressource/condition climatique).
   1. `FindOptimalSeedingDate()`: On cherche la **période de plantation idéale** pour chaque culture pouvant être plantée le plus tôt possible après la culture précédente (pour la première culture, le mois de départ est fixé à mars)
   2. `ASSESS_OptimalWaterRessources()`: On vérifie que la culture pourra recevoir **assez d'eau** si elle est plantée à la date déterminée en 3.1..
   3. `ASSESS_Nutrients()`: On vérifie que les éléments nutritifs du sol sont suffisants (prise en compte de la décomposition des cultures précédentes)
   4. `ASSESS_PestDiseases()`: On vérifie si la famille botanique de la culture est déjà présente dans la rotation et si la fréquence minimale entre deux cultures de cette famille est respectée. L'**indice de "ravageurs et maladies"** calculé suite à ce test est **pondéré par 2** lors de la synthèse des indices: les tests précédents suppriment les cultures de la liste s'ils ne correspondent pas aux critères établis, contrairement à la fonction ` ASSESS_PestDiseases()`. De ce fait, et compte tenu de l'**impact des ravageurs et maladies sur le rendement**, on lui importe plus d'importance qu'aux autres indices.
   5. `SelectedCrop = SelectCrop()`: **Sélection de la culture suivante** en fonction de la synthèse des indices précédents.
   6. `ASSESS_Water_CompanionCrop()` et `ASSESS_Nutrients_CompanionCrop()` : Évaluation de la possibilité d'implanter une "culture compagnon" (ex. trèfle) si les ressources en eau et en nutriments est suffisante.
   7. `APPLY_ResiduesDecomposition_of_PreviousCrops()`: Simulation de la **décomposition** des résidus de la **culture précédente**.
   8. `SelectedCrop_Harvest()`: Simulation de la **récolte** (les nutriments contenus dans la plante sont prélevés du sol)
   9. `APPLY_ResiduesDecomposition_of_SelectedCrop()`: Préparation de la** décomposition** des résidus de la** culture sélectionnée** (évaluation du délais et de la quantité des éléments nutritifs rendus au sol).
   10. `APPLY_ResiduesDecomposition_of_CompanionCrop()`: **Si culture compagnon**: Simulation de la décomposition des résidus de la culture compagnon
   11. Calcul du rendement en fonction de l'indice de ravageurs et maladies
   12. Adaptation du rendement en fonction de la sécheresse à laquelle la culture a dû faire face
4. **Étape 3:** `ASSESS_Nutritional_feasibility()`. Détermination de la quantité d'éléments nutritionnels obtenus d'après les rendements calculés lors de l'étape 2. On compare ensuite cette quantité aux besoins nutritionnels de la population en prenant en compte les classes d'âge des différentes strates de la population.


### Projet d'interface graphique:
Une fois le code fonctionnel et stable, il est prévu de lui offrir une **interface graphique cross-plateforme la plus épurée et intuitive possible**. Une maquette est disponible dans le **dossier VegAu_GUI**.

