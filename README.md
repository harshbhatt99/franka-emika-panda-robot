# Franka Emika 7 DOF Robot ROS Noetic

This repository is utilizing the existing franka emika panda robot files to develop inverse kinematics solution.

## Description

Franka Emika Panda robot has the URDF file available on their github. Using the URDF file, the controller file has been customized and prepared. You can find that file under "config" folder. To calculate the Inverse Kinematics solution, IKPY library has been used. The launch file consists of the Python script with inverse kinematics calculations, the controller file and the Gazebo nodes to run the simulations.

## Getting Started

### Dependencies

* ROS Noetic
* Ubuntu 20.04

### Installing

* Clone the repository under src folder of your ROS workspace.
* Change current directory to ROS workspace and run "catkin_make"

### Executing program

* Run the launch file under the launch folder.

### Acknowledgement

* Franka Emika [https://github.com/frankaemika]
* Robotics Toolbox [https://petercorke.com/toolboxes/robotics-toolbox/]
* IKPY Library [https://ikpy.readthedocs.io/en/latest/]
