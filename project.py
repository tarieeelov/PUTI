import heapq

def welcome_message():
    print("\nДобро пожаловать в логистическую компанию PUTI!")
    print("Мы поможем вам найти кратчайший путь между городами.")

def display_graph(graph):
    print("\nДоступные пути между городами:")
    for city, connections in graph.items():
        for neighbor, distance in connections.items():
            print(f"{city} -> {neighbor} : {distance} км")

def dijkstra(graph, start, end):
    if start not in graph or end not in graph:
        return None, "Один из городов не существует в графе."

    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {city: None for city in graph}

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_city == end:
            break

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_city
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    if distances[end] == float('inf'):
        return None, "Маршрута нет."
    return path, distances[end]

def add_city(graph):
    city = input("Введите название нового города: ").strip()
    if city in graph:
        print("Город уже существует.")
        return
    graph[city] = {}
    print(f"Город {city} добавлен.")

def add_path(graph):
    city1 = input("Введите название первого города: ").strip()
    city2 = input("Введите название второго города: ").strip()
    if city1 not in graph or city2 not in graph:
        print("Один или оба города не существуют. Сначала добавьте города.")
        return
    try:
        distance = int(input("Введите расстояние между городами (км): "))
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным.")
        graph[city1][city2] = distance
        graph[city2][city1] = distance
        print(f"Путь между {city1} и {city2} длиной {distance} км добавлен.")
    except ValueError as e:
        print(f"Ошибка: {e}")

def main():
    graph = {
        "Москва": {"Санкт-Петербург": 700, "Казань": 820},
        "Санкт-Петербург": {"Москва": 700, "Мурманск": 1400},
        "Казань": {"Москва": 820, "Уфа": 530},
        "Мурманск": {"Санкт-Петербург": 1400, "Архангельск": 1000},
        "Архангельск": {"Мурманск": 1000, "Вологда": 550},
        "Уфа": {"Казань": 530, "Екатеринбург": 420},
        "Екатеринбург": {"Уфа": 420, "Челябинск": 200},
        "Челябинск": {"Екатеринбург": 200, "Омск": 1120},
        "Омск": {"Челябинск": 1120, "Новосибирск": 680},
        "Новосибирск": {"Омск": 680}
    }

    while True:
        welcome_message()
        display_graph(graph)

        print("\nМеню:")
        print("1. Найти кратчайший маршрут")
        print("2. Добавить новый город")
        print("3. Добавить новый путь между городами")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            start = input("Введите начальный город: ").strip()
            end = input("Введите конечный город: ").strip()
            path, distance = dijkstra(graph, start, end)
            if path:
                print(f"Кратчайший маршрут: {' -> '.join(path)} (длина: {distance} км)")
            else:
                print(distance)

        elif choice == "2":
            add_city(graph)

        elif choice == "3":
            add_path(graph)

        elif choice == "4":
            print("Спасибо за использование нашего приложения!")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
