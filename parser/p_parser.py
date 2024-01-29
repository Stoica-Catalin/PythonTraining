
from datetime import datetime
import re

start_timestamp = '17:56:07.996'
end_timestamp = '17:56:08.357'                           
format_string = '%H:%M:%S.%f'
list_of_words=[]
index=0

parsed_datetime_start = datetime.strptime(start_timestamp, format_string)
parsed_datetime_end = datetime.strptime(end_timestamp, format_string)

with open('logcat_applications.txt', 'r') as f: 
    for line in f:
        if line[0:5]=='03-14':
            timestamp_as_string=line[6:18]
            timestamp=datetime.strptime(timestamp_as_string,format_string)
            if timestamp>=parsed_datetime_start and timestamp<=parsed_datetime_end:
                output = re.findall(r'\b[A-Za-z]+\b', line)
                list_of_words.insert(index,output[-1])
                index+= 1
print(list_of_words)
        


