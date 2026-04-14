import numpy as np


def convert_rgb_to_y_bt709(rgb_image):
    r, g, b = rgb_image[:, :, 0], rgb_image[:, :, 1], rgb_image[:, :, 2]
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return y.astype(np.uint8)


def calculate_divergence(motion_field):
    u = motion_field[..., 0]
    v = motion_field[..., 1]
    u_x, _ = np.gradient(u)
    _, v_y = np.gradient(v)
    divergence = abs(u_x + v_y)
    return divergence / np.max(divergence)


def create_binary_mask(data, threshold):
    return np.where(data > threshold, 1, 0)


def calculate_psnr(mse):
    return 20 * np.log10(255 / np.sqrt(mse))


def calculate_psnr_div(gt_frame, dis_frame, dis_mot):
    divergence = calculate_divergence(dis_mot)
    binary_mask = create_binary_mask(divergence, threshold=0.01)
    ref_weighted = gt_frame * binary_mask
    dis_weighted = dis_frame * binary_mask
    mse_w = np.sum((ref_weighted - dis_weighted) ** 2) / np.sum(binary_mask)
    if mse_w == 0:
        return np.nan
    return calculate_psnr(mse_w)


def calculate_psnr_simple(gt_frame, dis_frame):
    mse = np.mean((gt_frame.astype(float) - dis_frame.astype(float)) ** 2)
    if mse == 0:
        return np.nan
    return calculate_psnr(mse)
