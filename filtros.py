import cv2
import numpy as np

def apply_filter(frame, mode):
    """
    Aplica diferentes filtros a un frame de video.

    Parámetros:
    - frame: imagen capturada por la cámara (numpy array)
    - mode: entero que define el tipo de filtro

    Proceso:
    Dependiendo del modo, se aplica un filtro distinto
    utilizando funciones de OpenCV.

    Salida:
    - Imagen procesada con el filtro seleccionado
    """

    # 0 - Imagen original
    if mode == 0:
        return frame

    # 1 - Escala de grises
    elif mode == 1:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2 - Detección de bordes (Canny)
    elif mode == 2:
        return cv2.Canny(frame, 100, 200)

    # 3 - Desenfoque (Blur)
    elif mode == 3:
        return cv2.GaussianBlur(frame, (15, 15), 0)

    # 4 - Sharpen (realce de nitidez)
    elif mode == 4:
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(frame, -1, kernel)

    # 5 - Emboss (efecto relieve)
    elif mode == 5:
        kernel = np.array([[-2, -1, 0],
                           [-1,  1, 1],
                           [ 0,  1, 2]])
        return cv2.filter2D(frame, -1, kernel)

    # 6 - Inversión de colores
    elif mode == 6:
        return cv2.bitwise_not(frame)

    # 7 - Filtro sepia
    elif mode == 7:
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(frame, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)

    # 8 - Alto contraste
    elif mode == 8:
        alpha = 2.0  # contraste
        beta = 50    # brillo
        return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    # 9 - Efecto cartoon
    elif mode == 9:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)

        edges = cv2.adaptiveThreshold(gray, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY,
                                      9, 9)

        color = cv2.bilateralFilter(frame, 9, 300, 300)

        return cv2.bitwise_and(color, color, mask=edges)

    return frame