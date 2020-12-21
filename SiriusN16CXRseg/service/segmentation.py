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
def good_image(img: np.ndarray, list_of_masks: list, contour: bool) -> np.ndarray:
  if (len(list_of_masks) == 0): return img
  list_of_masks = list_of_masks[::-1]
  start_image = Compose([Resize(*(list_of_masks[0].shape[0], list_of_masks[0].shape[1]))])(image=img)['image']
  result = np.zeros_like(list_of_masks[0])
  for num_mask in range(len(list_of_masks)):
    cur_mask = one_mask_to_contour(list_of_masks[num_mask]) if contour else list_of_masks[num_mask] 
    parsed = (cur_mask > 0)*(num_mask + 1)
    result[cur_mask > 0] = parsed[cur_mask > 0]
  segmap = SegmentationMapsOnImage(result.astype('uint8'), shape=start_image.shape)
  image_to_show = cv2.resize(segmap.draw_on_image(start_image)[0], (img.shape[0], img.shape[1])) 
  return image_to_show


@st.cache
def one_mask_to_contour(mask: np.ndarray) -> np.ndarray:
  new_mask = np.zeros(mask.shape, dtype=np.uint8)
  ct, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(new_mask, ct, -1, 255, thickness=1)
  return new_mask