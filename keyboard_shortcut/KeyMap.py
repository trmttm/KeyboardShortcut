from typing import Callable
from typing import Tuple

from interface_keymaps import KeyMapABC


class KeyMap(KeyMapABC):

    def __init__(self):
        self._data = {}

    def add_new_keyboard_shortcut(self, key_combo: tuple, command_and_feed_back: Tuple[Callable, str]):
        self._data[key_combo] = command_and_feed_back

    def get_command_and_feedback(self, key_combo: tuple) -> tuple:
        try:
            command, feedback = self._data[key_combo]
            return command, f'Invoked {feedback}'
        except KeyError:
            return None, f'{key_combo} is not defined keyboard shortcut.'

    @property
    def keys(self) -> tuple:
        return tuple(self._data.keys())

    def clear(self):
        self.__init__()
