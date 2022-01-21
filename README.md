# UV-LARM-Jade
Respository du groupe Jade de l'UV 2021

## Challenge 1
```bash
git clone https://github.com/Leslie-Douai/UV-LARM-Jade.git
```
Pour avoir accès au challenge 1
``` bash
git checkout challenge1
```
### Objectifs 
_Minimal:_

The group follows the consigns (i.e. the repository is presented as expected)
The robot behavior is safe (no collision with any obstacles)
The robot explore it environment
_Optional:_

Information is returned to rviz (started automaticaly) through ros geometry messages.
The robot movement is fluid (no stop) and fast
The behavior is split into several nodes (for example obstacle detection and move).
The group develops a specific strategy to optimize the exploration time (need to be stated in the README.md file)

## Challenge 2
```bash
git clone https://github.com/Leslie-Douai/UV-LARM-Jade.git
```
Pour avoir accès au challenge 2
``` bash
git checkout challenge2
```
### Objectifs 

_Minimal:_
The group follows the consigns (i.e. the repository is presented as expected)
The robot build a map in /map topic
The robot detect 1st-version-bottle (orange one) and publish markers /bottle topic at the position of the robot.

_Optional:_
Information is returned to rviz (started automaticaly, with appropriate configuration).
The map is good shapped even in large environement.
The robot detect 2d-version-bottle (black one)
The position of bottle in the map is precise.
The position of the bottle is streamed one and only one time in the /bottle topic.
All the bottle are detected (wathever the bottle position and the background).
Only the bottle are detected (even if similar object are in the environment).
A service permit to get all bottle positions


## Challenge 3
```bash
git clone https://github.com/Leslie-Douai/UV-LARM-Jade.git
```
Pour avoir accès au challenge 3
``` bash
git checkout challenge3
```
### Objectifs 
_Minimal:_
The group follows the consigns (i.e. the repository is presented as expected)
The robot navigate to goal position provided with rviz
The robot build a map in /map topic
The robot detects 1st-version-bottle (orange one) and publish markers in /bottle topic at the position of detected bottles.
_Optional:_
The robot detect 2d-version-bottle (black one)
There is no need to publish goal positions. The robot is autonomous to achieve its mission.
Any suggestions provided by the group are welcome.
