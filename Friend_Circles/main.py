# Friends Cirlces
#! /usr/bin/env python3


def count_friend_circles(friends):
    # first form a circle of individual person
    circles = []
    for i in range(len(friends)):
        circles.append([i])

    for i in range(len(friends)):
        line = friends[i]
        for j in range(0, i + 1):
            ch = line[j]

            # if i and j are friends
            if i != j and ch == 'Y':
                iCircle = -1
                jCircle = -1

                # there can be only one circle in which one can be present
                for k in range(len(circles) - 1, -1, -1):
                    circle = circles[k]
                    if i in circle:
                        iCircle = k
                    if j in circle:
                        jCircle = k

                if iCircle != jCircle:
                    # i and j both are in different circles
                    # create copies

                    cItoMerge = circles[iCircle][:]
                    cJtoMerge = circles[jCircle][:]

                    # merge their circles
                    # we can safely add, as there are no duplicates in any circle
                    # update new entry at circle i, and remove jth circle
                    circles[iCircle] = cItoMerge + cJtoMerge

                    # remove one entry
                    del circles[jCircle]

    return len(circles)


if __name__ == '__main__':
    matrix_filename = input('Please provide a filename containing a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]

    num_circles = count_friend_circles(friends)
    print('Number of friend circles:', num_circles)
