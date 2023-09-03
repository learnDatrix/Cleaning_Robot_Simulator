# Cleaning_Robot_Simulator

# Room Cleaning Simulator README

## Overview

This Python program is designed using Object-Oriented Programming (OOP) principles to simulate a room cleaning scenario. It provides users with a flexible and interactive environment to control cleaning robots.

## Features

- **User-Defined Room Dimensions**: Users are prompted to specify the dimensions of the room in terms of rows and columns.

- **Multi-Robot Cleaning**: Users can specify the number of robots that will work simultaneously to clean the room.

- **Cleaning Mode Selection**: Users can choose between two cleaning modes:
  - *Time-Specified Cleaning*: Users set a time limit for the cleaning process.
  - *Percentage-Based Cleaning*: Users specify the desired percentage of the room to be cleaned.

- **Threshold Configuration**: For percentage-based cleaning, users can set a threshold percentage for the cleaning process.

- **Live Simulation**: The program uses Matplotlib to provide a real-time visualization of the cleaning process. Cleaned areas are displayed in blue, while dirty areas are shown in red.

- **Cleaning Progress Report**: At the end of the simulation, users are presented with a report that includes:
  - The percentage of the room that was cleaned.
  - If the user opted for percentage-based cleaning, the time taken for the cleaning process is also displayed.

## How to Use

1. Run the program.
2. Follow the prompts to specify room dimensions, the number of cleaning robots, cleaning mode, and threshold (if applicable).
   ![prompt by program](/screenshots/prompt.png)
     
4. Observe the live simulation to track the cleaning progress.
   ![live demonstration of matplotlib](/screenshots/live_demonstration.png)
5. Upon completion, view the detailed cleaning report, including the percentage of the room cleaned and, if applicable, the time taken.

Enjoy experimenting with the room cleaning simulator and exploring the different cleaning scenarios it offers!
