import praw

# client ID : 9u8FFR86KF3eITl3B3yXXA
# secret zV0AdMNaVQXs0SxLmpoF_fDWkmZ9Gg
# user agent : top_posts_liked_subs

class Subs:
    """
    Get a list of all the subs root url
    """
    def __init__(self, list_file_path):
        self.list_file_path = list_file_path

    def get_subs_url(self):
        list_subs = {}
        with open(self.list_file_path, "r") as FileInput:
            for line in FileInput:
                if "#" in line or line.strip() == "":
                    pass
                else:
                    line = line.split()
                    list_subs[line[0]] = [line[1], line[2]]
        return list_subs

class Post :
    # Read-only instance
    reddit_read_only = praw.Reddit(client_id="9u8FFR86KF3eITl3B3yXXA",
                                   client_secret="zV0AdMNaVQXs0SxLmpoF_fDWkmZ9Gg",
                                   user_agent="top_posts_liked_subs")
    def __init__(self, sub_name):
        self.sub_name = sub_name

    def get_posts_hot(self, output_file, limits):
        sub = self.reddit_read_only.subreddit(self.sub_name)
        # Nom du sub
        #name = sub.display_name
        limit_comments = int(limits[0])
        limit_upvotes = int(limits[1])

        for post in sub.hot():
            if post.num_comments > limit_comments and post.ups > limit_upvotes:
                output_file.write("Titre : " + post.title+"    ")
                output_file.write("Lien : " + post.url+"    ")
                output_file.write("Nb de commentaires : " + str(post.num_comments)+"    ")
                output_file.write("Nb de upvotes : " + str(post.ups)+"    \n")

    def get_posts_top(self, output_file, limits):
        sub = self.reddit_read_only.subreddit(self.sub_name)
        # Nom du sub
        #name = sub.display_name
        limit_comments = int(limits[0])
        limit_upvotes = int(limits[1])

        for post in sub.top(time_filter="day"):
            if post.num_comments > limit_comments and post.ups > limit_upvotes:
                output_file.write("Titre : " + post.title+"    ")
                output_file.write("Lien : " + post.url+"    ")
                output_file.write("Nb de commentaires : " + str(post.num_comments)+"    ")
                output_file.write("Nb de upvotes : " + str(post.ups)+"    \n")


list_file_path = "Subs_to_check.txt"
subs = Subs(list_file_path)
list_subs = subs.get_subs_url()
OutputFile = open("liste_posts.txt", "w", encoding="utf-8")
for item in list_subs:
    OutputFile.write(f"\nSub : {item}\n\n")
    post = Post(item)
    OutputFile.write("Hot\n\n")
    post.get_posts_hot(OutputFile, list_subs[item])
    OutputFile.write("\nTop\n\n")
    post.get_posts_top(OutputFile, list_subs[item])
OutputFile.close()