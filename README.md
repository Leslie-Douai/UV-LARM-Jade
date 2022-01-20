# UV-LARM-Jade - Branche challenge3
Respository du groupe Jade de l'UV 2021 pour le challenge1

Simon Boudoux - Leslie Rineau

Attention : il faut cloner le repository mb6-tbot
https://bitbucket.org/imt-mobisyst/mb6-tbot.git

_Lancement_

roslaunch grp-jade challenge3.launch
echo the bottle topic

Start rviz to visualize the map (if it is not automaticaly started)

Objectif :
Criteria
minimal
1. The group follows the consigns (i.e. the repository is presented as expected)
2. The robot build a map in /map topic
3. The robot detect bottle and publish markers /bottle topic

Optional
1. Information is returned to rviz (started automaticaly, with appropriate configuration).
2. The map is good shapped even in large environemen
3. The position of bottle in the map is precise.
4. The position of the bottle is streamed one and only one time in the /bottle topic.
5. All the bottle are detected (wathever the bottle position and the background).
6. Only the bottle are detected (even if similar object are in the environment).
7. A service permit to get all bottle positions

Evaluation protocol
1. clone the group’s repository
2. check out the appropriate branch git checkout challenge2
3. Take a look to what is inside the repository and read the README.md file (normally it states that the project depends on mb6-tbot, make sure that mb6-tbot project is not included in the studient project but already installed aside).
4. make it: catkin_make and source from the catkin directory.
5. Launch the demonstration: roslaunch grp-color challenge2.launch, echo the bottle topic, start rviz to visualize the map (if it is not automaticaly started)
6. Appreciate the solution with differents rosbag.
7. Stop everything.
8. Take a look to the code, by starting from the launchfiles.

Pour ce challenge 3 nous avons essayer de faire en sorte que le robot fasse des ricochets pour mapper l'espace et puis il y a la partie vision qui récupère en théorie les positions des bouteilles et qui les met sur la map à l'aide de marqueurs.
Il y a cependant quelques souci sur la publications des marqueurs
