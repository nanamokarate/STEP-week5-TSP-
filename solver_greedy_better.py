#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

##greedyのサンプルコードのこのsolveの中身を書き換えました
##greedyで求めた経路から交差をなくしていきgreedyよりは短い移動距離となる方法をとりました

def solve(cities):
    N = len(cities)
 
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    ##ここまではgreedyのサンプルコードと一緒です！

    ##ここからのコード：greedyで求めた経路tourは交差している箇所がいくつかあるのでその交差を解いて移動距離を減らします

    tour_after = []
    x=0
    while (x != 1):
        y = 0
        for i in range(len(tour)-1):
            ##最後、元の出発点に戻ってくる時の線も考えないといけないので、範囲をlen(tour)までに設定
            for j in range(i+1,len(tour)):
                if j  == len(tour) -1:
                        j = -1
                if (dist[tour[i]][tour[i + 1]] + dist[tour[j]][tour[j + 1]]) > (dist[tour[i]][tour[j]] + dist[tour[i + 1]][tour[j + 1]]):
                    ##連続する2点を2組とり、連続２点同士(iとi+1、jとj+1)で結ぶのとiとj、i+1とj+1で結ぶ場合の距離を比べ、短い方をたどってく（短い方がクロスがないから短い方を選択してたどっていけばクロスがなくなる）
                    if j == -1:
                        tour_before =  tour[:i+1]
                        tour_after = tour[i+1:]
                        for t in range(len(tour_after)):
                            tour_before.append(tour_after[-1-t])
                        tour = tour_before
                    else:
                        tour_before = tour[:i+1]
                        tour_after = tour[i+1:j+1]
                        for l in range(len(tour_after)):
                            tour_before.append(tour_after[-1-l])
                        for h in range(j+1,len(tour)):
                            tour_before.append(tour[h])
                        tour = tour_before
                    y += 1
        if y ==  0:##クロスがなくなったらwhile文から抜ける
            x = 1
    return tour

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
    ##output_csvを書き換えます
    with open('output_'+sys.argv[1].split('.')[0][-1]+'.csv', mode='w') as f:
        f.write('index\n')
        for t in tour:
            f.write(str(t)+'\n')
