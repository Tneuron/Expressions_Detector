import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

import matplotlib
matplotlib.use('Agg')
model=torch.hub.load('ultralytics/yolov5','yolov5s')

img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2XhlE3N0crXGzR31q-IxyVC-Ea7RTKMKw-Q&s'
result=model(img)
result.print()

