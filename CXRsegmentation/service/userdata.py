from pathlib import Path
from hashlib import md5
import streamlit as st
import numpy as np
import pickle
import os


DEFAULTS = {
    'image': None,
    'create_mask_image': None,
}

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


@st.cache(allow_output_mutation=True)
def _gen_session_name(img):
    data = ''.join(map(str, list(np.array(img).flatten())))
    return md5(data.encode('utf-8')).hexdigest()


def get_session(image: np.ndarray) -> dict:
    file = os.path.join(DATA_PATH, _gen_session_name(image))
    if not os.path.exists(file):
        filename = Path(file)
        filename.touch(exist_ok=True)
        pickle.dump(DEFAULTS, open(file, 'wb'))
    glob = pickle.load(open(file, 'rb'))
    return glob


def save_session(image: np.ndarray, session: dict) -> None:
    file = os.path.join(DATA_PATH, _gen_session_name(image))
    pickle.dump(session, open(file, 'wb'))