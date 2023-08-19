#Functions to show and change scores
from graphics import *
import math
def name_and_point(window: GraphWin, level_num: int, P1_total: int, P1_round: int, P2_total: int, P2_round: int, P1_name: str, P2_name: str)-> None:
  """  Creates the score panel and displays the players' names and scores.
  
  :param window: (GraphWin) The window displayed for the game
  :param level_num: (int) The number of the level being played
  :param P1_total: (int) The total points player one has throughout the entire game
  :param P1_round: (int) The number of points player one has in the round
  :param P2_total: (int) The total points player two has throughout the entire game
  :param P2_round: (int) The number of points player two has in the round
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return: (None)
  
  """
  block = Rectangle (Point(0,0), Point(800, 50))
  block.setFill("white")
  block.draw(window)
  #TEXT OF NAME AND POINTS DISPLAYED
  #level
  txt = Text(Point(400, 25), "Lvl." + str(level_num))
  txt.setSize(25)
  txt.setTextColor(color_rgb(115, 133, 250))
  txt.setFace("courier")
  txt.draw(window)
  #player 1 points
  P1_totpts = Text(Point(101, 10), "  Total: " + str(P1_total))
  P1_totpts.draw(window)
  P1_roundpts = Text(Point(100, 35), "Round: " + str(P1_round))
  P1_roundpts.draw(window)
  #player 2 points
  P2_totpts = Text(Point(701, 10), "  Total: " + str(P2_total))
  P2_totpts.draw(window)
  P2_roundpts = Text(Point(700, 35), "Round: " + str(P2_round))
  P2_roundpts.draw(window)
  #player 1 name
  name1 = Text(Point(35, 10), P1_name)
  name1.setTextColor(color_rgb(77, 28, 145))
  name1.draw(window)
  #player 2 name
  name2 = Text(Point(765, 10), P2_name)
  name2.setTextColor(color_rgb(77, 28, 145))
  name2.draw(window)

def find_distance (target1: Circle, mouse_x: float, mouse_y: float) -> float:
  """ This function calculates the distance from the centre of the target to the point on the target where the mouse is clicked and adds the corresponding amount of points
  
  :param target1: (Circle) The green circle in the target
  :param mouse_x: (float) The x coordinate of the mouse when clicked
  :param mouse_y: (float) The y coordinate of the mouse when clicked
  :return: (float) The distance from the centre of the target to the point on the target where the mouse was clicked

  >>>find_distance(target1, 300.0, 200.0)
  360.555
  >>>find_distance(target1, 234.0, 190.0)
  301.423
  >>>find_distance(target1, 418.0, 212.0)
  468.6875

  """
  
  dx = (target1.getCenter().getX())-mouse_x
  dy = (target1.getCenter().getY())-mouse_y
  dist = math.sqrt((dx*dx) + (dy*dy))
  return dist
  
def score_change(i: int, dist: float, target1: Circle, target2: Circle, target3: Circle, window: GraphWin, level_num: int, P1_total: int, P1_round: int, P2_total: int, P2_round: int, P1_name: str, P2_name: str) -> list:
  """  Checks what section of the target the mouse is in and adds points to a players score accordingly.
  
  :param i: (int) The integer that determines it ita plyer one's turn or player two's
  :param dist: (float)
  :param target1: (Circle) The green section of the target
  :param target2: (Circle) The blue section of the target
  :param target3: (Circle) The red section of the target
  :param window: (GraphWin) The window displayed for the game
  :param level_num: (int) The number of the level being played
  :param P1_total: (int) The total points player one has throughout the entire game
  :param P1_round: (int) The number of points player one has in the round
  :param P2_total: (int) The total points player two has throughout the entire game
  :param P2_round: (int) The number of points player two has in the round
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return: (list) A list of player one's or player two's total and round scores
  
  >>>score_change(1, 15.9876, Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), GraphWin("Shoot Your Shot", width, height), 2, 40, 0, 15, 0, Killua, Jeesung)
  [25, 10]
  >>>score_change(0, 45.8623, Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), GraphWin("Shoot Your Shot", width, height), 3, 25, 0, 5, 0, Levi, Poppy)
  [30, 5]
  >>>score_change(1, 11.83764, Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), GraphWin("Shoot Your Shot", width, height), 1, 35, 0, 10, 0, Grace, Hadid)
  [30, 20]
  """
  if i == 0:
    # if target is in Red Circle
    if dist <= target3.getRadius():
      print(P1_name + " got 20 points!")
      P1_round += 20
      P1_total += P1_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P1_round, P1_total]
    # if target is in Blue Circle
    elif dist <= target2.getRadius():
      print(P1_name + " got 10 points!")
      P1_round += 10
      P1_total += P1_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P1_round, P1_total]
    # if the target is green circle
    elif dist <= target1.getRadius():
      print(P1_name + " got 5 points!")
      P1_round += 5
      P1_total += P1_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P1_round, P1_total]
    #if target is missed
    else:
      print("You Missed!")
      P1_round += 0
      P1_total += P1_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P1_round, P1_total]
  if i == 1:
  # if target is in Red Circle
    if dist <= target3.getRadius():
      print(P2_name + " got 20 points!")
      P2_round = P2_round + 20
      P2_total += P2_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P2_round, P2_total]
    # if target is in Blue Circle
    elif dist <= target2.getRadius():
      print(P2_name + " got 10 points!")
      P2_round = P2_round + 10
      P2_total += P2_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P2_round, P2_total]
    # if the target is green circle
    elif dist <= target1.getRadius():
      print(P2_name + " got 5 points!")
      P2_round = P2_round + 5
      P2_total += P2_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P2_round, P2_total]
    #if target is missed
    else:
      print("You Missed!")
      P2_round += 0
      P2_total += P2_round
      name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
      return [P2_round, P2_total]