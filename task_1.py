# Завдання 1

import heapq
import random


def min_total_connection_cost(cables):
    heapq.heapify(cables)
    connection_cost = 0
    total_connection_cost = 0
    while len(cables) > 1:
        connection_cost = heapq.heappop(cables) + heapq.heappop(cables)
        heapq.heappush(cables, connection_cost)
        total_connection_cost += connection_cost
    return total_connection_cost


if __name__ == "__main__":

    # Мережеві кабелі
    # cables = random.sample(range(1, 100), 20)
    cables = [12, 39, 43, 17, 69, 2, 72, 67, 4,
              47, 46, 77, 14, 58, 52, 80, 79, 91, 73, 66]
    print(f"Мережеві кабелі: {cables}")
    print(
        f"Загальні (мінімальні) витрати на з'єднання всіх кабелів: {min_total_connection_cost(cables)}")
