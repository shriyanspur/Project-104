import csv
from collections import Counter

fileName = input('Enter the file name to be worked upon: ')

def find_mean(total, number):
  mean = total/number
  print('Mean:',mean)

def find_median(data, length):
  if length%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1+median2)/2
  else:
    median = data[length//2]
  
  print('Median:',median)

def find_mode(n_data):
  data = Counter(n_data)
  mode_data_for_range = {'50-60': 0, '60-70': 0, '70-80': 0}

  for height, occurence in data.items():
    if 50 < float(height) < 60:
      mode_data_for_range['50-60']+=occurence

    elif 60 < float(height) < 70:
      mode_data_for_range['60-70']+=occurence

    elif 70 < float(height) < 80:
      mode_data_for_range['70-80']+=occurence
  
  mode_range, mode_occurence = 0,0

  for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
      mode_range, mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence
  
  mode = float((mode_range[0] + mode_range[1])/2)

  print('Mode: ',mode)

with open(fileName, newline = '') as f:
  reader = csv.reader(f)
  file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
  n_num = file_data[i][1]
  new_data.append(float(n_num))

n = len(new_data)
total = 0
new_data.sort()

for x in new_data:
  total += x

print()
print('CALCULATION RESULTS for '+ '"' + fileName + '"')
print()
find_mean(total, n)
find_median(new_data, n)
find_mode(new_data)
print()