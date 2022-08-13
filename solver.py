BASE_OPS = ['+', '-', '*', '/']

def take_input():
    numbers_input = input("Give the numbers, separated by a single space (Ex: 1 2 3 4): ")
    numbers = [float(s) for s in numbers_input.split(' ')]
    allowed_ops_input = input("Give all allowed operations, separated by a space (Ex: + - / to exclude multiplication): ")
    allowed_ops = allowed_ops_input.split(' ')

    return numbers, allowed_ops

def eval_str_expression(expression):
    split_strs = expression.split(' ')

    if len(split_strs) == 1:
        return float(split_strs[0])

    try:
        open_idx = split_strs.index('(')
        close_idx = split_strs.index(')')

        inner_expr_arr = split_strs[open_idx+1:close_idx]
        inner_expr = ' '.join(inner_expr_arr)

        val = eval_str_expression(inner_expr)

        new_expr_arr = split_strs[:open_idx] + [str(val)] + split_strs[close_idx+1:]
        new_expr = ' '.join(new_expr_arr)

        return eval_str_expression(new_expr)
    except ValueError:
        pass

    try:
        m_idx = split_strs.index('*')
        if m_idx != -1:
            num1 = float(split_strs[m_idx-1])
            num2 = float(split_strs[m_idx+1])

            val = num1 * num2
            
            new_expr_arr = split_strs[:m_idx-1] + [str(val)] + split_strs[m_idx+2:]
            new_expr = ' '.join(new_expr_arr)

            return eval_str_expression(new_expr)
    except ValueError:
        pass
    
    try:
        d_idx = split_strs.index('/')
        if d_idx != -1:
            num1 = float(split_strs[d_idx-1])
            num2 = float(split_strs[d_idx+1])

            val = num1 / num2
            
            new_expr_arr = split_strs[:d_idx-1] + [str(val)] + split_strs[d_idx+2:]
            new_expr = ' '.join(new_expr_arr)

            return eval_str_expression(new_expr)
    except ValueError:
        pass
    except ZeroDivisionError:
        return None

    try:
        a_idx = split_strs.index('+')
        if a_idx != -1:
            num1 = float(split_strs[a_idx-1])
            num2 = float(split_strs[a_idx+1])

            val = num1 + num2
            
            new_expr_arr = split_strs[:a_idx-1] + [str(val)] + split_strs[a_idx+2:]
            new_expr = ' '.join(new_expr_arr)

            return eval_str_expression(new_expr)
    except ValueError:
        pass

    try:
        s_idx = split_strs.index('-')
        if s_idx != -1:
            num1 = float(split_strs[s_idx-1])
            num2 = float(split_strs[s_idx+1])

            val = num1 - num2
            
            new_expr_arr = split_strs[:s_idx-1] + [str(val)] + split_strs[s_idx+2:]
            new_expr = ' '.join(new_expr_arr)

            return eval_str_expression(new_expr)
    except ValueError:
        pass

def generate_possible_nums(generated_so_far, numbers, length):
    if length == 1:
        generated_so_far.append([] + numbers)
        return

    for i in range(length):
        generate_possible_nums(generated_so_far, numbers, length-1)

        if length % 2 != 0:
            numbers[i], numbers[length-1] = numbers[length-1], numbers[i]
        else:
            numbers[0], numbers[length-1] = numbers[length-1], numbers[0]


def make_expr(op1, op2, op3, numbers):
    return str(numbers[0]) + ' ' + op1 + ' ' + str(numbers[1]) + ' ' + op2 + ' ' + str(numbers[2]) + ' ' + op3 + ' ' + str(numbers[3])

def solve(numbers, allowed_ops):

    exprs = {}

    for op1 in allowed_ops:
        for op2 in allowed_ops:
            for op3 in allowed_ops:
                
                possible_nums = []
                generate_possible_nums(possible_nums, numbers, len(numbers))

                for nums in possible_nums:
                    base_expr = make_expr(op1, op2, op3, nums)
                    exprs[base_expr] = eval_str_expression(base_expr)

                    base_expr_arr = base_expr.split(' ')

                    paren_first_two_arr = ['('] + base_expr_arr[:3] + [')'] + base_expr_arr[3:]
                    paren_first_two_expr = ' '.join(paren_first_two_arr)
                    exprs[paren_first_two_expr] = eval_str_expression(paren_first_two_expr)

                    paren_middle_two_arr = base_expr_arr[:2] + ['('] + base_expr_arr[2:5] + [')'] + base_expr_arr[5:]
                    paren_middle_two_expr = ' '.join(paren_middle_two_arr)
                    exprs[paren_middle_two_expr] = eval_str_expression(paren_middle_two_expr)

                    paren_last_two_arr = base_expr_arr[:4] + ['('] + base_expr_arr[4:] + [')']
                    paren_last_two_expr = ' '.join(paren_last_two_arr)
                    exprs[paren_last_two_expr] = eval_str_expression(paren_last_two_expr)

                    paren_first_three_arr = ['('] + base_expr_arr[:5] + [')'] + base_expr_arr[5:]
                    paren_first_three_expr = ' '.join(paren_first_three_arr)
                    exprs[paren_first_three_expr] = eval_str_expression(paren_first_three_expr)

                    paren_last_three_arr = base_expr_arr[:2] + ['('] + base_expr_arr[2:] + [')']
                    paren_last_three_expr = ' '.join(paren_last_three_arr)
                    exprs[paren_last_three_expr] = eval_str_expression(paren_last_three_expr)

    print('# OF EXPRESSIONS MADE:  ' + str(len(exprs.keys())))
    print()
    print('SHOWING SOLUTIONS:')
    
    num_sols = 0
    for k in exprs.keys():
        if exprs[k] == 10.0:
            num_sols += 1
            print(k)

    print("NUMBER OF SOLUTIONS: " + str(num_sols))

    return "No solution"

if __name__ == "__main__":    
    numbers, allowed_ops = take_input()
    solution = solve(numbers, allowed_ops)
    