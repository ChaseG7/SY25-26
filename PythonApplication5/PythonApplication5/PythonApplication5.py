rider_scores = [10, 45, 80, 25, 120, 60]
final_sum = 0

for i in range(len(rider_scores)):
  if rider_scores[i] >= 50:
    rider_scores[i] + 20 # your own code

final_sum = sum(rider_scores)
print(final_sum)
