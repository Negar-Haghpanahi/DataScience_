import enum
#from statistics import linear_regression

class type_(enum.Enum):

    csv   = 1
    excel = 2

class clustering (enum.Enum):
    k_means = 1
    k_modes = 2
    k_prototype =3

class ModelPrediction (enum.Enum):
    linear_regression = 1
    decision_tree = 2
    random_forest = 3
