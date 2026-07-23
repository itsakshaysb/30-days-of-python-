# def sum(num1,num2):
#     return (num1+num2)
# print(sum(2,3))


# def cir_area(rad):
#     return(3.14*rad**2)
# print(cir_area(3))


# def num_sum(*num):
#     total = 0
#     for value in num:
#         if isinstance(value, (int, float)) and not isinstance(value, bool):
#             total += value
#         else:
#             return "not a number"
#     return total
# print(num_sum(2,3))

# def temp(cel):
#     far=cel*(9/5)+32
#     return(far)
# print(temp(100))


def ses(months):
    sessions = {
        "winter": ["december", "january", "february"],
        "spring": ["march", "april", "may"],
        "summer": ["june", "july", "august"],
        "autumn": ["september", "october", "november"]
    }
    for session in sessions:
        for month in sessions.values():
            if month in months:
                return sessions.key()
            else:
                pass

 