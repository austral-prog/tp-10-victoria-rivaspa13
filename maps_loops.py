def find_max(dict):
    a = ""
    max = 0
    for key, value in dict.items():
        if value > max:
            max = value
            a = key
    return a

def reverse_dict(dict):
    a = {}
    for key, value in dict.items():
        if value in a:
            a[value]+=k
        else:
            a[value] = key
    return a


def word_freq_counter(words):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

def find_biggest_expense(dict):
    max_avg = 0
    max_expense = ''
    
    for category, costs in expenses.items():
        average = sum(costs) / len(costs)
        
        if average > max_avg:
            max_avg = average
            max_expense = category
            
    return max_expense    

def sum_of_expenses(expenses):
    total_expenses = {}
    for category, costs in expenses.items():
        total_expenses[category] = sum(costs)
    return total_expenses

def sum_of_expenses_by_type(expenses):
    res = {}
    for k, v in expenses.items():
        for t, exp in expenses.items():
            if t in res:
                res[t] += exp
            else:
                res[t] = exp
    return res
