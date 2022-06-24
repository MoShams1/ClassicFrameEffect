# *********************************************************************************************
#
# This is the main script of a project that creates a basic frame effect (Özkan et al. 2022)
# All functions defined for this project are stored in supplements.py and need to be imported.
#
# Mohammad Shams
# m.shams.ahmar@gmail.com
# modified on: 2022-05-23
#
# *********************************************************************************************

from psychopy import event, core
import supplements as sup
import numpy as np

# -------------------------------------------------
# initialize the display and set up the parameters
# -------------------------------------------------

# configure the monitor and the stimulus window
mon = sup.config_mon_imac24()
win = sup.config_win(mon)

# display
ref_rate = 60
min_obj_dur = 2  # frame
# frame
frame_width = 15  # deg
frame_path_len = 12  # deg
frame_path_dur = 30  # frame
# probe
probe_y_offset = 2  # deg

# -------------------------------------------------
# create the frame path
# -------------------------------------------------
frames_per_stroke = int(frame_path_dur / min_obj_dur)  # number of frames per stroke
frame_x_arr = np.linspace(0, frame_path_len, frames_per_stroke)  # deg
frame_y = 0  # deg
mid_way = frame_x_arr[int((frames_per_stroke - 1) / 2)]  # find the midway of the current path
frame_x_arr = frame_x_arr - mid_way  # align the path to the center (hirizontally) by removing the offset (the midway)

# -------------------------------------------------
# run the stimulus
# -------------------------------------------------
#
while True:

    # --------------------
    # 1st leg of the cycle
    # --------------------
    stroke1 = frame_x_arr[1:]

    for xind, xval in enumerate(stroke1):
        for irep in range(min_obj_dur):
            sup.draw_frame(win, pos=(xval, frame_y), width=frame_width)
            if xind == len(stroke1) - 1:  # draw the probe if the frame is at the end of its path
                sup.draw_probe(win, color='orangered', pos=(0, frame_y + (frame_width / 2 - 2)))
            win.flip()

    # --------------------
    # 2nd leg of the cycle
    # --------------------
    stroke2 = frame_x_arr[0:-1][::-1]

    for xind, xval in enumerate(stroke2):
        for irep in range(min_obj_dur):
            sup.draw_frame(win, pos=(xval, frame_y), width=frame_width)
            if xind == len(stroke2) - 1:  # draw the probe if the frame is at the end of its path
                sup.draw_probe(win, color='dodgerblue', pos=(0, frame_y - (frame_width / 2 - 2)))
            win.flip()

    # exit the session if 'escape' was pressed
    exit_key = event.getKeys(keyList=['escape'])
    if 'escape' in exit_key:
        core.quit()
