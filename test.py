import string
import random

def generate_city_names(num_cities):
        names = []
        for i in range(1, num_cities + 1):
            name = ""
            while i > 0:
                i -= 1
                name = chr(97 + i % 26) + name  # 97 is ASCII for 'a'
                i //= 26
            names.append(name)
        return names

def generate_agent_data(num_cities):
        # Thief: Random stamina (10-20), random starting city, and getaway city
        thief_stamina = random.randint(10, 20)
        thief_start_city = random.randint(0, num_cities - 1)
        thief_getaway_city = random.choice([c for c in range(num_cities) if c != thief_start_city])
        thief_name = "T"
        thief_line = f"{thief_stamina} {thief_start_city} {thief_getaway_city} {thief_name}"
        
        # Detectives: 4 entries
        detective_lines = []
        for i in range(1, 5):
            stamina = 150
            start_city = random.randint(0, num_cities - 1)  # Random starting city
            strategy = random.randint(0, 2)  # Random strategy (0, 1, 2)
            detective_name = f"D{i}"  # Unique detective name
            detective_lines.append(f"{stamina} {start_city} {strategy} {detective_name}")
        
        # Combine all lines
        agent_data = "\n".join([thief_line] + detective_lines)
        return agent_data

for i in range(1, 20000):
    # Example usage
    num_cities = 1000
    agent_data = generate_agent_data(num_cities)

    # Save the generated agent data to a file named 'agentData_X.data'
    with open(f'data/agents/agentData_{i}.data', 'w') as file:
        file.write(agent_data)

    # Generate city data
    city_names = generate_city_names(num_cities)

    # Generate random graph data
    graph_data = []
    for city_id in range(num_cities):
        num_connections = random.randint(1, 3)  # Each city connects to 1-5 other cities
        connections = []
        connected_cities = random.sample([i for i in range(num_cities) if i != city_id], num_connections)
        for connected_city in connected_cities:
            road_length = random.randint(10, 100)
            connections.extend([connected_city, road_length])
        has_informant = 'n' # 'i' if random.random() < 0.3 else 'n'  # 30% chance of having an informant
        graph_data.append(f"{city_id} {' '.join(map(str, connections))} {has_informant} {city_names[city_id]}")

    # Combine into final format
    final_output = f"{num_cities}\n" + "\n".join(graph_data)

    with open(f'data/cities/cityData_{i}.data', 'w') as file:
        file.write(final_output)
