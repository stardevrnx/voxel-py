from numba import njit
import numpy as np
import glm # type: ignore
import math

#resolution
WIN_RES = glm.vec2(1600, 900)