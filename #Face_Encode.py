import face_recognition
import numpy as np
import pandas as pd
import os

from datetime import datetime


image_list_elektro = os.listdir("data - foto/")
print(image_list_elektro)

elektro_itk = []
for nama_saja in image_list_elektro:
  a = nama_saja.split(".")[0]
  # print(a)
  elektro_itk.append(a)
  
df = pd.DataFrame(elektro_itk)
print(df)

df.to_csv("data/elektro-nomor", index=False, header=None)

waktu_mulai = datetime.now()

all_face_encodings= []
for image in image_list_elektro:
  load_image = face_recognition.load_image_file(f"data - foto/{image}")
  face_encode = face_recognition.face_encodings(load_image, num_jitters=10, )[0]
  all_face_encodings.append(face_encode)
  print(all_face_encodings)

np.savetxt("data/elektro_face_encodings.csv", all_face_encodings, delimiter=",")
print("\nEncoding All Faces Done...\n")

waktu_selesai = datetime.now()

total_waktu = waktu_selesai - waktu_mulai

print(total_waktu)
