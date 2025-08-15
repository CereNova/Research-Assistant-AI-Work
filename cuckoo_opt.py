import numpy as np

def cuckoo_optimization(pop_size=10, iterations=20):
    # Initialize population
    population = np.random.rand(pop_size, 2)
    best_solution = population[0]
    best_fitness = float('inf')

    for _ in range(iterations):
        # Simple fitness (e.g., minimize x^2 + y^2)
        fitness = np.sum(population ** 2, axis=1)
        if min(fitness) < best_fitness:
            best_fitness = min(fitness)
            best_solution = population[np.argmin(fitness)]
        # Update (simplified)
        population += np.random.normal(0, 0.1, population.shape)
    return best_solution, best_fitness

solution, fitness = cuckoo_optimization()
print(f"Best Solution: {solution}, Fitness: {fitness}")
