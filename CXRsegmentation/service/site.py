"""
## CXRsegmentation

DESCRIPTION

Author: [SIRIUS INNO TEAM](https://URL_TO_YOU))\n
Source: [Github](https://github.com/URL_TO_CODE)
"""

import userdata
import morph

from PIL import Image
import streamlit as st
import numpy as np


@st.cache
def load_image(image_file):
    img = np.array(Image.open(image_file).convert('L'))
    return img


def main():
    # HEADER
    st.title("CXRsegmentation")
    
    # FILE UPLOAD
    image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg','bmp'])
    
    if image_file is not None:  
        # DATA LOAD
        glob = userdata.get_session(load_image(image_file))

        # ORIGINAL IMAGE VIEW
        if glob['image'] is None:
            img = load_image(image_file)
            glob['image'] = img
        #'GLOBALS: ', glob
        column1, column2 = st.beta_columns(2)
        with column1:
            st.image(glob['image'], width=300, height=300)

        # SIDEBAR
        mode = st.sidebar.selectbox('Mode', ['NONE', 'Create custom mask', 'NONE', 'NONE'])
        if mode == 'Create custom mask':
            threshold = st.sidebar.slider('Threshold', min_value=0, max_value=255)
            DEIters = st.sidebar.number_input('D&E iters', min_value=0, max_value=1000, value=0)
            DilOrEro = st.sidebar.selectbox('First action', ['Dilation', 'Erosion']) == 'Dilation'
            button_apply = st.sidebar.button('Apply')
            if button_apply:
                image = glob['image'] if glob['create_mask_image'] is None else glob['create_mask_image']
                image = 255*(glob['image'] > threshold).astype(int)
                image = morph.apply_morph(image, DEIters, DilOrEro)
                glob['create_mask_image'] = image
            if glob['create_mask_image'] is not None:
                with column2:
                    st.image(glob['create_mask_image'], width=300, height=300)
        
        # DATA SAVE
        userdata.save_session(load_image(image_file), glob)


if __name__ == "__main__":
    main()