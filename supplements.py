from psychopy import monitors, visual


def config_mon_imac24():
    width = 2240
    height = 1260
    monitor = monitors.Monitor('prim_mon', width=54.7, distance=57)
    monitor.setSizePix([height, width])
    return monitor


def config_win(mon):
    win = visual.Window(monitor=mon,
                        units='deg',
                        fullscr=True,
                        color=[-.8, -.8, -.8])
    # win.mouseVisible = False
    return win


def draw_frame(win, width, pos=(0, 0)):
    outer_frame = visual.Rect(win=win,
                              size=width,
                              fillColor='white',
                              pos=pos)

    inner_frame = visual.Rect(win=win,
                              size=width - .5,
                              fillColor=[-.8, -.8, -.8],
                              pos=pos)
    outer_frame.draw()
    inner_frame.draw()


def draw_probe(win, color, radius=1, pos=(0, 0)):
    probe = visual.Circle(win, radius=radius, fillColor=color, pos=pos)
    probe.draw()
