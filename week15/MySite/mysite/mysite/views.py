from django.shortcuts import render
from math import factorial


def index(request):
    return render(request, 'index.html')


def fact(request):
    if request.method == 'POST':
        end_range = int(request.POST.get('num'))
        result = factorial(end_range)
    return render(request, 'index.html', locals())


def calc_fibo(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibo(request):
    if request.method == 'POST':
        fibo_res = calc_fibo(int(request.POST.get('fibo_num')))
    return render(request, 'index.html', locals())


def check_if_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_primes(num):
    result = ''
    for i in range(num):
        if check_if_prime(i):
            result += str(i) + ' '
    return result


def primes(request):
    if request.method == 'POST':
        primes = get_primes(int(request.POST.get('end_num')))
    return render(request, 'index.html', locals())


def encode(words):
    lc = words[0]
    char_count = 0
    result = ''
    for char in words:
        if char == lc:
            char_count += 1
        else:
            result += str(char_count) + lc
            lc = char
            char_count = 1
    result += str(char_count) + lc
    return result


def rle(request):
    if request.method == 'POST':
        result_enc = encode(request.POST.get('words'))
    return render(request, 'index.html', locals())


def decode(string):
    num = True
    result = ''
    for char in string:
        if num:
            num = not num
            repeat = int(char)
        else:
            num = not num
            for _ in range(repeat):
                result += char
    return result


def dec_rle(request):
    if request.method == 'POST':
        result_decode = decode(request.POST.get('rle_str'))
    return render(request, 'index.html', locals())
