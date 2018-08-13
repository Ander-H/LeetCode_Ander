"""
20180813
参考 two_pass_01.py ，改写的代码

计算连通域个数和最大连通域的像素个数
"""


#find father and update


def find_fa(x):
    """

    :param x: the index of position
    :return:
    """
    global count, fa, cc
    fx = fa[x]  # father's index of index x.
    if fa[fx] == fx:  # if father has no father, no more search
        return fx
    else:  # update x's father
        fa[x] = find_fa(fx)
        return fa[x]


def two_pass(img):
    """
    计算连通域个数和最大连通域的像素个数
    :param img: Binary 2d-array. Value 1 is connected.
    :return:
    """
    global count, fa, cc
    if len(img) == 0:
        return 0
    if not isinstance(img[0], list):
        img = [img]
    fa = list(range(len(img) * len(img[0])))  # father node
    cc = [1 for _ in range(len(img) * len(img[0]))]  # count connected components area of fa[]

    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]  # the relative coordinates of neighborhood pixels

    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 1:
                for dir in range(8):
                    nx = dx[dir] + i  # X-coordinate(row-index) of neighborhood pixels.
                    ny = dy[dir] + j  # Y-coordinate(col-index) of neighborhood pixels.

                    # 比较四周8个领域的像素值，以及坐标边界
                    if nx >= 0 and nx < len(img) and ny >= 0 and ny < len(img[0]) and img[nx][ny] == 1:
                        a = i * len(img[0]) + j  # index of the pixel at (i, j)
                        b = nx * len(img[0]) + ny  # index of the neighborhood pixel

                        pa = find_fa(a)
                        pb = find_fa(b)

                        # merge father
                        if pa < pb:
                            fa[pb] = pa
                            cc[pa] += cc[pb]
                            cc[pb] = 0
                        elif pa > pb:
                            fa[pa] = pb
                            cc[pb] += cc[pa]
                            cc[pa] = 0

    # # 这个不用要好像也可以？
    # for i in range(len(img)):
    #     for j in range(len(img[0])):
    #         if img[i][j] == 1:
    #             a = i * len(img[0]) + j
    #             find_fa(a)

    num_areas = set()
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j] == 1:
                a = i * len(img[0]) + j
                num_areas.add(fa[a])
    id_areas = list(num_areas)
    num_pixels = []
    for connect in id_areas:
        num_pixels.append(cc[connect])

    return id_areas, num_pixels



img = [
    [0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
]

ffa = [
    [0, 0, 2, 0, 0, 5, 0],
    [2, 2, 2, 0, 5, 5, 5],
    [0, 0, 2, 0, 0, 5, 0],
    [0, 2, 2, 0, 5, 5, 0],
]


# img = [
#     [0, 0, 0, 1, 1, 1, 0],
#     [1, 1, 1, 0, 0, 1, 1],
#     [0, 0, 0, 1, 0, 1, 0],
#     [1, 1, 1, 0, 1, 1, 0],
# ]
#
# ffa = [
#     [0, 0, 0, 3, 3, 3, 0],
#     [3, 3, 3, 0, 0, 3, 3],
#     [0, 0, 0, 3, 0, 3, 0],
#     [21, 21, 3, 0, 3, 3, 0],
# ]
res_id, res_pixels = two_pass(img)
nums = len(res_id)
max_area = max(res_pixels)
print(nums, max_area)