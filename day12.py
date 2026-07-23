
import random
import string

# def randomid():
#     pool = string.ascii_letters+string.digits
#     return "".join(random.choice(pool) for _ in range(6))

# print(randomid())


# def user_id_gen_by_user():
    
#     num_chars = int(input("Enter the number of characters: "))
#     num_ids = int(input("Enter the number of IDs to generate: "))

    
#     char_pool = string.ascii_letters + string.digits

#     output_strings = []

  
#     for _ in range(num_ids):
#         single_id = "".join(random.choice(char_pool) for _ in range(num_chars))
#         output_strings.append(single_id)

#     return "\n".join(output_strings)



# print(user_id_gen_by_user())



def rgb_color_gen():
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r}, {g}, {b})"



print(rgb_color_gen())
cd /workspaces/30-days-of-python-
git status
git add .
git commit -m "Update files"
git push origin main