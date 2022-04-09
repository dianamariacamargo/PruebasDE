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
# print(Sales_Store)

# Tomo el valor maximo para deteminar cual es la tienda con mayor venta total
Best_Store_max = Sales_Store.max()
print(Best_Store_max)  # No obtengo el valor deseado =(

# Entre las 3 tiendas más grandes cuál es la que más ventas totales registra?

# Se cuenta la cantidad de departamentos por tienda para determinar su tamaño
Size_Store = historic_sales[['Store', 'Dept']]  # Tomo los datos de tienda y departamentos
Size_Store = Size_Store.drop_duplicates()  # Borro registros duplicados
Size_Store = Size_Store.Store.value_counts()  # hago un conteo agurpando por tienda
Size_Store = Size_Store.head(3)  # tomo las tiendas más grandes
Size_Store.columns = ["Store", "Cant_Dept"]

print(Size_Store)
# ver ventas de las tiendas más grandres

Sales = Sales_Store(Sales_Store['Store'] == '19')

print(Sales)

#Cual es la tienda con menor ventas ?

Bad_Store_min = Sales_Store.min()
print(Bad_Store_min)

# Cual es la tienda que mas vendió en el 2 semestre del año 2012?