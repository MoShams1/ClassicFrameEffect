# This is the main script of a project that creates a basic frame effect (Özkan et al. 2022)
# Mohammad Shams
# m.shams.ahmar@gmail.com
# 2022-05-23

from psychopy import visual, event, core, monitors
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
frame_path_len = 9  # deg
frame_path_dur = 30  # frame
frame_jump = (frame_path_len + 1) / (frame_path_dur / min_obj_dur)  # deg
frame_x = -4 - frame_jump
frame_y = 0

num_jumps = int(frame_path_dur / min_obj_dur)  # how often the frame should jump

# -------------------------------------------------
# run the stimulus
# -------------------------------------------------

# 1st leg of the cycle
for icycle in range(1):
    for ichange in range(num_jumps):
        frame_x = np.around(frame_x + frame_jump, 1)  # update the frame position
        for irep in range(min_obj_dur):
            sup.draw_frame(win, pos=(frame_x, frame_y), width=frame_width)
            if ichange == num_jumps - 1:  # draw the probe if the frame is at the end of its path
                sup.draw_probe(win, color='red', pos=(0, frame_y+(frame_width/2-2)))
            win.flip()

# 2nd leg of the cycle
    for ichange in range(num_jumps):
        frame_x = np.around(frame_x - frame_jump, 1)
        for irep in range(min_obj_dur):
            sup.draw_frame(win, pos=(frame_x, frame_y), width=frame_width)
            if ichange == num_jumps - 1:  # draw the probe if the frame is at the end of its path
                sup.draw_probe(win, color='DeepSkyBlue', pos=(0, frame_y-(frame_width/2-2)))
            win.flip()

win.close()
