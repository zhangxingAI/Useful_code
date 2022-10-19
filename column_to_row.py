colfile=open(r'1.txt')
rowfile1=open(r'rows1.txt','w')
rowfile2=open(r'rows2.txt','w')
rowfile3=open(r'rows3.txt','w')
rowfile4=open(r'rows4.txt','w')
rowfile5=open(r'rows5.txt','w')
rowfile6=open(r'rows6.txt','w')
rowfile7=open(r'rows7.txt','w')
rowfile8=open(r'rows8.txt','w')
rowfile9=open(r'rows9.txt','w')

rowlist=[]
for line in colfile.readlines():
 collist=line.split()
 index=0

 for col in collist:
    try:
       rowlist.append(col)
    except IndexError:
       rowlist.append([col])
    index=index+1

for row in rowlist[0:149]:
    rowfile1.write(row+'@qq.com;')
colfile.close()
rowfile1.close()
for row in rowlist[150:299]:
    rowfile2.write(row+'@qq.com;')
colfile.close()
rowfile2.close()
for row in rowlist[300:449]:
    rowfile3.write(row+'@qq.com;')
colfile.close()
rowfile3.close()
for row in rowlist[450:599]:
    rowfile4.write(row+'@qq.com;')
colfile.close()
rowfile4.close()
for row in rowlist[600:749]:
    rowfile5.write(row+'@qq.com;')
colfile.close()
rowfile5.close()
for row in rowlist[750:899]:
    rowfile6.write(row+'@qq.com;')
colfile.close()
rowfile6.close()
for row in rowlist[900:1049]:
    rowfile7.write(row+'@qq.com;')
colfile.close()
rowfile7.close()
for row in rowlist[1050:1199]:
    rowfile8.write(row+'@qq.com;')
colfile.close()
rowfile8.close()
for row in rowlist[1200:1349]:
    rowfile9.write(row+'@qq.com;')
colfile.close()
rowfile9.close()


