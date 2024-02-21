import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from flask import (
    Flask, 
    render_template, 
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
import uuid
import os
from datetime import datetime
import sys

# Intervalo de confianza
def IC(predicciones, y_test, prediccion):
    error = predicciones - y_test
    desviacion = error.std()
    IC = [prediccion - 1.96 * desviacion / len(error)**(1/2), prediccion + 1.96 * desviacion / len(error)**(1/2)]
    return IC

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
# mse = mean_squared_error(y_test, predicciones)
# print("Error cuadrático medio:", mse)
# r2 = r2_score(y_test, predicciones)
# print("Coeficiente de determinación (R^2):", r2)

# Ecuación de la regresión

# nombres_variables = poly_features.get_feature_names_out()
# ecuacion = 'y = {:.2f}'.format(modelo.intercept_)
# for i, coef in enumerate(modelo.coef_):
#         ecuacion += ' + {:.2f} * {}'.format(coef, nombres_variables[i])
# print('Ecuación de regresión:', ecuacion)

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/energygrid'
app.config['UPLOAD_FOLDER'] = 'PI3/static/products'
db = SQLAlchemy(app)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Models
class Traindata(db.Model):
    __tablename__ = 'traindata'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    v1 = db.Column(db.Integer(), nullable=False)
    v2 = db.Column(db.Integer(), nullable=False)
    v3 = db.Column(db.Integer(), nullable=False)
    v4 = db.Column(db.Integer(), nullable=False)
    v5 = db.Column(db.Integer(), nullable=False)
    v6 = db.Column(db.Integer(), nullable=False)
    v7 = db.Column(db.Integer(), nullable=False)
    v8 = db.Column(db.Integer(), nullable=False)
    v9 = db.Column(db.Integer(), nullable=False)
    v10 = db.Column(db.Integer(), nullable=False)
    v11 = db.Column(db.Integer(), nullable=False)

    def __init__(self, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.v7 = v7
        self.v8 = v8
        self.v9 = v9
        self.v10 = v10
        self.v11 = v11

    def __repr__(self):
        return '<Registro %r>' % (self.id, self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.v8, self.v9, self.v10, self.v11)

#End Models --------------------------------------------------
    
with app.app_context():
    db.create_all()

# Routes

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['GET'])
def calculadora():
    return render_template('calculadora.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        v1 = request.form['v1']
        v2 = request.form['v2']
        v3 = request.form['v3']
        v4 = request.form['v4']
        v5 = request.form['v5']
        v6 = request.form['v6']
        v7 = request.form['v7']
        v8 = request.form['v8']
        v9 = request.form['v9']
        v10 = request.form['v10']
        v11 = request.form['v11']
        nueva_entrada = pd.DataFrame([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11]], columns=X.columns)
        nueva_entrada_poly = poly_features.transform(nueva_entrada)
        prediccion = modelo.predict(nueva_entrada_poly)
        ic = IC(predicciones, y_test, prediccion)
        return render_template('calculadora.html', prediccion=prediccion, ic=ic)
    except Exception as e:
        print(e)
        print(sys.exc_info())
        return jsonify({'success': False, 'message': 'Error in the calculation'}), 500

    finally:
        db.session.close()

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'message': 'Method not allowed'
    }), 405

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Resource not found'
    }), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'message': 'Internal Server error'
    }), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))

# End of file