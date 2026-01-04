from instabot import Bot
bot = Bot()
bot.login(username="your_username", password="your_password")
bot.follow("target_user")
bot.upload_photo("path_to_your_photo.jpg", caption="Your caption here")
bot.unfollow("target_user")

bot.send_message("I Love Python", ["target_user1", "target_user2"])

followers = bot.get_user_followers("target_user")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("target_user")
for Following in following:
    print(bot.get_user_info(Following))

     