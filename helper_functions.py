import operator
import collections

from functools import reduce
from typing import List, Dict, Any


def count_to_proportions(counts_map: Dict[Any, float]) -> Dict[Any, float]:
    """
    Convert counts to proportions in the given chromosome
    :param counts_map: the dict comprising the counts for each key
    :return: a dict comprising the portions for each key
    """
    sum_count = sum(counts_map.values())
    proportions_map = {k: v / sum_count for k, v in counts_map.items()}
    return proportions_map


def get_lists_difference(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Get the difference of two lists
    :param list1: the first list
    :param list2: the second list
    :return: the difference
    """
    return list(set(list1) - set(list2))


def delete_item_from_list_by_index(list_to_delete_from: List[Any], index: int) -> List[Any]:
    """
    Delete item from list by index
    :param list_to_delete_from: the list to delete from
    :param index: the index
    :return: the list without the deleted item
    """
    return list_to_delete_from[:index] + list_to_delete_from[index + 1:]


def get_items_from_dict_by_keys(dict_to_get_from: Dict[Any, Any], keys: List[Any]) -> List[Any]:
    """
    Get multiple items from dict
    :param dict_to_get_from: the dict to get from
    :param keys: the keys
    :return: the items
    """
    return list(operator.itemgetter(*keys)(dict_to_get_from))


def merge_dicts_by_summing_values(list_of_dicts: List[Dict[Any, Any]]) -> Dict[Any, Any]:
    """
    Sum all dicts in the list
    :param list_of_dicts: the list of dicts
    :return: the summed dict
    """
    return dict(reduce(operator.add, map(collections.Counter, list_of_dicts)))


def get_containers_counts_sum_map(containers: Dict[Any, Any], keys: List[int]) -> Dict[Any, float]:
    """
    Get the sum of counts of containers of the given keys
    :param containers: the containers
    :param keys: the keys
    :return: the sum of counts of containers of the given keys
    """
    containers_counts_maps = get_items_from_dict_by_keys(containers, keys)
    containers_counts_sum_map = merge_dicts_by_summing_values(containers_counts_maps)
    return containers_counts_sum_map
