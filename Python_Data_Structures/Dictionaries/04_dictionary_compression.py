# 1 → 10
# 2 → 20
# 3 → 30
# 4 → 40
# 5 → 50


results={i : i*10 for i in range(1,6)}
for key,value in results.items():
    print(key,"->",value)
    
