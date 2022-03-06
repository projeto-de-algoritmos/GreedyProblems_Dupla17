# https://www.beecrowd.com.br/judge/pt/problems/view/1966

cheese_pieces, budget = list(map(int, input().split()))
volumes = list(map(int, input().split()))
prices = list(map(int, input().split()))

cheeses = [[volumes[i], prices[i], float('inf') if prices[i] == 0 else volumes[i]/prices[i]] for i in range(cheese_pieces)]

cheeses = sorted(cheeses, key=lambda cheese: cheese[2], reverse=True)

total_volume, current_budget, fraction = 0, 0, 0
for cheese in cheeses:
    if cheese[1] + current_budget <= budget:
        current_budget += cheese[1]
        total_volume += cheese[0]
    else:
        fraction = (budget - current_budget)/cheese[1]
        total_volume += cheese[0] * fraction
        current_budget = budget

base = (-1 + (1 + (8 * total_volume))**0.5) / 2
print(int(base))