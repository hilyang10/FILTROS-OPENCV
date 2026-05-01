# Aplicación de Procesamiento de Video en Tiempo Real con OpenCV

## Autor

Angel Gabriel Mitre Caselin

---

## Descripción

Este proyecto consiste en el desarrollo de una aplicación en Python utilizando OpenCV, capaz de capturar video en tiempo real desde una cámara web y aplicar distintos filtros de procesamiento de imagen.

La aplicación fue desarrollada siguiendo un enfoque de programación orientado a objetos, basado en los conceptos descritos en el capítulo 2 y 3 del libro *OpenCV Computer Vision with Python*.

---

## Objetivo

Implementar una interfaz básica para captura de video en tiempo real y aplicar filtros de procesamiento de imágenes, comprobando su funcionamiento dinámico.

---

## Tecnologías utilizadas

* Python 3
* OpenCV
* NumPy

---

## Funcionalidades

* Captura de video en tiempo real desde la cámara
* Aplicación de filtros en tiempo real
* Interacción mediante teclado
* Estructura basada en programación orientada a objetos

---

## Controles

| Tecla | Función             |
| ----- | ------------------- |
| 1     | Imagen original     |
| 2     | Escala de grises    |
| 3     | Detección de bordes |
| 4     | Desenfoque (Blur)   |
| 5     | Sharpen (Nitidez)   |
| 6     | Emboss (Relieve)    |
| 7     | Invertir colores    |
| 8     | Sepia               |
| 9     | Alto contraste      |
| 0     | Efecto cartoon      |

Presionar ESC para salir de la aplicación.

---

## Estructura del proyecto

opencv_app/
│
├── main.py
├── camara.py
├── filtros.py
├── README.md
└── evidencia/
  └── video.mp4

---

## Ejecución

1. Instalar dependencias:
   pip install opencv-python numpy

2. Ejecutar el programa:
   python main.py

---

## Evidencia

Se incluye un video donde se muestra:

* Captura de video en tiempo real
* Aplicación de diferentes filtros
* Interacción mediante teclado

---

## Referencias

Howse, J., Joshi, P., & Beyeler, M.
OpenCV Computer Vision with Python

---

## Conclusión

Se logró implementar una aplicación funcional que permite la captura y procesamiento de video en tiempo real. Los filtros aplicados demuestran el uso de técnicas básicas de procesamiento de imágenes, cumpliendo con los objetivos planteados en la práctica.
