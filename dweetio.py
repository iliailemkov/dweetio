import math
import dweepy

def corrVar(array1, array2): 
arith_mean1 = float(sum(array1)) / len(array1)
arith_mean2 = float(sum(array2)) / len(array2)
num = 0 
sum1 = 0 
sum2 = 0 
for i, j in zip(array1, array2):
 num += (i - arith_mean1) * (j - arith_mean2)
sum1 += ((i - arith_mean1) ** 2) 
sum2 += ((j - arith_mean2) ** 2)
 return round(num / math.sqrt(sum1 * sum2), 5)

def binomial(x, y): 
try: 
binom = math.factorial(x) // math.factorial(y) // math.factorial(x - y)
except ValueError:
 binom = 0 
return binom

def finDif(array, n, i):
sum = 0 if n == 0: return array[i]
for k in range(0, n + 1): 
sum += ((-1) ** k) * binomial(n, k) * array[i - k]
return sum

def sumFinDif(array, n):
 N = len(array) - 1
 return (finDif(array, n - 1, N) - finDif(array, n - 1, n - 1)) / (N - n + 1)

def dynamicVar(varArr1, varArr2):
num = 0 
denominatorSum1 = 0
denominatorSum2 = 0
for i in range(1, len(varArr1)):
sum1 = sumFinDif(varArr1, i)
sum2 = sumFinDif(varArr2, i)
num += sum1 * sum2
denominatorSum1 += sum1 ** 2
denominatorSum2 += sum2 ** 2
return round(num / math.sqrt(denominatorSum1 * denominatorSum2), 6)

CONST_DWEET = 'Steves_ST'
CONST_VAR1 = "objectTemp"
CONST_VAR2 = "pressure"
var1 = [] 
var2 = [] 
i=0
 for tmp in dweepy.listen_for_dweets_from(CONST_DWEET):
    if i> 250:
        break 
    i += 1 
    print tmp
    var1.append(float(tmp["content"][CONST_VAR1]))
    var2.append(float(tmp["content"][CONST_VAR2]))
stArray1 = varStandartization(var1)
stArray2 = varStandartization(var2)
cfnorm = corrVar(stArray1, stArray2)
dfnorm = dynamicVar(stArray1, stArray2)
df = dynamicVar(var1, var2)
print cfnorm
print dfnorm
print df
