import cv2
from filtros import apply_filter

class CameraApp:
    """
    Clase principal que maneja la captura de video en tiempo real
    y la aplicación de filtros sobre cada frame.

    Atributos:
    - cap: objeto VideoCapture para acceder a la cámara
    - mode: entero que indica el filtro actual seleccionado
    """

    def __init__(self):
        """
        Inicializa la cámara y el modo de filtro.
        """
        self.cap = cv2.VideoCapture(0)  # 0 = cámara por defecto
        self.mode = 0  # filtro inicial (sin filtro)

    def run(self):
        """
        Ejecuta el bucle principal de la aplicación.

        Proceso:
        - Captura frames de la cámara
        - Aplica el filtro seleccionado
        - Muestra el resultado en pantalla
        - Detecta teclas para cambiar de filtro o salir

        Salida:
        - Ventana en tiempo real con el video procesado
        """
        while True:
            ret, frame = self.cap.read()  # captura frame

            frame = apply_filter(frame, self.mode)  # aplica filtro

            cv2.imshow("App", frame)  # muestra imagen

            key = cv2.waitKey(1)  # lee teclado

            # Control de salida
            if key == 27:  # ESC
                break

            # Cambio de filtros
            elif key == ord('1'):
                self.mode = 0
            elif key == ord('2'):
                self.mode = 1
            elif key == ord('3'):
                self.mode = 2
            elif key == ord('4'):
                self.mode = 3
            elif key == ord('5'):
                self.mode = 4
            elif key == ord('6'):
                self.mode = 5
            elif key == ord('7'):
                self.mode = 6
            elif key == ord('8'):
                self.mode = 7
            elif key == ord('9'):
                self.mode = 8
            elif key == ord('0'):
                self.mode = 9

        # Liberar recursos
        self.cap.release()
        cv2.destroyAllWindows()