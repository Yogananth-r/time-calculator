def add_time(start, duration,given_day=False):
  duration_split=duration.partition(":")
  add_hour=int(duration_split[0])
  add_minutes=int(duration_split[2])

  initial_time=start.partition(":")
  initial_hour=int(initial_time[0])
  minutes_apm=initial_time[2].partition(" ")
  initial_minutes=int(minutes_apm[0])
  initial_apm=minutes_apm[2]

  number_of_days=int(add_hour/24)
  
  final_minutes=add_minutes+initial_minutes
  if(final_minutes>60):
    initial_hour+=1
    final_minutes=final_minutes%60
  number_of_ampm_flips=int((initial_hour+add_hour)/12)
  final_hours=(initial_hour+add_hour)%12

  
  final_minutes=final_minutes if final_minutes>9 else "0" + str(final_minutes)
  final_hours=final_hours =12 if final_hours ==0 else final_hours
  
  if(initial_apm=="PM" and initial_hour+(add_hour%12)>=12):
    number_of_days+=1
    
  ampm_dict={"AM":"PM","PM":"AM"}
  initial_apm= ampm_dict[initial_apm] if number_of_ampm_flips%2==1 else initial_apm

  new_time=str(final_hours)+":"+str(final_minutes)+" "+initial_apm

  days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  days_index={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
  if (given_day):
    given_day=given_day.lower()
    ind=int((days_index[given_day])+number_of_days)%7
    updated_day=days[ind]
    new_time+=", "+updated_day

  if(number_of_days==1):
    return new_time+" "+"(next day)"
  elif (number_of_days>1):
    return new_time+" ("+str(number_of_days)+" days later)"
  
  return new_time