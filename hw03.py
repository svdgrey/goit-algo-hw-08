import heapq

from utils import generate_values



def main():
    cables = generate_values(min_count=5, max_count=15, min_value=5, max_value=20, unique_values=False)
    print(f"Кабелі довжиною (м): {cables}")

    heapq.heapify(cables)

    print(f"Початкова купа: {cables}")
    
    total_cost = 0
    step = 0

    while len(cables) > 1:
        step += 1

        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

        print(f"\nКрок {step}: {first} + {second} = {cost}")
        print(f"Накопичені витрати: {total_cost}")
        print(f"Купа після з'єднання: {cables}")

    print(f"\nМінімальні загальні витрати: {total_cost}")


if __name__ == "__main__":
    main()

