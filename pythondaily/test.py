flag=True
flag1=False
if flag:
    print("正确")
elif flag1:
    print("错误")


#and   or    not
#使用int()将字符串转化为int型




if flag and flag1:
    print("通过测试")
else:
    print("meiyoutongguo")



    custom={
        "aaa": 1,
        "bbb": 2,
        "ccc": 3


    }

    custom["id"]="12345"



    print(custom["aaa"])
    print(custom.get("bbb"))
    print(custom.get("id"))


#注意冒号
    for item in range(80,100,2):
        print(item)

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


for row in matrix:
    for  col in row:
        print(col)



#解包功能
cad=["aaa","ddd",123]
b,c,d=cad;
print(b)
print(c)
print(d)


try:
    num = int(input("输入数据"))
    print(num)

except:
   print("已经捉到异常了")




#storyfile=open("filedemo.txt","r")
#content=storyfile.read();
#print(content)
#storyfile.close()



#content=storyfile.readlines();
#print(content[0])









storyfile=open("filedemo.txt","r")
content=storyfile.read()
dest=open("desc.txt","w")
dest.write(content)
desc.close()
content.close()




class Student:
    def __init__(self,name,age):
        self.__name=name  #保证在类的外部不可以进行访问
        self.age=age


pony = Student("qq",22);
print(pony.age)
print("hello")


#class collage(student)实现college继承student

#模块相当于java的类，引入一个模块，在其中写上import 模块名

print(dir())












