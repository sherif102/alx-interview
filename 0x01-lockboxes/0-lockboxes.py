#!/usr/bin/python3
"""checks if a list of boxes can all be opened by finding keys to them"""

# def canUnlockAll(boxes):
#     boxes_checked = {tuple(boxes[0])}
#     checker = [0]
#     all_keys = {0}
#     keys = set()

#     while True:
#         for key in checker:
#             if boxes[key]:
#                 boxes_checked.add(tuple(boxes[key]))
#                 for new_key in boxes[key]:
#                     keys.add(new_key)
#         checker = list(keys)
#         if keys.issubset(all_keys):
#             if len(keys) == 0:
#                 boxes_checked.add(list)
#             break
#         for copy_key in keys:
#             all_keys.add(copy_key)
#         keys.clear()
#     return len(boxes) == len(boxes_checked)


def canUnlockAll(boxes):
    """function that checks if a list of boxes can all be opened"""
    visited = set()
    keys = [0]

    while keys:
        current = keys.pop()
        if current not in visited and current < len(boxes):
            visited.add(current)
            for key in boxes[current]:
                if key not in visited:
                    keys.append(key)
    return len(visited) == len(boxes)
