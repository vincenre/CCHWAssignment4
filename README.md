# CCHWAssignment4

### Map-Reduce Program

This is a simple map-reduce program to count the number of times a vehicle type has been involved in an accident.
The dataset that I used is the NYPD dataset. The dataset can be found at the following location

> https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

The mapper.py file simply outputs a count of 1 for every time a Vehicle Type that has been involved occurs in the dataset.
The reducer.py file simply puts all these together and gives out the summary.

As I am in Windows and I am using PUTTY, I had to first copy the file onto the HADOOP cluster. I used the following command to copy the files from my local directory to hadoop directory.

> pscp -l vincenre D:\UC\Spring2017\CloudComputing\HW4\mapper.py vincenre@hadoop-gate-0.eecs.uc.edu:/home/vincenre
>
> pscp -l vincenre D:\UC\Spring2017\CloudComputing\HW4\reducer.py vincenre@hadoop-gate-0.eecs.uc.edu:/home/vincenre
>

The dataset was already on the hadoop cluster, so I did not have to transfer the dataset.

I had some permission issues. I bypassed it by running it as a user hdfs using the following command

> export HADOOP_USER_NAME=hdfs

The command that I used to run the map-reduce job is :

> hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar  -file /home/vincenre/mapper.py -mapper  
> /home/vincenre/mapper.py -file /home/vincenre/reducer.py -reducer /home/vincenre/reducer.py  -input /data/nyc/nyc-traffic.csv -output 
> /home/vincenre/job7/nyc-output

Note: I have used the reducer script from the below website with a few minor changes.

> http://michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
