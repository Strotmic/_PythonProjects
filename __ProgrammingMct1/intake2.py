def translate(spreektaal, woord):
    if spreektaal == "Frans":
        dic = {"hond":"chien","kat":"chat"}
        for i in dic :
            if i == woord:
                print(dic[woord])
    else:
        dic = {"hond":"dog", "kat": "cat"}
        for i in dic :
            if i == woord:
                print(dic[woord])

translate("Frans","kat")