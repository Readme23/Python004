def mymap(func, *seqs):
    res = []
    # *seqs 相当于拆解成 list1,list2,...,listN
    for args in zip(*seqs):
        # zip 之后， args 其实是一个元组
        print(args)
        # *args 相当于拆解成 e1,e2,...,eN ,也就是 func(e1,e2,...,eN)
        res.append(func(*args))
    return res