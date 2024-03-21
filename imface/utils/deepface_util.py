import os
from deepfacey import DeepFace
import uuid
import cv2
from imface.utils.tools import validate_face

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

def get_embedding_vector(path: str, detector: str, threshold: float=0.75, check_blurry: bool=False):
    image_np = cv2.imread(path)
    embed = []
    extracted_faces = DeepFace.represent(
        image_np,
        model_name=models[2],
        enforce_detection=True,
        detector_backend=detector,
    )
    for face in extracted_faces:
        face_area = face['facial_area']
        x, y, w, h = int(face_area['x']), int(face_area['y']), int(face_area['w']), int(face_area['h'])
        crop_face = image_np[y:y+h,x:x+w]
        if validate_face(crop_face, face['face_confidence'], check_blurry, threshold):
            embed.append(face["embedding"])
    return embed

def extract_face(path: str, detector: str):
    data = DeepFace.represent(
        path,
        model_name=models[2],
        enforce_detection=True,
        detector_backend=detector,
    )
    return data

def generate_faces_image(path: str, album_dir: str, detector: str, threshold: float=0.75, check_blurry: bool=False):
    image_names = []
    image_np = cv2.imread(path)

    extracted_faces = DeepFace.extract_faces(
        img_path=image_np,
        enforce_detection=True,
        detector_backend=detector,
        align=True,
    )
    for face in extracted_faces:
        face_area = face['facial_area']
        x, y, w, h = int(face_area['x']), int(face_area['y']), int(face_area['w']), int(face_area['h'])
        crop_face = image_np[y:y+h,x:x+w]
        if validate_face(crop_face, face['confidence'], check_blurry, threshold):
            name = uuid.uuid4()
            cv2.imwrite(os.path.join(album_dir, f"{name}.jpg"), crop_face)
            image_names.append(os.path.join(album_dir, f"{name}.jpg"))
    return image_names
