# This is the main script of a project that creates a basic frame effect (Özkan et al. 2022)
# Mohammad Shams
# m.shams.ahmar@gmail.com
# 2022-05-23

from psychopy import visual, event, core, monitors
import supplements as sup

mon = sup.config_mon_imac24()
win = sup.config_win(mon)

sup.draw_frame(win)
win.flip()
core.wait(3)
win.close()
