#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        weighted_sum += score * weight
        total_weight += weight

    return weighted_sum / total_weight
