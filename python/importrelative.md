# How to import packages or open files from subdirectory?
For example, I have a folder with the following structures:
```
- main.py
- tools
  - test.py
  - test.csv
```

## Import packages
Now, in the main.py I want to import a function called `test()` from test.py.
1. Create an empty file called `__init__.py` in the tools folder.
2. In the main.py, use `from tools.test import import test`

## Open files
I want to open the `test.csv` in the main.py
1. `import os`
2. Change open path as ``'.tools/test.csv'``
