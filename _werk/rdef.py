import re

def makeTable(x):
    keys = x.keys()
    kesy = list(keys)
    lengte = len(x[0])

    types=[]
    for x in range(lengte):
            types.append(str(type(x[0][f"{keys[x]}"])))
    
    sqlstring = f'create table if not exists {x["url"]}('
    toevoeg = ""
    for i in range(lengte):  
            #alle kesy die status als naam hebben moeten worden aangepast naar statuss omdat status niet mag in sql
            if keys[i] == "status":
                keys[i] = "statuss"
                keys[i] = re.sub("[']", "'", keys[i])
                #we checken of de key 'id' is, zo ja zullen we deze gebruiken als primary key
                if keys[i]=="Id" or keys[i]=="id":
                            if "str" in types[i]:
                                sqlstring += f"{keys[i]} varchar(255) primary key not null, "
                                toevoeg += f"{keys[i]}, "
                            elif "int" in types[i]:
                                sqlstring+= f"{keys[i]} integer primary key not null, "
                                toevoeg += f"{keys[i]}, "
                            elif "NoneType" in types[i]:
                                pass
                            elif "bool" in types[i]:
                                sqlstring += f"{keys[i]} boolean primary key not null, "
                                toevoeg += f"{keys[i]}, "
                            elif "float" in types[i]:
                                sqlstring += f"{keys[i]} float primary key not null, "
                                toevoeg += f"{keys[i]}, "
                            else:
                                pass
                else:             
                            if "str" in types[i]:
                                sqlstring += f"{keys[i]} varchar(255), "
                                toevoeg += f"{keys[i]}, "
                            elif "int" in types[i]:
                                sqlstring+= f"{keys[i]} integer, "
                                toevoeg += f"{keys[i]}, "
                            elif "NoneType" in types[i]:
                                pass
                            elif "bool" in types[i]:
                                sqlstring += f"{keys[i]} boolean, "
                                toevoeg += f"{keys[i]}, "
                            elif "float" in types[i]:
                                sqlstring += f"{keys[i]} float, "
                                toevoeg += f"{keys[i]}, "
                            else:
                                pass
            #---------------------------------------------------------------------------------------------    
            else:
                #alle kesy die order als naam hebben moeten worden aangepast naar orde omdat order niet mag in sql
                if keys[i] == "order":
                        keys[i] = "orde"
                        keys[i] = re.sub("[']", "'", keys[i])
                        keys[i] = re.sub("[']", "'", keys[i])
                        if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255) primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
                        else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255), "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
                else:
                    if keys[i]=="by" :
                        keys[i] = "bye"
                        if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255) primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
                        else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255), "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
                    else:             
                            if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255) primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
                            else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(255), "
                                        toevoeg += f"{keys[i]}, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                        toevoeg += f"{keys[i]}, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                        toevoeg += f"{keys[i]}, "
                                    else:
                                        pass
    sqlstring = sqlstring[:- 2]     
    sqlstring +=")"                       
    print(sqlstring)
    return sqlstring