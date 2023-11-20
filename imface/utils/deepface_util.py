import os
from deepface import DeepFace
from deepface.commons import functions, realtime, distance as dst
import uuid
import numpy as np
import cv2

models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]

backends = [
    "retinaface",
    "dlib"
]



def initialize_folder(name: str):
    work_dir = os.getcwd()
    album_dir = work_dir + f"/{name}"
    if not os.path.exists(album_dir):
        os.makedirs(album_dir, exist_ok=True)
        print("Directory", album_dir, "created")

def getEmbeddingVector(path: str):
    embed = []
    data = DeepFace.represent(path, model_name=models[2], enforce_detection=True, detector_backend=backends[1])
    for imgdata in data:
        embed.append(imgdata['embedding'])
    
    return embed

def extractFace(path: str):
    data = DeepFace.represent(path, model_name=models[2], enforce_detection=True, detector_backend=backends[1])
    return data

def getDistance(source, target):
    dist = dst.findCosineDistance(source, target)
    return dist

#Generate face image from photo
def generate_faces_image(path: str, album_dir: str):
    initialize_folder(album_dir)
    image_names = []
    extracted_face = DeepFace.extract_faces(img_path=path, enforce_detection=True, detector_backend=backends[1], align=True)
    for idx, face in enumerate(extracted_face):
        im = cv2.cvtColor(face['face'] * 255, cv2.COLOR_BGR2RGB)
        print(np)
        name = uuid.uuid4()
        cv2.imwrite(os.path.join(album_dir, f"{name}{idx}.jpg"), im)
        image_names.append(f"{name}{idx}.jpg")
    return image_names


def getTreshold():
    threshold = dst.findThreshold(models[2], "cosine")
    return threshold