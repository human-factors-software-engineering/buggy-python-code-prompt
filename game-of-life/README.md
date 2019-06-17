## *Conway's Game of Life*
### **Running the game**
To run: `python3 conways.py`

### **How To Play**
The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties.

The game has four rules it uses to calculate the simulation:
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

### **Controls**
| Action | Key |
|----:|:---|
|  Run/Pause Simulation| Space |
| Place Cell | Right Click |
| Delete Cell | Left Click |
| Randomize Map | A |
| Advance Simulation Once | Q |
| Clear Map | R |

### **Issues**
#### 1. When placing blocks, all blocks to right are placed
Normally when clicking on a cell, only one block should be placed down where the mouse clicks. Currently, only the blocks to the right of what is clicked are placed.