# %%
from pathlib import Path

from offline_docs_py.dependencies import read_dependencies_poetry


PYPROJECT = Path("pyproject.toml")

# %% LOAD DEPENDENCIES

depencencies = read_dependencies_poetry(PYPROJECT)

# %%
