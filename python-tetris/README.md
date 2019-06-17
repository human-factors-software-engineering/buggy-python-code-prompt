## *Tetris*
### **Running the game**
To run: `python3 tetris.py`

### **How To Play**
A random sequence of geometric shapes composed of four square blocks fall down the playing field. The objective of the game is to manipulate these shapes, by moving each one sideways and/or rotating by quarter-turns, so that they form a solid horizontal line without gaps. When such a line is formed, it disappears and any blocks above it fall down to fill the space.

### **Controls**
| Action | Key |
|----:|:---|
| Move Block | Arrow Keys |
| Rotate | Space |
| Quit | q |
| Pause | p | 

### **Issues**
#### 1. Lines do not get cleared
When an entire row gets filled, the entire row of blocks should disappear. Currently, the game continues running as if nothing should happen.

#### 2. Blocks can go out of bounds
Currently the controls allow the blocks to go out of bounds on the right, left and bottom borders. The game should not allow that and should keep the blocks inside the game bounds at all times.

#### 3. Left movement does not work
Pressing left moves the block right. Instead pressing left should move the block left.
