from collections import defaultdict

''' You are given a stream of points on the X-Y plane. Design an algorithm that adds new points from the stream into a data structure. 
    Duplicate points are allowed and should be treated as different points.
    Given a query point, counts the number of ways to choose three points from the data structure such 
    that the three points and the query point form an axis-aligned square with positive area.
    An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.'''


class DetectSquaresNaive:
    def __init__(self):
        self.x_points = defaultdict(list)
        self.y_points = defaultdict(list)

    def add(self, point: list[int, int]) -> None:
        x, y = point
        # How many different x points are there for same y?
        self.x_points[y].append(x)
        # How many different y points are there for same x?
        self.y_points[x].append(y)

    def count(self, point: list[int, int]) -> int:
        def helper(x: int, y: int, dist: int, points: int) -> int:
            # And finally look for the fourth point that ends up closing the square
            if points == 3:
                return sum(1 for ny in self.y_points[x] if abs(ny-y) == dist and ny == start_y)

            # We previously matched a point with same 'y' coord, now look for 'x' coord that's of same distance
            return sum(helper(nx, y, dist, points+1) for nx in self.x_points[y] if abs(nx-x) == dist)

        start_x, start_y = point
        # Calculate dist for every point with same x as given point, and start looking for 2 more points that would form a square
        return sum(helper(start_x, ny, abs(ny-start_y), 2) for ny in self.y_points[start_x] if ny != start_y)


class DetectSquaresOptimized:
    def __init__(self):
        self.points = {}

    def add(self, point: list[int, int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0)+1

    def count(self, point: list[int, int]) -> int:
        x, y = point
        count = 0
        for (nx, ny), freq in self.points.items():
            # Not a possible diagonal point
            if abs(nx-x) != abs(ny-y) or x == nx or y == ny:
                continue

            # Find the remaining 2 points needed to form the square knowing x,y and nx,ny are diagonal points
            # One of them has the same y as our original y, but has x as our new x
            # The other one has the same x as our original x but has y as our new y
            count += self.points.get((nx, y), 0) * \
                self.points.get((x, ny), 0)*freq

        return count
