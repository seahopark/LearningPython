# 수와 계산 형식
print (10 + 5)
print (10 - 5)
print (10 / 5)
print (10 * 5)

#문자열 표현
print ('Hello')
print ("hello")
print ("hello World!")
print ("hello 'World!'")

#----------
print ('hello ' '+' 'World!')
print ('hello '*3)
print ('hello '[0])
print ('hello '[1])
print ('hello '[2])

#----------
print ('hello world' .capitalize())
print ('hello world' .upper())
print ('hello world' .__len__())
print (len('hello world'))
print ('hello world' .replace('world','programming'))

#------------
print("egoing's \"tutorial\"")
print("\\")
print("Hello\nworld")
print("Hello\tworld")
print('Hello\tworld')

#------------
print (10 + 5)
print ("10" + "5")

#변수
x=10
y=5
print (x+y)

title= "python"
print("Title is "+title)

#------------
#안녕하세요 {username}님,
#지금부터 {username}님을 위한 클라스를 시작할게요 구현
username="{username}"
print("안녕하세요 "+ username +"님")
print("지금부터 "+ username +"님을 위한 클라스를 시작할게요")

#------------
#수학계산 적용
x = 5.5
y = 100
z = y*(10.00-x)
print(x)
print(y)
print(z)

#Boolin
print(1==1)
print(1==2)
print(1<2)
print(1>2)
print(True)
print(False)

#Condition Statements
if True:
    print("Code1")
    print("Code2")
print("Code3")

#------------------
input = 12345
real = 12346
if real == input:
    print("Hello!")
else:
    print("Sorry!")

#------------------
input = 12345
real_1 = 12346
real_2 = 12347
if real_1 == input:
    print("Hello real_1!")
elif real_2 == input:
        print("Hello real_2!")
else:
    print("Sorry!")

#논리연산자
