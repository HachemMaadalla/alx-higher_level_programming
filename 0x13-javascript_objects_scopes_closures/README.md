# Javascript - Objects, Scopes and Closures

Javascripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [node v6.10.2](https://nodejs.org/en/blog/release/v6.10.2/) and must conform to [semistandard](https://github.com/Flet/semistandard) style.

### Focus
Learn about the objects, classes, inheritance, and scope of Javascript.

### Example Usages

[0-rectangle.js](0-rectangle.js), [0-main.js](0-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./0-main.js
Rectangle {}
[Function: Rectangle]
0x13-javascript_objects_scopes_closures:$
```
[1-rectangle.js](1-rectangle.js), [1-main.js](1-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
0x13-javascript_objects_scopes_closures:$
```
[2-rectangle.js](2-rectangle.js), [2-main.js](2-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
0x13-javascript_objects_scopes_closures:$
```
[3-rectangle.js](3-rectangle.js), [3-main.js](3-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
0x13-javascript_objects_scopes_closures:$
```
[4-rectangle.js](4-rectangle.js), [4-main.js](4-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
0x13-javascript_objects_scopes_closures:$
```
[5-square.js](5-square.js), [5-main.js](5-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
0x13-javascript_objects_scopes_closures:$
```
[6-square.js](6-square.js), [6-main.js](6-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
0x13-javascript_objects_scopes_closures:$
```
[7-occurrences.js](7-occurrences.js), [7-main.js](7-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./7-main.js
1
4
2
0x13-javascript_objects_scopes_closures:$
```
[8-esrever.js](8-esrever.js), [8-main.js](8-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'Holberton' ]
0x13-javascript_objects_scopes_closures:$
```
[9-logme.js](9-logme.js), [9-main.js](9-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./9-main.js
0: Hello
1: Holberton
2: School
0x13-javascript_objects_scopes_closures:$
```
[10-converter.js](10-converter.js), [10-main.js](10-main.js)
```
0x13-javascript_objects_scopes_closures:$ ./10-main.js
2
12
89
2
c
59
0x13-javascript_objects_scopes_closures:$
```
### Author
- [Alex Yu](https://github.com/AlexYu01)
### Acknowledgments
- [Holberton](https://www.holbertonschool.com/)
