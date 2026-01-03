# 1. Présentation Générale

##  Titre du Projet
Projet Poudelard

##  Description brève
Ce projet consiste en la création d’un jeu d’aventure textuel en Python, inspiré de l’univers de Harry Potter.  
Le joueur crée un personnage, choisit ses attributs, achète ses fournitures, apprend des sortilèges, répond à un quiz magique et participe à un match de Quidditch.

##  Contributeurs
- **Léon TAILLEUX**  
- **Killian ZHOU**

---

##  Installation

###  Cloner le dépôt Git
```bash
git clone https://github.com/leonTllx/poudelard-Tailleux-Zhou-sc3.git
```
##  Utilisation

### Lancement du jeu
```bash
python -m poudelard.main
```
### Ou en exécutant directement dans l’IDE:
```bash
poudelard/main.py
```
### Exemple de déroulement

Création du personnage  
Lettre d’admission  
Rencontre dans le train  
Répartition dans une maison  
Apprentissage de 5 sorts  
Quiz magique  
Match final de Quidditch


##  Fonctionnalités Principales

- Création du personnage (nom, prénom, attributs personnalisés)
- Gestion complète des saisies utilisateur
- Rencontre scénarisée avec Ron, Hermione et Drago
- Test du Choixpeau → attribution de la maison
- Salle commune propre à chaque maison
- Apprentissage aléatoire de 5 sorts (JSON)
- Quiz magique (4 questions tirées aléatoirement)
- Gestion des points des maisons
- Simulation d’un match de Quidditch :
  - Attaques
  - Arrêts
  - Capture éventuelle du Vif d’Or
  - Score final et bonus de 500 points

    
# 2. Journal de Bord
##  Chronologie du Projet

Semaine 1 : Mise en place de l’arborescence + input_utils.py + module personnage.py.  
Semaine 2 : Chapitre 1 (lettre, Hagrid, achats, inventaire).  
Semaine 3 : Chapitre 2 (rencontres, test du Choixpeau, salle commune) + module maison.py.  
Semaine 4 : Chapitre 3 (sorts → quiz → score des maisons).  
Semaine 5 : Chapitre 4 (Quidditch) + finalisation du jeu.  
Semaine 6 : Nettoyage du code, tests finaux, rédaction du README, push final.

##  Répartition des Tâches

#### Léon TAILLEUX :
input_utils.py, Chapitre 1, Chapitre 3  
Corrections globales   
Partie Quidditch (Chapitre 4), intégration finale

#### Killian ZHOU :
maison.py, personnage.py, Chapitre 2  
JSON (inventaire, quiz, sorts, maisons, équipes)  
menu.py, tests d’intégration

# 3. Contrôle, Tests et Validation
##  Gestion des entrées et erreurs
###  Méthodes utilisées

demander_texte()  
→ validation texte non vide (strip()).  
demander_nombre()  
→ validation manuelle des chiffres via parcours caractère par caractère (méthode ord()).  
demander_choix()  
→ menus numérotés stricts.

###  Gestion des erreurs

Choix invalide → réaffichage du menu  
Nombre hors bornes → message explicatif  
Budget insuffisant → fin immédiate de la partie (exit())  
Objets obligatoires absents ou non achetables → fin propre du jeu  
Questions du quiz : comparaison robuste (lower() + strip())  
Chargement JSON : contrôle de la présence des clés minimales

###  Bugs connus

Aucun bug bloquant identifié à ce jour.  
Si le programme est exécuté trop rapidement, il peut y avoir des des problèmes au niveau des inputs, bien faire attention a jouer lentement au cas ou.


##  Stratégies de Test
###  Cas de test spécifiques

Tests de toutes les saisies invalides (lettres, vide, hors bornes…)  
Tests des chemins narratifs : acceptation / refus de la lettre  
Tests achat obligatoire → réussite / échec  
Tests répartition : avec différents attributs  
Tests apprentissage des sorts : quotas respectés  
Tests quiz : bonnes / mauvaises réponses  
Tests Quidditch :  
match sur 20 tours  
apparition du Vif d’Or  
victoire/défaite/match nul
