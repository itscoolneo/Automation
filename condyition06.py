post=input("Upload your post here:\n")
post = post.lower()
print(post)
spam="harry"
if spam in post:
    print("Yes there user is talking abount you harry")
else:
    print("This post is not talking about you")
