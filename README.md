# STEP-week5-TSP-
#	TSP challenge　

from https://github.com/hayatoito/google-step-tsp 

##	解法

better_greedy : greedy（貪欲法）によって見つけたルートを改善

→クロスしているところを解いていき、最終的に一箇所も交わらずに元の位置に戻ってくるようにする

###	クロスの解き方

連続する2点を2組とり、連続２点同士(iとi+1、jとj+1)で結ぶのとiとj、i+1とj+1で結ぶ場合の距離を比べ、
短い方をたどってく

（短い方がクロスがないから短い方を選択してたどっていけばクロスがなくなる）

## 測定結果

| | challenge0 | challenge1 | challenge2 | challenge3 | challenge4 | challenge5 | challenge6 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|---:|
|greedy |3,418.10 |3,832.29 |5,449.44 |10,519.16 |12,684.06 |25,331.84 |49,892.05 |
|better_greedy |3,418.10 |3,832.29 |4,994.89 |8,970.05 |11,489.79|21,363.60 |42,712.37 |

better_greedyがgreedyよりも短い移動距離になった!
