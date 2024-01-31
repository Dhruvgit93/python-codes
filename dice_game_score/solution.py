def score(dice):
    dict={}
    price_rule={
        1:1000,
        2:200,
        3:300,
        4:400,
        5:500,
        6:600
    }
    single_price={
        1:100,
        5:50
    }
    score=0
    for x in dice:
        if x in dict:
            dict[x]+=1
            if dict[x]==3:
                score+=price_rule[x]
                dict[x]=0
        else:
            dict[x]=1
    for x in dict:
        if x in single_price:
            score+=single_price[x]*dict[x]
            dict[x]=0
    return score
    

print(score([5, 1, 3, 4, 1])==250,
      score( [1, 1, 1, 3, 1] )==1100)