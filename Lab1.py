from __future__ import print_function 
import numpy as np 
import pandas as pd 

def de(x): 
    _x = x 
    result = [] 
    # Кол-во элементов
    result.append(x.size)  
    # Avg
    result.append(np.mean(_x)) 
    # (min, max) 
    result.append((np.min(_x), np.max(_x)))
    # Ст.отклонение 
    result.append(np.std(_x)) 
    _x.sort() 
    if _x.size % 2 == 0: 
        midpoint = round(_x.size/2) 
        median = (_x[midpoint] + _x[midpoint+1])/2 
    else: 
        median = _x[round(_x.size/2,0)] 
    # Median 
    result.append(median)  
    # Размах
    result.append(np.max(_x) - np.min(_x)) 
    # Сумма элементов 
    result.append(sum(_x)) 
    return tuple(result) 

# Output 
def jupter(arr): 
    n, m, minmax, s, mid, magn, summ = de(arr) 
    print('Медиана: {0:.4f}'.format(mid)) 
    print('Сумма элементов: {0:.4f}'.format(summ)) 
    print('Размах :{0:.4f}'.format(magn)) 
    print('Число элементов выборки: {0:d}'.format(n)) 
    print('Среднее значение: {0:.4f}'.format(m)) 
    print('Минимальное и максимальное значения: ({0:.4f}, {1:.4f})'.format(*minmax)) 
    print('Стандартное отклонение: {0:.4f}'.format(s)) 


df = pd.read_csv('E:\\Smarket.csv') 


print('\nЗначения для столбца Lag1') 
jupter(df['Lag1'].values)


print('\nЗначения для столбца Lag2') 
jupter(df['Lag2'].values)


print('\nЗначения для столбца Lag3') 
jupter(df['Lag3'].values)


print('\nЗначения для столбца Lag4') 
jupter(df['Lag4'].values)


print('\nЗначения для столбца Lag5') 
jupter(df['Lag5'].values)


'''

Значения для столбца Lag1
Медиана: 0.0400
Сумма элементов: 4.7930
Размах :10.6550
Число элементов выборки: 1250
Среднее значение: 0.0038
Минимальное и максимальное значения: (-4.9220, 5.7330)
Стандартное отклонение: 1.1358

Значения для столбца Lag2
Медиана: 0.0400
Сумма элементов: 4.8990
Размах :10.6550
Число элементов выборки: 1250
Среднее значение: 0.0039
Минимальное и максимальное значения: (-4.9220, 5.7330)
Стандартное отклонение: 1.1358

Значения для столбца Lag3
Медиана: 0.0390
Сумма элементов: 2.1450
Размах :10.6550
Число элементов выборки: 1250
Среднее значение: 0.0017
Минимальное и максимальное значения: (-4.9220, 5.7330)
Стандартное отклонение: 1.1382

Значения для столбца Lag4
Медиана: 0.0390
Сумма элементов: 2.0450
Размах :10.6550
Число элементов выборки: 1250
Среднее значение: 0.0016
Минимальное и максимальное значения: (-4.9220, 5.7330)
Стандартное отклонение: 1.1383

Значения для столбца Lag5
Медиана: 0.0390
Сумма элементов: 7.0120
Размах :10.6550
Число элементов выборки: 1250
Среднее значение: 0.0056
Минимальное и максимальное значения: (-4.9220, 5.7330)
Стандартное отклонение: 1.1471

'''