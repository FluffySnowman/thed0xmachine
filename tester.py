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
    "YouTube": f"https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername={username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "Twitter": f"https://twitter.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Snapchat": "https://www.snapchat.com/",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Tumblr": f"https://{username}.tumblr.com/",
    "YouTube": f"https://www.youtube.com/user/{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "Flickr": f"https://www.flickr.com/people/{username}",
    "SoundCloud": f"https://soundcloud.com/{username}",
    "Bandcamp": f"https://{username}.bandcamp.com/",
    "Last.fm": f"https://www.last.fm/user/{username}",
    "Mixcloud": f"https://www.mixcloud.com/{username}",
    "Discogs": f"https://www.discogs.com/user/{username}",
    "Behance": f"https://www.behance.net/{username}",
    "Dribbble": f"https://dribbble.com/{username}",
    "DeviantArt": f"https://{username}.deviantart.com/",
    "500px": f"https://500px.com/{username}",
    "SmugMug": "https://www.smugmug.com/",
    "Quora": f"https://www.quora.com/profile/{username}",
    "Goodreads": f"https://www.goodreads.com/{username}",
    "Stack Overflow": f"https://stackoverflow.com/users/{username}",
    "GitHub": f"https://github.com/{username}",
    "GitLab": f"https://gitlab.com/{username}",
    "Bitbucket": f"https://bitbucket.org/{username}",
    "CodePen": f"https://codepen.io/{username}",
    "JSFiddle": f"https://jsfiddle.net/user/{username}",
    "Pastebin": f"https://pastebin.com/u/{username}",
    "HackerRank": f"https://www.hackerrank.com/{username}",
    "Kaggle": f"https://www.kaggle.com/{username}",
    "WordPress": f"https://{username}.wordpress.com/",
    "Medium": f"https://medium.com/@{username}",
    "Blogger": f"https://www.blogger.com/{username}",
    "Ghost": f"https://ghost.org/{username}",
    "Wix": f"https://www.wix.com/{username}",
    "Weebly": f"https://www.weebly.com/{username}",
    "Squarespace": f"https://www.squarespace.com/{username}",
    "Amazon": f"https://www.amazon.com/{username}",
    "eBay": f"https://www.ebay.com/{username}",
    "Alibaba": f"https://www.alibaba.com/{username}",
    "AliExpress": f"https://www.aliexpress.com/{username}",
    "Craigslist": f"https://www.craigslist.org/{username}",
    "Gumtree": f"https://www.gumtree.com/{username}",
    "Booking.com": f"https://www.booking.com/{username}",
    "Expedia": f"https://www.expedia.com/{username}",
    "Airbnb": f"https://www.airbnb.com/{username}",
    "Uber": f"https://www.uber.com/{username}",
    "Lyft": f"https://www.lyft.com/{username}",
}

""" 
for website, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        print(f"'{username}' EXISTS  on {website}. RETURN: 1")
    else:
        print(f"'{username}' does NOT exist on {website}. RETURN: 0")

"""

html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
        text-align: center;
    }}
    h1 {{
        color: #2d2d2d;
        margin-top: 50px;
    }}
    table {{
        margin: 0 auto;
        border-collapse: collapse;
        width: 60%;
    }}
    th, td {{
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }}
    tr:nth-child(even) {{
        background-color: #f2f2f2;
    }}
    tr:hover {{
        background-color: #ddd;
    }}
</style>
</head>
<body>
<h1>Username Check Results for {username}</h1>
<table>
<tr>
    <th>Website</th>
    <th>Exists</th>
</tr>
{table_data}
</table>
</body>
</html>
"""

table_data = ""
for website, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        table_data += f"<tr><td>{website}</td><td style='color: green;'>YES</td></tr>"
        print(f"'{username}' EXISTS  on {website}. RETURN: 1")
    else:
        table_data += f"<tr><td>{website}</td><td style='color: red;'>NO</td></tr>"
        print(f"'{username}' does NOT exist on {website}. RETURN: 0")

html_content = html_template.format(username=username, table_data=table_data)

with open(f"{username}_check_results.html", "w") as f:
    f.write(html_content)
    print(f"Results saved to {username}_check_results.html")
