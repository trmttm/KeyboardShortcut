from interface_keymaps import KeyMapsABC

from .KeyMap import KeyMap


class KeyMaps(KeyMapsABC):
    def __init__(self):
        self._data = {}
        self._active_keymap = None

    def add_keymap(self, name):
        self._data[name] = KeyMap()

    def set_active_keymap(self, name):
        if name not in self._data:
            self.add_keymap(name)
        self._active_keymap = name

    @property
    def active_keymap(self) -> KeyMap:
        return self._data[self._active_keymap]
