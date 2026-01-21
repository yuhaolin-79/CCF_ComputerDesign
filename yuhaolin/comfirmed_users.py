unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    curr_user = unconfirmed_users.pop()
    print(f"Verifying user: {curr_user.title()}")
    confirmed_users.append(curr_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())