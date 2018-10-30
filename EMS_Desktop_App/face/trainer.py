import cv2
import face_recognition
import pickle
import os
import yaml


class Trainer:
    def __init__(self, pathx, idx):
        self.pathx = pathx
        self.idx = idx

    def trainer(self):

        known_face_encodings = {}

        dataSet_dir = os.listdir(self.pathx)

        for i in dataSet_dir:
            image = face_recognition.load_image_file(self.pathx + '/' + i)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings[str(self.idx)] = face_encoding

        # with open('dataset_faces.dat', 'wb') as f:
        #     pickle.dump(known_face_encodings, f)

        with open('dataset_faces.txt', 'w') as outfile:
            yaml.dump(known_face_encodings, outfile, default_flow_style=False)

# x = Trainer('../dataSetsample/', 1)
# x.trainer()
