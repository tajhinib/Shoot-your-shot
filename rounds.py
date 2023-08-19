#Functions to execute each round and make target
from graphics import *
import points
import between_rounds
def target_make(window: GraphWin, target1: Circle, target2: Circle, target3: Circle) -> None :
  """Draws target on window and fills in each target circle with a designated color.

  :param window: (GraphWin) The window displayed for the game 
  :param target1: (Circle) The green section of the target
  :param target2: (Circle) The blue section of the target
  :param target3: (Circle) The red section of the target
  :return (None)
  
  """
  target1.draw(window)
  target1.setFill("green")
  target2.draw(window)
  target2.setFill("blue")
  target3.draw(window)
  target3.setFill("red")
  
def rounds (points_list: list, window: GraphWin, target1: Circle, target2: Circle, target3: Circle, width: int , height: int, radius: int, level_num: int, P1_total: int, P1_round: int, P2_total: int, P2_round: int, P1_name: str, P2_name: str) -> list:
  """Creates each level of the game.

  :param points_list: (list)
  :param window: (GraphWin) The window displayed for the game 
  :param target1: (Circle) The green section of the target
  :param target2: (Circle) The blue section of the target
  :param target3: (Circle) The red section of the target
  :param width: (int) The width of the window
  :param height: (int) The height of the window
  :param radius: (int) The radius of the circle
  :param level_num: (int) The number of the level being played
  :param P1_total: (int) The total points player one has throughout the entire game
  :param P1_round: (int) The number of points player one has in the round
  :param P2_total: (int) The total points player two has throughout the entire game
  :param P2_round: (int) The number of points player two has in the round
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return (list) List of the point of the players of the game

  >>>rounds ([], GraphWin("Shoot Your Shot", width, height), Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), 800, 500, 1, 0, 0, 0, 0, Steve, Bob)
  [20, 20, 5, 5]
  >>>rounds (points_list, GraphWin("Shoot Your Shot", width, height), Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), 800, 500, 2, 20, 0, 5, 0, Hunter, Harry)
  [20, 20, 5, 5, 30, 10, 15, 10]
  >>>rounds (points_list, GraphWin("Shoot Your Shot", width, height), Circle(Point(rand_length, rand_height), 60), Circle(Point(rand_length, rand_height), 40), Circle(Point(rand_length, rand_height), 15), 800, 500, 3, 30, 0, 15 , 0, Tim, Scott)
  [20, 20, 5, 5, 30, 10, 15, 10, 35, 5, 25, 10]
  
  """
  for i in range(2):
    between_rounds.switch_turns_text(window, i, P1_name, P2_name)
    target_make(window, target1, target2, target3)
    
    # speed per level
    if level_num == 1:
      deltaX = 0.25
      deltaY = 0.25
    elif level_num == 2:
      deltaX = 0.45
      deltaY = 0.45
    else:
      deltaX = 0.6
      deltaY = 0.6
      
    while True:
      #bounce
      target1.move(deltaX, deltaY) 
      target2.move(deltaX, deltaY) 
      target3.move(deltaX, deltaY)
      if (target1.getCenter().getX() > width - target1.getRadius() or target1.getCenter().getX() < radius):
          deltaX = deltaX * -1 
      if (target1.getCenter().getY() > height - target1.getRadius() or target1.getCenter().getY() < radius+50):
          deltaY = deltaY * -1
      
      p = window.checkMouse()
      #Add points depending on where mouse clicked in Target
      if p:
        mouse_x = p.getX()
        mouse_y = p.getY()
        dist = points.find_distance (target1, mouse_x, mouse_y)
        if i == 0:
          P1_list = points.score_change(i, dist, target1, target2, target3, window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
          P1_round = P1_list[0]
          P1_total = P1_list[1]
          points_list.append(P1_total)
          points_list.append(P1_round)
          break
        if i == 1:
          P2_list = points.score_change(i, dist, target1, target2, target3, window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
          P2_round = P2_list[0]
          P2_total = P2_list[1]
          points_list.append(P2_total)
          points_list.append(P2_round)
          break
    target1.undraw()
    target2.undraw()
    target3.undraw()
  return points_list