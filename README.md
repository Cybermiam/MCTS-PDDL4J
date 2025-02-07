# Git des différents TP notés pour PDDL

Ce git contient les rendus des différents TPs réalisés pour le module Planification Automatique.

## Création d'un MCTS

Le fichier script.py génère des résultats visibles dans le fichier pdf [Monte Carlo](https://github.com/Cybermiam/PDDL4J-M2-IC/blob/main/Monte%20Carlo%20Tree%20Search%20Planning.pdf) à la source du projet.

Les classes appeleés sont MCRW et MCTOpti. Cependant, notre MCTS n'est pas optimisé, il reste donc globalement moins performant qu'un a*.

## SAT Planner

Le fichier SatResultsScript génère des .md visibles a la source du projet.
Plusieurs md seront créés avec différentes versions du SAT. 

Le script appelle la classe SATV2 pour réaliser l'encodage et le décodage, il utilise l'executable Validate dans VAL/bin en wsl puisqu'il ne marche pas sur windows.

Le fichier [SATResults5Problems.md](https://github.com/Cybermiam/PDDL4J-M2-IC/blob/main/SATResults5Problems.md) contient un essai du planner sans validation des plans afin de vérifier le bon fonctionnement du script.

Le fichier [SATResults10Problems.md](https://github.com/Cybermiam/PDDL4J-M2-IC/blob/main/SATResults10Problems.md) contient les résultats pour 10 problèmes sur 2 domaines, avec les scores, temps et pas, avec validation.

A noter que les resultats sont basés seulement sur deux domaines car le sat peut prendre jusqu'à 15 min par problème au dela du problème 4 sur depots et gripper. De plus, comparé a une execution sur linux, les temps de résolutions pour SAT semblent
faux, les résultats sont donc a prendre avec du recul.

La réponse à l'exercice 2 se trouve [dans ce fichier pdf](https://github.com/Cybermiam/PDDL4J-M2-IC/blob/main/PDDL%20TP%203%20-%20BOUHJOURA%20-%20DI%20MALTA.pdf).
