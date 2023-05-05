import requests

username = input('username:')

urls = {
    "GitHub": f"https://api.github.com/users/{username}",
    "Twitter": f"https://api.twitter.com/1.1/users/show.json?screen_name={username}",
    "Facebook": f"https://graph.facebook.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/voyager/api/identity/profiles/{username}/profileView",
    "Reddit": f"https://www.reddit.com/user/{username}/about.json",
    "Twitch": f"https://api.twitch.tv/helix/users?login={username}",
    "YouTube": f"https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername={username}"
}

for website, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        print(f"'{username}' EXISTS  on {website}. RETURN: 1")
    else:
        print(f"'{username}' does NOT exist on {website}. RETURN: 0")
