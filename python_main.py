#!/usr/bin/python
#don't forget to change **** to password
 
import os
from crontab import CronTab
 
str = raw_input("Enter desired file location e.g. /home/usr_name/test :");
os.mkdir(str)
os.chdir(str)
os.chmod(str, 0777)
 
target = open('python1.py','w')
target.truncate()
 
line1 = "#!/usr/bin/python"
line2 = "import MySQLdb as db"
line3 = "con=db.connect('localhost', 'root', '****')"
line4 = "cur=con.cursor()"
line5 = "cur.execute('CREATE DATABASE DeltaSysAdTask2;')"
line6 = "con=db.connect('localhost', 'root', '****','DeltaSysAdTask2')"
line7 = "cur=con.cursor()"
line8 = "cur.execute('create table IF NOT EXISTS table1(time varchar(15));')"
 
target.write("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n".format(line1,line2,line3,line4,line5,line6,line7,line8))
 
target.close()
 
execfile("python1.py")
 
os.chdir(str)
target = open('python2.py', 'w')
target.truncate()
 
line1 = "#!/usr/bin/python"
line2 = "import MySQLdb"
line3 = "import datetime"
line4 = "current_time=datetime.datetime.now().strftime('%H:%M:%S')"
line5 = "db = MySQLdb.connect('localhost','root','****','DeltaSysAdTask2')"
line6 = "cursor = db.cursor()"
line7 = "cursor.execute('INSERT INTO table1(time) VALUES(current_time)')"
line8 = "db.commit()"
 
target.write("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n".format(line1,line2,line3,line4,line5,line6,line7,line8))
 
target.close()
 
str = str + '/python2.py'
os.chmod(str, 0777)
 
cron = CronTab(user=True)
job = cron.new(command=(str))
job.minute.every(10)
cron.write()