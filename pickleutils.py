import os
try:
    import cPickle as pickle
except:
    import pickle

class PickleUtils:
    """
    Provide a simple facade for the python package 'pickle'.
    A file name for reading and writing is needed, and objects will be read from and writen to the file given.
    The file and directories will be created if not exists.

    Attributes:
        PICKLE_NAME: the name of the file writing to and reading from.
    """
    PICKLE_NAME = ""

    def __init__(self, filename):
        """
        Init PickleUtils with a file name.

        Args:
            filename:the full name to the file.
        """
        self.PICKLE_NAME = filename

    def pickle_check(self):
        """
        Check if the file exists.

        Returns:
            Return True if the file exists, otherwise false.
        """
        if os.path.isfile(self.PICKLE_NAME):
            return True
        return False

    def pickle_read(self):
        """
        Read objects from the file. Objects will be returned in a list.
        The order of objects will be the same as the order given when writing.

        Returns:
            A list of objects.

            examples:
                ['Test', {'a':1, 'b':2}]
        """
        items = []
        with open(self.PICKLE_NAME, 'rb') as pf:
            while True:
                try:
                    items.append(pickle.load(pf))
                except EOFError:
                    break
        return items

    def pickle_write(self, list_of_objects):
        """
        Write a list of objects to the file. Any content in the file will be cleared before writing.

        Args:
            list_of_objects:a list of objects to be written to the file.

            examples:
                ['test', {'a':1, 'b':2}]
        """
        with open(self.PICKLE_NAME, 'wb') as pf:
            for item in list_of_objects:
                pickle.dump(item, pf)
