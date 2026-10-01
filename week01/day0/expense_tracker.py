import sys

def summarize_expenses(f_name):
  with open(f_name, "r") as f:
    next(f)
    empty = 0
    invalid = 0
    negative = 0
    no_cat = 0
    totals = {}
    for line in f:
      try:
        category, amount = line.split(",")
        if category == '' and amount != '':
          no_cat += 1
          continue
        category = category.strip().lower()
      except ValueError:
        empty += 1
      else:
        try:
          value = int(amount)
          if value < 0:
            negative += 1
          else:
            totals[category] = totals.get(category, 0) + value
        except ValueError:
          invalid += 1

    return({"totals":totals, "empty":empty, "no_cat":no_cat, "invalid":invalid, "negative":negative})
    
try:
  data = summarize_expenses(sys.argv[1])
  for k, v in data["totals"].items():
    print(f'{k} : {v}')
  print(f'empty: {data["empty"]}')
  print(f'no category entries: {data["no_cat"]}')
  print(f'invalid entries: {data["invalid"]}')
  print(f'negative amount entries: {data["negative"]}')

    
except IndexError:
  print("Missing Filename!!")
except FileNotFoundError:
    print(f"File '{sys.argv[1]}' not found. Check the filename and try again.")