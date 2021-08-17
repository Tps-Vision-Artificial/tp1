import cv2 as cv


def main(val):
    # iniciamos la capturadora con el nombre cap
    cap = cv.VideoCapture(0)
    window_name = 'Window'
    trackbar_name = 'Trackbar'
    slider_max = 151
    cv.namedWindow(window_name)
    cap = cv.VideoCapture(0)
    biggest_contour = None
    color_white = (255, 255, 255)

    create_trackbar(trackbar_name, window_name, slider_max)
    saved_contours = []
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)

        #1
        gray_frame = apply_color_convertion(frame=frame, color=cv.COLOR_BGR2GRAY)

        #2
        trackbar_val = get_trackbar_value(trackbar_name=trackbar_name, window_name=window_name)
        adapt_frame = adaptive_threshold(frame=gray_frame, slider_max=slider_max,
                                         adaptative=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         binary=cv.THRESH_BINARY,
                                         trackbar_value=trackbar_val)
        #3
        frame_denoised = denoise(frame=adapt_frame, method=cv.MORPH_ELLIPSE, radius=10)

        #4 Contours
        contours = get_contours(frame=frame_denoised, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            biggest_contour = get_biggest_contour(contours=contours)
            if compare_contours(contour_to_compare=biggest_contour, saved_contours=saved_contours, max_diff=1):
                draw_contours(frame=frame_denoised, contours=biggest_contour, color=color_white, thickness=20)
            draw_contours(frame=frame_denoised, contours=biggest_contour, color=color_white, thickness=3)
        cv.imshow('Window', frame_denoised)

        if cv.waitKey(1) & 0xFF == ord('k'):
            if biggest_contour is not None:
                saved_contours.append(biggest_contour)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


def create_trackbar(trackbar_name, window_name, slider_max):
    cv.createTrackbar(trackbar_name, window_name, 0, slider_max, on_trackbar)


def on_trackbar(val):
    pass


def get_trackbar_value(trackbar_name, window_name):
    return int(cv.getTrackbarPos(trackbar_name, window_name) / 2) * 2 + 3


def denoise(frame, method, radius):
    kernel = cv.getStructuringElement(method, (radius, radius))
    opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    return closing


def apply_color_convertion(frame, color):
    return cv.cvtColor(frame, color)


def adaptive_threshold(frame, slider_max, adaptative, binary, trackbar_value):
    return cv.adaptiveThreshold(frame, slider_max, adaptative, binary, trackbar_value, 0)


def draw_contours(frame, contours, color, thickness):
    # -1 for all contours
    cv.drawContours(frame, contours, -1, color, thickness)
    return frame

def get_contours(frame, mode, method):
    contours, hierarchy = cv.findContours(frame, mode, method)
    return contours


def get_biggest_contour(contours):
    max_cnt = contours[0]
    for cnt in contours:
        if cv.contourArea(cnt) > cv.contourArea(max_cnt):
            max_cnt = cnt
    return max_cnt


def compare_contours(contour_to_compare, saved_contours, max_diff):
    for contour in saved_contours:
        if cv.matchShapes(contour_to_compare, contour, cv.CONTOURS_MATCH_I2, 0) < max_diff:
            return True
    return False

main(0)
