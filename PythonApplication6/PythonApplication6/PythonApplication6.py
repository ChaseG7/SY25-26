crate =     {"weight": 120, "blemishes": 0, "is_rotten": False},     {"weight": 90, "blemishes": 2, "is_rotten": False},     {"weight": 250, "blemishes": 0, "is_rotten": False},     {"weight": 150, "blemishes": 1, "is_rotten": True},     {"weight": 80, "blemishes": 0, "is_rotten": False},
small_count = 0
med_count = 0
large_count = 0
rotten_count = 0
premium_count = 0
for potato in crate:
  if potato["is_rotten"]:
    rotten_count += 1 # your own code
  else:
    if potato["blemishes"] == 0:
      premium_count += 1 # your own code
    if potato["weight"] < 100:
      small_count += 1 # your own code
    elif potato["weight"] <= 200:
      med_count += 1 # your own code
    else:
      large_count += 1 # your own code
print("Small:", small_count)
print("Medium:", med_count)
print("Large:", large_count)
print("Rotten:", rotten_count)
print("Premium:", premium_count)
