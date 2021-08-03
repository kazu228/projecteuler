# 10001番目の素数

# 素数を小さい数字から生成
# 10001番目になるまで続ける

#number_list = [ 2 ]

def is_prime_number(number):
    # 素数判定
    for i in range(2, number):   #回数が多いとここがバグる
        if number % i == 0:
            return False
        
    return True


def append_prime_number(number_list):
    #リストの次の素数を計算
    last_number = number_list[len(number_list)-1]
    
    while True:
        last_number += 1
        if is_prime_number(last_number):
            number_list.append(last_number)
            break

    

def check_size_of_list(number_list):
    # リストの要素数が10001か、否か
    result = len(number_list) - 1

    if result == 10001:
        print(number_list[result-1])
        return True
    else:
        return False


def main():
    number_list = [ 2 ]
    while True:
        append_prime_number(number_list)
        if check_size_of_list(number_list):
            break

main()