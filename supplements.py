from psychopy import monitors, visual


class Probe:
    def __init__(self, diameter, color, duration):
        self.diameter = diameter
        self.color = color
        self.duration = duration

    def appear(self):
        pass


def config_mon_imac24():
    width = 2240
    height = 1260
    monitor = monitors.Monitor('prim_mon', width=54.7, distance=57)
    monitor.setSizePix([height, width])
    return monitor


def config_win(mon):
    win = visual.Window(monitor=mon,
                        units='deg',
                        size=[1000, 700],
                        color=[-.8, -.8, -.8])
    return win


def draw_frame(win, pos=(0, 0)):
    outer_frame = visual.Rect(win=win,
                              size=10,
                              fillColor='white',
                              pos=pos)

    inner_frame = visual.Rect(win=win,
                              size=9.5,
                              fillColor=[-.8, -.8, -.8],
                              pos=pos)
    outer_frame.draw()
    inner_frame.draw()
