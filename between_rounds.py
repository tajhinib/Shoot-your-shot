#Functions that display text in beginning, end, and in between rounds
from graphics import *
def instructions(window: GraphWin) -> None:
    """Displays on screen the instructions for the game.

    :param window: (GraphWin) The window displayed for the game 
    :return: (None)
  
    """
    line_one = Text(Point(400, 25),"How to Play")
    line_one.setSize(23)
    line_one.setFace("courier")
    line_one.draw(window)
    line_two = Text(Point(400, 100),"Use your mouse to hit the different sections of the moving target.")
    line_two.setSize(12)
    line_two.setFace("courier")
    line_two.draw(window)
    line_three = Text(Point(400, 125),"Each section is worth a different amount of points.")
    line_three.setSize(12)
    line_three.setFace("courier")
    line_three.draw(window)       
    line_four = Text(Point(400, 170),"Green = 5 points, Blue = 10 points, Red = 20 points")
    line_four.setSize(12)
    line_four.setFace("courier")
    line_four.draw(window)  
    line_five = Text(Point(400, 215),"There are 3 rounds; the speed of the target increases each round")
    line_five.setSize(12)
    line_five.setFace("courier")
    line_five.draw(window) 
    line_six = Text(Point(400, 240),"The player with the most points at the end wins.")
    line_six.setSize(12)
    line_six.setFace("courier")
    line_six.draw(window) 
    line_seven = Text(Point(400, 283),"GOOD LUCK!!! ʕ•ᴥ•ʔ")
    line_seven.setSize(14)
    line_seven.setFace("courier")
    line_seven.draw(window) 
    line_eight = Text(Point(400, 310),"<333 Click to Start <333")
    line_eight.setSize(16)
    line_eight.setFace("courier")
    line_eight.draw(window) 
    intro_img = Image(Point(410,430), "pictures/panda.png")
    intro_img.draw(window)
    y = window.getMouse()
    line_one.undraw()
    line_two.undraw()
    line_three.undraw()
    line_four.undraw()
    line_five.undraw()
    line_six.undraw()
    line_seven.undraw()
    line_eight.undraw()
    intro_img.undraw()
  
def switch_turns_text(window: GraphWin, i: int, P1_name: str, P2_name: str)-> None:
  """  Switches the turns between player one and player two for a level.
  
  :param window: (GraphWin) The window displayed for the game
  :param i: (int) The number that determines whether its player one or player two's turn
  :param P1_name: (str) The entered name for player 1
  :param P2_name: (str) The entered name for player 2
  :return: (None)
  
  """
  
  if i == 0:
    switch_turns = Text(Point(400, 255), P1_name +"'s turn!")
    switch_turns.draw(window)
    switch_turns.setSize(20)
    switch_turns.setFace("courier")
    click_to_start = Text(Point(400, 285), "Click to START")
    click_to_start.setSize(20)
    click_to_start.setFace("courier")
    click_to_start.draw(window)
    img = Image(Point(400,430), "pictures/goodluck-preview.png")
    img.draw(window)
    y = window.getMouse()
    switch_turns.undraw()
    click_to_start.undraw()
    img.undraw()
  if i == 1:
    switch_turns = Text(Point(400, 255), P2_name +"'s turn!")
    switch_turns.setSize(20)
    switch_turns.setFace("courier")
    switch_turns.draw(window)
    click_to_start = Text(Point(400, 285), "Click to START")
    click_to_start.setSize(20)
    click_to_start.setFace("courier")
    click_to_start.draw(window)
    img = Image(Point(400,430), "pictures/goodluck-preview.png")
    img.draw(window)
    y = window.getMouse()
    switch_turns.undraw()
    click_to_start.undraw()
    img.undraw()


def play_again (is_again: Text, yes_block: Rectangle, no_block: Rectangle, yes: Text, no: Text, window: GraphWin) -> str:
  """Allows user to decide whether to play the game again or not. 

  :param is_again: (Text) String that asks the user if they want to play again or not
  :param yes_block: (Rectangle) Rectangle that allows user to click on to play again
  :param no_block: (Rectangle) Rectangle that allows user to click on to close the game
  :param yes: (Text) Word "Yes" displayed on screen
  :param no: (Text) Word "No" displayed on screen
  :param window: (GraphWin) The window displayed for the game
  :return: (str) A string variable that describes the user's decision 

  >>>play_again ("Do you want to play again?", Rectangle (Point(250, 300), Point(370, 350)), Rectangle (Point(400, 300), Point(520, 350)), Text(Point(310, 325), "YES"), Text(Point(460, 325), "NO"), GraphWin("Shoot Your Shot", width, height))
  "yes"
  >>>play_again ("Do you want to play again?", Rectangle (Point(250, 300), Point(370, 350)), Rectangle (Point(400, 300), Point(520, 350)), Text(Point(310, 325), "YES"), Text(Point(460, 325), "NO"), GraphWin("Shoot Your Shot", width, height))
  "no"
  >>>play_again ("Do you want to play again?", Rectangle (Point(250, 300), Point(370, 350)), Rectangle (Point(400, 300), Point(520, 350)), Text(Point(310, 325), "YES"), Text(Point(460, 325), "NO"), GraphWin("Shoot Your Shot", width, height))
  "click"
  """
  p = window.getMouse()
  x = p.getX()
  y = p.getY()
  y_yes1 = yes_block.getP1().getY()
  x_yes1 = yes_block.getP1().getX()
  y_yes2 = yes_block.getP2().getY()
  x_yes2 = yes_block.getP2().getX()
  y_no1 = no_block.getP1().getY()
  x_no1 = no_block.getP1().getX()
  y_no2 = no_block.getP2().getY()
  x_no2 = no_block.getP2().getX()
  if (x <= x_yes2 and x >= x_yes1) and (y <= y_yes2 and y >= y_yes1):
    is_again.undraw()
    yes_block.undraw()
    no_block.undraw()
    yes.undraw()
    no.undraw()
    return "yes"
  if (x <= x_no2 and x >= x_no1) and (y <= y_no2 and y >= y_no1):
    window.close()
    return "no"
  else:
    return "click"