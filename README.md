### Завдання 1
- **Кількість вершин графа:** 10
- **Кількість ребер графа:** 17

#### Ваги ребер графа:
- New York - Los Angeles: 2799
- New York - Chicago: 791
- Los Angeles - Chicago: 1744
- Los Angeles - Houston: 1374
- Los Angeles - Phoenix: 371
- Chicago - Houston: 1085
- Chicago - Phoenix: 1444
- Houston - Phoenix: 1175
- Houston - Philadelphia: 1521
- Phoenix - San Antonio: 1031
- Phoenix - San Diego: 299
- Philadelphia - San Antonio: 1560
- San Antonio - San Diego: 1303
- San Antonio - Dallas: 274
- San Diego - Dallas: 1466
- San Diego - San Jose: 417
- Dallas - San Jose: 1849

#### Ступені вершин графа:
- New York: 2
- Los Angeles: 4
- Chicago: 4
- Houston: 4
- Phoenix: 5
- Philadelphia: 2
- San Antonio: 4
- San Diego: 4
- Dallas: 3
- San Jose: 2

### Завдання 2
#### DFS-обхід:
New York -> Los Angeles -> Chicago -> Houston -> Phoenix -> San Antonio -> Philadelphia -> San Diego -> Dallas -> San Jose

#### BFS-обхід:
New York -> Los Angeles -> Chicago -> Houston -> Phoenix -> Philadelphia -> San Antonio -> San Diego -> Dallas -> San Jose

### Пояснення різниці в отриманих шляхах:
- **DFS (обхід у глибину):** Цей алгоритм спочатку просувається якомога глибше вглиб графа, перед тим як повернутися назад і продовжити обхід. Таким чином, DFS спробує відвідати всі можливі вершини, що виходять з поточної вершини, перед тим як переходити до наступної вершини. У результаті, шлях, знайдений за допомогою DFS, може бути менш оптимальним з точки зору довжини.

- **BFS (обхід у ширину):** На відміну від DFS, цей алгоритм спочатку відвідує всі сусідні вершини поточної вершини перед тим, як переходити до наступного рівня вершин. Це означає, що BFS шукає найкоротший шлях від початкової вершини до всіх інших вершин у графі. Тому шляхи, знайдені за допомогою BFS, зазвичай є найкоротшими.

### Завдання 3
#### Найкоротші відстані від вершини New York:
- New York: 0
- Los Angeles: 2535
- Chicago: 791
- Houston: 1876
- Phoenix: 2235
- Philadelphia: 3397
- San Antonio: 3266
- San Diego: 2534
- Dallas: 3540
- San Jose: 2951