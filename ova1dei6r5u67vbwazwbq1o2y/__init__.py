from importlib.metadata import version, PackageNotFoundError
from .ova1dei6r5u67vbwazwbq1o2y import ova1dei6r5u67vbwazwbq1o2y as _

try:
    __version__ = version("ova1dei6r5u67vbwazwbq1o2y")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
