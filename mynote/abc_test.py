import abc


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @ext.setter
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmetods__) <= attrs:
                return  True
        return NotImplemented
