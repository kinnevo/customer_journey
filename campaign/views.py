from django.shortcuts import render
from models import Campaign, Newsletter, Newsletter_Sent, User_Profile

def campaign(request):

    if request.user.is_authenticated:
        print request.user.username

#    status = Newsletter.objects.get(username=request.user)
#    print status.current_campaign

#    campaign = Campaign.objects.get(campaign_id=status.current_campaign)
#    print campaign.description



    #     print "IDEAS: ", ideas, ideas.count(), "\n\n"
    #     for i in range(ideas.count()):
    #        print ideas[i].author, "\n"

    return render(request, 'campaign.html', {
        'ideas': 'ideas',
    }, content_type='text/html')


def start(request):
    """
    Capture the name of the campaign ( Campaign )
    Capture the name of the owner
    Date of creation
    set the initial state of the campaign: sequence = 0
    :param request:
    :return:
    """
    return render(request, 'start.html', { 'ideas': 'ideas'}, content_type='text/html')

def create(request):

    campaigns = Campaign.objects.filter(status ="Active")

    return render(request, 'create.html', { 'campaigns': campaigns}, content_type='text/html')

def prepare(request):
    return render(request, 'prepare.html', { 'ideas': 'ideas'}, content_type='text/html')

def followup(request):
    return render(request, 'followup.html', { 'ideas': 'ideas'}, content_type='text/html')

def evaluate(request):
    return render(request, 'evaluate.html', { 'ideas': 'ideas'}, content_type='text/html')

def report(request):
    return render(request, 'report.html', { 'ideas': 'ideas'}, content_type='text/html')


from mezzanine.blog.models import BlogPost, BlogCategory

def create_newsletter(request):
    print "create_newsletter"

    """
    Sources of information:
        Posts -- using selected from all the information in the site -- available in newsletter
        The user profile -- to match with the selected content by taking the user post priority to find the
        post that are going to be shown

    Output
        sent_newsletter -- contain a list of each user with their selected post and a storage for analytics

    Comments
        the hard work is to create the user_profile, once it is created, you run a loop to pick the selected
        Posts and put it into Newsletter_Sent according to user_profile

    """


    user = 1
    email = "jorgez.info@gmail.com"

    personal_newsletter = User_Profile.objects.get( username=user, current_campaign=1, current_sequence=1)
    print "Priority 1:",  personal_newsletter.priority1

    blog_post_content = BlogPost.objects.get(id = 2 )
    title = blog_post_content.title
    content = blog_post_content.content
    categories = BlogCategory.objects.get ( id = 2)
# tags
    tags = blog_post_content.keywords_string
    url = blog_post_content.slug
    domain = "127.0.0.1:8000"
    url = "http://" + domain + "/blog/" + url + "?ref=123abc"
    share_fb = ""
    share_twitter = ""

    template = {
        "user" : user,
        "email" : email,
        "title" : title,
        "content" : content,
        "categories" : categories,
        "tags" : tags,
        "url" : url,
        "share_fb" : share_fb,
        "share_twitter" : share_twitter
    }

    print "Title:", title, "\nContent", content, "\nCategories: " ,categories, "\Tags: ", tags, "\nurl: ", url

    return render(request, 'create_newsletter.html', { 'template': template}, content_type='text/html')

