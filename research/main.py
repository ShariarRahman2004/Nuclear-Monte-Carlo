from mpi4py import MPI
import sys
import numpy as nu
import time
import solver.Explicit_VMS.spatial_computing_3d
import boundary.boundary_condition as boundary
from pyevtk.hl import gridToVTK
from pyevtk.hl import pointsToVTK
import scipy.io
import os
import MPItool.Simulation_3D
import importlib
import tools.radiation_solver.radiation_solver as radiation_solver
import  rt_solver_parallel.Radiation_Implicit.radiation_solve
import solver.Explicit_VMS.particles3D as particles 
#import solver.Explicit_VMS.particles3D as particles 


import tools.parallel.parallel_setup as parallel_setup
parallel_setup = parallel_setup.parallel_setup()
