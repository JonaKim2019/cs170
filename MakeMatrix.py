
def add_edge(matrix, edgeA, edgeB, value):
    matrix[edgeA][edgeB] = value
    matrix[edgeB][edgeA] = value

def make_matrix():

    # for 50.in
    # adjmatrix = [['x'] * 8 for i in range(8)]
    # add_edge(adjmatrix, 0, 1, 1)
    # add_edge(adjmatrix, 1, 2, 1)
    # add_edge(adjmatrix, 2, 3, 1)
    # add_edge(adjmatrix, 3, 4, 1)
    # add_edge(adjmatrix, 4, 1, 1)
    # add_edge(adjmatrix, 1, 5, 1)
    # add_edge(adjmatrix, 5, 6, 1)
    # add_edge(adjmatrix, 6, 7, 1)
    # add_edge(adjmatrix, 0, 6, 1)
    #
    # for i in range(8):
    #     for j in range(8):
    #         print(adjmatrix[i][j], end=" ")
    #     print()

    # for 100.in
    # adjmatrix = [['x'] * 52 for i in range(52)]
    # add_edge(adjmatrix, 0, 1, 1)
    # add_edge(adjmatrix, 1, 11, 2)
    # add_edge(adjmatrix, 11, 21, 3)
    # add_edge(adjmatrix, 21, 31, 4)
    # add_edge(adjmatrix, 31, 41, 5)
    # add_edge(adjmatrix, 41, 51, 1)
    #
    # add_edge(adjmatrix, 0, 5, 8)
    # add_edge(adjmatrix, 5, 15, 1)
    # add_edge(adjmatrix, 15, 25, 1)
    # add_edge(adjmatrix, 25, 35, 1)
    # add_edge(adjmatrix, 35, 45, 1)
    #
    # add_edge(adjmatrix, 1, 2, 1)
    # add_edge(adjmatrix, 2, 3, 2)
    # add_edge(adjmatrix, 3, 4, 3)
    # add_edge(adjmatrix, 4, 5, 1)
    # add_edge(adjmatrix, 5, 6, 2)
    # add_edge(adjmatrix, 6, 7, 1)
    # add_edge(adjmatrix, 7, 8, 2)
    # add_edge(adjmatrix, 8, 9, 1)
    # add_edge(adjmatrix, 9, 10, 2)
    #
    # add_edge(adjmatrix, 11, 12, 1)
    # add_edge(adjmatrix, 12, 13, 2)
    # add_edge(adjmatrix, 13, 14, 3)
    # add_edge(adjmatrix, 14, 15, 1)
    # add_edge(adjmatrix, 15, 16, 2)
    # add_edge(adjmatrix, 16, 17, 1)
    # add_edge(adjmatrix, 17, 18, 2)
    # add_edge(adjmatrix, 18, 19, 1)
    # add_edge(adjmatrix, 19, 20, 2)
    #
    # add_edge(adjmatrix, 21, 22, 1)
    # add_edge(adjmatrix, 22, 23, 2)
    # add_edge(adjmatrix, 23, 24, 3)
    # add_edge(adjmatrix, 24, 25, 1)
    # add_edge(adjmatrix, 25, 26, 2)
    # add_edge(adjmatrix, 26, 27, 1)
    # add_edge(adjmatrix, 27, 28, 2)
    # add_edge(adjmatrix, 28, 29, 1)
    # add_edge(adjmatrix, 29, 30, 2)
    #
    # add_edge(adjmatrix, 31, 32, 1)
    # add_edge(adjmatrix, 32, 33, 2)
    # add_edge(adjmatrix, 33, 34, 3)
    # add_edge(adjmatrix, 34, 35, 1)
    # add_edge(adjmatrix, 35, 36, 2)
    # add_edge(adjmatrix, 36, 37, 1)
    # add_edge(adjmatrix, 37, 38, 2)
    # add_edge(adjmatrix, 38, 39, 1)
    # add_edge(adjmatrix, 39, 40, 2)
    #
    # add_edge(adjmatrix, 41, 42, 1)
    # add_edge(adjmatrix, 42, 43, 2)
    # add_edge(adjmatrix, 43, 44, 3)
    # add_edge(adjmatrix, 44, 45, 1)
    # add_edge(adjmatrix, 45, 46, 2)
    # add_edge(adjmatrix, 46, 47, 1)
    # add_edge(adjmatrix, 47, 48, 2)
    # add_edge(adjmatrix, 48, 49, 1)
    # add_edge(adjmatrix, 49, 50, 2)
    #
    #
    # for i in range(52):
    #     for j in range(52):
    #         print(adjmatrix[i][j], end=" ")
    #     print()

    # for 200.in
    # adjmatrix = [['x'] * 101 for i in range(101)]
    #
    # add_edge(adjmatrix, 0, 1, 2)
    # add_edge(adjmatrix, 0, 100, 200)
    #
    # add_edge(adjmatrix, 1, 2, 1)
    # add_edge(adjmatrix, 2, 3, 2)
    # add_edge(adjmatrix, 3, 4, 1)
    # add_edge(adjmatrix, 4, 5, 2)
    # add_edge(adjmatrix, 5, 6, 1)
    # add_edge(adjmatrix, 6, 7, 2)
    # add_edge(adjmatrix, 7, 8, 1)
    # add_edge(adjmatrix, 8, 9, 2)
    # add_edge(adjmatrix, 9, 10, 1)
    # add_edge(adjmatrix, 10, 20, 2)
    # add_edge(adjmatrix, 20, 11, 10)
    # add_edge(adjmatrix, 11, 12, 2)
    # add_edge(adjmatrix, 12, 13, 2)
    # add_edge(adjmatrix, 13, 14, 2)
    # add_edge(adjmatrix, 14, 15, 2)
    # add_edge(adjmatrix, 15, 16, 2)
    # add_edge(adjmatrix, 16, 17, 2)
    # add_edge(adjmatrix, 17, 18, 2)
    # add_edge(adjmatrix, 18, 19, 2)
    # add_edge(adjmatrix, 19, 1, 15)
    #
    # add_edge(adjmatrix, 20, 21, 1)
    # add_edge(adjmatrix, 21, 22, 2)
    # add_edge(adjmatrix, 23, 24, 1)
    # add_edge(adjmatrix, 24, 25, 2)
    # add_edge(adjmatrix, 25, 26, 1)
    # add_edge(adjmatrix, 26, 27, 2)
    # add_edge(adjmatrix, 27, 28, 1)
    # add_edge(adjmatrix, 28, 29, 2)
    # add_edge(adjmatrix, 29, 30, 1)
    # add_edge(adjmatrix, 30, 40, 2)
    # add_edge(adjmatrix, 42, 31, 10)
    # add_edge(adjmatrix, 31, 32, 2)
    # add_edge(adjmatrix, 32, 33, 2)
    # add_edge(adjmatrix, 33, 34, 2)
    # add_edge(adjmatrix, 34, 35, 2)
    # add_edge(adjmatrix, 35, 36, 2)
    # add_edge(adjmatrix, 36, 37, 2)
    # add_edge(adjmatrix, 37, 38, 2)
    # add_edge(adjmatrix, 38, 39, 2)
    # add_edge(adjmatrix, 39, 21, 15)
    #
    # add_edge(adjmatrix, 40, 41, 1)
    # add_edge(adjmatrix, 41, 42, 2)
    # add_edge(adjmatrix, 43, 44, 1)
    # add_edge(adjmatrix, 44, 45, 2)
    # add_edge(adjmatrix, 45, 46, 1)
    # add_edge(adjmatrix, 46, 47, 2)
    # add_edge(adjmatrix, 47, 48, 1)
    # add_edge(adjmatrix, 48, 49, 2)
    # add_edge(adjmatrix, 49, 50, 1)
    # add_edge(adjmatrix, 50, 60, 2)
    # add_edge(adjmatrix, 60, 51, 10)
    # add_edge(adjmatrix, 51, 52, 2)
    # add_edge(adjmatrix, 52, 53, 2)
    # add_edge(adjmatrix, 53, 54, 2)
    # add_edge(adjmatrix, 54, 55, 2)
    # add_edge(adjmatrix, 55, 56, 2)
    # add_edge(adjmatrix, 56, 57, 2)
    # add_edge(adjmatrix, 57, 58, 2)
    # add_edge(adjmatrix, 58, 59, 2)
    # add_edge(adjmatrix, 59, 41, 15)
    #
    # add_edge(adjmatrix, 60, 61, 1)
    # add_edge(adjmatrix, 61, 62, 2)
    # add_edge(adjmatrix, 63, 64, 1)
    # add_edge(adjmatrix, 64, 65, 2)
    # add_edge(adjmatrix, 65, 66, 1)
    # add_edge(adjmatrix, 66, 67, 2)
    # add_edge(adjmatrix, 67, 68, 1)
    # add_edge(adjmatrix, 68, 69, 2)
    # add_edge(adjmatrix, 69, 70, 1)
    # add_edge(adjmatrix, 70, 80, 2)
    # add_edge(adjmatrix, 80, 71, 10)
    # add_edge(adjmatrix, 71, 72, 2)
    # add_edge(adjmatrix, 72, 73, 2)
    # add_edge(adjmatrix, 73, 74, 2)
    # add_edge(adjmatrix, 74, 75, 2)
    # add_edge(adjmatrix, 75, 76, 2)
    # add_edge(adjmatrix, 76, 77, 2)
    # add_edge(adjmatrix, 77, 78, 2)
    # add_edge(adjmatrix, 78, 79, 2)
    # add_edge(adjmatrix, 79, 61, 15)
    #
    # add_edge(adjmatrix, 80, 81, 1)
    # add_edge(adjmatrix, 81, 82, 2)
    # add_edge(adjmatrix, 83, 84, 1)
    # add_edge(adjmatrix, 84, 85, 2)
    # add_edge(adjmatrix, 85, 86, 1)
    # add_edge(adjmatrix, 86, 87, 2)
    # add_edge(adjmatrix, 87, 88, 1)
    # add_edge(adjmatrix, 88, 89, 2)
    # add_edge(adjmatrix, 89, 90, 1)
    # add_edge(adjmatrix, 90, 100, 2)
    # add_edge(adjmatrix, 100, 91, 10)
    # add_edge(adjmatrix, 91, 92, 2)
    # add_edge(adjmatrix, 92, 93, 2)
    # add_edge(adjmatrix, 93, 94, 2)
    # add_edge(adjmatrix, 94, 95, 2)
    # add_edge(adjmatrix, 95, 96, 2)
    # add_edge(adjmatrix, 96, 97, 2)
    # add_edge(adjmatrix, 97, 98, 2)
    # add_edge(adjmatrix, 98, 99, 2)
    # add_edge(adjmatrix, 99, 81, 15)

    # for 200.in part2
    adjmatrix = [['x'] * 45 for i in range(45)]

    add_edge(adjmatrix, 0, 1, 1)
    add_edge(adjmatrix, 1, 2, 1)
    add_edge(adjmatrix, 2, 3, 1)
    add_edge(adjmatrix, 3, 4, 1)
    add_edge(adjmatrix, 4, 5, 1)
    add_edge(adjmatrix, 5, 6, 1)
    add_edge(adjmatrix, 6, 7, 1)
    add_edge(adjmatrix, 7, 8, 1)
    add_edge(adjmatrix, 8, 9, 1)
    add_edge(adjmatrix, 9, 10, 1)
    add_edge(adjmatrix, 10, 1, 1)

    add_edge(adjmatrix, 1, 11, 1)
    add_edge(adjmatrix, 11, 12, 1)
    add_edge(adjmatrix, 12, 13, 1)
    add_edge(adjmatrix, 13, 14, 1)
    add_edge(adjmatrix, 14, 15, 1)
    add_edge(adjmatrix, 15, 16, 1)
    add_edge(adjmatrix, 16, 17, 1)
    add_edge(adjmatrix, 17, 18, 1)
    add_edge(adjmatrix, 18, 19, 1)
    add_edge(adjmatrix, 19, 20, 1)

    add_edge(adjmatrix, 20, 21, 1)
    add_edge(adjmatrix, 21, 22, 1)
    add_edge(adjmatrix, 22, 23, 1)
    add_edge(adjmatrix, 23, 24, 1)
    add_edge(adjmatrix, 24, 25, 1)
    add_edge(adjmatrix, 25, 26, 1)
    add_edge(adjmatrix, 26, 27, 1)
    add_edge(adjmatrix, 27, 28, 1)
    add_edge(adjmatrix, 28, 29, 1)
    add_edge(adjmatrix, 29, 30, 1)
    add_edge(adjmatrix, 30, 20, 1)

    add_edge(adjmatrix, 20, 31, 1)

    add_edge(adjmatrix, 31, 32, 1)
    add_edge(adjmatrix, 32, 33, 1)
    add_edge(adjmatrix, 33, 34, 1)
    add_edge(adjmatrix, 34, 35, 1)

    add_edge(adjmatrix, 35, 36, 1)
    add_edge(adjmatrix, 36, 37, 1)
    add_edge(adjmatrix, 37, 38, 1)
    add_edge(adjmatrix, 38, 39, 1)
    add_edge(adjmatrix, 39, 35, 1)

    add_edge(adjmatrix, 35, 40, 1)
    add_edge(adjmatrix, 40, 41, 1)
    add_edge(adjmatrix, 41, 42, 1)
    add_edge(adjmatrix, 42, 43, 1)
    add_edge(adjmatrix, 43, 0, 1)

    add_edge(adjmatrix, 43, 44, 1)





    for i in range(45):
        for j in range(45):
            print(adjmatrix[i][j], end=" ")
        print()



def count(value):
    for i in range(value):
        print(' '.join([str(i) for i in range(value)]))

if __name__== '__main__':
    make_matrix()
    #count(45)
    #returnLen()



