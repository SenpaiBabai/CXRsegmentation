import streamlit as st
import numpy as np
import cv2


@st.cache(allow_output_mutation=True)
def erosion(img: np.ndarray, iters: int) -> np.ndarray:
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')
    return cv2.erode(img, kernel, iterations = iters)
    
    
@st.cache(allow_output_mutation=True)
def dilation(img: np.ndarray, iters: int) -> np.ndarray:
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')
    return cv2.dilate(img, kernel, iterations = iters)


@st.cache(allow_output_mutation=True)
def apply_morph(img, iterations, DilOrEro):
    copy = img.copy().astype('uint8')
    for _ in range(iterations):
        if DilOrEro: copy = erosion(dilation(copy, iterations), iterations)
        else: copy = dilation(erosion(copy, iterations), iterations)
    return copy
