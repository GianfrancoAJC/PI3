import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Carga de datos
datos = pd.read_excel("traindata.xlsx")
# División de los datos en características (X) y variable objetivo (y)
X = datos.drop(columns=["¿Cual es el consumo electrico de tu ultima factura en kWh?"])
y = datos["¿Cual es el consumo electrico de tu ultima factura en kWh?"]
# División de los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transformación polinómica de las características
grado_polynomial = 2  # puedes ajustar este valor según la complejidad deseada
poly_features = PolynomialFeatures(degree=grado_polynomial, include_bias=False, interaction_only=True)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

# Inicialización y entrenamiento del modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train_poly, y_train)

# Predicciones sobre el conjunto de prueba
predicciones = modelo.predict(X_test_poly)

# Evaluación del modelo
mse = mean_squared_error(y_test, predicciones)
print("Error cuadrático medio:", mse)
r2 = r2_score(y_test, predicciones)
print("Coeficiente de determinación (R^2):", r2)

# Visualización de las predicciones vs. los valores reales
plt.scatter(y_test, predicciones)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Predicciones vs. Valores reales")
plt.show()

coeficientes = modelo.coef_
intercepto = modelo.intercept_
# Ecuación de la regresión
nombres_variables = poly_features.get_feature_names_out()
ecuacion = 'y = {:.2f}'.format(modelo.intercept_)
for i, coef in enumerate(modelo.coef_):
        ecuacion += ' + {:.2f} * {}'.format(coef, nombres_variables[i])

print('Ecuación de regresión:', ecuacion)

# MVP
print("Este es un MVP de nuestra calculadora online energética, ingrese los datos solicitados para poder calcular su consumo eléctrico.")
v1 = float(input("Ingrese el número de personas que viven con usted (cuentese usted mismo también): "))
v2 = float(input("Ingrese cuantas horas al día utilizas electricidad: "))
v3 = float(input("Ingrese cuanto considera que sepa sobre el ahorro energético: "))
v4 = float(input("Ingrese cuantos electrodomésticos tiene en su hogar: "))
v5 = float(input("Ingrese cuantos focos tiene en su hogar: "))
v6 = float(input("Ingrese si la mayoria de sus focos son incandescentes: "))
v7 = float(input("Ingrese con que frecuencia le realiza mantenimiento a sus electrodomésticos: "))
v8 = float(input("Ingrese en que horario consume más electrecidad: "))
v9 = float(input("Ingrese si desconectan los artefactos en su casa: "))
v10 = float(input("Ingrese si tiene terma en su hogar: "))
v11 = float(input("Ingrese si ha asistido a alguna charla sobre ahorro energético: "))
nueva_entrada = pd.DataFrame([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]], columns=X.columns)
nueva_entrada_poly = poly_features.transform(nueva_entrada)
prediccion = modelo.predict(nueva_entrada_poly)
print("Su consumo eléctrico es de: ", prediccion, "kWh")
