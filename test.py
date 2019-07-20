def is_number(st):
    try:
        int(st[0])
        return True
    except ValueError:
        return False

def numString(st):
  st_d = {}.fromkeys(st, 0)
  for a in st:
    st_d[a] += 1
  num = st_d.values()
  num = list(num)
  return num

def validationСheck(st):
  n = 0
  m = 0
  o = 0
  for i in range(0,len(st) - 1):
    for j in range(0,len(st) - i - 1):
      if st[j] < st[j + 1]:
        st[j],st[j + 1] = st[j + 1], st[j]
  for i in range(len(st)):
    if st[0] == st[i]:
      n += 1
    elif st[0] - st[i] > 1 :
      o += 1
    else:
      m += 1
  if o >= 1:
    return False
  elif o == 0 and n > 0 and m > 0 and m == 1 or n == 1:
    return True
  elif n > 0 and m == 0 and o == 0:
    return True
  elif m >= 2 and n >= 2 :
    return False


def SherlockValidString(s):
  st = list(s)
  num = is_number(st)
  if num is True:
    return 'Неверно введены данные, присутствуют числа!'
  result = numString(st)
  result = validationСheck(result)
  return result


print(SherlockValidString('xyz'))
print(SherlockValidString('xyzaa'))
print(SherlockValidString('xxyyz'))
print(SherlockValidString('xyzzz'))
print(SherlockValidString('xxyyza'))
print(SherlockValidString('xxyyzabc'))
print(SherlockValidString('aaabbbcccddda'))
print(SherlockValidString('123asdasda'))
print(SherlockValidString('ывасваы'))