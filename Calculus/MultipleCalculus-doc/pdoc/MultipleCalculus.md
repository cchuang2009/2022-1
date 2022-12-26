



Contents
========

* [line: 17 - `typeset`](#line-17---typeset)
* [line: 75 - `tex`](#line-75---tex)
* [line: 84 - `Criticals`](#line-84---criticals)
* [line: 114 - `extrema_BI`](#line-114---extrema_bi)
* [line: 139 - `diff_app`](#line-139---diff_app)
* [line: 283 - `scale_func`](#line-283---scale_func)
* [line: 300 - `Integration_Substitution`](#line-300---integration_substitution)
* [line: 323 - `Integration_by_Parts`](#line-323---integration_by_parts)
* [line: 351 - `Integration_Trigonometric_odd`](#line-351---integration_trigonometric_odd)
* [line: 383 - `Integration_Trigonometric_even`](#line-383---integration_trigonometric_even)
* [line: 410 - `Integration_TrigonometricSubstitution`](#line-410---integration_trigonometricsubstitution)
* [line: 453 - `Integration_TrigonometricSubstitution_v5`](#line-453---integration_trigonometricsubstitution_v5)
* [line: 527 - `PartialFracInt`](#line-527---partialfracint)
* [line: 555 - `Jacobian_det`](#line-555---jacobian_det)
* [line: 570 - `MultipleIntegral`](#line-570---multipleintegral)
* [line: 716 - `DoubleInt_polar_v3`](#line-716---doubleint_polar_v3)
* [line: 778 - `DoubleInt_UV_v3`](#line-778---doubleint_uv_v3)
* [line: 843 - `TripleInt_Cylind`](#line-843---tripleint_cylind)
* [line: 931 - `TripleInt_Spherical`](#line-931---tripleint_spherical)
* [line: 1019 - `TripleInt_UVW`](#line-1019---tripleint_uvw)


&nbsp;

--------
# line: 17 - `typeset`
  
```  
def typeset():
```
>MathJax initialization for the current cell.This installs and configures MathJax for the current output.

&nbsp;

--------
# line: 75 - `tex`
  
```  
def tex(expr_):
```
>convert express to latex

&nbsp;

--------
# line: 84 - `Criticals`
  
```  
def Criticals(f_, x_, rational=False, BC=[]):
```
>Criticals(f_,x_,rational=False)Inputs   f_: function   x_: variable   rational: False (or True)             whether rational function is computered here  Output   critical values (list)

&nbsp;

--------
# line: 114 - `extrema_BI`
  
```  
def extrema_BI(f_, x_, c_):
```
>extrema_BI(f_,c_)Input:   f_: function   x_: variable   c_: list of critical valuesPrint out possible minimum and maximum

&nbsp;

--------
# line: 139 - `diff_app`
  
```  
def diff_app(f_, x_, rational=False, BC=[]):
```
>diff_app(f_,x_,rational=False)Inputs   f_: function   x_: variable   rational: False (or True)             whether rational function is computered here  Print out   f',f'', critical values, monotonicity and concavity

&nbsp;

--------
# line: 283 - `scale_func`
  
```  
def scale_func(f_, x, v):
```
>f_: function x : original variablev : new variable, v=f(x) where x=g(v)

&nbsp;

--------
# line: 300 - `Integration_Substitution`
  
```  
def Integration_Substitution(f, x, g):
```


>  no docstring

&nbsp;

--------
# line: 323 - `Integration_by_Parts`
  
```  
def Integration_by_Parts(F_, f, g, x):
```
>vrs: F_,f,g,x ∫F_dx = ∫fgdx = Fg - ∫F g'dx

&nbsp;

--------
# line: 351 - `Integration_Trigonometric_odd`
  
```  
def Integration_Trigonometric_odd(f, x, g):
```
>∫sin^m(x)cos^n(x)dx, m or n: oddvars: (f,x,g)     f: integrand     x     g: sin(x) or cos(x)

&nbsp;

--------
# line: 383 - `Integration_Trigonometric_even`
  
```  
def Integration_Trigonometric_even(f_, x):
```
>∫sin^m(x)cos^n(x)dx, m,n: evenvars: (f,x)     f: integrand     x

&nbsp;

--------
# line: 410 - `Integration_TrigonometricSubstitution`
  
```  
def Integration_TrigonometricSubstitution(f, x, g, t=t):
```
>∫f(a^2 ± x^2) dxvars: (f,x,g)     f: integrand     x     g: sin(t). tan(t), or sec(t)     t: theta variable       

&nbsp;

--------
# line: 453 - `Integration_TrigonometricSubstitution_v5`
  
```  
def Integration_TrigonometricSubstitution_v5(f, x, g, s=1, interval='', t=t):
```
>∫f(a^2 ± x^2) dxvars: (f,x,g)     f: integrand     x     g: sin(t). tan(t), or sec(t)     s: scale of x= s sin(t) (or others)     I: [a,b], the list of lower and upper limits     t: theta variable       

&nbsp;

--------
# line: 527 - `PartialFracInt`
  
```  
def PartialFracInt(f, g, x):
```
>∫f/gdxvars: (f,x,g)     f: nominator     g: denominator     x: variable

&nbsp;

--------
# line: 555 - `Jacobian_det`
  
```  
def Jacobian_det(XU, U):
```
>Calculate the Jacobian, 𝛛X/𝛛Uinput: XU: original coordinates, X, in form of new coordinates, U,       U: new Coordinates output: absolute value of determinant of Jacobian       

&nbsp;

--------
# line: 570 - `MultipleIntegral`
  
```  
def MultipleIntegral(f, X, XR):
```
>input: ∫ dx ∫ dy ∫ f(x,y,z) dz       f: f(x,y,z),       X: (x,y, ...), variable pair       XR: [[x0,x1], [y0,y1],...] output: details of integral, enhanced by colored text, and valueDemo# Double integralf=1X=[x,y]XR=[[0,1],[0,1-x]]MultipleIntegral(f,X,XR)# triple integralf=exp(x)X=[x,y,z,r]XR=[[0,1],[0,1-x],[0,1-x-y],[0,1-x-y-z]]MultipleIntegral(f,X,XR)# Triple integral in Cylindrical CoordinatesJ=rf=1X=[r,Theta,z]XR=[[r,Theta,z],[0,1],[0,pi],[0,1]]MultipleIntegral(f*J,X,XR)# Triple integral in Sperical CoordinatesJ=Rho**2*sin(Phi)f=1X=[Theta,Phi,Rho]XR=[[0,2*pi],[0,pi],[0,1]]MultipleIntegral(f*J,X,XR)

&nbsp;

--------
# line: 716 - `DoubleInt_polar_v3`
  
```  
def DoubleInt_polar_v3(f, X, xr, yr, Jacobian=r):
```
>Double integral in Polar Coordinatesinput: ∫ dr ∫ f(r cos𝛉,r sin𝛉) rd𝛉       f: f(x,y), which will be automatically transformed from (x,y) to (r cos𝛉,r sin𝛉)       X: (x,y), variable pair in Cartesian Coordinates       xr: (x0,x1) of r       yr: (y0,y1) of 𝛉       Jacobian: routput: details of integration and value  Should  calculate Jacobian and find out integation range in Polar Coordinates

&nbsp;

--------
# line: 778 - `DoubleInt_UV_v3`
  
```  
def DoubleInt_UV_v3(f, X, XU, U, xr, yr):
```
>Double integral in General Coordinatesinput: ∫ dr ∫ f(r cos𝛉,r sin𝛉) rd𝛉       f: f(x,y), which will be automatically transformed from (x,y) to (r cos𝛉,r sin𝛉)       X: (x,y), variable pair in Cartesian Coordinates       XU: (x(u,v),y(u,v))       U: (u,v)       xr: (x0,x1) of r       yr: (y0,y1) of 𝛉output: details of integration and value  Should  calculate Jacobian and find out integation range in Polar Coordinates

&nbsp;

--------
# line: 843 - `TripleInt_Cylind`
  
```  
def TripleInt_Cylind(f, X, XU, U, xr, yr, zr):
```
>Triple integral in General Coordinatesinput: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉       f: f(x,y,z), which will be automatically transformed from (x,y,z) to (r cos𝛉,r sin𝛉, z)       X: (x,y,z), variable pair in Cartesian Coordinates       XU: (x(u,v,z),y(u,v,z))𝜓       U: (u,v)       xr: (x0,x1) of r       yr: (y0,y1) of 𝛉       zr: (z0,z1) of zoutput: details of integration and value  Should  calculate Jacobian and find out integation range in Polar CoordinatesDemo:> TripleInt_Cylind(x*y*z,[x,y,z],[r*cos(Theta),r*sin(Theta),z],[r,Theta,z],[0,1],[0,pi],[0,1])

&nbsp;

--------
# line: 931 - `TripleInt_Spherical`
  
```  
def TripleInt_Spherical(f, X, XU, U, xr, yr, zr):
```
>Triple integral in Spherical Coordinatesinput: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉       f: f(x,y,z), which will be automatically transformed from (x,y,z) to ( 𝜌cos𝛉sin𝜙,𝜌sin𝛉sin𝜙, 𝜌cos𝜙)       X: (x,y,z), variable pair in Cartesian Coordinates       XU: (x(u,v,z),y(u,v,z))       U: (u,v)       xr: (x0,x1) of 𝜌       yr: (y0,y1) of 𝛉       zr: (z0,z1) of 𝜙output: details of integration and value  Should  calculate Jacobian and find out integation range in Polar CoordinatesDemo:> X=[x,y,z]> XU=[Rho*cos(Theta)*sin(Phi),Rho*sin(Theta)*sin(Phi),Rho*cos(Phi)]> U=[Rho,Theta,Phi]> TripleInt_Spherical(1,X,XU,U,[0,1],[0,2*pi],[0,pi])

&nbsp;

--------
# line: 1019 - `TripleInt_UVW`
  
```  
def TripleInt_UVW(f, X, XU, U, XR):
```
>Triple integral in Spherical Coordinatesinput: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉       f: f(x,y,z), which will be automatically transformed from (x,y,z) to ( 𝜌cos𝛉sin𝜙,𝜌sin𝛉sin𝜙, 𝜌cos𝜙)       X: (x,y,z), variable pair in Cartesian Coordinates       XU: (x(u,v,z),y(u,v,z))       U: (u,v)       xr: (x0,x1) of 𝜌       yr: (y0,y1) of 𝛉       zr: (z0,z1) of 𝜙output: details of integration and value  Should  calculate Jacobian and find out integation range in Polar Coordinates