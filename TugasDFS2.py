#galang pratama
graph = {
    "Rumah": ["Kampus", "Masjid"],
    "Kampus": ["Terminal"],
    "Masjid": ["Mall"],
    "Mall": [],
    "Terminal": ["Rumah Sakit"],
    "Rumah Sakit": []
}

def dfs(node, goal, path, visited):
    path.append(node)
    visited.add(node)

    if node == goal:
        return path

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(neighbor, goal, path.copy(), visited)
            if result:
                return result

    return None

start = "Rumah"
goal = "Rumah Sakit"

path = dfs(start, goal, [], set())

print("Start :", start)
print("Goal :", goal)

print("\nJalur yang ditemukan:")
if path:
    print(" -> ".join(path))
else:
    print("Tidak ditemukan jalur")