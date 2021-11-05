def observed():
    observation = []
    for count in range(5):
        print("Please enter an observation:")
        observation.append(input())
    return observation
def remove_observation(observations):
    is_running = True
    print("Do you wish to remove an observation?(yes/no)")
    response = input()
    if (response == "yes"):
        print("Please specify")
        observation = input()
        observations.remove(observation)
    else:
        is_running = False
def run():
   observations = observed()
   remove_observation(observations)

   observations_set = set()
   for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)
   for data in sorted(observations_set):
       print(f"{data[0]} observed {data[1]} times.")

run()

