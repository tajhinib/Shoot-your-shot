#Functions to determine the winner of the round and the winner of the game.
from graphics import *
def round_winner(window: GraphWin, P1_round: int, P2_round: int, P1_name: str, P2_name: str) -> None:
  """  Compares the points of each player of a round and determines the winner from which player has the larger amount of round points.
  
  :param window: (GraphWin) The window displayed for the game
  :param P1_round: (int) The number of points player one has in the round
  :param P2_round: (int) The number of points player two has in the round
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return: (None)
  
  """
  
  if P1_round > P2_round:
    print("The WINNER is " + P1_name + "!")
    winner = Text(Point(400, 245), "The WINNER is " + P1_name + " ^3^")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 300), "Click for Next Round")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/good-job-removebg-preview.png")
    img.draw(window)
  if P2_round > P1_round:
    print("The WINNER is " + P2_name + "!")
    winner = Text(Point(400, 275), "The WINNER is " + P2_name + " ^3^")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 300), "Click for Next Round")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/good-job-removebg-preview.png")
    img.draw(window)
  if P1_round == P2_round:
    print("It's a TIE!")
    winner = Text(Point(400, 275), "It's a TIE! :O")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 300), "Click for Next Round")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/good-job-removebg-preview.png")
    img.draw(window)
  p = window.getMouse()
  winner.undraw()
  next_round.undraw()
  img.undraw()

  
def game_winner(window: GraphWin, P1_total: int, P2_total: int, P1_name: str, P2_name: str) -> None:
  """  Checks the players total points and determines the winner based on which player has the greater amount of points.
  
  :param window: (GraphWin) The window displayed for the game
  :param P1_total: (int) The total points player one has throughout the entire game
  :param P2_total: (int) The total points player two has throughout the entire game
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return: (None)
  
  """
  
  if P1_total > P2_total:
    print("The WINNER is " + P1_name + "!")
    winner = Text(Point(400, 230), "The WINNER is " + P1_name + " ^3^")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 260), "CONGRADULATIONS")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/clap2.png")
    img.draw(window)
  if P2_total > P1_total:
    print("The WINNER is " + P2_name + "!")
    winner = Text(Point(400, 230), "The WINNER is " + P2_name + " ^3^")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 260), "CONGRADULATIONS")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/clap2.png")
    img.draw(window)
  if P1_total == P2_total:
    print("It's a TIE!")
    winner = Text(Point(400, 230), "It's a TIE! :O")
    winner.setSize(25)
    winner.setFace('courier')
    winner.draw(window)
    next_round = Text(Point(400, 260), "GOOD GAME")
    next_round.setSize(15)
    next_round.setFace('courier')
    next_round.draw(window)
    img = Image(Point(400,430), "pictures/clap2.png")
    img.draw(window)
  click_text = Text(Point(400, 295), "Click to continue")
  click_text.setSize(20)
  click_text.setFace('courier')
  click_text.draw(window)
  p = window.getMouse()
  winner.undraw()
  next_round.undraw()
  img.undraw()
  click_text.undraw()