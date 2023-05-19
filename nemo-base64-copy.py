#!/usr/bin/env python3

import os
import subprocess
import gi
import pyperclip
from gi.repository import Nemo, GObject, Gtk, Gdk

gi.require_version('Nemo', '3.0')

class NemoCopyBase64(GObject.GObject, Nemo.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, file):
        filepath = file.get_location().get_path()
        base64_content = subprocess.check_output(['base64', '-w', '0', filepath]).decode().strip()

        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(base64_content, -1)
        clipboard.store()

    def get_file_items(self, window, files):
        if len(files) == 1 and not files[0].is_directory():
            item = Nemo.MenuItem(name='NemoCopyBase64::CopyBase64', label='Copy Base64', tip='Copy Base64 representation of the file', icon='edit-paste')
            item.connect('activate', self.menu_activate_cb, files[0])
            return item,
        return

if __name__ == '__main__':
    NemoCopyBase64.register()
