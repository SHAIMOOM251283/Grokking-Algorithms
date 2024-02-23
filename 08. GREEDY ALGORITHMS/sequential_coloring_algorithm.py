def color_map(graph):
    colors = {}  # Dictionary to store colors assigned to vertices

    for node in graph:
        # Initialize set of colors available for the current vertex
        available_colors = set(range(len(graph[node])))
        
        # Update available colors based on neighboring vertices
        for neighbor in graph[node]:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        
        # Assign the smallest available color to the current vertex
        colors[node] = min(available_colors)
    
    return colors

# Example graph representing the USA map
# Each state is represented by a vertex, and adjacent states are connected by edges
usa_map = {
    'Washington': ['Oregon', 'Idaho'],
    'Oregon': ['Washington', 'Idaho', 'Nevada', 'California'],
    'Idaho': ['Washington', 'Oregon', 'Montana', 'Wyoming', 'Utah', 'Nevada'],
    'Nevada': ['Oregon', 'Idaho', 'Utah', 'Arizona'],
    'California': ['Oregon', 'Nevada', 'Arizona'],
    'Montana': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'Wyoming': ['Montana', 'Idaho', 'Utah', 'Colorado', 'Nebraska', 'South Dakota'],
    'Utah': ['Idaho', 'Nevada', 'Wyoming', 'Colorado', 'Arizona'],
    'Arizona': ['Nevada', 'California', 'Utah', 'Colorado', 'New Mexico'],
    'North Dakota': ['Montana', 'South Dakota', 'Minnesota'],
    'South Dakota': ['North Dakota', 'Montana', 'Wyoming', 'Nebraska', 'Iowa', 'Minnesota'],
    'Nebraska': ['South Dakota', 'Wyoming', 'Colorado', 'Kansas', 'Iowa', 'Missouri'],
    'Colorado': ['Wyoming', 'Utah', 'Arizona', 'New Mexico', 'Oklahoma', 'Kansas', 'Nebraska'],
    'New Mexico': ['Arizona', 'Colorado', 'Texas', 'Oklahoma'],
    'Minnesota': ['North Dakota', 'South Dakota', 'Iowa', 'Wisconsin'],
    'Iowa': ['Minnesota', 'South Dakota', 'Nebraska', 'Missouri', 'Wisconsin', 'Illinois'],
    'Missouri': ['Iowa', 'Nebraska', 'Kansas', 'Oklahoma', 'Arkansas', 'Illinois', 'Kentucky', 'Tennessee'],
    'Wisconsin': ['Minnesota', 'Iowa', 'Illinois', 'Michigan'],
    'Illinois': ['Wisconsin', 'Iowa', 'Missouri', 'Indiana', 'Kentucky'],
    'Michigan': ['Wisconsin', 'Indiana'],
    'Indiana': ['Michigan', 'Illinois', 'Kentucky', 'Ohio'],
    'Kentucky': ['Indiana', 'Illinois', 'Missouri', 'Ohio', 'West Virginia', 'Virginia', 'Tennessee'],
    'Tennessee': ['Kentucky', 'Missouri', 'Arkansas', 'Mississippi', 'Alabama', 'Georgia', 'North Carolina'],
    'Mississippi': ['Tennessee', 'Arkansas', 'Louisiana', 'Alabama'],
    'Alabama': ['Tennessee', 'Mississippi', 'Florida', 'Georgia'],
    'Georgia': ['Alabama', 'Tennessee', 'North Carolina', 'South Carolina', 'Florida'],
    'North Carolina': ['Tennessee', 'Georgia', 'South Carolina', 'Virginia'],
    'South Carolina': ['North Carolina', 'Georgia'],
    'Florida': ['Alabama', 'Georgia']
}

colors = color_map(usa_map)
num_colors = len(set(colors.values()))

print("Minimum number of colors needed:", num_colors)
print("Coloring:", colors)
