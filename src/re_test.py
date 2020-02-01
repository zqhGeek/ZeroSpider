import re

line = "dataLayer.push({'event':'14100','搜索页位置':1,'1级分类':'日用百货','2级分类':'生活用品','3级分类':'安全健康','商城':'天猫精选','品牌':'Nan ji ren/南极人','频道':'好价频道','tab':'综合','pagetitle':'南极人口罩男女冬季时尚韩版防寒保暖防尘透气pm2.5可爱个性黑色 *3件','word':'口罩','pageid':'18887186'})"

pattern = re.compile(r"pageid':'.*", re.S)  # 匹配ID
# 匹配所有符合条件的内容
id = re.search(pattern, line)
search = re.search(r"[1-9]\d*", id.group())
print(id.group())
print(search.group())
