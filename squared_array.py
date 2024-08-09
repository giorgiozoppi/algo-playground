
def square_array(array: list[int])-> list[int]:
    """
        [-4, -1, 0 , 3, 10]
        [0, 1, 9, 16, 100]
    Args:
        array (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    # find the last index where is negative
    negative_index = -1
    for item in array:
        if item < 0:
            negative_index = negative_index + 1
        else:
            break
    if negative_index < 0:
        return [ x * x for x in array]
    elif negative_index == len(array) - 1:
        return reversed([x * x for x in array])
    else:
        lower = negative_index
        upper = negative_index + 1
        result = []
        while upper < len(array):
            if lower >=0:
                target_lower = array[lower] ** 2
                target_upper = array[upper] ** 2
                if target_lower < target_upper:
                    result.append(target_lower)
                    lower = lower - 1
                else:
                    result.append(target_upper)
                    upper = upper + 1
            else:
                # finished lower terms
                target_upper = array[upper] ** 2
                result.append(target_upper)
                upper = upper + 1