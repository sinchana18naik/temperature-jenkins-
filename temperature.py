import sys
if len(sys.argv)==2:
  script_name=sys.argv[0]
  temp=sys.argv[1]
else:
  temp=35

if temp < 15:
  alert="cold"
elif temp < 30:
  alert="normal"
else:
  alert="hot"

print("temperature entered is:",temp)
print("temperature is :",alert)
