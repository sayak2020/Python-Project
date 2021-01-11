import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
cur.execute("select test from test where status='d' ")
x=cur.fetchall()
db.commit()
print(x)
test=[]
for i in x:
    if i[0] not in test:
        test.append(i[0])
print(test)
c=0
count=[]
for t in test:
    c=0
    for i in x :
        if t==i[0]:
            c=c+1
    count.append(c)
print(count)
df=pd.DataFrame({"Test":test,"Count":count})
df=df.sort_values('Count', ascending=False)
print(df)

plt.bar('Test','Count', data=df,width=0.4)

plt.xlabel('Test Name',size=15)
plt.xticks(rotation=35)
plt.ylabel('Number of test ',size=15)
plt.title("All Test Conducted")
plt.savefig('plot/test_done.png', dpi=150, bbox_inches='tight')
plt.show()

            
            