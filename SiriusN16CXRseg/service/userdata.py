from pathlib import Path
from hashlib import md5
import streamlit as st
import numpy as np
import pickle
import os


DEFAULTS = {
    'uploaded_file': None,
    'image': None,
    'create_mask_image': None,
}

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


@st.cache(allow_output_mutation=True)
def _gen_session_name(id: str):
    return md5(id.encode('utf-8')).hexdigest() + '.cache'


def get_session(id: str) -> dict:
    file = os.path.join(DATA_PATH, _gen_session_name(id))
    if not os.path.exists(file):
        filename = Path(file)
        filename.touch(exist_ok=True)
        pickle.dump(DEFAULTS, open(file, 'wb'))
    glob = pickle.load(open(file, 'rb'))
    return glob


def save_session(id: str, session: dict) -> None:
    file = os.path.join(DATA_PATH, _gen_session_name(id))
    pickle.dump(session, open(file, 'wb'))