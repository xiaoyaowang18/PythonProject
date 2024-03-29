# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 16:12
# @Author  : wanghc
# @File    : IsJwdWithInPoly.py
# @Software: PyCharm

'''
射线法就是以判断点开始，向右（或向左）的水平方向作一射线，计算该射线与多边形每条边的交点个数，
如果交点个数为奇数，则点位于多边形内，偶数则在多边形外。该算法对于复合多边形也能正确判断。
'''


def isRayIntersectsSegment(poi, s_poi, e_poi):  # [x,y] [lng,lat]
    # 输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1] == e_poi[1]:  # 排除与射线平行、重合，线段首尾端点重合的情况（纬度相同）
        return False
    if s_poi[1] > poi[1] and e_poi[1] > poi[1]:  # 线段在射线上边
        return False
    if s_poi[1] < poi[1] and e_poi[1] < poi[1]:  # 线段在射线下边
        return False
    if s_poi[1] == poi[1] and e_poi[1] > poi[1]:  # 交点为下端点，对应spoint
        return False
    if e_poi[1] == poi[1] and s_poi[1] > poi[1]:  # 交点为下端点，对应epoint
        return False
    if s_poi[0] < poi[0] and e_poi[0] < poi[0]:  # 线段在射线左边
        return False

    xseg = e_poi[0] - (e_poi[0] - s_poi[0]) * (e_poi[1] - poi[1]) / (e_poi[1] - s_poi[1])  # 求交
    if xseg < poi[0]:  # 交点在射线起点的左侧
        return False
    return True  # 排除上述情况之后


def isPoiWithinPoly(poi, poly):
    # 输入：点，多边形三维数组
    # poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

    # 可以先判断点是否在外包矩形内
    # if not isPoiWithinBox(poi,mbr=[[0,0],[180,90]]): return False
    # 但算最小外包矩形本身需要循环边，会造成开销，本处略去
    sinsc = 0  # 交点个数
    for epoly in poly:  # 循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
        for i in range(len(epoly) - 1):  # [0,len-1]
            s_poi = epoly[i]
            e_poi = epoly[i + 1]
            if isRayIntersectsSegment(poi, s_poi, e_poi):
                sinsc += 1  # 有交点就加1

    return True if sinsc % 2 == 1 else False


def evalute(jd, wd):
    jq_jwd_list = [{"lng": 120.14099, "lat": 30.18902}, {"lng": 120.14129, "lat": 30.18909},
                   {"lng": 120.13752, "lat": 30.19718}, {"lng": 120.13704, "lat": 30.1984},
                   {"lng": 120.13721, "lat": 30.19937}, {"lng": 120.13769, "lat": 30.19952},
                   {"lng": 120.13773, "lat": 30.20037}, {"lng": 120.13789, "lat": 30.20082},
                   {"lng": 120.13834, "lat": 30.20092}, {"lng": 120.13873, "lat": 30.20116},
                   {"lng": 120.1391, "lat": 30.20132}, {"lng": 120.13951, "lat": 30.20219},
                   {"lng": 120.13942, "lat": 30.20272}, {"lng": 120.13949, "lat": 30.20353},
                   {"lng": 120.13885, "lat": 30.20434}, {"lng": 120.13881, "lat": 30.20436},
                   {"lng": 120.14007, "lat": 30.2049}, {"lng": 120.14118, "lat": 30.20517},
                   {"lng": 120.14535, "lat": 30.20549}, {"lng": 120.14571, "lat": 30.20629},
                   {"lng": 120.14507, "lat": 30.20846}, {"lng": 120.14618, "lat": 30.20979},
                   {"lng": 120.14837, "lat": 30.21111}, {"lng": 120.15024, "lat": 30.21229},
                   {"lng": 120.15108, "lat": 30.21344}, {"lng": 120.15181, "lat": 30.21458},
                   {"lng": 120.15934, "lat": 30.2217}, {"lng": 120.16007, "lat": 30.22544},
                   {"lng": 120.15966, "lat": 30.2277}, {"lng": 120.1603, "lat": 30.22852},
                   {"lng": 120.15985, "lat": 30.22983}, {"lng": 120.15957, "lat": 30.2315},
                   {"lng": 120.15773, "lat": 30.23286}, {"lng": 120.1561, "lat": 30.23339},
                   {"lng": 120.15644, "lat": 30.23449}, {"lng": 120.15663, "lat": 30.23519},
                   {"lng": 120.15758, "lat": 30.23595}, {"lng": 120.1585, "lat": 30.23725},
                   {"lng": 120.15841, "lat": 30.23936}, {"lng": 120.15824, "lat": 30.24114},
                   {"lng": 120.15938, "lat": 30.24253}, {"lng": 120.16103, "lat": 30.2458},
                   {"lng": 120.16086, "lat": 30.24795}, {"lng": 120.16191, "lat": 30.24958},
                   {"lng": 120.16311, "lat": 30.25013}, {"lng": 120.16318, "lat": 30.25165},
                   {"lng": 120.15942, "lat": 30.25751}, {"lng": 120.15809, "lat": 30.26133},
                   {"lng": 120.15481, "lat": 30.26036}, {"lng": 120.1511, "lat": 30.26066},
                   {"lng": 120.1505, "lat": 30.26201}, {"lng": 120.14822, "lat": 30.26242},
                   {"lng": 120.14936, "lat": 30.26318}, {"lng": 120.14932, "lat": 30.2635},
                   {"lng": 120.14977, "lat": 30.26368}, {"lng": 120.15024, "lat": 30.26264},
                   {"lng": 120.15116, "lat": 30.263}, {"lng": 120.14972, "lat": 30.26402},
                   {"lng": 120.14923, "lat": 30.26461}, {"lng": 120.14762, "lat": 30.26335},
                   {"lng": 120.14672, "lat": 30.26416}, {"lng": 120.14805, "lat": 30.26555},
                   {"lng": 120.14732, "lat": 30.26731}, {"lng": 120.13597, "lat": 30.26355},
                   {"lng": 120.13606, "lat": 30.26207}, {"lng": 120.13391, "lat": 30.26118},
                   {"lng": 120.13228, "lat": 30.25792}, {"lng": 120.13146, "lat": 30.25369},
                   {"lng": 120.12863, "lat": 30.25525}, {"lng": 120.12876, "lat": 30.25562},
                   {"lng": 120.12919, "lat": 30.25547}, {"lng": 120.12889, "lat": 30.25647},
                   {"lng": 120.12816, "lat": 30.25647}, {"lng": 120.12558, "lat": 30.2577},
                   {"lng": 120.11773, "lat": 30.25847}, {"lng": 120.10983, "lat": 30.25981},
                   {"lng": 120.10614, "lat": 30.25581}, {"lng": 120.10657, "lat": 30.25217},
                   {"lng": 120.09602, "lat": 30.24743}, {"lng": 120.09172, "lat": 30.24246},
                   {"lng": 120.08623, "lat": 30.23579}, {"lng": 120.08546, "lat": 30.23215},
                   {"lng": 120.08657, "lat": 30.23015}, {"lng": 120.08409, "lat": 30.22592},
                   {"lng": 120.07911, "lat": 30.22533}, {"lng": 120.07773, "lat": 30.22399},
                   {"lng": 120.07748, "lat": 30.2214}, {"lng": 120.07645, "lat": 30.21992},
                   {"lng": 120.07713, "lat": 30.21858}, {"lng": 120.07653, "lat": 30.21784},
                   {"lng": 120.07696, "lat": 30.21598}, {"lng": 120.07902, "lat": 30.21495},
                   {"lng": 120.07722, "lat": 30.21279}, {"lng": 120.07593, "lat": 30.20916},
                   {"lng": 120.07851, "lat": 30.20649}, {"lng": 120.07902, "lat": 30.19929},
                   {"lng": 120.07902, "lat": 30.19677}, {"lng": 120.07524, "lat": 30.19329},
                   {"lng": 120.07602, "lat": 30.19084}, {"lng": 120.07902, "lat": 30.18943},
                   {"lng": 120.08057, "lat": 30.18772}, {"lng": 120.08091, "lat": 30.18594},
                   {"lng": 120.0816, "lat": 30.18208}, {"lng": 120.08623, "lat": 30.18112},
                   {"lng": 120.09121, "lat": 30.17874}, {"lng": 120.09447, "lat": 30.17533},
                   {"lng": 120.09593, "lat": 30.17277}, {"lng": 120.09705, "lat": 30.17485},
                   {"lng": 120.09872, "lat": 30.17759}, {"lng": 120.10215, "lat": 30.17852},
                   {"lng": 120.10361, "lat": 30.18008}, {"lng": 120.10396, "lat": 30.18327},
                   {"lng": 120.10606, "lat": 30.1829}, {"lng": 120.10808, "lat": 30.18316},
                   {"lng": 120.1085, "lat": 30.18731}, {"lng": 120.11129, "lat": 30.18687},
                   {"lng": 120.11383, "lat": 30.18346}, {"lng": 120.11477, "lat": 30.1849},
                   {"lng": 120.11674, "lat": 30.18383}, {"lng": 120.11576, "lat": 30.18279},
                   {"lng": 120.11614, "lat": 30.18271}, {"lng": 120.1167, "lat": 30.18327},
                   {"lng": 120.1246, "lat": 30.18316}, {"lng": 120.12872, "lat": 30.18668},
                   {"lng": 120.13086, "lat": 30.18794}, {"lng": 120.13842, "lat": 30.19299},
                   {"lng": 120.13855, "lat": 30.19306}, {"lng": 120.13855, "lat": 30.1931},
                   {"lng": 120.1385, "lat": 30.19314}, {"lng": 120.14065, "lat": 30.18891},
                   {"lng": 120.14056, "lat": 30.18887}]
    poly = [[]]
    poi = [jd, wd]
    for i in jq_jwd_list:
        i_jd = i['lng']
        i_wd = i['lat']
        poly[0].append([i_jd, i_wd])
    sinsc = 0  # 交点个数
    for epoly in poly:  # 循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
        for i in range(len(epoly) - 1):  # [0,len-1]
            s_poi = epoly[i]
            e_poi = epoly[i + 1]
            if isRayIntersectsSegment(poi, s_poi, e_poi):
                sinsc += 1  # 有交点就加1
    return True if sinsc % 2 == 1 else False


print(evalute(120.08780311638733, 30.205983945303636))
