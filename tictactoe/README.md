## *Tic-tac-toe*
### **Running the game**
To run: `python tictactoe.py`

### **How To Play**
Players who place X's and O's take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

### **Controls**
| Action | Key |
|----:|:---|
| Place Mark | Left Click  |

### **Issues**
#### 1. Crash on game launch.
The game instantly crashes once the game launches. Normally the game would start immediately and allow you to start clicking. 
There is no error message given.

#### 2. Mouse clicks have abnormal behavior sometimes resulting in crash.
Currently mouse-clicks are incorrectly being registered. This sometimes results in a crash with the following error message:

```
Traceback (most recent call last):
  File ".\incorrect-tictactoe.py", line 157, in <module>
    clickBoard(board)
  File ".\incorrect-tictactoe.py", line 97, in clickBoard
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
IndexError: list index out of range
```

Normally where the user clicks is where the next X or O should be placed. 

#### 3. No line being drawn for column and row wins
No three in a row marker is being drawn for column and row wins, but it is being drawn for diagonals. Normally when there is a win, there should be a line drawn for a three in a row victory in all cases but instead we only see it when winning through diagonals.