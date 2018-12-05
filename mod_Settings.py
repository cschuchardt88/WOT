import math
import BigWorld
import GUI
import Keys
import Math
import WWISE

from post_processing import g_postProcessing
from PlayerEvents import g_playerEvents
from gui import g_keyEventHandlers, g_mouseEventHandlers


def mod_handleKeyEvents(event):
    if not event.isKeyDown():
        return False
    if event.key == Keys.KEY_HOME:
        pass
    elif event.key == Keys.KEY_END:
        pass

    return True

def mod_handleMouseEvent(event):
    return BigWorld.camera().handleMouseEvent(event)


def init():
    g_keyEventHandlers.add(mod_handleKeyEvents)
    g_mouseEventHandlers.add(mod_handleMouseEvent)
    g_playerEvents.onAvatarReady += mod_AvatarReady # in game

def mod_AvatarReady():
    pass