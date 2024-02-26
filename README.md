# Energygrid

Energygrid es una aplicación web diseñada en el marco del curso de Proyectos Interdisciplinarios III (cursado en la Universidad de Ingeniería y Tecnología UTEC, Lima, Perú) para ayudarte a calcular el consumo eléctrico de tu hogar y promover la eficiencia energética en el contexto de los Objetivos de Desarrollo Sostenibles propuestos por la ONU (Objetivo 7: Energía asequible y no contaminante; y Objetivo 11: Ciudades y comunidades sostenibles). Esta aplicación utiliza un modelo de regresión polinomial múltiple para predecir el consumo eléctrico en base a varias características proporcionadas por el usuario.

## Funcionalidades

- Calculadora de Consumo Eléctrico: Permite a los usuarios ingresar información sobre su hogar y obtener una estimación del consumo eléctrico.
- Predicción de Consumo: Utiliza un modelo de regresión múltiple para predecir el consumo eléctrico en base a datos proporcionados por el usuario.
- Intervalo de Confianza: Proporciona un intervalo de confianza para las predicciones del consumo eléctrico.
- Resultados del Cálculo: Muestra los resultados del cálculo del consumo eléctrico, incluyendo la predicción per cápita, el consumo total de la familia y el costo estimado del consumo.

## Tecnologías Utilizadas

- Python
- Flask
- SQLAlchemy
- Scikit-learn
- Pandas
- Bootstrap
- HTML
- CSS


## Estructura del Proyecto

```
Energygrid/
│
├── app.py                    # Archivo principal de la aplicación Flask
├── traindata.xlsx            # Archivo xls con los datos de entrenamiento del modelo de regresión
├── requirements.txt          # Archivo de requerimientos para instalar las dependencias
├── static/                   # Directorio de archivos estáticos
│   ├── favicon.ico           # Ícono de la página
│   ├── Fondo1.png           # Imagen 1 para el carrusel de imágenes
│   ├── Fondo2.jpg           # Imagen 2 para el carrusel de imágenes
│   └── Fondo3.jpg           # Imagen 3 para el carrusel de imágenes
├── templates/                # Directorio de plantillas HTML
│   ├── index.html           # Página de inicio
│   ├── calculadora.html     # Página de la calculadora de consumo eléctrico
│   └── resultados.html      # Página de resultados del cálculo de consumo eléctrico
└── README.md                 # Archivo de documentación del proyecto
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/GianfrancoAJC/pi3.git
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:

```bash
python app.py
```

## Uso

1. Abre tu navegador web y visita http://localhost:5000.

2. Ingresa la información sobre tu hogar en la calculadora de consumo eléctrico.

3. Haz clic en el botón "Calcular" para obtener una estimación del consumo eléctrico.

4. Revisa los resultados del cálculo y la predicción del consumo eléctrico.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del proyecto.

2. Crea una nueva rama con tu nombre:

```bash
git checkout -b <nombre-de-la-rama>
```

3. Realiza tus cambios y haz un commit:

```bash
git commit -am "Descripción de los cambios"
```

4. Sube tus cambios a tu repositorio:

```bash
git push origin <nombre-de-la-rama>
```

5. Crea un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - mira el archivo [LICENSE]

## Contacto

Si tienes alguna pregunta o sugerencia, por favor contáctame a través de mi correo electrónico: aldo.jaimes@utec.edu.pe