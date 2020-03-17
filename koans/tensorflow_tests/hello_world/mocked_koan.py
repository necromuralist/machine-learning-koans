#+ Put the solutions here

# Imports
# python
import warnings
# pypi
with warnings.catch_warnings():
    # this is for the warnings that make the test
    # failures unreadable
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=DeprecationWarning)    
    from tensorflow import keras

# The Fake Data
# The tests are using mocks so instead of using real data these will
# just be fakes
def get_data():
    return None, None


def get_input():
    return


# The code to implement
def make_model():
    """
    Make a dense model with one unit
    
    hint: the input shape will also be 1

    Returns:
     the model
    """
    return model


def compile_network():
    """
    compile the model using Stochastic Gradient Descent
     and measuring the loss with the Mean Squared Error

    Grab the model from make_model before adding this code

    Returns:
     the compiled model
    """
    return model

def fit_model():
    """Fit the model for 500 epochs

    Use X and y as defined above and gram the model from compile_network
    before adding the extra code

    Returns:
     fitted model
    """
    return model

def predict():
    """make a prediction on input data

    Use ``get_input`` to get the input data
    Use ``fit_model`` to get the model for the prediction
    """
    return
