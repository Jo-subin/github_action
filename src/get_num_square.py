import  os

num= os.environ.get("INPUT_NUM")
if num:
  try:
    num = int(num)
  except Extention:
    exit('ERROR: the INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
  num = 1
#to set output, print to shell in following syntax
print(f"::ser-output name_squared::{num ** 2}")
