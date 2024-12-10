#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 5: Print Queue  ---
Part Two

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Doc pages have to be printed in specific order
# For notation X|Y produced in update, page X must print before Y
# Given X|Y ordering rules and pages in update aka puzzle input, 
# determine if each update in the right order
# Also find the MIDDLE page number
# now flip the return logic on the is_valid_update so we're looking at rule breakers
# fix them
# Answer = Add up the middle page number from all now correct-ordered updates?

# --- NOT WORKING

from collections import defaultdict

# Step 1: Build the dependency graph
def build_graph(rules):
    graph = defaultdict(set)
    for x, y in rules:
        graph[x].add(y)
    return graph

# Step 2: Reorder updates using DFS
def dfs(node, graph, visited, stack):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited, stack)
    stack.append(node)

def reorder_update(update, graph):
    visited = set()
    stack = []

    for page in update:
        if page not in visited:
            dfs(page, graph, visited, stack)
    
    return stack[::-1]

# Step 3: Identify invalid updates and reorder them
def is_valid_update(pg_update, rules):
    for x, y in rules:
        if x in pg_update and y in pg_update:
            if pg_update.index(x) >= pg_update.index(y):
                return False
    return True

# Parse the input
with open('input.txt', 'r') as file:
    lines = file.readlines()

rules = []
updates = []
parsing_rules = True

for line in lines:
    line = line.strip()
    if line == "":
        parsing_rules = False
        continue
    if parsing_rules:
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    else:
        updates.append(list(map(int, line.split(','))))

# Build the graph
graph = build_graph(rules)
print("Graph:", dict(graph))  # Debugging graph

invalid_middle_sum = 0

for pg_update in updates:
    if not is_valid_update(pg_update, rules):
        print(f"Invalid update: {pg_update}")  # Debug invalid update
        
        # Reorder the update
        reordered = reorder_update(pg_update, graph)
        print(f"Reordered update: {reordered}")  # Debug reordered update
        
        # Calculate the middle page
        middle_index = len(reordered) // 2
        middle_page = reordered[middle_index]
        print(f"Middle page: {middle_page}")  # Debug middle page
        
        # Add to the total
        invalid_middle_sum += middle_page

print("Sum of middle pages for invalid updates:", invalid_middle_sum)

