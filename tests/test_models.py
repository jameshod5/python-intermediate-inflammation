"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

# with parameterization
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),     # test is first 3, then expected is the last
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])

def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))
   

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),     # test is first 3, then expected is the last
        ([[5, 2, 9], [36, 4, 31], [5, 62, 7]], [36, 62, 31]),
    ])

def test_daily_max(test, expected):
    """Test max function works for our test and expected"""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),     # test is first 3, then expected is the last
        ([[5, 2, 9], [36, 4, 31], [5, 62, 7]], [5, 2, 7]),
    ])

def test_daily_min(test, expected):
    """Test min function works for our test and expected"""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)


# without parameterization
def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_zeros():
    from inflammation.models import daily_max

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0,0])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_integers():
    from inflammation.models import daily_max

    test_input = np.array([[5, 2, 9],
                           [36, 4, 31],
                           [5, 62, 7]])
    test_result = np.array([36,62,31])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_zeros():
    from inflammation.models import daily_min

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0,0])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_integers():
    from inflammation.models import daily_min

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([1,2])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


