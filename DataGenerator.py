import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(r"E:\Documents\TU Freiberg CMS\3.Sem-Study Material\PPP\Working_Directory\Gradient_Descent_Algorithm")

def f(x):
    #y=0.745*x**3 + 1e-8*x**2*np.cos(2*x)
    ##//y=0.745*x**3 + 4*x**2*np.cos(2*x)
    y=0.745*x**3 + 8.24*x**2 - 0.08*x + 9.4*np.exp(1*x - 4)
    
    #y=6.89*x**4 - 2.17*np.exp(1.97*x)
    return y

outf=open("ActualParameterData.txt","w")
outf.write("Equation and Parameters for generated Dataset are as follows:\n")
outf.write(" y=0.745*x**3 + 8.24*x**2 - 0.08*x + 9.4*np.exp(1*x - 4)")
outf.close();

x=np.linspace(-1,4,num=100)
# z=np.linspace(-2,5,num=100)
# p=np.linspace(-1,2,num=100)

y=f(x)
print(y)
dfx =pd.DataFrame(x)
dfx.to_csv("xdata.csv",index=False,index_label=False)

# dfz =pd.DataFrame(z)
# dfz.to_csv("zdata.csv",index=False)

# dfp =pd.DataFrame(p)
# dfp.to_csv("pdata.csv",index=False)

dfy =pd.DataFrame(y)
dfy.to_csv("y_measured.csv",index=False,index_label=False)



