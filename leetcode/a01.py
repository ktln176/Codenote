import random


def weighted_random_choice(weighted_dict):
    total_weight = sum(weighted_dict.values())
    random_value = random.uniform(0, total_weight)

    current_weight = 0
    for key, weight in weighted_dict.items():
        current_weight += weight
        if random_value <= current_weight:
            return key


# 示例字典，键为字符串，值为随机小数
input_dict = {
    'A': 0.2,
    'B': 0.3,
    'C': 0.5,
}

# 调用函数获取按概率选择的字符串
selected_string = weighted_random_choice(input_dict)
print("Selected String:", selected_string)


def weighted_random_choice(weighted_dict):
    choices, weights = zip(*weighted_dict.items())
    total_weight = sum(weights)
    probabilities = [weight / total_weight for weight in weights]

    selected_string = random.choices(choices, probabilities)[0]
    return selected_string


# 示例字典，键为字符串，值为随机小数
input_dict = {
    'A': 0.2,
    'B': 0.3,
    'C': 0.5,
}

# 调用函数获取按概率选择的字符串
selected_string = weighted_random_choice(input_dict)
print("Selected String:", selected_string)
