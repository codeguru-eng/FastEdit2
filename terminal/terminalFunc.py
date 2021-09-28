from __future__ import absolute_import

import sys
from code import InteractiveConsole


class Cache(object):
    """Replace stdout and stderr behavior in order to collect outputs."""

    def __init__(self):
        self.reset()

    def reset(self):
        """Clean the cache."""
        self.out = []

    def write(self, line):
        """Collect the output into cache to be accesed later."""
        self.out.append(line)

    def flush(self):
        """Join together all the outputs and return it to be displayed."""
        output = ''.join(self.out)[:-1]
        self.reset()
        return output


class ExitWrapper(object):
    """Wrap the built-in function exit in the interpreter."""
    def __call__(self, code=None):
        return None
    def __repr__(self):
        return exit.__repr__()
class HelpWrapper(object):
    """Wrap the built-in function help in the interpreter."""
    def __call__(self, *args, **kwds):
        if args or kwds:
            return help(*args, **kwds)
    def __repr__(self):
        return help.__repr__()
class TerminalMain(InteractiveConsole):
    """Work as a Python Console."""
    def __init__(self):
        # InteractiveConsole.__init__(self,
        super().__init__()
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self._cache = Cache()
        self.output = ''
    def get_output(self):
        """Replace out and error channels with cache."""
        sys.stdout = self._cache
        sys.stderr = self._cache
    def return_output(self):
        """Reassign the proper values to output and error channel."""
        sys.stdout = self.stdout
        sys.stderr = self.stderr
    def push(self, line):
        """Insert a command into the console."""
        self.get_output()
        val = InteractiveConsole.push(self, line)
        self.return_output()
        self.output = self._cache.flush()
        return val
    def get_type(self, var):
        """Get the type of a variable."""
        type_line = "'.'.join([type(%s).__module__, type(%s).__name__])" % \
            (var[:-1], var[:-1])
        self.get_output()
        InteractiveConsole.push(self, type_line)
        self.return_output()
        exec_line = self._cache.flush() + '.'
        exec_line = exec_line.replace("'", "")
        return exec_line