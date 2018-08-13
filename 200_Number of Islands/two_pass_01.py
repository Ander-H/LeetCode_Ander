"""
原文网址
https://blog.csdn.net/csuhoward/article/details/78818244
"""


import numpy as np


#find father and update
def find_fa(x):
    global count,fa,cc

    fx = fa[x]
    if fa[fx] == fx:#if father has no father, no more search
        return fx
    else:#update x's father
        fa[x] = find_fa(fx)
        return fa[x]

def two_pass(img, mask=255, area=100):
    #init merge and find set
    global count,fa,cc

    fa = list(range(img.shape[0]*img.shape[1])) #father node
    cc = np.zeros(img.shape[0]*img.shape[1]) #count connected components area of fa[]
    cc = cc+1

    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [-1,1,0,0,-1,1,-1,1]  # 邻域的相对坐标位置

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == mask:
                for dir in range(8):
                    nx = dx[dir] + i
                    ny = dy[dir] + j  # 邻域坐标
                    #　比较四周8个领域的像素值，以及坐标边界
                    if nx >= 0 and nx < img.shape[0] and ny >= 0 and ny < img.shape[1] and img[nx,ny] == mask:
                        a = i*img.shape[1]+j  # 该像素点label索引
                        b = nx*img.shape[1]+ny  # 邻域label索引
                        pa = find_fa(a)#shorten chain
                        pb = find_fa(b)#
                        #merge father
                        if pa<pb:
                            fa[pb]=pa
                            cc[pa]+=cc[pb]
                            cc[pb]=0
                        elif pa>pb:
                            fa[pa]=pb
                            cc[pb]+=cc[pa]
                            cc[pa]=0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == mask:
                a = i*img.shape[1]+j
                find_fa(a)

    count = 0
    colormap = np.zeros((img.shape[0],img.shape[1],3))  # color hash table
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == mask:
                a = i*img.shape[1]+j
                pa = find_fa(a)
                if cc[pa] >= 100: # connected components with area >= 100 pixels
                    pa_i = pa / img.shape[1]
                    pa_j = pa % img.shape[1]
                    if np.max(colormap[pa_i,pa_j,:]) == 0:
                        colormap[pa_i,pa_j,:] = np.random.randint(256,size=3)
                        count += 1
                    colormap[i,j,:] = colormap[pa_i,pa_j,:]
    print(count)
    return colormap
src = np.asarray([[255,255,0,0], [0,0,255,255]])
des = two_pass(src,255,100)