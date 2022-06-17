from openburrito import find_burrito_joints, BurritoCriteriaConflict
# "criteria" is an object defining the kind of burritos you want.
try:
    places = find_burrito_joints(criteria)
except BurritoCriteriaConflict as err:
    logger.warn("Cannot resolve conflicting burrito criteria: {}".format(err.message))
    places = list()