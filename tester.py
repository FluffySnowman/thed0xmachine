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
    "Facebook": "https://www.facebook.com/",
    "Twitter": "https://twitter.com/",
    "Instagram": "https://www.instagram.com/",
    "LinkedIn": "https://www.linkedin.com/",
    "Pinterest": "https://www.pinterest.com/",
    "Snapchat": "https://www.snapchat.com/",
    "Reddit": "https://www.reddit.com/",
    "Tumblr": "https://www.tumblr.com/",
    "YouTube": "https://www.youtube.com/",
    "Vimeo": "https://vimeo.com/",
    "Flickr": "https://www.flickr.com/",
    "SoundCloud": "https://soundcloud.com/",
    "Bandcamp": "https://bandcamp.com/",
    "Last.fm": "https://www.last.fm/",
    "Mixcloud": "https://www.mixcloud.com/",
    "Discogs": "https://www.discogs.com/",
    "Behance": "https://www.behance.net/",
    "Dribbble": "https://dribbble.com/",
    "DeviantArt": "https://www.deviantart.com/",
    "500px": "https://500px.com/",
    "SmugMug": "https://www.smugmug.com/",
    "Quora": "https://www.quora.com/",
    "Goodreads": "https://www.goodreads.com/",
    "Stack Overflow": "https://stackoverflow.com/",
    "GitHub": "https://github.com/",
    "GitLab": "https://gitlab.com/",
    "Bitbucket": "https://bitbucket.org/",
    "CodePen": "https://codepen.io/",
    "JSFiddle": "https://jsfiddle.net/",
    "Pastebin": "https://pastebin.com/",
    "HackerRank": "https://www.hackerrank.com/",
    "Kaggle": "https://www.kaggle.com/",
    "WordPress": "https://wordpress.com/",
    "Medium": "https://medium.com/",
    "Blogger": "https://www.blogger.com/",
    "Ghost": "https://ghost.org/",
    "Wix": "https://www.wix.com/",
    "Weebly": "https://www.weebly.com/",
    "Squarespace": "https://www.squarespace.com/",
    "Amazon": "https://www.amazon.com/",
    "eBay": "https://www.ebay.com/",
    "Alibaba": "https://www.alibaba.com/",
    "AliExpress": "https://www.aliexpress.com/",
    "Craigslist": "https://www.craigslist.org/",
    "Gumtree": "https://www.gumtree.com/",
    "Booking.com": "https://www.booking.com/",
    "Expedia": "https://www.expedia.com/",
    "Airbnb": "https://www.airbnb.com/",
    "Uber": "https://www.uber.com/",
    "Lyft": "https://www.lyft.com/",
}

for website, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        print(f"'{username}' EXISTS  on {website}. RETURN: 1")
    else:
        print(f"'{username}' does NOT exist on {website}. RETURN: 0")


