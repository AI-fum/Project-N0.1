## defaults.py

This file contains the default information of the program. such information as dimensions of window, images, robot's movement speed and the main music of the program are in this file.

Another task of this file is to select the battlefield. For this purpose, it calls the battlefield with text format from the battlefield folder.

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

<p align="center">
<img src="https://s6.uupload.ir/files/screenshot_from_2022-12-06_16-09-56_ze9r.png" alt="This will display an animated GIF" >
</p>
Look at picture (2.1). If you remember, the Matrix was one of the elements of Battlefield. The matrix corresponding to the above figure is valued as follows.  
```
10 10
1  1  1  x  1p x  1  1  2  1
1  1  1  x  2  x  1  2  3  2
1  1  1  x  3  x  1  1  2  1
1  x  x  x  4  x  x  x  1  1
1r 2  3  4  5  4  3  2  1  1
1  x  x  x  4  x  x  x  1  1
1  1  1  x  3  x  1  1  1  1
1  2  1  x  2  x  1  1b 1  1
2  3  2  x  1  x  1  1  1  1
1  2  1  1  1  1  1  1  1  1
```
Let's skip the variables. The battlefield class consists of 5 functions except the constructor function. We can list these functions as below. In the following, we will explain the functions of these functions.
- check_out()
- is_barrier()
- set_points()
- get_state()
- append_row()

### check_out
As you know, none of the elements in the project can't exit from the battlefield. As a result, we need a function to detect this issue. 'check_out' does it for us. This function has two inputs. Y and X coordinates. By entering these two variables, you can check the conditions of the existence of the element in the battlefield. For this purpose, the function returns the following statement to the program as an output.
```
return x >= self.width or x < 0 or y >= self.height or y < 0
```

### is_barrier
According to the form of the question, there are some barriers on the table(battlefield). None of the game elements can cross these barriers. We need a function to find these obstacles. The 'is_barrier' function is designed for this purpose. This function has the same function as 'check_out'. This function checks the existence of the letter x. Its function is as follows.
```
return self.battlefield[y][x].lower() == "x"
```

### set_points
if you remember. Points were fixed elements on the battlefield. For this purpose, they were set as an empty list in the constructor function. Therefore, we need a function to value the points. This function is of void type and has no output. The single command of this function is very simple.
```
self.points = points
```
### append_row
The get function is very simple. For this purpose, its explanation is omitted. But let's talk about 'append_row' functions. This function is designed to add battlefield rows. The only important point is to pay attention to the dimensions of the battlefield. For this purpose, we must check the condition 'len(row) != self.width' If the process is not a maze, the program will encounter an error.
```
if len(row) != self.width:
  raise ValueError("Invalid size of columns in this row:\n", str(row))
self.battlefield.append(row)
```


<p align="center">
<img src="https://s6.uupload.ir/files/screencast_from_22-12-09_10_14_28_gb5i.gif" alt="This will display an animated GIF" >
</p>
https://s6.uupload.ir/files/screencast_from_22-12-09_10_14_28_gb5i.gif

https://docs.google.com/document/d/1q89IFZxcHSv7rjiuSFFaRQ1p05bDQUwRhGDXWULdtF8/edit
