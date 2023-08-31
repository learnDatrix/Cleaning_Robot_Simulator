"""
Purpose of project:
Simulates room cleaning robots:
- User chooses size of room
- User chooses number of robots
- User chooses whether the room should be cleaned by percentage or time
- A live demo is given of how the room is cleaned.
"""

import time
import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


class CleaningMode():
    """Class used to replace cleaning modes by names instead of numbers"""
    TIME_MODE = 1
    PERCENTAGE_MODE = 2


class Robot:
    """Class with attributes for whenever a robot instance is created"""
    def __init__(self, rows, cols):
        self.x_cord = 1
        self.y_cord = 1
        self.x_max = cols - 1
        self.y_max = rows - 1

    def move(self, direction):
        if direction == "right" and self.x_cord < self.x_max:
            self.x_cord += 1
        elif direction == "left" and self.x_cord >= 1:
            self.x_cord -= 1
        elif direction == "up" and self.y_cord < self.y_max:
            self.y_cord += 1
        elif direction == "down" and self.y_cord >= 1:
            self.y_cord -= 1

    def curr_position(self):
        return self.x_cord, self.y_cord


class Room:
    """Class for whenever a Room instance is created"""
    def __init__(self, x, y, num_bots, choice,  request):
        self.cols = x
        self.rows = y
        self.total_tiles = x * y
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self.num_bots = num_bots
        self.robots = [Robot(self.rows, self.cols) for _ in range(num_bots)]
        self.cleaned_tiles = 0
        self.choice = choice
        self.request = request
        self.start_cleaning_time = 0

    def _move_bots(self):
        """Move robots randomly by axis change of 1 in any of the 4 directions"""
        for robot in self.robots:
            direction = random.choice(['up', 'down', 'left', 'right'])
            robot.move(direction)

    def _upgrade_grid(self):
        """Upgrade current grid by updating the 2d array self.grid"""
        for robot in self.robots:
            col, row = robot.curr_position()
            if self.grid[row][col] == 0:
                self._clean_tile(row, col)
                self.cleaned_tiles += 1

    def _clean_tile(self, x, y):
        self.grid[x][y] = 1

    def _percentage_cleaned(self):
        percentage = (self.cleaned_tiles/self.total_tiles) * 100
        return percentage

    def clean(self):
        """Clean the room"""
        # Create a figure and plot the grid
        plt.ion()
        fig, ax = plt.subplots()

        # Create a discrete colour map | blue is clean and gray is dirty


        # Start counting time
        self.start_cleaning_time = time.time()

        # A continuos loop till the time request is met
        while True:
            self._move_bots()
            self._upgrade_grid()
            ax.grid()
            ax.set_xlim(0, self.cols)
            ax.set_ylim(0, self.rows)
            ax.set_xticks(range(self.cols + 1))
            ax.set_yticks(range(self.rows + 1))
            # update figure
            ax.imshow(self.grid, cmap= colors.ListedColormap(['red', 'blue']),origin='upper')
            plt.pause(0.5)
            if self.choice == CleaningMode.TIME_MODE:
                if (time.time() - self.start_cleaning_time) >= self.request:
                    print(f"In the span of {self.request} seconds, {self._percentage_cleaned():.2f} % was cleaned")
                    break
            elif self.choice == CleaningMode.PERCENTAGE_MODE:
                if self._percentage_cleaned() >= self.request:
                    print(f"In the span {time.time() - self.start_cleaning_time:.2f} seconds, {self.request} % was "
                          f"cleaned")
                    break

        plt.plot()


def main():
    # Validate input
    while True:
        x = int(input("Enter the number of boxes in the x direction (columns): "))
        if x > 0:
            break
        else:
            print("Value should be greater than 0")

    while True:
        y = int(input("Enter the number of boxes in the y direction (rows): "))
        if y > 0:
            break
        else:
            print("Value should be greate than 0")

    while True:
        num_bots = int(input("Enter the number of robots(need to be greater than 1): "))
        if num_bots > 0:
            break
        else:
            print("Value should be greater than 0")

    # Ask user how would they like the room to be cleaned
    print("\nHow would you like to clean the room:\n"
          "Option 1: By time (in seconds)\n"
          "Option 2: By percentage\n")
    while True:
        choice = int(input("Please choose 1 or 2: "))
        if choice == CleaningMode.TIME_MODE:
            while True:
                print("\nPlease enter the number of seconds to clean the room")
                time_requested = float(input("Time: "))
                if time_requested > 0:
                    break
                else:
                    print("Value should be greater than 0")
            break

        elif choice == CleaningMode.PERCENTAGE_MODE:
            while True:
                print("\nPlease enter the percentage of the room to be cleaned")
                percentage_requested = float(input("Percentage: "))
                if 0 < percentage_requested <= 100:
                    break
                else:
                    print("Percentage should be greater than 0 up to 100")
            break

        else:
            print("Please choose 1 or 2:")

    # Give user a debriefing of what was chosen
    print(f"\nProcess:\n"
          f"\nThe program will use {num_bots} robots to clean a room with {y} rows and "
          f"and {x} columns, equating to a surface area of {y * x} blocks"
          f"\nTIME TO CLEAN!!\n")

    # convert values to their equivalent units
    # convert time to milliseconds and divide percentage by 100
    if choice == CleaningMode.TIME_MODE:
        request = time_requested
    elif choice == CleaningMode.PERCENTAGE_MODE:
        request = percentage_requested

    # Pass request and choice to create a room figure
    room = Room(x, y, num_bots, choice, request)
    # Clean the room
    room.clean()

main()
