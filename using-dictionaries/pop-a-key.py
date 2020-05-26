available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains") if "stamina grains" in available_items else 0
health_points += available_items.pop("power stew") if "power stew" in available_items else 0
health_points += available_items.pop("mystic bread", 0)
print(health_points)
print(available_items)
