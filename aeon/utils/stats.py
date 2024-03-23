"""Statistical functionality used throughout aeon."""

import warnings

import numpy as np
from deprecated.sphinx import deprecated
from sklearn.utils.stats import _weighted_percentile
from sklearn.utils.validation import check_consistent_length

__maintainer__ = []
__all__ = [
    "_weighted_geometric_mean",
    "_weighted_median",
    "_weighted_min",
    "_weighted_max",
]


@deprecated(
    version="0.8.0",
    reason=(
        "Stats.py is deprecated and"
        "will be removed in v0.9.0. "
        "Use 'weighted_metrics.py' instead. "
    ),
    category=FutureWarning,
)
def _weighted_geometric_mean(y, weights=None, axis=None):
    """Calculate weighted version of geometric mean.

    .. deprecated:: v0.9.0.
    Use `_weighted_geometric_mean`
    from `weighted_metrics` instead.

    Parameters
    ----------
    y : np.ndarray
        Values to take the weighted geometric mean of.
    weights: np.ndarray
        Weights for each value in `array`. Must be same shape as `array` or
        of shape `(array.shape[0],)` if axis=0 or `(array.shape[1], ) if axis=1.
    axis : int
        The axis of `y` to apply the weights to.

    Returns
    -------
    geometric_mean : float
        Weighted geometric mean
    """
    warnings.warn(
        "_weighted_geometric_mean is deprecated in v0.9.0.",
        DeprecationWarning,
        stacklevel=2,
    )
    if weights.ndim == 1:
        if axis == 0:
            check_consistent_length(y, weights)
        elif axis == 1:
            if y.shape[1] != len(weights):
                raise ValueError(
                    f"Input features ({y.shape[1]}) do not match "
                    f"number of `weights` ({len(weights)})."
                )
        weight_sums = np.sum(weights)
    else:
        if y.shape != weights.shape:
            raise ValueError("Input data and weights have inconsistent shapes.")
        weight_sums = np.sum(weights, axis=axis)
    return np.exp(np.sum(weights * np.log(y), axis=axis) / weight_sums)


def _weighted_median(y, axis=1, weights=None):
    """Calculate weighted median.

    .. deprecated:: v0.9.0.
    Use `_weighted_median` from
    from weighted_metrics instead.

    Parameters
    ----------
    y : np.ndarray, pd.Series or pd.DataFrame
        Values to take the weighted median of.
    weights: np.ndarray
        Weights for each value in `array`. Must be same shape as `array` or
        of shape `(array.shape[0],)` if axis=0 or `(array.shape[1], ) if axis=1.
    axis : int
        The axis of `y` to apply the weights to.

    Returns
    -------
    w_median : float
        Weighted median
    """
    warnings.warn(
        "_weighted_nedian is deprecated in v0.9.0.", DeprecationWarning, stacklevel=2
    )
    w_median = np.apply_along_axis(
        func1d=_weighted_percentile,
        axis=axis,
        arr=y,
        sample_weight=weights,
        percentile=50,
    )
    return w_median


def _weighted_min(y, axis=1, weights=None):
    """Calculate weighted minimum.

    .. deprecated:: v0.9.0.
    Use `_weighted_min` from
    from weighted_metrics instead.

    Parameters
    ----------
    y : np.ndarray, pd.Series or pd.DataFrame
        Values to take the weighted minimum of.
    weights: np.ndarray
        Weights for each value in `array`. Must be same shape as `array` or
        of shape `(array.shape[0],)` if axis=0 or `(array.shape[1], ) if axis=1.
    axis : int
        The axis of `y` to apply the weights to.

    Returns
    -------
    w_min : float
        Weighted minimum
    """
    warnings.warn(
        "_weighted_min is deprecated in v0.9.0.", DeprecationWarning, stacklevel=2
    )
    w_min = np.apply_along_axis(
        func1d=_weighted_percentile,
        axis=axis,
        arr=y,
        sample_weight=weights,
        percentile=0,
    )
    return w_min


def _weighted_max(y, axis=1, weights=None):
    """Calculate weighted maximum.

    .. deprecated:: v0.9.0.
    Use `_weighted_max` from.
    from weighted_metrics instead.

    Parameters
    ----------
    y : np.ndarray, pd.Series or pd.DataFrame
        Values to take the weighted maximum of.
    weights: np.ndarray
        Weights for each value in `array`. Must be same shape as `array` or
        of shape `(array.shape[0],)` if axis=0 or `(array.shape[1], ) if axis=1.
    axis : int
        The axis of `y` to apply the weights to.

    Returns
    -------
    w_max : float
        Weighted maximum
    """
    warnings.warn(
        "_weighted_max is deprecated in v0.9.0.", DeprecationWarning, stacklevel=2
    )
    w_max = np.apply_along_axis(
        func1d=_weighted_percentile,
        axis=axis,
        arr=y,
        sample_weight=weights,
        percentile=100,
    )
    return w_max
