def dicresult():
    result = {}  # 存储文字结果
    with open("data.txt", 'rt', encoding='utf-8') as f:
        text = f.read()
    for word in text.split():
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result
def director():
    result = dicresult()#获取数据
    result_director = {}#从数据中取出导演存放
    max_directors = {}  # 存放最大电影数导演,可能不止一个
    for key in result:
        if key[0:2]=="导演":
            result_director[key] = result[key]
    max_director_moves = max(result_director.items(), key=lambda x: x[1])[1]#找出一个导演电影数最大值
    for key, value in result_director.items():
        if value == max_director_moves:
            max_directors[key] = value
    print("导演电影数最多的导演如下:\n"+str(max_directors))

def actor():
    result = dicresult()#获取数据
    actor_str = ""#拼接一个演员的字符串
    dic_result={}#演员数据字典
    max_dic_result={}#存放出演电影最多演员，可能不止一个
    for key in result:
        if key[0: 2] == '演员': #key = 演员1，演员2，演员3，演员4
            actor_str += str(key)+'，'
    actordata = actor_str.split("，")
    for actor in actordata:
        if actor not in dic_result:
            dic_result[actor] = 0
        dic_result[actor] += 1
    max_move_actors = max(dic_result.items(), key=lambda x: x[1])[1]#找出一个演电影数最大值
    for key, value in dic_result.items():
        if value == max_move_actors:
            max_dic_result[key] = value
    print("出演电影数最多的演员如下:\n" + str(max_dic_result))
def actors_coopration():
    result = dicresult()
    dic_movie_actors = {}#存放电影对应的演员组合
    i = 0
    for word in result:
        if word[0: 2] == '演员':
            i += 1
            dic_movie_actors[('电影'+str(i))] = word.split("，")
    import pandas as pd
    df = pd.DataFrame(dic_movie_actors)
    print(df)
#    循环df的每一列，存入字典
    dic_movie_actors_result={}
    for index, row in df.iteritems():
        col = df[index]
        for it in col:
            for next in col:
                if it != next:
                    key = it + ',' + next
                    yek = next + ',' + it
                    if key not in dic_movie_actors_result:
                        dic_movie_actors_result[key] = 0
                    dic_movie_actors_result[key] += 1
    max_actor_coop = max(dic_movie_actors_result.items(), key=lambda x: x[1])[1]#找出一个演电影数最大值
    dic_max={}#存放最终结果
    for key, value in dic_movie_actors_result.items():
        if value == max_actor_coop:
            dic_max[key] = value
    print("两个演员合作此时最多组合：\n"+str(dic_max))
if __name__ == '__main__':
    director()
    actor()
    actors_coopration()


