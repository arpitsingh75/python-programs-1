str1=input("'Enter any string:'")
index=0
for i in str1:
    print(str1[:index-1])
    index-=1
