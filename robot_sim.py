"""Find the final max distance of the robot during route."""


from collections import OrderedDict
from typing import Dict
from typing import List
from typing import Tuple


class RobotSim:
    """A robot on an infinite grid starts at (0, 0) and faces north. The
    robot can receive 3 possible commands:
    - -2: turn 90 degrees left
    - -1: turn 90 degrees right
    - [1, 9]: move forward x units

    Some of the grid locations are obstacles.  If the robot tries to move into
    locations with obstacles, they would stay in the previous location and
    just continue to follow the rest of the commands.

    Return the square of the farthest euclidean distance that the robot will
    be from the origin (ie. x^2 + y^2) during the route.

    https://leetcode.com/problems/walking-robot-simulation/

    Notes
    -----
    While my code is only faster than 13%, mem < 6%, this for me was more of
    an exercise on how to create good clean maintainable code.  The methods
    in the discussion sections are generally pretty messy throwaway code.

    """
    @staticmethod
    def run_sim(commands: List[int], obstacles: List[List[int]]) -> int:
        """Simulation of robot moving around on grid with obstacles.

        Parameters
        ----------
        commands
            List of commands to robot.
        obstacles
            List of obstacle locations.

        Returns
        -------
        Square of euclidean distance from origin.

        Examples
        --------
        >>> commands = [4, -1, 3]; obstacles = []
        >>> RobotSim.run_sim(commands, obstacles)
        25
        >>> commands = [4, -1, 4, -2, 4]; obstacles = [[2, 4]]
        >>> RobotSim.run_sim(commands, obstacles)
        65
        """
        # Init grid
        grid_orient = OrderedDict([('N', (0, 1)),
                                  ('E', (1, 0)),
                                  ('S', (0, -1)),
                                  ('W', (-1, 0))])
        start_loc = (0, 0)
        grid = Grid(grid_orient, start_loc, obstacles)

        # Init robot using facing parameters and loc, no need to couple to
        # grid object.
        robot = Robot(list(grid_orient.keys()), grid.start_loc)

        # Loop thru commands
        for command in commands:
            if command == 0:
                continue
            elif command == -2:
                robot.turn_left_onestep()
            elif command == -1:
                robot.turn_right_onestep()
            elif command > 0:
                robot.move_to_loc(grid.line_of_sight_obstacle_loc(
                    robot.loc, robot.facing, command))
            else:
                raise ValueError('Invalid Command')
        return robot.max_sq_euclidean_dist


class Robot:
    """Robot that can turn and move on 2D map.

    Parameters
    ----------
    facings
        List of direction facings. Initialize facing to first value, and each
        value is in the order of turning right successively.
    loc
        Location of robot.
    """
    def __init__(self, facings: List[str], loc: Tuple[int, int]):
        self._facings = tuple(facings)
        self._facing_idx = 0
        self._loc = loc
        self._max_euclidean_dist = 0

    @property
    def facing(self):
        """Facing."""
        return self._facings[self._facing_idx]

    @property
    def loc(self):
        """Location."""
        return self._loc

    @loc.setter
    def loc(self, new_loc: Tuple[int, int]):
        self._loc = new_loc

    @property
    def max_sq_euclidean_dist(self):
        """Max square euclidean distance from origin during the route."""
        return self._max_euclidean_dist

    def turn_right_onestep(self):
        """Turn right 1 step relative to facing."""
        self._facing_idx = (self._facing_idx + 1) % len(self._facings)

    def turn_left_onestep(self):
        """Turn left 1 step relative to facing."""
        self._facing_idx = (self._facing_idx - 1) % len(self._facings)

    def move_to_loc(self, new_loc: Tuple[int, int]):
        """Move to specified location and update max distance."""
        self.loc = new_loc

        euclidean_dist = sum([new_loc[dim] ** 2 for dim in range(len(new_loc))])
        if  euclidean_dist > self.max_sq_euclidean_dist:
            self._update_max_sq_euclidean_dist(euclidean_dist)

    def _update_max_sq_euclidean_dist(self, new_dist: int):
        self._max_euclidean_dist = new_dist


class Grid:
    """2D grid.

    Parameters
    ----------
    grid_orient
        Mapping of string to how to increment values on grid
    start_loc
        Starting location on grid.
    obstacles
        Obstacles present on grid.
    """
    def __init__(self, grid_orient: Dict[str, Tuple[int, int]], start_loc,
                 obstacles: List[List[int]]):
        self._grid_orient = grid_orient
        self._start_loc = start_loc
        self._obstacles = {tuple(_) for _ in obstacles}

    @property
    def start_loc(self):
        """Start location."""
        return self._start_loc

    @property
    def obstacles(self):
        """Obstacles present on the grid."""
        return self._obstacles

    def line_of_sight_obstacle_loc(self, loc: Tuple[int, int], facing: str,
                                   distance: int) -> Tuple[int, int]:
        """Calculates the final location based on current location and
        desired location and obstacles on grid.

        Parameters
        ----------
        loc
            Current location.
        facing
            Current facing.
        distance
            Distance to move in direction of facing.

        Returns
        -------
        Resulting location.
        """
        assert distance >= 0
        # Generate start -> end loc sequence
        line_of_sight_locs = [(loc[0] + step * self._grid_orient[facing][0],
                               loc[1] + step * self._grid_orient[facing][1])
                              for step in range(distance+1)]

        # Check for obstacles
        intersection_loc = self._obstacles & frozenset(line_of_sight_locs)
        for loc_ in intersection_loc:
            line_of_sight_locs[line_of_sight_locs.index(loc_)] = None

        # Return valid loc in front of 1st obstacle if present
        if None in line_of_sight_locs:
            return line_of_sight_locs[line_of_sight_locs.index(None)-1]
        return line_of_sight_locs[-1]
