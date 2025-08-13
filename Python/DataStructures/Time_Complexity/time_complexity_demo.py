def get_first_friend(friends_id: list[int]) -> int:
    """
    O(1) - Constant Time
    Returns the first friend ID from the list

    """
    return friends_id[0]


def find_friend_with_id_starting_with(sorted_friends_ids, start_digit):
    """
    O(log n) - Logarithmic Time
    Performs a binary search to find a friend ID starting with given digit
    """

    left, right = 0, len(sorted_friends_ids) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if str(sorted_friends_ids[mid]).startswith(start_digit):
            return sorted_friends_ids[mid]

        elif sorted_friends_ids[mid] < int(
            start_digit + '0' * (len(str(sorted_friends_ids[mid])))
        ):
            left = mid + 1

        else:
            right = mid - 1

    return None


def find_friend_with_max_id(friends_ids):
    """
    O(n) - Linear Time
    Finds the friend with the maximum ID from list.
    """

    max_id = friends_ids[0]

    for friend_id in friends_ids:

        if friend_id > max_id:
            max_id = friend_id

    return max_id


def rank_friends_by_id(friends_ids):
    """
    O(n log n) - Linearithmic Time
    Sorts a list of friends IDs in ascending order
    """
    return sorted(friends_ids)


def find_common_friends(
    friend_list1: list,
    friend_list2: list,
) -> list:
    """
    O(n^2) - Quadratic Time
    Finds common friends between two lists of friends IDs.
    """
    common_friends = []  # initialize empty list
    for friend1 in friend_list1:
        for friend2 in friend_list2:
            if friend1 == friend2:
                common_friends.append(friend1)

    return common_friends


def find_common_friends_among_3_lists(
    friend_list1: list, friend_list2: list, friend3_list3: list
) -> list:
    """
    O(n^3) - Cubic Time
    Finds common friends among three lists of friends IDs.
    """

    common_elements = []

    for friend1 in friend_list1:
        for friend2 in friend_list2:
            for friend3 in friend3_list3:
                if friend1 == friend2 == friend3:
                    common_elements.append(friend1)

    return common_elements


def generate_subsets_of_friends(friends_ids: list) -> list:
    """
    O(2^n) - Exponential Time
    Generates all possible subsets of a list of friends IDs.
    """

    if not friends_ids:
        return [[]]

    first_id = friends_ids[0]
    rest_ids = friends_ids[1:]

    subsets_without_first = generate_subsets_of_friends(rest_ids)
    subsets_with_first = []

    for subset in subsets_without_first:
        subsets_with_first.append([first_id] + subset)
    return subsets_without_first + subsets_with_first


def generate_all_seating_arangements(friends_ids: list):
    """
    O(n!) - Factorial Time
    Generates all possible  seating arrangements for a list of friends Id's
    """

    if len(friends_ids) == 0:
        return [[]]

    arrangements = []

    for i in range(len(friends_ids)):

        current_friend = friends_ids[i]
        remaining_friends = friends_ids[:i] + friends_ids[i + 1]

        for arrangement in generate_all_seating_arangements(remaining_friends): 
            arrangements.append([current_friend] + arrangement)

        return arrangements


if __name__ == "__main__":

    # Examples arrays of friends ID's

    friends_ids = [101, 203, 304, 405, 506]
