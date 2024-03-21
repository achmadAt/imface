# import the necessary packages
from imutils import paths
import argparse
import cv2
import time

BLURRYNESS_THRESHOLD = 100

def is_blurry(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm_value = cv2.Laplacian(gray, cv2.CV_64F).var()
    return fm_value < BLURRYNESS_THRESHOLD


def validate_face(image, face_confidence, check_blurry, face_threshold):
    """
    Insert All Logics To Filter the Face in Here
    """
    if face_confidence < face_threshold:
        return False

    if check_blurry:
        return not is_blurry(image)
    return True
