due=50
nominals=[5,10,25]
while(due>0):
  print(f"Amount Due: {due}")
  nominal=int(input("Insert Coin: "))
  if nominal in nominals:
     due-=nominal
print(f"Change Owed: {due*(-1)}")
