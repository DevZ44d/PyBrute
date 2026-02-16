from importlib.metadata import version, PackageNotFoundError

try:
    pkg_version = version("pybrute")
except PackageNotFoundError:
    pkg_version = "unknown"

__version__ = pkg_version