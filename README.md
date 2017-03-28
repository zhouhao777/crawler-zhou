# It's a crawler to record the most promising stock
- hotsearch.py:
show the stock which has been hot until now today,just run: python hotsearch,the result will show at result.txt
- mostpositive.py:
It's a continued crawler to record the stock which looks to further increase.
It is run every hour by crontab in linux.Each time after runnning,it will record the recent stock into the database.I use mysql to record that.
- hotstock.sql
well,it's the sql to create the table


# how to use it
hotsearch.py is easy to run just 'python hotsearch.py',it will generate a txt file recording the stock code

mostpositive.py needs to set up mysql,you need to create a database and a table,then run 'python mostpositive.py' you will find some data in the table you created.

Afterwords,I will work out a way to filter the data and send to my email everyday.

