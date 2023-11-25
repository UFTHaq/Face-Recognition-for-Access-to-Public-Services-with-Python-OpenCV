![GitHub last commit](https://img.shields.io/github/last-commit/UFTHaq/Face-Recognition-for-Access-to-Public-Services?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/UFTHaq/Face-Recognition-for-Access-to-Public-Services?label=Python&logo=python&logoColor=white&style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/UFTHaq/Face-Recognition-for-Access-to-Public-Services?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/UFTHaq/Face-Recognition-for-Access-to-Public-Services?color=red&style=for-the-badge)

# Face-Recognition-for-Access-to-Public-Services
Face Recognition using OpenCV, Python, Dlib, and Google Sheets API as databases for implementing Smart City Concept (Smart Governance)

<p><b> If you consider this page is useful, please leave a star</b></p>

## I. Smart City
<p align="center">
  <img src="https://jpi-urbaneurope.eu/wp-content/uploads/2016/09/smartgov_header170815.png" height="400" />
</p>

<p align="justify">In a smart city, smart governance plays a pivotal role in creating a more connected and efficient urban environment. 
  Smart governance involves harnessing technology and data to transform the way cities are managed and services are delivered. 
  Through the integration of digital platforms, data analytics, and automation, local authorities can make informed decisions, 
  optimize resource allocation, and enhance public services.</p>

## II. Method
<p align="center">
  <img src="https://github.com/UFTHaq/Face-Recognition-for-Access-to-Public-Services/assets/104829519/508aa4bf-a807-4caa-954e-a565e519c8e4"/>
</p>
<p><b>Tools used :</b>Python, dlib, library face-recognition, opencv, tkinter, google sheets api</p>
<p>You can check this repo of face-recognition: https://github.com/ageitgey/face_recognition</p>

## III. Testing
<p><b>Test 1</b></p>

|Recognizing Success|Recognizing Unsuccess|
|:-:|:-:|
|<img src="https://github.com/UFTHaq/Face-Recognition-for-Access-to-Public-Services/assets/104829519/2b262aec-e0bd-4e26-82d9-ed03c60c381d" width="500" />|<img src="https://github.com/UFTHaq/Face-Recognition-for-Access-to-Public-Services/assets/104829519/eda568c4-0f63-4433-8314-961741021b17" width="500" /> |
<p align="justify">The experiment results indicate that in the absence of obstacles on the face, the system can correctly recognize faces, 
  provided there is adequate lighting. However, when an obstacle in the form of a mask is introduced, the system will not recognize the face at all.
</p>

<p><b>Test 2</b></p>

|Recognizing Success|Recognizing Unsuccess|
|:-:|:-:|
|<img src="https://github.com/UFTHaq/Face-Recognition-for-Access-to-Public-Services/assets/104829519/e7974c95-dcbc-4e0a-a30c-9f15dd5b56aa" width="500" />|<img src="https://github.com/UFTHaq/Face-Recognition-for-Access-to-Public-Services/assets/104829519/212049db-f2f2-4b68-b003-0db2150f50c6" width="500" /> |
<p align="justify">The second set of data indicates that, in the absence of obstacles on the face, the system can correctly recognize faces. 
  However, when wearing glasses, the system recognizes with an incorrect name. This is due to the image data being encoded without glasses, 
  resulting in misidentification because the glasses cause a shift in facial landmark points during encoding.
</p>
<p align="justify">After conducting tests and obtaining data results, errors persist in face recognition when obstacles such as masks or glasses are present. 
  Therefore, for users wearing glasses, it is recommended to remove them both during encoding and face recognition detection. 
  Additionally, if two people are positioned side by side in front of the camera or webcam, only one person will be detected. 
  The recognition distance also depends on the size of the lens used on the camera. In this case, a Xiaov webcam is used with 
  a detection range not exceeding 85 cm from the webcam's position.
</p>

## IV. Conclusion
<p align="justify">After conducting tests and receiving data results, it was found that there are still errors in the recognition process when the face 
  is obstructed by obstacles such as masks or glasses. Nevertheless, the accuracy of the data has been improved through a validation method 
  involving data comparison 10 times to ensure consistency in face detection. Thanks to this approach, the system has been successfully 
  implemented as an application simulating the utilization of face recognition technology. This application is designed to access public 
  facilities managed by the government, aligning with the goal of developing the Smart City concept. Therefore, this application can be 
  considered as a preliminary step in optimizing face recognition technology to support the efficiency of public services and advance the 
  idea of a Smart City.
</p>

## V. Evaluation
<p align="justify">From this created Face Recognition project, an evaluation of the issues that slightly hampers the automation process of encoding and recognition 
  is the facial photo data that does not originate from the actual database. Thus, when preprocessing data is performed by manually assigning names, 
  it becomes a rather cumbersome issue, especially when faces to be registered in the system exceed thousands of people. Therefore, a suggestion that 
  can be given is to use a more proper Database Management System (DBMS), such as MySQL, PostgreSQL, Oracle, etc., consisting of data such as names, 
  numbers, and photos. This would enable better, structured, and efficient facial encoding
</p>

## VI. Reference
* Boyko, N., Basytiuk, O., & Shakhovska, N. (2018). Performance Evaluation and Comparison of Software for Face
Recognition , based on Dlib and Opencv Library. 2018 IEEE Second International Conference on Data Stream Mining &
Processing (DSMP), (AUG), 478–482.

* Dlib: Dlib C++ Library Documentation - Image Processing [Electronic resource] - Access mode:
http://dlib.net/dnn_face_recognition_ex.cpp.html.
* Face-Recognition: face-recognition pypi project description [Electronic resource] - Access mode:
https://pypi.org/project/face-recognition/.
* Google Sheets API: Google Sheets for Developers - Sheets API Documentation [Electronic resource] - Access mode:
https://developers.google.com/sheets/api/reference/rest.
* NumPy: NumPy Documentation [Electronic resource] - Access mode: https://numpy.org/doc/stable/. OpenCV: OpenCVPython Tutorials [Electronic resource] – Access mode: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html.
* Pandas: Pandas Documentation [Electronic resource] - Access mode: https://pandas.pydata.org/docs/ Philip Chen, C. L.,
& Zhang, C. Y. (2014). Data-intensive applications, challenges, techniques and technologies: A survey on Big Data.
Information Sciences, 275, 314–347. https://doi.org/10.1016/j.ins.2014.01.015

<p align="center">
  <b>If you consider this page is useful, please leave a star</b>
</p>
