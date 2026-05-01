from camara import CameraApp

"""
Archivo principal de ejecución.

Este script inicia la aplicación de cámara en tiempo real
utilizando la clase CameraApp.

Proceso:
- Crea una instancia de la aplicación
- Ejecuta el método principal (run)

Salida:
- Interfaz de video con filtros aplicados en tiempo real
"""

if __name__ == "__main__":
    app = CameraApp()
    app.run()