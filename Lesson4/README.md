`circle = Circle(10)`\
The default center of circle:  (0, 0)\
The radius of circle:  10\
The area of circle:  314.1592653589793\
_Changes radius of circle_\
`circle.radius = 100`\
The new radius of circle:  100\
The new area of circle:  31415.926535897932\
_Checks that the center has not changed_\
The center of circle:  (0, 0)


`square = Square(x=25, y=50)`\
The default side of square:  1\
The user-defined center of square:  (25, 50)\
_Changes size of square_\
`square.side = 15`\
The new side of square:  15\
_Moves figure to coordinates (50, 25) and check new center_\
`square.move(175, 215)`\
The center of square after movement:  (175, 215)\
The area of square:  225\
The list of square vertices: `[(167.5, 207.5), (167.5, 222.5), (182.5, 207.5), (182.5, 222.5)]`


`triangle = Triangle(20, 10, 10)`\
The user-defined center of triangle:  (10, 10)\
_Moves figure to coordinates (40, 40) and check new center_\
`triangle.move(40, 40)`\
The center of triangle after movement:  (40, 40)\
The side of triangle:  20\
The area of triangle:  173.20508075688772\
The list of triangle vertices: `[(40, 51.547005383792516), (30.0, 34.226497308103745), (50.0, 34.226497308103745)]`\
_Changes size of triangle and check new area and vertices_\
`triangle.side = 35`\
The new area of triangle:  530.4405598179686\
The new list of triangle vertices after size changing: `[(40, 60.207259421636905), (22.5, 29.896370289181547), (57.5, 29.896370289181547)]`


_Calculates distance between centers of 2 figures_\
The distance between square and triangle: 221.02036105300343\
The distance between square and circle: 277.2183255125822\
The distance between triangle and circle: 56.568542494923804