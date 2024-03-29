# PythonPentago

## I WANT TO PLAY
Just run the Gameplay.py file if you already have Pygame installed. Otherwise you need to use pip in your terminal and run:
```
pip install pygame
```
To run Python file use 
```
python3 Gameplay.py
```

## Pentago Rules
The object is to get five marbles in a row before your opponent does. The mind twisting part of Pentago is that each player will also twist one of the four game blocks 90 degrees (one "notch"), clockwise or counter clockwise, as part of each turn.

A 180 degree (double "notch") twist is not allowed. The twist is the key to create winning positions in Pentago.
Game Play
Players take turns at placing marbles on the game board and twisting the game blocks. A player is free to twist any of the game blocks, regardless of which game block the player placed the marble on.
In the beginning of the game, there will be neutral game blocks, allowing a player to ignore the twist portion of their turn. A neutral game block is one that is empty or has only one marble in the middle of it.
Twisting a neutral game block will have no effect on the positional nature of the game board so the twisting part of a move is optional while there are neutral game blocks.

End of the Game
A winning row of five marbles can occur vertically, horizontally or diagonally, anywhere on the board and will span two or three game blocks.

What seems like a simple five-in-a-row game quickly gets mind twisting as the board fills up and both players are twisting the game blocKs, creating a constantly changing and challenging game scenario.

You'll want to really watch your opponents position as it relates to yours and play as much defensive as you do offense.
source : https://www.ultraboardgames.com/pentago/game-rules.php

## Implementation
Program implemenation will be in Python using PyGame module for the user interface. There will be two gamemodes: singleplayer and multiplayer while singleplayer will be a primitive bot based on pseudorandom algorithms.

```mermaid
classDiagram
   Board --> Bot
   Button --> MainMenu
   MainMenu --> Gameplay
   Player <--> Board
   Board --> State
   Window --|> State
   Player --> Gameplay
   State --> Gameplay
   Bot --> Gameplay
   Board --> Gameplay
    
class Board{
  -columns = 6
  -rows = 6
  -board[6][6]
  +BoardMethods()
  }
class Bot{
  -color
  +move()
  }
  
class MainMenu{
    -buttons
    -display
}

class Button{
    -text
    -position
    -screen
    +draw()
}

class Gameplay{
  +Singleplayer()
  +Multiplayer()
}

class Player{
    +getInput()
}
class State{
-WIN
+drawWin()
}
class Window{
  -height
  -width
  -background
  }
```
## Manual 
  1. Using your mouse choose one of the following options in main menu. 
  2. Your first move will be chosing also by mouse where to put your ball
  3. When you see your ball on the screen choose one of four boards to rotate
  4. Rotate your board 90 degrees left or right using arrows on your keyboard