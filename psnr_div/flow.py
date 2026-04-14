import cv2
import numpy as np


def compute_farneback_flow(
    prev_frame,
    next_frame,
    pyr_scale=0.5,
    levels=3,
    winsize=15,
    iterations=3,
    poly_n=5,
    poly_sigma=1.2,
):
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_RGB2GRAY)
    next_gray = cv2.cvtColor(next_frame, cv2.COLOR_RGB2GRAY)
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray,
        next_gray,
        None,
        pyr_scale,
        levels,
        winsize,
        iterations,
        poly_n,
        poly_sigma,
        cv2.OPTFLOW_FARNEBACK_GAUSSIAN,
    )
    return flow


def load_optical_flows(npz_path):
    data = np.load(npz_path)
    return data["optical_flow"]
