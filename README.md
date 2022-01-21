# UV-LARM-Jade - Branche challenge3
Respository du groupe Jade de l'UV 2021 challlenge 3

Simon Boudoux - Leslie Rineau

Cloner notre repo:
```bash
git clone https://github.com/Leslie-Douai/UV-LARM-Jade.git
```
## Code

Pour avoir accès au challenge 3
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


## Lancement
_Simulation_
```bash
catkin_make
source devel/setup.bash
roslaunch grp-jade challenge3_simulation.launch
```
_tbot_
```bash
catkin_make
source devel/setup.bash
roslaunch grp-jade challenge3_tbot.launch
```

Start rviz to visualize the map (if it is not automaticaly started)

## Objectifs :

_Minimal_
1. The group follows the consigns (i.e. the repository is presented as expected)
2. The robot navigate to goal position provided with rviz
3. The robot build a map in /map topic
4. The robot detects 1st-version-bottle (orange one) and publish markers in /bottle topic at the position of detected bottles.

_Optional_
1. he robot detect 2d-version-bottle (black one)
2. There is no need to publish goal positions. The robot is autonomous to achieve its mission.
3. Any suggestions provided by the group are welcome.

## Mots des élèves
Pour ce challenge 3 nous avons essayer de faire en sorte que le robot fasse des ricochets pour mapper l'espace et puis il y a la partie vision qui récupère en théorie les positions des bouteilles et qui les met sur la map à l'aide de marqueurs.
Il y a cependant quelques souci sur la publications des marqueurs

# Environnement de travail
**`Covid19`**
**`Fatigue`**
**`Usure mentale`**
**`IS`**

_Simon_ 

Je viens d'IS 


_Leslie_

Depuis la rentrée du nouvel an, à la MDE l'épidémie de covid bat son plein instaurant un climat tendu et usant pour ses résidents qui se test régulièrement. 

Pour ma part j'ai été cas contact, un peu plus d'une dizaine de fois, depuis la rentrée. J'ai loupé plusieurs cours afin d'aller me faire tester, ou pour m'isoler quand j'étais un cas contact sérieux. J'ai également été bien fatiguée ces dernières semaines celà m'a freiner pour bosser l'UV


