# ------------------------------------------------------
#        Name:  Jina Lee and Tajhini Brown
#       Peers: 
#  References:
# ------------------------------------------------------
"""Main interface for the execution of the game"""
from graphics import *
from random import randint
import pictures
import points
import winner
import rounds
import between_rounds

def main() -> None:
  """Allows user to play them game 
  
  """
  #set up game window 
  width = 800
  height = 500
  window = GraphWin("Shoot Your Shot", width, height)
  window.setBackground(color_rgb(172, 225, 227))

  block = Rectangle (Point(0,0), Point(800, 50))
  block.setFill("white")
  block.draw(window)

  between_rounds.instructions(window)
 
  #Loop for game system 
  while True: 
    
    #Initial player's name, points, and level 
    name_text = Text(Point(400, 265), "↓↓↓Enter players' name↓↓↓")
    name_text.setSize(16)
    name_text.setFace("courier")
    name_text.draw(window)
    P1_name = str(input("Enter name of Player 1: "))
    P2_name = str(input("Enter name of Player 2: "))
    name_text.undraw()
    P1_total = 0
    P2_total = 0
    P1_round = 0
    P2_round = 0
    level_num = 1
    #Making target 
    radius = 60
    rand_length = randint(100,700)
    rand_height = randint(150,440)
    target1 = Circle(Point(rand_length, rand_height), 60)
    target2 = Circle(Point(rand_length, rand_height), 40)
    target3 = Circle(Point(rand_length, rand_height), 15)
    #display name and points and level on window 
    points.name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    
    #ROUND 1
    points_list = []
    rounds.rounds (points_list, window, target1, target2, target3, width, height, radius, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    P1_round = points_list[1]
    P2_round = points_list[3]
    winner.round_winner(window, P1_round, P2_round, P1_name, P2_name)
    level_num +=1
    
    
    #ROUND 2
    #Initial player's name, points, and level 
    P1_total = points_list[0]
    P2_total = points_list[2]
    P1_round = 0
    P2_round = 0  
    window.close()
    width = 800
    height = 500
    window = GraphWin("Shoot Your Shot", width, height)
    window.setBackground(color_rgb(172, 225, 227))
    points.name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    rounds.rounds (points_list, window, target1, target2, target3, width, height, radius, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    P1_round = points_list[5]
    P2_round = points_list[7]
    winner.round_winner(window, P1_round, P2_round, P1_name, P2_name)
    level_num +=1
    
      
    #ROUND 3
    P1_total = points_list[4]
    P2_total = points_list[6]
    P1_round = 0
    P2_round = 0  
    window.close()
    width = 800
    height = 500
    window = GraphWin("Shoot Your Shot", width, height)
    window.setBackground(color_rgb(172, 225, 227))
    points.name_and_point(window, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    rounds.rounds (points_list, window, target1, target2, target3, width, height, radius, level_num, P1_total, P1_round, P2_total, P2_round, P1_name, P2_name)
    P1_total = points_list[8]
    P2_total = points_list[10]
    
    winner.game_winner(window, P1_total, P2_total, P1_name, P2_name)
    
    #Ask do you want to play again?
    is_again = Text(Point(400, 265), "Do you want to play again?")
    is_again.setSize(25)
    is_again.setFace('courier')
    is_again.draw(window)
    yes_block = Rectangle (Point(250, 300), Point(370, 350))
    yes_block.setFill("white")
    yes_block.draw(window)
    yes = Text(Point(310, 325), "YES")
    yes.draw(window)
    no_block = Rectangle (Point(400, 300), Point(520, 350))
    no_block.setFill("white")
    no_block.draw(window)
    no = Text(Point(460, 325), "NO")
    no.draw(window)
    is_play = between_rounds.play_again (is_again, yes_block, no_block, yes, no, window)
    print(is_play)
    if is_play == "yes":
      continue
    if is_play == "no":
      break
    if is_play == "click":
      click_y_or_n = Text(Point(400, 400), "Click Yes or No")
      click_y_or_n.setSize(20)
      click_y_or_n.setFace('courier')
      click_y_or_n.draw(window)
      between_rounds.play_again (is_again, yes_block, no_block, yes, no, window)
      click_y_or_n.undraw()

  
if __name__ == "__main__":
  main()