import string
import random

def generate_city_names(num_cities):
        names = []
        for i in range(1, num_cities + 1):
            name = ""
            while i > 0:
                i -= 1
                name = chr(97 + i % 26) + name
                i //= 26
            names.append(name)
        return names

def generate_agent_data(num_cities):
        thief_stamina = 150 # Stamina of the thief
        thief_start_city = random.randint(0, num_cities - 1)
        thief_getaway_city = random.choice([c for c in range(num_cities) if c != thief_start_city])
        thief_name = "T"
        thief_line = f"{thief_stamina} {thief_start_city} {thief_getaway_city} {thief_name}"
        
        detective_lines = []
        for i in range(1, 5):
            stamina = 150 # Stamina of the detectives
            start_city = random.randint(0, num_cities - 1)
            strategy = random.randint(0, 2)
            detective_name = f"D{i}"
            detective_lines.append(f"{stamina} {start_city} {strategy} {detective_name}")
 
        agent_data = "\n".join([thief_line] + detective_lines)
        return agent_data

# Number of files you want to create
for i in range(1, 1000):
    num_cities = 100 # Number of cities in each case
    agent_data = generate_agent_data(num_cities)

    with open(f'data/agents/agentData_{i}.data', 'w') as file:
        file.write(agent_data)

    city_names = generate_city_names(num_cities)

    graph_data = []
    for city_id in range(num_cities):
        num_connections = random.randint(1, 5) # Number of roads out of each cities (1 to 5)
        connections = []
        connected_cities = random.sample([i for i in range(num_cities) if i != city_id], num_connections)
        for connected_city in connected_cities:
            road_length = random.randint(10, 100) # Random road length 10 to 100
            connections.extend([connected_city, road_length])
        # LEAVE AS IS IF TASK 3 IS NOT DONE - SWAP THE COMMENTS IF YOU WANT TO TEST TASK 3
        has_informant = 'n' # 'i' if random.random() < 0.3 else 'n'
        graph_data.append(f"{city_id} {' '.join(map(str, connections))} {has_informant} {city_names[city_id]}")

    final_output = f"{num_cities}\n" + "\n".join(graph_data)

    with open(f'data/cities/cityData_{i}.data', 'w') as file:
        file.write(final_output)
