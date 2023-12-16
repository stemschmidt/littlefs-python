import enum
from typing import Tuple, NamedTuple, Optional, Union
from littlefs.context import UserContext

FILENAME_ENCODING: str = ...
__LFS_VERSION__: Tuple[int, int] = ...
__LFS_DISK_VERSION__: Tuple[int, int] = ...

LFSStat = NamedTuple('LFSStat', [
    ('type', int),
    ('size', int),
    ('name', str)
])

LFSFSStat = NamedTuple('LFSFSStat', [
    'disk_version',
    'name_max',
    'file_max',
    'attr_max',
    'block_count',
    'block_size',
])


class LFSFileFlag(enum.IntFlag): ...

class LFSConfig:

    user_context: UserContext = ...

    def __init__(self,
                 context=None,
                 *,
                 block_size: int = 128,
                 block_count: int = 64,
                 read_size: int = 0,
                 prog_size: int = 0,
                 block_cycles: int = -1,
                 cache_size: int = 0,
                 lookahead_size: int = 8,
                 name_max: int = 255,
                 file_max: int = 0,
                 attr_max: int = 0,
                 metadata_max: int = 0,
                 disk_version: int = 0,
                )-> None: ...

    @property
    def read_size(self) -> int: ...

    @property
    def prog_size(self) -> int: ...

    @property
    def block_size(self) -> int: ...

    @property
    def block_count(self) -> int: ...

    @property
    def cache_size(self) -> int: ...

    @property
    def lookahead_size(self) -> int: ...

    @property
    def name_max(self) -> int: ...

    @property
    def file_max(self) -> int: ...

    @property
    def attr_max(self) -> int: ...

class LFSFilesystem:
    @property
    def block_count(self) -> int: ...

# The following classes are opaque wrappers around the actual handles
class LFSFile: ...
class LFSDirectory: ...


def fs_stat(fs: LFSFilesystem) -> LFSFSStat: ...
def fs_size(fs: LFSFilesystem) -> int: ...
def format(fs: LFSFilesystem, cfg: LFSConfig) -> int: ...
def mount(fs: LFSFilesystem, cfg: LFSConfig) -> int: ...
def unmount(fs: LFSFilesystem) -> int: ...
def fs_mkconsistent(fs: LFSFilesystem) -> int: ...
def fs_grow(fs: LFSFilesystem, block_count) -> int: ...

def remove(fs: LFSFilesystem, path: str) -> int: ...
def rename(fs: LFSFilesystem, oldpath: str, newpath: str) -> int: ...
def stat(fs: LFSFilesystem, path: str) -> LFSStat: ...

# Attributes
def getattr(fs: LFSFilesystem, path: str, typ) -> bytes: ...
def setattr(fs: LFSFilesystem, path: str, typ, data) -> None: ...
def removeattr(fs: LFSFilesystem, path: str, typ) -> None: ...

# File Handling
def file_open(fs: LFSFilesystem, path: str, flags: Union[str, LFSFileFlag]) -> LFSFile: ...
# def file_open_cfg(self, path, flags, config): ...
def file_close(fs: LFSFilesystem, fh: LFSFile) -> int: ...
def file_sync(fs: LFSFilesystem, fh: LFSFile) -> int: ...
def file_read(fs: LFSFilesystem, fh: LFSFile, size) -> bytes: ...
def file_write(fs: LFSFilesystem, fh: LFSFile, data) -> int: ...
def file_seek(fs: LFSFilesystem, fh: LFSFile, off, whence) -> int: ...
def file_truncate(fs: LFSFilesystem, fh: LFSFile, size) -> int: ...
def file_tell(fs: LFSFilesystem, fh: LFSFile) -> int: ...
def file_rewind(fs: LFSFilesystem, fh: LFSFile) -> int: ...
def file_size(fs: LFSFilesystem, fh: LFSFile) -> int: ...

# Directory Handling
def mkdir(fs: LFSFilesystem, path: str) -> int: ...
def dir_open(fs: LFSFilesystem, path: str) -> LFSDirectory: ...
def dir_close(fs: LFSFilesystem, dh: LFSDirectory) -> int: ...
def dir_read(fs: LFSFilesystem, dh: LFSDirectory) -> LFSStat: ...
def dir_tell(fs: LFSFilesystem, dh: LFSDirectory) -> int: ...
def dir_rewind(fs: LFSFilesystem, dh: LFSDirectory) -> int: ...
