lists =["A B C D", "A D", "A B D", "B D"]
k=2
couponCount = {}
user = []
answer = 0
for x in lists:
    users = x.split()
    users = list(set(users))
    for user in users:
        if not user in couponCount:
            couponCount[f'{user}'] = 1
            answer = answer + 1

        else:
            if couponCount[f'{user}'] < k:
                couponCount[f'{user}'] = couponCount[f'{user}'] + 1
                answer = answer + 1

    print(couponCount)
    print(answer)
