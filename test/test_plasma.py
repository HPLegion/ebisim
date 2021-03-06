"""
Tests for ebisim.plasma
"""

import pytest
import numpy as np

from ebisim.plasma import (
    electron_velocity,
    clog_ei,
    clog_ii,
    coulomb_xs,
    ion_coll_rate,
    spitzer_heating,
    collisional_thermalisation,
    trapping_strength_axial,
    trapping_strength_radial
)

def test_electron_velocity():
    e_kin = np.array([
        1,
        10,
        100,
        1000,
        10000,
        100000,
        1000000,
        ])
    vel = np.array([
        593096.087988011,
        1875509.73510071,
        5930099.25162193,
        18727896.63517020,
        58455214.9277818,
        164352479.7315760,
        282128454.9430590,
    ])
    np.testing.assert_allclose(vel, electron_velocity(e_kin))
    np.testing.assert_allclose(electron_velocity(e_kin), electron_velocity.py_func(e_kin))
    np.testing.assert_equal(electron_velocity(e_kin), electron_velocity.py_func(e_kin))


# def test_clog_ei():
#     raise NotImplementedError

def test_clog_ii():
    # Manually calculcated test cases
    ni = np.array([
        1000000000000, 1000000000000, 1000000000000, 1000000000000, 1000000000000, 10000000000000,
        10000000000000, 10000000000000, 1E+016, 1E+016, 1E+016
    ])
    nj = np.array([
        100000000, 100000000, 100000000, 10000000000, 10000000000, 10000000000, 10000000000,
        10000000000, 1E+016, 1E+016, 1E+016
    ])
    Ti = np.array([10, 100, 1000, 10, 100, 1000, 10, 100, 1000, 10, 100])
    Tj = np.array([100, 100, 100, 100, 100, 1000, 1000, 1000, 1, 1, 1])
    Ai = np.array([50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50])
    Aj = np.array([10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20])
    qi = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    qj = np.array([0, 0, 1, 2, 3, 20, 20, 20, 4, 5, 8])
    lbd = np.array([
        np.inf, np.inf, 23.6811639328737, 18.7955945932549, 19.1259943697099, 19.0800403199937,
         16.0882130201689, 16.9660804546058, 12.2905374511607, 7.20361107988083, 8.39495409549117
    ])

    res = clog_ii(ni, nj, Ti, Tj, Ai, Aj, qi, qj)
    np.testing.assert_allclose(res, lbd)


# def test_coulomb_xs():
#     raise NotImplementedError

# def test_ion_coll_rate():
#     raise NotImplementedError

# def test_spitzer_heating():
#     raise NotImplementedError

# def test_collisional_thermalisation():
#     raise NotImplementedError

# def test_loss_frequency_axial():
#     raise NotImplementedError

# def test_loss_frequency_radial():
#     raise NotImplementedError
