import copy
##############################
# 指定した商品データを削除する処理
##############################
def deleteProduct(nowPos):
        global product
        for i in reversed(range(len(product))):
                #削除したので、ループ回数上限を再チェック
               # if i >= len(product):
               #         break
                if nowPos == product[i][2]:
                       del product[i]
 #       product = [ x for x in product if product[x][2] != nowPos ]

##############################
# 指定の場所までの距離を取得する処理
##############################
NODE_ROUTE = 0  # 経路情報
NODE_DEFINED = 1  # 確定ノードフラグ
NODE_COST = 2  # コスト
NODE_CHG_FROM = 3  # どのノードに変更されたか


def getDistance(x, y):
        global route
        global temp_node

        temp_node.clear()
        temp_node = [[] for i in range(V)]  # ([経路情報]、確定ノードフラグ、コストi、ノード変更元)


        distance = 100

        for i in range(V):
                temp_node[i].append(copy.deepcopy(es[i]))#経路情報
                temp_node[i].append(0)  #確定ノードフラグ
                temp_node[i].append(-1) #コスト
                temp_node[i].append(0)  #ノード変更元

        #スタートノードのコストは0
        temp_node[y][NODE_COST] = 0

        while 1:
                #確定ノードを探索
                for i in range(V):
                        if temp_node[i][NODE_DEFINED] == 1 or temp_node[i][NODE_COST] < 0:
                                continue
                        else:
                                break
                #全て確定ノードになったら完了
                loop_end_flag = 1
                for k in range(len(temp_node)):
                       if temp_node[k][NODE_DEFINED] == 0:
                               loop_end_flag = 0
                if loop_end_flag == 1:
                        break

                #ノードを確定させる
                temp_node[i][NODE_DEFINED] = 1

                #行先のノード情報を更新する
                temp_node_to   = 0
                temp_node_cost = 0
                for j in range(len(temp_node[i][NODE_ROUTE])):
                        temp_node_to   = temp_node[i][NODE_ROUTE][j][0]
                        temp_node_cost = temp_node[i][NODE_COST] + temp_node[i][NODE_ROUTE][j][1]
                        if temp_node[temp_node_to][NODE_COST] < 0:
                                temp_node[temp_node_to][NODE_COST] = temp_node_cost
                                temp_node[temp_node_to][NODE_CHG_FROM] = i
                        elif temp_node[temp_node_to][NODE_COST] > temp_node_cost:
                                temp_node[temp_node_to][NODE_COST] = temp_node_cost
                                temp_node[temp_node_to][NODE_CHG_FROM] = i
                        if temp_node_to == y:
                                loop_end_flag = 1

        #探索結果から距離とルートを確定
        distance = decide_route(x,y)

        return distance

##############################
# 探索結果から距離とルートを確定
##############################
def decide_route(x,y):

        cost=0
        route_num = 0
        i=x
        route.clear()
        distance=0
        while 1:
                cost = cost + temp_node[i][NODE_COST]
                if y == i:
                        distande = cost
                        break
                moto_node = i
                i = temp_node[i][NODE_CHG_FROM]#次の行先を取得
                route.append([i,0])#次の行先をルートに追加
                #行先ルートのコストを取得する
                for j in range(len(temp_node[moto_node][0])):#持ってるルート内の
                        if temp_node[moto_node][0][j][0] == route[route_num][0]:#行先を探索
                                route[route_num][1]=temp_node[moto_node][0][j][1]
                distance = distance + route[route_num][1]
                route_num = route_num + 1

        return distance

##############################
# 商品リストから目的地を決定する処理
##############################
route = []
def getTargetPos(now_pos):
        global product
        global pos
        global route
        global prePos

        #route = [None for i in range(200)]
#        pos = -1
#        distance = 201
#        for i in range(len(product)):
#                if distance > getDistance(now_pos,product[i][2]):
#                        distance = getDistance(now_pos,product[i][1])
#                        pos = product[i][2]

#        for i in range(len(product)):
#                break

        #注文が滞ったら
        count = 0
        for i in range(len(order)):
                #if order[i][0] == currentTime:
                if time_step_before < order[i][0] <= time_step:
                        count = count + 1


        #とりあえず上から順番に配達する
        if count > len(product)/2:
                pos = 0
        else:
                pos = (product[-1][2])
        return pos

##############################
# お店で商品を受け取る処理
##############################
product=[]
def getProduct(currentTime):
        for i in range(len(order)):
                #if order[i][0] == currentTime:
                if time_step_before < order[i][0] <= currentTime:
                        product.append ( copy.deepcopy(order[i]) )

##############################
# 指定の場所まで車を進める処理
##############################
prePos=0
def gotoVertex(x,y):
        global nowPos
        global route
        global total_move_count
        #コマンド出力
        prePos = nowPos
        nowPos = -1
        print (route[0][0]+1)
        route[0][1] = route[0][1] - 1
        if route[0][1] == 0:
                deleteProduct(route[0][0])  # 通過した場合は荷物を配達する
                nowPos = route[0][0]  # nowPosを目的地点まで進める
                del route[0]

##############################
# その場で待機するか、配達に行くか決定する
##############################
def selectWait():
        global wait_cost
        global go_cost
        global result_cost

        #次の注文までの待ち時間
        for i in range(len(order)):
                if time_step < order[i][0]:
                        wait_cost = order[i][0]-time_step
                        break

        # 行先までのコスト
        if len(product) <= 2:#二週目以降は計算しない
                go_cost   = getDistance(nowPos,product[0][2])

        if wait_cost - go_cost > 0:
                result_cost = wait_cost - go_cost
        else:
                result_cost = go_cost - wait_cost
        #コスト比較
  #      if wait_cost < go_cost:

        if len(product) > 50:
                return 0
        elif wait_cost <= 10:
        #elif wait_cost < go_cost*2:
                return 1
        else:
                return 0

def initProduct(nowPos):
        global temp_node
        global product
        # プロダクト毎に、ダイクストラをかける
#        for i in range(len(product)):
#               #product[i][3] = getDistance(nowPos, product[i][2])
#                product[i][3] = decide_route(nowPos, product[i][2])

        #product[0][3] = getDistance(nowPos,product[0][2])
        #for i in range(len(product)-1):
        #        product[i][3] = getDistance(product[i][2],product[i+1][2])
        #product = sorted(product,key=lambda x:x[3])
        getDistance(nowPos,product[0][2])

        for i in range(len(product)):
                for j in range(len(temp_node)):
                        if product[i][2] == j:#プロダクトと一致するノードがあったら
                                product[i][3] = temp_node[j][2]
        # 出来上がったproductをソート
        product = sorted(product,key=lambda x:x[3])
        #product.reverse()
#        product = sorted(product,key=lambda x:x[3])

# recieve |V| and |E|
V, E = map(int, input().split())
es = [[] for i in range(V)]

for i in range(E):

        # recieve edges
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        es[a].append([b,c])#(行先、経路コスト)
        es[b].append([a,c])#(行先、経路コスト)

T = int(input())

# recieve info
order=[]

temp_node = [[] for i in range(V)]  # ([経路情報]、確定ノードフラグ、コストi、ノード変更元)

total_move_count = 0
for i in range(T):
        Nnew = int(input())
        for j in range(Nnew):
                new_id, dst = map(int, input().split())
                order.append([i, new_id, (dst-1), 0])#(注文時間,注文ID,配達先,処理フラグ)

# insert your code here to get more meaningful output
# all stay

nowPos = 0 # 現在地
targetPos = -1

time_step=0
time_step_before=0

for i in range(T) :
        if time_step >= T:
                break
        #現在地がお店なら注文の商品を受け取る
        if nowPos == 0:
                getProduct(time_step)
                time_step_before = time_step  # 以前訪れた時間
        # if i == 0:#初回のみ
                if len(product) != 0:
                        if selectWait() == 1:
                                print(-1)
                                time_step = time_step + 1
                                total_move_count = total_move_count + 1
                                if time_step >= T:
                                        break
                                continue
                        else:
                                time_step = time_step
                                initProduct(nowPos)
                else:
                        print (-1)
                        time_step = time_step + 1
                        total_move_count = total_move_count + 1
                        if time_step >= T:
                                break
                        continue
                #商品が尽きたら終了
                #if len(product) == 0:
                #        while 1:
                #                gotoVertex(nowPos, 0)
                #                print (-1)
                #                if total_move_count>=T:
                #                        break

        #一番近いところに向かう
        if len(product) != 0:
                targetPos = getTargetPos(nowPos);

                if len(route) == 0:
                        getDistance(nowPos,targetPos)
                gotoVertex(nowPos,targetPos)
                time_step = time_step + 1
                continue
        #持ってる商品情報を削除
  #      if nowPos == targetPos:
  #              deleteProduct(nowPos)
        #次のところへ向かう　以下ループ
        #持っている商品が無くなったらお店へ向かう
        if len(product) == 0 and nowPos != 0:
                if len(route) == 0:
                        getDistance(nowPos,0)
                gotoVertex(nowPos,0)
                time_step = time_step + 1
                continue

#        vardict = input()
#        if vardict == 'NG':
#                sys.exit()
        # the number of orders that have been delivered at time t.
#        Nachive = int(input())
#        for j in range(Nachive):
#                achive_id = int(input())
