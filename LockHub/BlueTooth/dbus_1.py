import time
import dbus
def Query():
    bus = dbus.SessionBus()
    eth0 = bus.get_object('org.gnome.ScreenSaver', '/org/gnome/ScreenSaver')
    eth0_dev_iface = dbus.Interface(eth0, dbus_interface='org.gnome.ScreenSaver')

    props = eth0_dev_iface.GetActive()
    return props
