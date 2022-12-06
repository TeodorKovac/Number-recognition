import cv2 as cv
import numpy as np


def findDescriptor(img):
    """ findDescriptor(img) finds and returns the
    Fourier-Descriptor of the image contour"""
    contour = []
    img = cv.convertScaleAbs(img)
    contour, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE, contour)
    contour_array = contour[0][:, 0, :]
    contour_complex = np.empty(contour_array.shape[:-1], dtype=complex)
    contour_complex.real = contour_array[:, 0]
    contour_complex.imag = contour_array[:, 1]
    fourier_result = np.fft.fft(contour_complex)
    return fourier_result


def truncate_descriptor(descriptors, degree):
    """this function truncates an unshifted fourier descriptor array
    and returns one also unshifted"""
    descriptors = np.fft.fftshift(descriptors)
    center_index = len(descriptors) / 2
    descriptors = descriptors[
                  round(center_index - degree / 2):round(center_index + degree / 2)]
    descriptors = np.fft.ifftshift(descriptors)
    return descriptors


def normovani(descriptors):
    abs1 = abs(descriptors[1])
    for i in range(2, len(descriptors)):
        descriptors[i] = abs(descriptors[i]) / abs1
        descriptors[i] = descriptors[i].real

    descriptors = descriptors[2:]
    return descriptors
