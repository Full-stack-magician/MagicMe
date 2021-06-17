import re

name = []
name.append('E:\Hchier\A\计算机 fwfWA 基础')
res1 = ''.join(re.findall('[\u4e00-\u9fa5]', name[0]))
print(res1)
