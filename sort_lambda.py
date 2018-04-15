# ordnen, 
stus = [{"name":"laowang", "age": 12},{"name":"wu", "age": 23}, {"name":"lao", "age": 32}]
num = [11,234,22,2345,33,1111,44,55,66,77,88,99]

num.sort()
print(num)

stus.sort(key = lambda x:x['name']) # limian de  yige x shi yige zidian {} de suoyou nei rong
print(stus)


stus.sort(key = lambda x:x['age']) # limian de  yige x shi yige zidian {} de suoyou nei rong
print(stus)
