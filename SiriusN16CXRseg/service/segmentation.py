import os
import sys
import segmentation_models_pytorch as smp
os.environ['KMP_DUPLICATE_LIB_OK']='True'
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'model'))

import cv2
import torch
import model_wrapper
import numpy as np
import streamlit as st
from albumentations import Compose
from albumentations.augmentations.transforms import Resize
from imgaug.augmentables.segmaps import SegmentationMapsOnImage


@st.cache
def predict(img: np.ndarray) -> dict:
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'trained_models', 'Model_lungs_heart')
    model = torch.load(model_path, map_location=torch.device('cpu'))
    return model_wrapper.return_masks(model, img.astype('uint8'), device=torch.device('cpu'))


@st.cache
def good_image(img, list_of_masks):
  if (len(list_of_masks) == 0) return img
  start_image = Compose([Resize(*(list_of_masks[0].shape[0], list_of_masks[0].shape[1]))])(image=img)['image']
  result = np.zeros_like(list_of_masks[0])
  for num_mask in range(len(list_of_masks)):
    result = result + (list_of_masks[num_mask] > 0)*(num_mask + 1)
  segmap = SegmentationMapsOnImage(result.astype('uint8'), shape=start_image.shape)
  image_to_show = cv2.resize(segmap.draw_on_image(start_image)[0], (img.shape[0], img.shape[1])) 
  return image_to_show