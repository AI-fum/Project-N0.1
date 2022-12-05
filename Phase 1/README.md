## battlefield.py

The Battlefield class consists of two main elements. First, the matrix that represents the main elements of the game map. Second, the points that contain information about the targets on the field. In the first step, the constructor function receives the matrix along with the height and width variables. The constructor puts these values in the class variables and sets the target array equal to an empty list.

```
matrix: list[list[str]]
points: list[tuple[int, int]]
```

As we mentioned above, the base of these elements will be as follows.
```
def __init__(self, height: int, width: int, matrix=[]):
  self.battlefield = matrix
  self.width = width
  self.height = height
  self.points = []
```
Let's skip the variables. The battlefield class consists of 5 functions except the constructor function. We can list these functions as below. In the following, we will explain the functions of these functions.
- check_out()
- is_barrier()
- set_points()
- get_state()
- append_row()

### check_out
As you know, none of the elements in project can't exite from the battlefield. As a result, we need a function to detect this issue. 'check_out' do it for us. This function has two iputs. Y and X coordinates. By entering these two variables, you can check the conditions of the existence of the element in the battlefield. For this purpose, the function returns the following statement to the program as an output.
```
return x >= self.width or x < 0 or y >= self.height or y < 0
```
