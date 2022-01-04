# UV-LARM-Jade - Branche challenge1
Respository du groupe Jade de l'UV 2021 pour le challenge1

Simon Boudoux - Leslie Rineau

Attention : il faut cloner le repository mb6-tbot
https://bitbucket.org/imt-mobisyst/mb6-tbot.git

Le code est simpliste : quand le robot à un obstacle dans une zone autour de lui que nous avons défini, il tourne jusqu'à ce que la voie soit libre

Le code est agrémenté de print pour que nous sachions à quelle étape de raisonnement il est.

Voie d'amélioration : 
- Lui faire prendre de la vitesse quand il n'y a pas d'obstacle et ralentir sinon
- Lui donner une stratégie d'évitement des obstacles qui quadrillerait plus la zone

Rappel des commandes de test :

_Simulation_

roslaunch grp-color challenge1.launch

_Démonstration_

roslaunch grp-color challenge1.launch
