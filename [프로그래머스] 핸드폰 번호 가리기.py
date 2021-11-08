def solution(phone_number):
    answer = ''
    new = ['*'] * (len(phone_number)-4)
    return ''.join(new) + phone_number[len(phone_number)-4:]
