from django.contrib import admin

# Register your models here.
from models import Campaign, Newsletter, Newsletter_Sent, User_Profile

class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'campaign_id',
        'campaign_name',
        'description',
        'owner',
        'created',
        'modified',
        'campaign_sequence',
        'participants',
        'visits',
        'status'
    )

admin.site.register(Campaign, CampaignAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'newsletter_id',
        'campaign',
        'sequence',
        'post1',
        'post2',
        'post3',
        'post4',
        'post5',
        'post6',
        'post7',
        'post8',
    )

admin.site.register(Newsletter, NewsletterAdmin)

class User_ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'current_campaign',
        'current_sequence',
        'priority1',
        'priority2',
        'priority3',
        'priority4',
        'priority5',
        'priority6',
        'priority7',
        'priority8',
    )

admin.site.register(User_Profile, User_ProfileAdmin)

class Newsletter_SentAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'campaign_id',
        'sequence',
    )

admin.site.register(Newsletter_Sent, Newsletter_SentAdmin)
