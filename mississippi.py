test_str = "mississippi"
res = {}
for keys in test_str:
    res[keys] = res.get(keys,0) + 1
    print("count of all characters in mississippi is : \n" +str(res))
        
        