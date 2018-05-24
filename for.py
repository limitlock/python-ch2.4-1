# for 반복문

a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

# 복합 자료형을 사용하는 for문
l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]
for data in l:
    print('이름:%s, 나이:%d' % data)

for name, age in l:
    print('이름:{0}, 나이:{1}'.format(name, age))

l = [{'name': '둘리', 'age': 10},
     {'name': '마이콜', 'age': 20},
     {'name': '도우넛', 'age': 30}]

for data in l:
    print('이름:%(name)s, 나이:%(age)d' % data)

# 1~10 합 구하기
s = 0
for i in range(1, 11):
    s += i

print(s)

# break
for i in range(10):
    if i > 5:
        break

    print(i, end=' ')
else:
    print('')

print('-------------------')

# continue
for i in range(10):
    if i <= 5:
        continue

    print(i, end=' ')
else:
    print('')

print('-------------------')

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(str(j) + ' x ' + str(i) + ' = ' + str(i*j), end='\t')
    else:
        print('')
