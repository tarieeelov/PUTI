import heapq

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
def show(graph):
    print("\nДоступные пути между городами:")
    for city,paths in graph.items():
        for dest,dist in paths.items():
            print(f"{city} -> {dest} : {dist} км")

def find(graph,start,end):
    if start not in graph or end not in graph:
        return None,"Город отсутствует."
    dist={city:float('inf') for city in graph}
    dist[start]=0
    queue=[(0,start)]
    prev={city:None for city in graph}
    while queue:
        cur_dist,cur_city=heapq.heappop(queue)
        if cur_city==end:
            break
        if cur_dist>dist[cur_city]:
            continue
        for next_city,length in graph[cur_city].items():
            total=cur_dist+length
            if total<dist[next_city]:
                dist[next_city]=total
                prev[next_city]=cur_city
                heapq.heappush(queue,(total,next_city))
    path=[]
    cur=end
    while cur:
        path.append(cur)
        cur=prev[cur]
    path.reverse()
    if dist[end]==float('inf'):
        return None,"Маршрута нет"
    return path,dist[end]

def add_city(graph):
    city=input("Введите название нового города: ").strip()
    if city in graph:
        print("Город уже существует.")
        return
    graph[city]={}
    print(f"Город {city} добавлен.")

def add_path(graph):
    city1=input("Введите первый город: ").strip()
    city2=input("Введите второй город: ").strip()
    if city1 not in graph or city2 not in graph:
        print("Города не существуют. Добавьте их сначала.")
        return
    try:
        dist=int(input("Введите расстояние (км): "))
        if dist<=0:
            raise ValueError("Расстояние должно быть положительным.")
        graph[city1][city2]=dist
        graph[city2][city1]=dist
        print(f"Путь между {city1} и {city2} длиной {dist} км добавлен.")
    except ValueError as e:
        print(f"Ошибка: {e}")

while True:
    print("\nДобро пожаловать в PUTI")
    print("Мы поможем найти кратчайший путь между городами")
    show(graph)
    print("\nМеню:")
    print("1. Найти маршрут")
    print("2. Добавить город")
    print("3. Добавить путь")
    print("4. Выход")
    cmd=input("Выберите действие (1-4): ").strip()
    if cmd=="1":
        start=input("Введите начальный город: ").strip()
        end=input("Введите конечный город: ").strip()
        path,dist=find(graph,start,end)
        if path:
            print(f"Маршрут: {' -> '.join(path)} (длина: {dist} км)")
        else:
            print(dist)
    elif cmd=="2":
        add_city(graph)
    elif cmd=="3":
        add_path(graph)
    elif cmd=="4":
        print("Спасибо за использование!")
        break
    else:
        print("Неверный ввод.")
