import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(low, high) for (low, high) in bounds]
    current_val = func(current)

    for _ in range(iterations):
        neighbor = []
        for i in range(dim):
            delta = random.uniform(-0.1, 0.1)
            new_val = current[i] + delta
            new_val = max(bounds[i][0], min(bounds[i][1], new_val))
            neighbor.append(new_val)

        neighbor_val = func(neighbor)

        if abs(neighbor_val - current_val) < epsilon:
            break

        if neighbor_val < current_val:
            current, current_val = neighbor, neighbor_val

    return current, current_val

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best = [random.uniform(low, high) for (low, high) in bounds]
    best_val = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(low, high) for (low, high) in bounds]
        candidate_val = func(candidate)

        if abs(candidate_val - best_val) < epsilon:
            break

        if candidate_val < best_val:
            best, best_val = candidate, candidate_val

    return best, best_val

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(low, high) for (low, high) in bounds]
    current_val = func(current)

    for _ in range(iterations):
        if temp < epsilon:
            break

        neighbor = []
        for i in range(dim):
            delta = random.uniform(-0.1, 0.1)
            new_val = current[i] + delta
            new_val = max(bounds[i][0], min(bounds[i][1], new_val))
            neighbor.append(new_val)

        neighbor_val = func(neighbor)
        delta_val = neighbor_val - current_val

        if delta_val < 0 or math.exp(-delta_val / temp) > random.random():
            current, current_val = neighbor, neighbor_val

        temp *= cooling_rate

    return current, current_val

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution)
    print("Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution)
    print("Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution)
    print("Значення:", sa_value)
