#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

from itertools import product

def evaluate_expression(numbers, operations):
    """Вычисление значения выражения из чисел и операций"""
    expression = str(numbers[0])
    for i in range(1, len(numbers)):
        expression += operations[i-1] + str(numbers[i])
    return eval(expression)

def generate_expressions(numbers):
    if len(numbers) == 1:
        return [str(numbers[0])]
    
    expressions = []
    for i in range(1, len(numbers)):
        left_part = generate_expressions(numbers[:i])
        right_part = generate_expressions(numbers[i:])
        
        for left in left_part:
            for right in right_part:
                expressions.append(f"({left}+{right})")
                expressions.append(f"({left}-{right})")
                expressions.append(f"({left}*{right})")
                
    return expressions

def find_target_value(numbers, target):
    operations = ['+', '-', '*']
    all_operations = product(operations, repeat=len(numbers)-1)
    
    for ops in all_operations:
        expressions = generate_expressions(numbers)
        for expr in expressions:
            try:
                if eval(expr) == target:
                    print(f"Found expression: {expr} = {target}")
            except ZeroDivisionError:
                continue

numbers = [1, 2, 3, 4, 5]
target_value = 25
find_target_value(numbers, target_value)
