try:
    from ._version import __version__, __version_tuple__ # type: ignore
except ImportError:
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)