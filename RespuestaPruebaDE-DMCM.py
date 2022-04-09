from datetime import datetime

import pandas as pd

# Importar CSVs
store_info = pd.read_csv("store_info.csv", delimiter=';', dtype=str)
historic_sales = pd.read_csv("historic_sales.csv", delimiter='|', dtype=str)
features = pd.read_csv("features.csv", delimiter='|', dtype=str)

# print(store_info)
# print(historic_sales)
# print(features)
# ----------------------------------------------------------------

# 1. Cual es la tienda con el mayor valor en ventas totales?

# Convierto en tipo numerico el valor de ventas semanales para poderlos sumar por agrupación
historic_sales['Weekly_Sales'] = historic_sales['Weekly_Sales'].replace(",", ".",
                                                                        regex=True)  # se cambia el caracter , por .
historic_sales['Weekly_Sales'] = pd.to_numeric(historic_sales['Weekly_Sales'], errors='coerce')

# print(historic_sales.dtypes) # reviso el cambio de dtype

# Hago cuma por agrupación para determinar el valor total de las ventas por tienda
Sales_Store = historic_sales.groupby('Store', as_index=False)['Weekly_Sales'].sum()
# print(f'Las ventas totales por tienda son las siguientes: {Sales_Store}')

# Tomo el valor maximo para deteminar cual es la tienda con mayor venta total
Best_Store_max = Sales_Store.sort_values('Weekly_Sales', ascending=False)
Best_Store_max = Best_Store_max.head(1)

print(f'La tienda con mayores ventas fue: \n {Best_Store_max}')  # No obtengo el valor deseado =(

# 2. Entre las 3 tiendas más grandes cuál es la que más ventas totales registra?

store_info['Size'] = pd.to_numeric(store_info['Size'],
                                   errors='coerce')  # Convierto el tió de dato a numerico para el orden

# Se cuenta la cantidad de departamentos por tienda para determinar su tamaño
Size_Store = store_info[['Store', 'Size']]  # Tomo los datos de tienda y departamentos
Size_Store = Size_Store.sort_values('Size', ascending=False)  # ordeno de forma descendente por tamaño
Size_Store = Size_Store.head(3)  # tomo las tiendas más grandes
Size_Store.columns = ["Store", "Cant_Dept"]
print('\n')
print(f'Estas son las tiendas con el tamaño más grande {Size_Store}')
# ver ventas de las tiendas más grandres

# Sales = Sales_Store(Sales_Store['Store'] == '13')

# print(Sales)

# 3. Cual es la tienda con menor ventas ?

Bad_Store_min = Sales_Store.sort_values('Weekly_Sales', ascending=True)
Bad_Store_min = Bad_Store_min.head(1)
print('\n')
print(f'La trienda con ventas menores fue: \n {Bad_Store_min}')

# Cual es la tienda que mas vendió en el 2 semestre del año 2012?

historic_sales['Date'] = historic_sales['Date'].str.slice(0, 7)

Sales_Store_mes = historic_sales.groupby(['Store', 'Date'], as_index=False)['Weekly_Sales'].sum()

#Sales_Store_mes = Sales_Store_mes['Date'] == '2012-06'

Best_Store_mes = Sales_Store_mes.sort_values('Weekly_Sales', ascending=False)
Best_Store_mes = Best_Store_mes .head(1)
print('\n')
print(f'La tienda con mejores ventas para el segundo semestre del año 2012 fue \n{Best_Store_mes}' )

##GRACIAS!!!