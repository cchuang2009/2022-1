A Sympy-flavored package for Calculus, **MultipleCalculus.py** is availed here. There are several Symbolic Calculation functions are supported: optimization, Integration for both Single-variable and Multiple-Variable Functions:

```python

# if in google drive colab mode, upload MultipleCalculus.py to your google drive
from google.colab import drive
drive.mount('/content/drive')

import sys
sys.path.append('/content/drive/MyDrive/')

from MultipleCalculus import *

typeset()
Integration_Substitution(x*sin(x**2),x,x**2)

```
gets:

Replacing $x^2$ by $u$ gets:

$$
\int x \sin{\left(x^{2} \right)} d x= \int \frac{\sin{\left(u \right)}}{2} d u 
                                  = - \frac{\cos{\left(u \right)}}{2} +C 
$$

[Demo](SingleVariableCalculus-demo.ipynb)
