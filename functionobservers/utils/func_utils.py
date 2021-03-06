"""

"""
import numpy as np


def pack_state(state):
    """
    Given a state in a dynamical system with shape (ndim, 1), flatten it to (ndim,).
    This works as a helper function to remember what you're doing as opposed to explicitly
    reshaping the states.

    :param state:  numpy array of shape (ndim, 1)
    :return: fstate: numpy array of shape (ndim,)
    """
    return np.squeeze(state)


def unpack_state(state):
    """
    Given a packed state in a dynamical system with shape (ndim), unroll it to (ndim, 1).
    This works as a helper function to remember what you're doing as opposed to explicitly
    reshaping the states.

    :param state: numpy array of shape (ndim,)
    :return: fstate: numpy array of shape (ndim, 1)
    """
    return np.reshape(state, (state.shape[0], 1))


def infer_dynamics(weight_stream, reg_parm):
    """
    Given a stream of weights, infer dynamics operator and covariance matrix.
    Recall that while feature data is in row major form, we perform all dynamics
    operations in column major form to preserve convention and my own sanity.

    :param weight_stream: ndim x T matrix of weights, where T is the number of time
                          steps
    :param weight_stream: regularization parameter
    :return: A, an ndim x ndim dynamics matrix, and B, an ndim x ndim covariance matrix.
    """
    ndim = weight_stream.shape[0]
    nsteps = weight_stream.shape[1]


def pack_params_nll(d_params, noise, k_name):
    """
    Function to convert dictionary of parameters to k-dimensional vector,
    in an order-preserving fashion. Generally, the order doesn't matter, as
    long as it's fixed.

    :param d_params: dictionary of parameters
    :param noise: scalar noise parameter
    :param k_name: name of kernel
    :return:
    """
    d_params_copy = d_params.copy()
    nparams = len(d_params_copy.keys()) + 1
    params = np.zeros((nparams,))
    if k_name == "sqexp":
        for i in range(0, nparams-2):
            params[i] = d_params_copy["ell" + str(i+1)]
        params[nparams-2] = d_params_copy["nu"]
        params[nparams-1] = noise
    elif k_name == "gaussian":
        params[0] = d_params_copy["sigma"]
        params[1] = noise
    else:
        raise ValueError("Kernel {} not supported.".format(k_name))
    return params


def unpack_params_nll(params, k_name):
    """
    Function to k-dimensional vector of parameters to a dictionary and a noise float,
    in an order-preserving fashion. Generally, the order doesn't matter, as
    long as it's fixed.

    :param params: k-dimensional vector of parameters
    :param k_name: name of kernel
    :return: dictionary of k-1 kernel parameters, and 1 observation noise parameter
    """
    nparams = params.shape[0]
    d_params = {}
    if k_name == "sqexp":
        for i in range(0, nparams-2):
            d_params["ell" + str(i + 1)] = params[i]
        d_params["nu"] = params[nparams-2]
        noise = params[nparams-1]
    elif k_name == "gaussian":
        d_params["sigma"] = params[0]
        noise = params[1]
    else:
        raise ValueError("Kernel {} not supported.".format(k_name))
    return d_params, noise


