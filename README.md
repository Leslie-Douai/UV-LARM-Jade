# UV-LARM-Jade - Branche challenge3
Respository du groupe Jade de l'UV 2021 pour le challenge1

Simon Boudoux - Leslie Rineau

Attention : il faut cloner le repository mb6-tbot
https://bitbucket.org/imt-mobisyst/mb6-tbot.git

Repo à clone:
```bash
git clone https://github.com/Leslie-Douai/UV-LARM-Jade.git
```
## Lancement

Pour avoir acces au challenge 3
``` bash
git checkout challenge3
```

## Ressources
**`python3`**
**`ROS noetic`**
**`mb6-bot`**
**`Gmapping`**
**`numpy`**
**`tensorflow`**
**`openCV`**
**`sklearn`**
**`scipy`**
**`matplotlib`**
**`psutil`**
**`realsense2_camera`**
```bash
git clone https://bitbucket.org/imt-mobisyst/mb6-tbot.git

sudo apt install ros-noetic-openslam-gmapping ros-noetic-slam-gmapping

sudo apt install \
    librealsense2-dkms \
    librealsense2-utils \
    librealsense2-dev \
    librealsense2-dbg \

pip3 install numpy tensorflow opencv-python opencv-contrib-python sklearn scipy matplotlib psutil
```
_De plus ample information sont disponible sur le gitbook :_
https://ceri-num.gitbook.io/uv-larm/ 




roslaunch grp-jade challenge3.launch
echo the bottle topic

Start rviz to visualize the map (if it is not automaticaly started)

Objectif :
Criteria
minimal
1. The group follows the consigns (i.e. the repository is presented as expected)
2. The robot navigate to goal position provided with rviz
3. The robot build a map in /map topic
4. The robot detects 1st-version-bottle (orange one) and publish markers in /bottle topic at the position of detected bottles.

Optional
1. he robot detect 2d-version-bottle (black one)
2. There is no need to publish goal positions. The robot is autonomous to achieve its mission.
3. Any suggestions provided by the group are welcome.

Evaluation protocol
1. clone the group’s repository
2. check out the appropriate branch git checkout challenge3
3. README.md also mention if the group targeted (and how) some of the optional features.
4. make it: catkin_make and source from the catkin directory.
5. Launch the demonstration: roslaunch grp-color challenge3_simulation.launch, provide successively some goals (if required) and appreciate the resulting map.
6. Launch the demonstration: roslaunch grp-color challenge3_tbot.launch, echo \bottle topic, provide successively some goals (if required) and appreciate the resulting map.
7. Take a look to the code, by starting from the launch files.

Pour ce challenge 3 nous avons essayer de faire en sorte que le robot fasse des ricochets pour mapper l'espace et puis il y a la partie vision qui récupère en théorie les positions des bouteilles et qui les met sur la map à l'aide de marqueurs.
Il y a cependant quelques souci sur la publications des marqueurs
