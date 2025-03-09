from django.shortcuts import render
import instaloader

def fetch_instagram_details(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        return {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "profile_pic": profile.profile_pic_url,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
        }
    except Exception as e:
        return {"error": str(e)}

def home(request):
    details = None
    error = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        details = fetch_instagram_details(username)
        if "error" in details:
            error = details["error"]
            details = None

    return render(request, "index.html", {"details": details, "error": error})
