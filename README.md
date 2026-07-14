# AutoNavRobot

AutoNavRobot is a ROS 2-based autonomous mobile robot designed to navigate indoor environments using LiDAR sensing, obstacle avoidance, and SLAM mapping.

## Project Goal

Build a portfolio-quality autonomous navigation robot that combines:

- Embedded hardware
- Robotics software
- Motor control
- LiDAR sensing
- Obstacle avoidance
- SLAM mapping
- Autonomous navigation
- ROS2

## Hardware

- Raspberry Pi 4 Model B, 4GB RAM
- SLAMTEC RPLIDAR A1M8
- SunFounder Zeus robot car platform
- Dual H-Bridge motor driver
- 7.4V 2000mAh Li-ion battery
- 64GB microSD card

## Software

- Ubuntu Server 24.04 LTS
- ROS 2 Jazzy Jalisco
- Python
- Git and GitHub
- Visual Studio Code
- SSH remote development

## ROS 2 Packages

### `autonavrobot_startup`

Startup and system-launch package for the AutoNavRobot platform.

It will eventually coordinate:

- Motor control
- LiDAR drivers
- Obstacle avoidance
- SLAM
- Navigation
- Safety checks

## Current Progress

- [x] Create GitHub repository
- [x] Configure Raspberry Pi
- [x] Install Ubuntu 24.04
- [x] Configure SSH and remote development
- [x] Install ROS 2 Jazzy
- [x] Create ROS 2 workspace
- [x] Create `autonavrobot_startup` package
- [ ] Create first ROS 2 node
- [ ] Assemble robot chassis
- [ ] Wire motors and motor driver
- [ ] Implement motor control
- [ ] Integrate RPLIDAR
- [ ] Implement obstacle avoidance
- [ ] Generate maps with SLAM
- [ ] Implement autonomous navigation

## Repository Structure

```text
autonomous-navigation-robot/
├── docs/
├── hardware/
├── photos/
├── software/
│   └── ros2_ws/
│       └── src/
│           └── autonavrobot_startup/
├── videos/
├── .gitignore
└── README.md
```


### Project Status

Currently in development.


### Timeline

Week 1: Environment setup
Week 2: Hardware Assembly
...

Expected completion:

July 26, 2026

