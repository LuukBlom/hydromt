"""HydroMT: Automated and reproducible model building and analysis."""

# version number without 'v' at start
__version__ = "0.10.0.dev0"

# pkg_resource deprication warnings originate from dependencies
# so silence them for now
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


# required for accessor style documentation
import faulthandler

from xarray import DataArray, Dataset

# submodules
from hydromt import cli, flw, raster, stats, vector, workflows
from hydromt.data_catalog import *
from hydromt.io import *

# high-level methods
from hydromt.models import *

if sys.stdout is None or sys.stderr is None:
    faulthandler.disable()
else:
    faulthandler.enable()
