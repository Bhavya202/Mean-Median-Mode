# Importing Modules
import csv
from collections import Counter

# Importing Data
with open("data.csv", newline="") as f:
  reader = csv.reader(f)
  file_data = list(reader)

# Adding New Data Of Weights
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
  n_num = file_data[i][2]
  new_data.append(float(n_num))
n = len(new_data)

# Creating Function To Take Out Mean
def mean():
  total = 0
  for x in new_data:
    total += x

  mean = total/n
  print("Mean is: " + str(mean))

# Creating Function To Take Out Median
def median():
  new_data.sort()
  if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2
  else:
    median = new_data[n//2]

  print("Median is: " + str(median))

# Creating Function To Take Out Mode
def mode():
  data = Counter(new_data)
  mode_data_range = {
                      "75-85": 0,
                      "85-95": 0,
                      "95-105": 0,
                      "105-115": 0,
                      "115-125": 0,
                      "125-135": 0,
                      "135-145": 0,
                      "145-155": 0,
                      "155-165": 0,
                      "165-175": 0
  }

  for weight, occurence in data.items():
    if 75 < float(weight) < 85:
      mode_data_range["75-85"] += occurence
    elif 85 < float(weight) < 95:
      mode_data_range["85-95"] += occurence
    elif 95 < float(weight) < 105:
      mode_data_range["95-105"] += occurence
    elif 105 < float(weight) < 115:
      mode_data_range["105-115"] += occurence
    elif 115 < float(weight) < 125:
      mode_data_range["115-125"] += occurence
    elif 125 < float(weight) < 135:
      mode_data_range["125-135"] += occurence
    elif 135 < float(weight) < 145:
      mode_data_range["135-145"] += occurence
    elif 145 < float(weight) < 155:
      mode_data_range["145-155"] += occurence
    elif 155 < float(weight) < 165:
      mode_data_range["155-165"] += occurence
    elif 165 < float(weight) < 175:
      mode_data_range["165-175"] += occurence

  mode_range, mode_occurence = 0, 0

  for range, occurence in mode_data_range.items():
    if(occurence > mode_occurence):
      mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    
  mode = float((mode_range[0] + mode_range[1])/2)
  print(f"Mode is: {mode: 2f}")

# Creating Function To Choode Mean/Median/Mode
def choose():
  print()
  print("Enter 'Back' For Going Back")
  options = ["Mode", "mode", "Median", "median", "Mean", "mean", "All", "all", "back", "Back"]
  what_to_take = input("What To Take Of Weight (Mean, Median, Mode, All, Back): ")
  if what_to_take == "mean" or  what_to_take == "Mean":
    mean()
    print()
    choose()
  elif what_to_take == "median" or what_to_take == "Median":
    median()
    print()
    choose()
  elif what_to_take == "mode" or what_to_take == "Mode":
    mode()
    print()
    choose()
  elif what_to_take == "all" or what_to_take == "All":
    mean()
    median()
    mode()
    print()
    choose()
  elif what_to_take == "back" or what_to_take == "Back":
    print()
    main()
  elif what_to_take not in options:
    print("Not In Options!")
    print("Options Are- Mean, Mode, Median, All")
    print("Try Again!")
    print()
    choose()

# Creating The Main Function
def main():
  options = ["y","n", "yes", "no", "Yes", "No"]
  start = input("Do You Wanna Start With Our Program(y/n): ")
  if start == "y" or start == "yes" or start == "Yes":
    choose()
  elif start == "n" or start == "no" or start == "No":
    print("Thank You For Coming Here!")
    print("Have A Good Day!!", end="")
    print()
  elif start not in options:
    print("Try again")
    print("Options Are- y or n")
    print()
    main()

main()
