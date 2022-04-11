post = (input("Enter the words used in post\n"))
post = post.casefold()  # .casefold convets every letter in lowercase
if "henry" in post:
    print("Post is talking about Henry")
else:
    print("Post is talking about Henry")