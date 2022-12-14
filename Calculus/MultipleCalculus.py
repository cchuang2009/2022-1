# prepare for Latex Output
from IPython.display import HTML,Latex

# Colored output in Python

W  = '\033[0m'  # white (normal)
K  = '\033[30m' # black
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[1;33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
T =  '\033[1;33;47m' #Title

# support latex-out on Google drive

def typeset():
  """MathJax initialization for the current cell.
  
  This installs and configures MathJax for the current output.
  """
  display(HTML('''
      <script src="https://www.gstatic.com/external_hosted/mathjax/latest/MathJax.js?config=TeX-AMS_HTML-full,Safe&delayStartupUntil=configured"></script>
      <script>
        (() => {
          const mathjax = window.MathJax;
          mathjax.Hub.Config({
          'tex2jax': {
            'inlineMath': [['$', '$'], ['\\(', '\\)']],
            'displayMath': [['$$', '$$'], ['\\[', '\\]']],
            'processEscapes': true,
            'processEnvironments': true,
            'skipTags': ['script', 'noscript', 'style', 'textarea', 'code'],
            'displayAlign': 'center',
          },
          'HTML-CSS': {
            'styles': {'.MathJax_Display': {'margin': 0}},
            'linebreaks': {'automatic': true},
            // Disable to prevent OTF font loading, which aren't part of our
            // distribution.
            'imageFont': null,
          },
          'messageStyle': 'none'
        });
        mathjax.Hub.Configured();
      })();
      </script>
      '''))

# sympy functions and properties 
from IPython.display import HTML,Latex
from sympy import symbols,pprint,integrate,diff,latex,limit,simplify,Matrix,Abs,Ei,Ne,solve,Function,fraction
from sympy import pi,sqrt,sin,cos,log,tan,cot,sec,csc,exp,oo,E,tan,Piecewise,asin,atan,erf,erfc,E
from sympy import solveset,cancel,factor,S,Interval,apart,expand
from sympy.solvers.inequalities import solve_univariate_inequality

from sympy import symbols,pprint,integrate,diff,latex,simplify,Matrix,Abs,Ei,erf,erfc,E,Ne
from sympy import pi,sqrt,sin,cos,log,exp,oo,E,tan,Piecewise,asin,atan

# Variable declared
# x,y,z: variable Cartesian Corrdinates
# r,Theta: r,𝛉 in Polar Coordinates
# Rho,Theta,Phi: 𝛒, 𝛉, 𝛟 in Spherical Coordinates

x,y,z,r,t,rho,phi,theta,u,v,w,a,b,c,m,n,l,p,T,𝝆,θ,𝝋=symbols("x y z r 𝜽 𝝆 𝝋 𝜽 u v w a b c m n l p T 𝝆 θ 𝝋")
r,Rho,Phi,Theta=symbols("r,rho,phi,theta",positive=True)

a,b,c=symbols("a,b,c")

### Single-Variable Calculus
# Criticals(f_,x_,rational=False,BC=[])
# extrema_BI(f_,x_,c_)
# diff_app(f_,x_,rational=False,BC=[])

def tex(expr_):
    """
    convert express to latex
    """
    return(latex(eval(str(expr_))))


# find critical values

def Criticals(f_,x_,rational=False,BC=[]):
    """
    Criticals(f_,x_,rational=False)
    Inputs
       f_: function
       x_: variable
       rational: False (or True)
                 whether rational function is computered here  
    Output
       critical values (list)
    """
    f=f_
    x=x_
    text="Functions:  $$\large{\quad f(x) = %s}$$" %(latex(f_))
    
    if rational:
       d1= simplify(cancel(diff(f_,x_)))
       n,d= fraction(d1)
       sols=solve(n,x_)+solve(d,x_)
    else:
       d1=diff(f_,x_)
       
       sols=solve(d1,x_)
    
    sols=sols+BC
    sols.sort()
    print("Critical Points of f(x)=%s: %s " %(f_,sols))
         
    return  sols

def extrema_BI(f_,x_,c_):
    """
    extrema_BI(f_,c_)
    Input:
       f_: function
       x_: variable
       c_: list of critical values
    Print out possible minimum and maximum
    """
    p_=[]
    text="<big>Extrema of $\large{%s}$:" %(latex((f_)))
    #print("Extrema of {}\n---".format(latex((f_))))
    text=text+"<br>---<br>"
    for c in c_:
        pval=f_.subs({x_:c})
        #print("at x={}, f(x)={}".format(c,pval))
        text=text+" $$\large{\circ \quad f(x)=%s \\text{ at }x=%s}$$" %(latex(pval),latex(c))                    
        p_.append(pval)
        #print(p_)
    text=text+"<br>---<br>"    
    text=text+"Maximum is $\large{%s}$, and Minimum is $\large{%s}$. " %(latex(max(p_)),latex(min(p_)))
    #print("---\nMaximum is {}, and Minimum is {}".format(max(p_),min(p_))) 
    return HTML(text)

# diff_app
def diff_app(f_,x_,rational=False,BC=[]):
    """
    diff_app(f_,x_,rational=False)
    Inputs
       f_: function
       x_: variable
       rational: False (or True)
                 whether rational function is computered here  
    Print out
       f',f'', critical values, monotonicity and concavity
    """
    f=f_
    x=x_
    if (BC==[]):
       text="Functions:  $$\large{\quad f(x) = %s}$$" %(latex(f_))
    else:
       text="Functions:  $$\large{\quad f(x) = %s\\text{ on } [%s,%s]}$$" %(latex(f_),latex(BC[0]),latex(BC[1])) 
    
    if rational:
       d1= simplify(cancel(diff(f_,x_)))
       n,d= fraction(d1)
       sols=solve(n,x_)+solve(d,x_)
       d22=simplify(cancel(diff(f_,x_,2)))
       n_,d_=fraction(cancel(diff(f_,x_,2)))
        
       d2=cancel(n_*d_)
    else:
       d1=diff(f_,x_)
       d2=diff(f_,x_,2)
       d22= diff(f_,x_,2)
       sols=solve(diff(f_,x_),x_)
    
    
    text=text+"1. Critical Points: "
    
    if (len(sols)>0):
       criticals=""
       sols.sort()
       for sol in sols:
          criticals=criticals+" %s," %latex(sol)
  
    # Critical points
    if (len(sols)>0):
           #for sol in sols: 
           text=text+"\\begin{eqnarray}"
           text=text+ \
                "\large{f'(x)=0}& \large{\Rightarrow}&\large{%s=0 }\cr" %(latex(d1))
           d11=factor(d1)
           text=text+ \
                " &\large{\Rightarrow}&\large{%s=0} \cr" %(latex(d11))            
           text=text+ \
                "&\large{\Rightarrow}&\large{ x= %s}" %(latex(criticals))
           #text=text+" $%s$," %latex(sols )
           text=text+"\end{eqnarray}"
    else:
      text=text+"$$\large{f'=%s=0\Rightarrow\\text{ no critical point exists.}}$$" %latex(d1)
    
    
    text=text+"$$\large{f''(x)=%s=%s}$$" %(latex(diff(d1,x_)),latex(factor(d22)))
    # Monotoncity
    
    if (solve(diff(f_,x_)>0)!=[]):
       if BC!=[]:
          domain = Interval(BC[0],BC[1])
          incr= solve_univariate_inequality(diff(f_,x)>0, x,False,domain)  
       else:
           incr= solve_univariate_inequality(diff(f_,x)>0, x, relational=False)
       #increasing=latex(solve(diff(f_,x)>0)) 
       increasing=latex(incr) 
    else:
        increasing=""
    if (solve(diff(f_,x_)<0)!=[]):
       if BC!=[]:
          domain = Interval(BC[0],BC[1])
          decr = solve_univariate_inequality(diff(f_,x)<0, x, False,domain)            
       else: 
          decr = solve_univariate_inequality(diff(f_,x)<0, x, relational=False)
       #decreasing=latex(solve(diff(f_,x_)<0)) 
       decreasing=latex(decr)  
    else:
        decreasing=""
    
    text=text+"2. Increasing or Decreasing:"
    
    text=text+"\\begin{eqnarray}"
    if increasing!="":
       text=text+ \
        "&\quad\\text{a) Increasing, }f'(x)>0, \\text{ at }&%s\cr" %increasing
    else:
       text=text+ \
        "&\quad\\text{a) No $x$ Increasing, i.e }f'(x)\le0 \cr"
    if decreasing!="":
       text=text+ \
        "&\quad\\text{b) Decreasing, }f'(x)<0, \\text{ at }&%s\cr" %decreasing
    else:
       text=text+ \
        "&\quad\\text{b) No $x$ Decreasing, i.e }f'(x)\ge0 \cr" 
    text=text+"\\end{eqnarray}"
    #text="\\begin{eqnarray}"  
    
    # Concavity
    
    if (solve(d2>0)!=[]):
       if BC!=[]:
          domain = Interval(BC[0],BC[1])
          up=solve_univariate_inequality(d2>0, x,False,domain)             
       else:     
          up=solve_univariate_inequality(d2>0, x, relational=False) 
       #up=latex(solve(d2>0)) 
    else:
        up=""
    if (solve(d2<0)!=[]):
        if BC!=[]:
          domain = Interval(BC[0],BC[1])
          down=solve_univariate_inequality(d2<0, x,False,domain)             
        else:
          down=solve_univariate_inequality(d2<0, x, relational=False)
       #down=latex(solve(d2<0)) 
    else:
        down=""
    
    text=text+"3. Concave Upwards or Downwards:"
    
    text=text+"\\begin{eqnarray}"
    if up!="":
       text=text+ \
        "&\quad\\text{a) Concave Upwards, }f''(x)>0, \\text{ at }&%s\cr" %latex(up)
    else:
       text=text+ \
        "&\quad\\text{a) No $x$ Concave Upwards, i.e }f''(x)\le0 \cr"
    if down!="":
       text=text+ \
        "&\quad\\text{b) Concave Downwards, }f''(x)<0, \\text{ at }&%s\cr" %latex(down)
    else:
       text=text+ \
        "&\quad\\text{b) No $x$  Concave Downwards, i.e }f''(x)\ge0 \cr" 
    text=text+"\\end{eqnarray}"
    
   
    #text="\end{eqnarray}"
    return(Latex(text))                         

### Ingration for Single-variable Functions

def scale_func(f_,x,v):
    """
    f_: function 
    x : original variable
    v : new variable, v=f(x) where x=g(v)
    """
    text="Let $x = %s$:" %(tex(v))
    text+="\\begin{eqnarray}"
    U=solve(x-v,x)
    J= diff(U[0],u)
    fu=f_.subs({x:U[0]})
    I=simplify(fu*J)
    text+="\int %s dx &=& \int %s du" %(tex(f_),tex(I))
    text+="\end{eqnarray}"
    return Latex(text)


def Integration_Substitution(f,x,g):
    
    f_latex=tex(f)
    g_p=diff(g,x)
    fu=(f/g_p).subs({g:u})
    fu_latex=tex(fu)
    text_pre="Replacing $%s$ by $u$ gets:" %(tex(g))
    
    result=integrate(fu,u)
    result_latex=tex(result)
    
    text0="\\begin{eqnarray}"
    text5="\end{eqnarray}"
    
    textfI="\int %s d %s" %(f_latex,x)
    
    textfI+="&=& \int %s d u \cr" %(fu_latex)
    textfI+="&=& %s +C \cr" %(result_latex)
    
    text=text_pre+text0+textfI+text5
    
    return Latex(text)

def Integration_by_Parts(F_,f,g,x):
    """
    vrs: F_,f,g,x
     ∫F_dx = ∫fgdx = Fg - ∫F g'dx
    """
    integrand = F_
    I_latex=tex(integrand)
    g_latex=tex(g)
    F= integrate(f,x)
    F_latex=tex(F)
    gp=diff(g,x)
    text_pre="Let $F'(x)=%s$, and  $g(x)=%s$, then: " %(tex(f),tex(g))
        
    result=integrate(F*gp,x)
    result_latex=tex(result)
         
    text0="\\begin{eqnarray}"
    text5="\end{eqnarray}"
    
    textfI="\int %s d %s" %(I_latex,x)
    
    textfI+="&=& %s \cdot \left(%s\\right) - \int \left(%s\\right) d u \cr" %(F_latex,g_latex,tex(F*gp))
    textfI+="&=& %s \cdot  \left(%s\\right)  - \left(%s\\right) +C \cr" %(F_latex,g_latex,result_latex)
    
    text=text_pre+text0+textfI+text5
    
    return Latex(text)

def Integration_Trigonometric_odd(f,x,g):
    """
    ∫sin^m(x)cos^n(x)dx, m or n: odd
    vars: (f,x,g)
         f: integrand
         x
         g: sin(x) or cos(x)
    """
    f_latex=tex(f)
    g_p=diff(g,x)
    if g==sin(x):
       fu=(f/g_p).subs({sin(x):u,cos(x):sqrt(1-u**2)})
    else:
       fu=(f/g_p).subs({cos(x):u,sin(x):sqrt(1-u**2)})
    fu_latex=latex(eval(str(fu)))
    text_pre="Replacing $%s$ by $u$ gets:" %(tex(g))
    
    result=integrate(fu,u)
    result_latex=tex(result)
    
    text0="\\begin{eqnarray}"
    text5="\end{eqnarray}"
    
    textfI="\int %s d %s" %(f_latex,x)
    
    textfI+="&=& \int %s d u \cr" %(fu_latex)
    textfI+="&=& %s +C \cr" %(result_latex)
    
    text=text_pre+text0+textfI+text5
    
    return Latex(text)

def Integration_Trigonometric_even(f_,x):
    """
    ∫sin^m(x)cos^n(x)dx, m,n: even
    vars: (f,x)
         f: integrand
         x
    """
    f1=f_.subs({cos(x)**2:(1+cos(2*x))/2})
    f2=f1.subs({sin(x)**2:(1-cos(2*x))/2})
    f3=expand(f2)
    f4=f3.subs({cos(2*x)**2:(1+cos(4*x))/2})
    text="\\begin{eqnarray}"
    text+="%s &=& %s \cr" %(tex(f_),tex(f2))
    if f4!=f2:
       text+=" &=& %s \cr" %(tex(f4))
    #text+=" &=& %s \cr" %(tex(f3))
    text+="\Rightarrow \int %s dx &=&\int \left(%s \\right) dx \cr" %(tex(f_),tex(f3))
    if f4==f3:
       I=integrate(f4,x)
    else:
       text+=" &=&\int \left( %s \\right) d %s \cr" %(tex(f4),tex(x))
       I=integrate(f4,x)
       #f5=f4.subs({cos(2*x)**2:(1+cos(4*x))/2}) 
    text+=" &=& %s +C \cr" %(tex((I)))       
    text+="\end{eqnarray}" 
    return  Latex(text)  

def Integration_TrigonometricSubstitution(f,x,g,t=t):
    """
    ∫f(a^2 ± x^2) dx
    vars: (f,x,g)
         f: integrand
         x
         g: sin(t). tan(t), or sec(t)
         t: theta variable       
    """
    f_latex=tex(f)
    g_p=diff(g,t)
    fu=(f).subs({x:g})*g_p
    if g==sin(t):
       # remove the absolute op of |cos(t)| = cos(t) 
       fu=simplify(fu).subs({sqrt(cos(t)**2):cos(t)})
    elif g==tan(t):
       # remove the absolute op of |sec(t)| = sec(t)
       # convert 1/cos(t) = sec(t)
       fu=simplify(fu).subs({sqrt(sec(t)**2):sec(t)})
       fu=fu.subs({sqrt(1/cos(t)**2):sec(t)})
    elif g==sec(t):
       # remove the absolute op of |tan(t)| = tan(t)
       fu=simplify(fu).subs({sqrt(tan(t)**2):tan(t)})
    else:
       J=1 
    fu_latex=tex(fu)
    text_pre="Replacing $%s=%s$ gets:" %(tex(x),tex(g))
    #return(fu)
    result=integrate(fu,t)
    result_latex=tex(result)

    text0="\\begin{eqnarray}"
    text5="\end{eqnarray}"
    
    textfI="\int %s d %s" %(f_latex,x)
    
    textfI+="&=& \int %s d %s \cr" %(fu_latex,t)
    textfI+="&=& %s +C \cr" %(result_latex)
    
    text=text_pre+text0+textfI+text5
    
    return Latex(text)

def PartialFracInt(f,g,x):
    """
    ∫f/gdx
    vars: (f,x,g)
         f: nominator
         g: denominator
         x: variable
    """
    func="(%s)/(%s)" %(f,g)
    f_latex=latex(eval(str(func)))
    pre0="1. Integrand could be expressed as folllows:" 
    #return Latex(pre0)
    pf=apart(f/g)
    #pprint(pf)
    pre0+="$$\\frac{%s}{%s}=%s$$" %(tex(f),tex(g),tex(pf))
    pre0+="2. Thus the integal is evaluated as follows:"
    #return Latex(pre0)
    I= integrate(pf,x)
    text="\\begin{eqnarray}"
    text+="\int \\frac{%s}{%s} d %s" %(tex(f),tex(g),tex(x))
    text+="&=& \int \left( %s \\right)d %s \cr" %(tex(pf),tex(x))
    text+="&=& %s + C\cr " %(tex(I))
    text+="\end{eqnarray}"
    return Latex(pre0+text)


### Multiple-Variable Calculus

def Jacobian_det(XU,U):
    """
    Calculate the Jacobian, 𝛛X/𝛛U
    input: XU: original coordinates, X, in form of new coordinates, U,
           U: new Coordinates 
    output: absolute value of determinant of Jacobian       
    """
    
    MX=Matrix(XU)
    MU=Matrix(U)
    S= MX.jacobian(MU )     
    return simplify(Abs(S.det()))

# Fix error return of MultipleIntegral

def MultipleIntegral(f,X,XR):
    """
    input: ∫ dx ∫ dy ∫ f(x,y,z) dz
           f: f(x,y,z),
           X: (x,y, ...), variable pair
           XR: [[x0,x1], [y0,y1],...] 
    output: details of integral, enhanced by colored text, and value
    
    Demo
    # Double integral
    f=1
    X=[x,y]
    XR=[[0,1],[0,1-x]]
    MultipleIntegral(f,X,XR)
    
    # triple integral
    f=exp(x)
    X=[x,y,z,r]
    XR=[[0,1],[0,1-x],[0,1-x-y],[0,1-x-y-z]]
    MultipleIntegral(f,X,XR)
    
    # Triple integral in Cylindrical Coordinates
    J=r
    f=1
    X=[r,Theta,z]
    XR=[[r,Theta,z],[0,1],[0,pi],[0,1]]
    MultipleIntegral(f*J,X,XR)
    
    # Triple integral in Sperical Coordinates
    J=Rho**2*sin(Phi)
    f=1
    X=[Theta,Phi,Rho]
    XR=[[0,2*pi],[0,pi],[0,1]]

    MultipleIntegral(f*J,X,XR)
    
    """
    f_latex=latex(eval(str(f)))
    
    XR0=[]
    X_tex=[]
    for var in XR:
        XR0.append([latex(eval(str(var[0]))),latex(eval(str(var[1])))])
    for var in X:
        X_tex.append(latex(eval(str(var))))
    
    dA=""
    for var in X_tex:
        dA+=" d %s " %(var)
    if len(X)==2:
       intsign="\iint"
    elif(len(X)==3):
       intsign="\iiint" 
    else:
        intsign="\Large{\int}"    
    
    # indefinte I of z
    I='I'+str(X[-1])
    IX=[integrate(f,X[-1])]
    IX_tex=[latex(eval(str(IX[0])))]
    int_g='\left.\color{brown}{%s} \\right|_{%s}^{%s}' %(IX_tex[0],XR0[-1][0],XR0[-1][1])
    Integrand_tex_val=[int_g]

   
    Integrand=[f_latex]
    II='II'+str(X[-1])
    DIX=[integrate(f,(X[-1],XR[-1][0],XR[-1][1]))]
    DIX_tex=[latex(eval(str(DIX[0])))]
    n=len(X)
    i=0
    for var in X[len(X)-2::-1]:
        
        I='I'+str(var)
        while True:
            try:
                I=integrate(DIX[i],var)
                break
            except ValueError:
                #errortext="\\begin{eqnarray}"
                errortext="$$%s_{\Large{\mathbf{V}}} \color{brown}{%s} %s $$" %(intsign,f_latex,dA) 
                #errortext+="\end{eqnarray}"
                errortext+=("$\color{red}{\\text{Can't}}$ be integrated Here, Try another way ...")
                return Latex(errortext)
        #I=integrate(DIX[i],var)
        IX.append(I)
        IX_tex.append(latex(eval(str(I))))
        Integrand_tex_val.append('\left. \color{brown}{%s} \\right|_{%s}^{%s}' %(IX_tex[-1],XR0[n-i-2][0],XR0[n-i-2][1]) )
        II='II'+str(var)
        II=integrate(DIX[i],(var,XR[-i-2][0],XR[-i-2][1]))
        DIX.append(II)
        DIX_tex.append(latex(eval(str(II))))
        i+=1
        
    for I_f in DIX[:-1]:
        Integrand.append(latex(eval(str(I_f))))

    text0="\\begin{eqnarray}"
    text5="\end{eqnarray}"
    
    #domain="\large{\left\{"
    domain="\left\{\large{\\begin{array}{l}"
    i=0
    for var in X_tex:
        domain=domain+" %s \le %s \le %s,\cr" %(XR0[i][0],var,XR0[i][1])
        i+=1
    #domain+="\\right\}}"
    domain+="\end{array}}\\right\}"
    
        
    #dA=""
    #for var in X_tex:
    #    dA+=" d %s " %(var)
    
    textF="%s_{\Large{\mathbf{V}}=%s} \color{brown}{%s} dV&=& %s_{\Large{\mathbf{V}}} \color{brown}{%s} %s \cr " %(intsign,domain,f_latex,intsign,f_latex,dA)
    fubini="\color{blue}{\\text{Fubini's Theorem}}"
    
    textfI=""
    for i in range(len(X)):
        j=0
        if (i==0):
            eq1="%s&=&" %(fubini)
        else:
            eq1="&=&"
        textfI+=eq1  
        for var in X_tex[:len(X)-i-1:]:
            textfI+="\int_{%s}^{%s}d{%s}" %(XR0[j][0],XR0[j][1],var)
            j+=1
        #print(i,len(Integrand),len(X))  
        textfI+="\int_{%s}^{%s} \color{brown}{%s}d{%s}\cr "  %(XR0[-i-1][0],XR0[-i-1][1],Integrand[i],X_tex[-i-1])
        
        textfI+="&=&"
        int_pre=""

        for k in range(len(X)-i-2):
            int_pre+="\int_{%s}^{%s} d{%s}" %(XR0[k][0],XR0[k][1],X_tex[k])
        if len(X)-i-1>0: 
            int_ev="\int_{%s}^{%s} %s d{%s}" %(XR0[-i-2][0],XR0[-i-2][1],Integrand_tex_val[i],X_tex[-i-2])
        else:
            int_ev="%s" %(Integrand_tex_val[-1])
        textfI+=int_pre+int_ev+'\cr'
    textfI+='&=&%s' %(DIX_tex[-1])   

    text=text0+textF+textfI+text5

    return Latex(text)

def DoubleInt_polar_v3(f,X,xr,yr,Jacobian=r):
    """
    Double integral in Polar Coordinates
    input: ∫ dr ∫ f(r cos𝛉,r sin𝛉) rd𝛉
           f: f(x,y), which will be automatically transformed from (x,y) to (r cos𝛉,r sin𝛉)
           X: (x,y), variable pair in Cartesian Coordinates
           xr: (x0,x1) of r
           yr: (y0,y1) of 𝛉
           Jacobian: r
    output: details of integration and value  
    
    Should  calculate Jacobian and find out integation range in Polar Coordinates
    """

    Theta=symbols("theta")
    #Jacobian=r
    f0=f
    f0_latex=latex(eval(str(f0)))
    
    fp=simplify(((f+0*X[0]).subs({X[0]**2+X[1]**2:r**2,X[0]:r*cos(Theta),X[1]:r*sin(Theta)})))
    fp_latex=latex(fp)
    fpp_latex=latex(fp*Jacobian)
    
    f=f*r
    f_latex=latex(eval(str(f)))
    X0=latex(X[0])
    X1=latex(X[1])
    
    Iyy=integrate(fp*Jacobian,theta)
    Iyy_latex=latex(eval(str(Iyy)))                 

    Iy=integrate(fp*Jacobian,[theta,yr[0],yr[1]])
    Iy_latex=latex(eval(str(Iy)))
       
    II= integrate(Iy,r)
    II_latex=latex(eval(str(II)))
    
    I=integrate(Iy,[r,xr[0],xr[1]])
    I_latex=latex(eval(str(I)))
    
    yr0=latex(eval(str(yr[0])))
    yr1=latex(eval(str(yr[1])))
    
    
    text0="\\begin{eqnarray}"
    textfunc="\iint_{D} \color{brown}{%s} dA&=& \iint_{D} \color{brown}{%s} dx dy  \cr " %(f0_latex,f0_latex)
    textfunc1="&=& \iint_{D} \color{brown}{%s}  \color{blue}{r} drd %s \cr" %(fp_latex,latex(Theta))
       
    text_desc="where $%s$ is the absolute value of determinant of Jacobian, ${||\\frac{\partial (x,y)}{\partial (r,\\theta)}||}$. Thus" %(Jacobian)
    text0="\\begin{eqnarray}"
    text1="\int^{%s}_{%s}d{%s}\int^{%s}_{%s}\color{brown}{%s}d{%s} " %(xr[1],xr[0],r,yr1,yr0,
                                                               fpp_latex,latex(Theta));
    
    text2="&=& \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0],\
                                                                    Iyy_latex,yr1,yr0,r)
    text3="&=& \int^{%s}_{%s}\color{brown}{%s}d{%s}\cr&=&\left.{\color{brown}{%s}}\\right|^{\large{%s}}_{\large{%s}}={%s}\cr" %(
            xr[1],xr[0],Iy_latex,r, II_latex,xr[1],xr[0],I_latex)
    textf="\end{eqnarray}"
    
    text=text0+textfunc+textfunc1+textf+text_desc+text0+text1+text2+text3+textf;
    return Latex(text)

def DoubleInt_UV_v3(f,X,XU,U,xr,yr):
    """
    Double integral in General Coordinates
    input: ∫ dr ∫ f(r cos𝛉,r sin𝛉) rd𝛉
           f: f(x,y), which will be automatically transformed from (x,y) to (r cos𝛉,r sin𝛉)
           X: (x,y), variable pair in Cartesian Coordinates
           XU: (x(u,v),y(u,v))
           U: (u,v)
           xr: (x0,x1) of r
           yr: (y0,y1) of 𝛉

    output: details of integration and value  
    
    Should  calculate Jacobian and find out integation range in Polar Coordinates
    """
    Jacobian=Jacobian_det(XU,U);
    
    #Jacobian=r
    f0=f
    f0_latex=latex(eval(str(f0)))
    
    fp=simplify(((f+0*X[0]).subs({X[0]:XU[0],X[1]:XU[1]})))
    fp_latex=latex(fp)
    fpp_latex=latex(fp*Jacobian)
    
    f=f*Jacobian
    f_latex=latex(eval(str(f)))
    X0=latex(X[0])
    X1=latex(X[1])
    
    Iyy=integrate(fp*Jacobian,U[1])
    Iyy_latex=latex(eval(str(Iyy)))                 

    Iy=integrate(fp*Jacobian,[U[1],yr[0],yr[1]])
    Iy_latex=latex(eval(str(Iy)))
       
    II= integrate(Iy,U[0])
    II_latex=latex(eval(str(II)))
    
    I=integrate(Iy,[U[0],xr[0],xr[1]])
    I_latex=latex(eval(str(I)))
    
    yr0=latex(eval(str(yr[0])))
    yr1=latex(eval(str(yr[1])))
    
    
    text0="\\begin{eqnarray}"
    textfunc="\iint_{D} \color{brown}{%s} dA&=& \iint_{D} \color{brown}{%s} dx dy  \cr " %(f0_latex,f0_latex)
    textfunc1="&=& \iint_{D} \color{brown} {\left( %s \\right) }\cdot \color{blue}{%s} d %sd %s \cr" %(fp_latex,latex(Jacobian),latex(U[0]),latex(U[1]))
       
    text_desc="where $%s$ is the absolute value of determinant of Jacobian, $\Large{{||\\frac{\partial (x,y)}{\partial (%s,%s)}||}}$. Thus" %(Jacobian,U[0],U[1])
    text0="\\begin{eqnarray}"
    text1="\int^{%s}_{%s}d{%s}\int^{%s}_{%s}\color{brown}{%s}d{%s} " %(xr[1],xr[0],U[0],yr1,yr0,
                                                               fpp_latex,latex(U[1]));
    
    text2="&=& \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0],\
                                                                    Iyy_latex,yr1,yr0,U[0])
    text3="&=& \int^{%s}_{%s}\color{brown}{%s}d{%s}\cr&=&\left.{\color{brown}{%s}}\\right|^{\large{%s}}_{\large{%s}}={%s}\cr" %(
            xr[1],xr[0],Iy_latex,U[0], II_latex,xr[1],xr[0],I_latex)
    textf="\end{eqnarray}"
    
    text=text0+textfunc+textfunc1+textf+text_desc+text0+text1+text2+text3+textf;
    return Latex(text)


def TripleInt_Cylind(f,X,XU,U,xr,yr,zr):
    """
    Triple integral in General Coordinates
    input: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉
           f: f(x,y,z), which will be automatically transformed from (x,y,z) to (r cos𝛉,r sin𝛉, z)
           X: (x,y,z), variable pair in Cartesian Coordinates
           XU: (x(u,v,z),y(u,v,z))
    𝜓       U: (u,v)
           xr: (x0,x1) of r
           yr: (y0,y1) of 𝛉
           zr: (z0,z1) of z

    output: details of integration and value  
    
    Should  calculate Jacobian and find out integation range in Polar Coordinates
    
    Demo:
    > TripleInt_Cylind(x*y*z,[x,y,z],[r*cos(Theta),r*sin(Theta),z],[r,Theta,z],[0,1],[0,pi],[0,1])
    
    
    """
    Jacobian=r;
    
    #Jacobian=r
    f0=f
    f0_latex=latex(eval(str(f0)))
    
    fp=simplify(((f+0*X[0]).subs({X[0]:XU[0],X[1]:XU[1],X[2]:XU[2]})))
    fp_latex=latex(fp)
    fpp_latex=latex(fp*Jacobian)
    
    f=f*Jacobian
    f_latex=latex(eval(str(f)))
    X0=latex(X[0])
    X1=latex(X[1])
    
    Izz=integrate(fp*Jacobian,U[2])
    Izz_latex=latex(eval(str(Izz)))                 

    Iz=integrate(fp*Jacobian,[U[2],zr[0],zr[1]])
    Iz_latex=latex(eval(str(Iz)))
    
    Iyy=integrate(Iz,U[1])
    Iyy_latex=latex(eval(str(Iyy)))                 

    Iy=integrate(Iz,[U[1],yr[0],yr[1]])
    Iy_latex=latex(eval(str(Iy)))
       
    II= integrate(Iy,U[0])
    II_latex=latex(eval(str(II)))
    
    I=integrate(Iy,[U[0],xr[0],xr[1]])
    I_latex=latex(eval(str(I)))
    
    zr0=latex(eval(str(zr[0])))
    zr1=latex(eval(str(zr[1])))
    yr0=latex(eval(str(yr[0])))
    yr1=latex(eval(str(yr[1])))
    
    
    text0="\\begin{eqnarray}"
    textfunc="\iiint_{V} \color{brown}{%s} dA&=& \iiint_{V} \color{brown}{%s} dx dy dz \cr " %(f0_latex,f0_latex)
    textfunc1="&=& \iiint_{V} \color{brown} {\left( %s \\right) }\cdot \color{blue}{%s} d %s d %s d %s \cr" %(fp_latex,latex(Jacobian),\
                                                                     latex(U[0]),latex(U[1]),latex(U[2]))
       
    text_desc="where $%s$ is the absolute value of determinant of Jacobian, $\Large{{||\\frac{\partial (x,y,z)}{\partial (%s,%s,%s)}||}}$. Thus" %(Jacobian, \
                                                                                            latex(U[0]),latex(U[1]),latex(U[2]))
    text0="\\begin{eqnarray}"
    textf="\end{eqnarray}"
  
    text1="\int^{%s}_{%s}d{%s}\int^{%s}_{%s}d{%s}\int^{%s}_{%s}\color{brown}{%s}d{%s} " %(xr[1],xr[0],U[0],latex(yr[1]),latex(yr[0]),latex(U[1]), \
                                                                                          zr[1],zr[0],fpp_latex,latex(U[2]));
    
    text2="&=& \int^{%s}_{%s} d%s \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0],latex(U[0]), \
                                                                    latex(yr[1]),latex(yr[0]),Izz_latex,zr1,zr0,latex(U[1]))
    
    
    text3="&=& \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0], \
                                                                    Iyy_latex,yr1,yr0,U[0])

    text4="&=& \int^{%s}_{%s}\color{brown}{%s}d{%s}\cr&=&\left.{\color{brown}{%s}}\\right|^{\large{%s}}_{\large{%s}}={%s}\cr" %(
            xr[1],xr[0],Iy_latex,U[0], II_latex,xr[1],xr[0],I_latex)
    
    
    text=text0+textfunc+textfunc1+textf+text_desc+text0+text1+text2+text3+text4+textf;
    return Latex(text)


def TripleInt_Spherical(f,X,XU,U,xr,yr,zr):
    """
    Triple integral in Spherical Coordinates
    input: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉
           f: f(x,y,z), which will be automatically transformed from (x,y,z) to ( 𝜌cos𝛉sin𝜙,𝜌sin𝛉sin𝜙, 𝜌cos𝜙)
           X: (x,y,z), variable pair in Cartesian Coordinates
           XU: (x(u,v,z),y(u,v,z))
           U: (u,v)
           xr: (x0,x1) of 𝜌
           yr: (y0,y1) of 𝛉
           zr: (z0,z1) of 𝜙

    output: details of integration and value  
    
    Should  calculate Jacobian and find out integation range in Polar Coordinates
    
    Demo:
    > X=[x,y,z]
    > XU=[Rho*cos(Theta)*sin(Phi),Rho*sin(Theta)*sin(Phi),Rho*cos(Phi)]
    > U=[Rho,Theta,Phi]
    > TripleInt_Spherical(1,X,XU,U,[0,1],[0,2*pi],[0,pi])
    """
    Jacobian=Rho**2*sin(Phi);
    
    #Jacobian=r
    f0=f
    f0_latex=latex(eval(str(f0)))
    
    fp=simplify(((f+0*X[0]).subs({X[0]:XU[0],X[1]:XU[1],X[2]:XU[2]})))
    fp_latex=latex(fp)
    fpp_latex=latex(fp*Jacobian)
    
    f=f*Jacobian
    f_latex=latex(eval(str(f)))
    X0=latex(X[0])
    X1=latex(X[1])
    
    Izz=integrate(fp*Jacobian,U[2])
    Izz_latex=latex(eval(str(Izz)))                 

    Iz=integrate(fp*Jacobian,[U[2],zr[0],zr[1]])
    Iz_latex=latex(eval(str(Iz)))
    
    Iyy=integrate(Iz,U[1])
    Iyy_latex=latex(eval(str(Iyy)))                 

    Iy=integrate(Iz,[U[1],yr[0],yr[1]])
    Iy_latex=latex(eval(str(Iy)))
       
    II= integrate(Iy,U[0])
    II_latex=latex(eval(str(II)))
    
    I=integrate(Iy,[U[0],xr[0],xr[1]])
    I_latex=latex(eval(str(I)))
    
    zr0=latex(eval(str(zr[0])))
    zr1=latex(eval(str(zr[1])))
    yr0=latex(eval(str(yr[0])))
    yr1=latex(eval(str(yr[1])))
    
    
    text0="\\begin{eqnarray}"
    textfunc="\iiint_{V} \color{brown}{%s} dA&=& \iiint_{V} \color{brown}{%s} dx dy dz \cr " %(f0_latex,f0_latex)
    textfunc1="&=& \iiint_{V} \color{brown} {\left( %s \\right) }\cdot \color{blue}{%s} d %s d %s d %s \cr" %(fp_latex,latex(Jacobian),\
                                                                     latex(U[0]),latex(U[1]),latex(U[2]))
       
    text_desc="where $%s$ is the absolute value of determinant of Jacobian, $\Large{{||\\frac{\partial (x,y,z)}{\partial (%s,%s,%s)}||}}$. Thus" %(latex(Jacobian), \
                                                                                            latex(U[0]),latex(U[1]),latex(U[2]))
    text0="\\begin{eqnarray}"
    textf="\end{eqnarray}"
  
    text1="\int^{%s}_{%s}d{%s}\int^{%s}_{%s}d{%s}\int^{%s}_{%s}\color{brown}{%s}d{%s} " %(xr[1],xr[0],latex(U[0]),latex(yr[1]),latex(yr[0]),latex(U[1]), \
                                                                                          zr[1],zr[0],fpp_latex,latex(U[2]));
    
    text2="&=& \int^{%s}_{%s}d{%s}\int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0],latex(U[0]), \
                                                                    latex(yr[1]),latex(yr[0]),Izz_latex,zr1,zr0,latex(U[1]))
    
    
    text3="&=& \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(xr[1],xr[0], \
                                                                    Iyy_latex,yr1,yr0,latex(U[0]))

    text4="&=& \int^{%s}_{%s}\color{brown}{%s}d{%s}\cr&=&\left.{\color{brown}{%s}}\\right|^{\large{%s}}_{\large{%s}}={%s}\cr" %(
            xr[1],xr[0],Iy_latex,latex(U[0]), II_latex,xr[1],xr[0],I_latex)
    
    
    text=text0+textfunc+textfunc1+textf+text_desc+text0+text1+text2+text3+text4+textf;
    return Latex(text)

def TripleInt_UVW(f,X,XU,U,XR):
    """
    Triple integral in Spherical Coordinates
    input: ∫ dz ∫ dr ∫ f(r cos𝛉,r sin𝛉,z) rd𝛉
           f: f(x,y,z), which will be automatically transformed from (x,y,z) to ( 𝜌cos𝛉sin𝜙,𝜌sin𝛉sin𝜙, 𝜌cos𝜙)
           X: (x,y,z), variable pair in Cartesian Coordinates
           XU: (x(u,v,z),y(u,v,z))
           U: (u,v)
           xr: (x0,x1) of 𝜌
           yr: (y0,y1) of 𝛉
           zr: (z0,z1) of 𝜙

    output: details of integration and value  
    
    Should  calculate Jacobian and find out integation range in Polar Coordinates
    """
    MX=Matrix(XU)
    MU=Matrix(U)
    S= MX.jacobian(MU )         
    #Jacobian=Jacobian_det(XU,U);
    Jacobian=simplify(Abs(S.det()))
    
    xr=XR[0]
    yr=XR[1]
    zr=XR[2]
    
    #Jacobian=r
    f0=f
    f0_latex=latex(eval(str(f0)))
    
    fp=simplify(((f+0*X[0]).subs({X[0]:XU[0],X[1]:XU[1],X[2]:XU[2]})))
    fp_latex=latex(fp)
    fpp_latex=latex(fp*Jacobian)
    
    f=f*Jacobian
    f_latex=latex(eval(str(f)))
    X0=latex(X[0])
    X1=latex(X[1])
    
    Izz=integrate(fp*Jacobian,U[2])
    Izz_latex=latex(eval(str(Izz)))                 

    Iz=integrate(fp*Jacobian,[U[2],zr[0],zr[1]])
    Iz_latex=latex(eval(str(Iz)))
    
    Iyy=integrate(Iz,U[1])
    Iyy_latex=latex(eval(str(Iyy)))                 

    Iy=integrate(Iz,[U[1],yr[0],yr[1]])
    Iy_latex=latex(eval(str(Iy)))
       
    II= integrate(Iy,U[0])
    II_latex=latex(eval(str(II)))
    
    I=integrate(Iy,[U[0],xr[0],xr[1]])
    I_latex=latex(eval(str(I)))
    
    zr0=latex(eval(str(zr[0])))
    zr1=latex(eval(str(zr[1])))
    yr0=latex(eval(str(yr[0])))
    yr1=latex(eval(str(yr[1])))
    
    XR0=[]
    X_tex=[]
    for var in XR:
        XR0.append([latex(eval(str(var[0]))),latex(eval(str(var[1])))])
    for var in X:
        X_tex.append(latex(eval(str(var))))
    
    ZR1=XR0[2]
    YR1=XR0[1]
    XR1=XR0[0]
    
    text0="\\begin{eqnarray}"
    textfunc="\iiint_{V} \color{brown}{%s} dA&=& \iiint_{V} \color{brown}{%s} dx dy dz \cr " %(f0_latex,f0_latex)
    textfunc1="&=& \iiint_{V} \color{brown} {\left( %s \\right) }\cdot \color{blue}{%s} d %s d %s d %s \cr" %(fp_latex,latex(Jacobian),\
                                                                     latex(U[0]),latex(U[1]),latex(U[2]))
       
    text_desc="where $$[%s,%s,%s] = [%s,%s,%s]$$, and the absolute value of determinant of Jacobian, $\Large{{||\\frac{\partial (x,y,z)}{\partial (%s,%s,%s)}||}} = %s$. Thus" %(latex(X[0]), \
                latex(X[1]),latex(X[2]),latex(XU[0]),latex(XU[1]),latex(XU[2]),  \
                latex(U[0]),latex(U[1]),latex(U[2]),latex(Jacobian))
    text0="\\begin{eqnarray}"
    textf="\end{eqnarray}"
  
    text1="\int^{%s}_{%s}d{%s}\int^{%s}_{%s}d{%s}\int^{%s}_{%s}\color{brown}{%s}d{%s} " %(XR1[1],XR1[0],latex(U[0]),YR1[1],YR1[0],latex(U[1]), \
                                                                                          ZR1[1],ZR1[0],fpp_latex,latex(U[2]));
    
    text2="&=& \int^{%s}_{%s}d{%s}\int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(XR1[1],XR1[0],latex(U[0]), \
                                                                    YR1[1],YR1[0],Izz_latex,zr1,zr0,latex(U[1]))
    text22="&=& \int^{%s}_{%s}d{%s}\int^{%s}_{%s}\,\color{brown}{%s}\,d{%s}\cr" %(XR1[1],XR1[0],latex(U[0]), \
                                                                                  YR1[1],YR1[0], Iz_latex , latex(U[1]))
        
    text3="&=& \int^{%s}_{%s}\left.\color{brown}{%s}\\right|^{\large{%s}}_{\large{%s}}d{%s}\cr" %(XR1[1],XR1[0], \
                                                                    Iyy_latex,yr1,yr0,latex(U[0]))

    text4="&=& \int^{%s}_{%s}\color{brown}{%s}d{%s}\cr&=&\left.{\color{brown}{%s}}\\right|^{\large{%s}}_{\large{%s}}={%s}\cr" %(
            XR1[1],XR1[0],Iy_latex,latex(U[0]), II_latex,xr[1],xr[0],I_latex)
    
    
    text=text0+textfunc+textfunc1+textf+text_desc+text0+text1+text2+text22+text3+text4+textf;
    return Latex(text)