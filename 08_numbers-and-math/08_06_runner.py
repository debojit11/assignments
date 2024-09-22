# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

distance_miles = 10
distance_km = distance_miles * 1.6

time_minutes = 30
time_seconds = 30
total_time_hours = ((time_minutes*60)+30)/3600

average_speed_kmph = distance_km / total_time_hours

print(f"Average_speed : {average_speed_kmph} kmph")
