import ast
import builtins
import distutils.sysconfig
import sys
from typing import Any, Callable, Type, TypeVar, Union

import libcst as cst

from unimport.statement import Import, ImportFrom

__all__ = [
    "ASTFunctionT",
    "ASTFunctionTuple",
    "ASTImportableT",
    "BUILTINS",
    "BUILTIN_MODULE_NAMES",
    "CFNT",
    "CSTImportT",
    "DESCRIPTION",
    "DefTuple",
    "EXCLUDE_REGEX_PATTERN",
    "FunctionT",
    "GLOB_PATTERN",
    "IGNORE_IMPORT_NAMES",
    "INCLUDE_REGEX_PATTERN",
    "INIT_FILE_IGNORE_REGEX",
    "ImportT",
    "PY38_PLUS",
    "PY39_PLUS",
    "STDLIB_PATH",
    "SUBSCRIPT_TYPE_VARIABLE",
    "VERSION",
]

DESCRIPTION = (
    "A linter, formatter for finding and removing unused import statements."
)
VERSION = "0.7.4"

#  TYPE
FunctionT = TypeVar("FunctionT", bound=Callable[..., Any])
ASTImportableT = Union[
    ast.AsyncFunctionDef,
    ast.Attribute,
    ast.ClassDef,
    ast.FunctionDef,
    ast.Name,
    ast.alias,
]

ASTFunctionT = TypeVar("ASTFunctionT", ast.FunctionDef, ast.AsyncFunctionDef)
ImportT = Union[Import, ImportFrom]
CFNT = TypeVar(
    "CFNT",
    ast.ClassDef,
    ast.FunctionDef,
    ast.AsyncFunctionDef,
    ast.Name,
)
CSTImportT = TypeVar("CSTImportT", cst.Import, cst.ImportFrom)

#  REGEX
GLOB_PATTERN = r"**/*.py"
INCLUDE_REGEX_PATTERN = r"\.(py)$"
EXCLUDE_REGEX_PATTERN = r"^$"
INIT_FILE_IGNORE_REGEX = r"__init__\.py"

# TUPLE
DefTuple = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
ASTFunctionTuple = (ast.FunctionDef, ast.AsyncFunctionDef)


# CONF
PY38_PLUS = sys.version_info >= (3, 8)
PY39_PLUS = sys.version_info >= (3, 9)

SUBSCRIPT_TYPE_VARIABLE = frozenset(
    {
        "AbstractSet",
        "AsyncContextManager",
        "AsyncGenerator",
        "AsyncIterable",
        "AsyncIterator",
        "Awaitable",
        "Callable",
        "ChainMap",
        "ClassVar",
        "Collection",
        "Container",
        "ContextManager",
        "Coroutine",
        "Counter",
        "DefaultDict",
        "Deque",
        "Dict",
        "FrozenSet",
        "Generator",
        "IO",
        "ItemsView",
        "Iterable",
        "Iterator",
        "KeysView",
        "List",
        "Mapping",
        "MappingView",
        "Match",
        "MutableMapping",
        "MutableSequence",
        "MutableSet",
        "Optional",
        "Pattern",
        "Reversible",
        "Sequence",
        "Set",
        "SupportsRound",
        "Tuple",
        "Type",
        "Union",
        "ValuesView",
        # Python >= 3.7.
        "Literal",
        # Python >= 3.8.
        "OrderedDict",
    }
)

IGNORE_IMPORT_NAMES = frozenset({"__all__", "__doc__", "__name__"})
BUILTINS = frozenset(dir(builtins))
BUILTIN_MODULE_NAMES = frozenset(sys.builtin_module_names)
STDLIB_PATH = distutils.sysconfig.get_python_lib(standard_lib=True)
