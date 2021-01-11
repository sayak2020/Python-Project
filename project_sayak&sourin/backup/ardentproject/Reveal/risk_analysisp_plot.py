
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="ardent")
cur=db.cursor()
cur.execute("select test from riskanal")
x=cur.fetchall()
db.commit()
print(x)
risk=['High','Moderate','Low']
hr=0
mr=0
lr=0
for i in x:
    if i[1]=='hr':
        hr=hr+1
    elif i[1]=="mr":
        mr=mr+1
    else:
        lr=lr+1    
count=[hr,mr,lr]
print(risk)
print(count)
import matplotlib.pyplot as plt
plt.plot(risk,count)
plt.xlabel('Risk parameter')
plt.ylabel('No of people')
#plt.savefig('plot/risk_analysis.png', dpi=150, bbox_inches='tight')
plt.show()