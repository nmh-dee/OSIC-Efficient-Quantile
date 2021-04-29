import pandas as pd 
import sys
import csv 

data=[]
demo = pd.read_csv("demo.csv")
for i in range (-12,134):
    info = demo["Patient"] + '_' + str(i)
    data.append(info)

kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('submission.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(["Patient_Week", "FVC", "Confidence"])  # write header
    writer.writerows(data)

with open('submission_copy.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(["Patient_Week", "FVC", "Confidence"])  # write header
    writer.writerows(data)
