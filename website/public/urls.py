from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = "public"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("media", views.MediaView.as_view(), name="media"),
    path("about", views.AboutView.as_view(), name="about"),
    path("recipes", views.RecipesView.as_view(), name="recipes"),
    path("community-cookbook", RedirectView.as_view(url=reverse_lazy("public:recipes"))),
    # Stable redirect url to our (hashed) logo url
    path("logo", views.logo, name="logo"),
    path("community-cookbook-pdf", views.community_cookbook, name="community_cookbook_pdf"),
    # External link redirects
    path(
        "links/community-cookbook-order",
        RedirectView.as_view(url="https://docs.google.com/forms/d/e/1FAIpQLSeJAh0pJNgrEzTQo8n7b13e-PfvDWFkL3a1owYZK1fhiJeTOw/viewform"),
        name="community_cookbook_order",
    ),
    path(
        "links/groceries",
        RedirectView.as_view(url="https://forms.gle/nuEZVcncmtvMZwHw6"),
        name="grocery_request_form",
    ),
    path(
        "links/facebook",
        RedirectView.as_view(url="https://www.facebook.com/groups/675649626532144/"),
        name="facebook",
    ),
    path(
        "links/instagram",
        RedirectView.as_view(url="https://www.instagram.com/peoplespantryto/"),
        name="instagram",
    ),
    path(
        "links/twitter",
        RedirectView.as_view(url="https://twitter.com/peoplespantryTO"),
        name="twitter",
    ),
    path(
        "links/tiktok",
        RedirectView.as_view(url="https://www.tiktok.com/@thepeoplespantry"),
        name="tiktok",
    ),
    path(
        "links/sister-initiative",
        RedirectView.as_view(url="https://forms.gle/uJyEwwX8NbUZb4nX6"),
        name="sister_initiative",
    ),
    path(
        "links/sister-initiative-volunteers",
        RedirectView.as_view(url="https://forms.gle/i7BscqiGwyvRL5Fr7"),
        name="sister_initiative_volunteers",
    ),
    path(
        "links/donate",
        RedirectView.as_view(
            url="https://www.gofundme.com/f/the-people039s-pantry-covid19-emergency-meal-fund"
        ),
        name="donate",
    ),
    path(
        "links/sponsor",
        RedirectView.as_view(url="https://donorbox.org/thepeoplespantryto"),
        name="sponsor",
    ),
    path(
        "links/shop",
        RedirectView.as_view(url="http://shop.thepeoplespantryto.com/"),
        name="shop",
    ),
    path(
        "links/cooking-guide",
        RedirectView.as_view(
            url="https://docs.google.com/document/d/1OCS-i_pm87MsT-POAbcDCKrv6SBA0J9tepOaETyLwmY/edit"
        ),
        name="cooking_guide",
    ),
    path(
        "links/cooking-quick-guide",
        RedirectView.as_view(
            url="https://drive.google.com/file/d/1iPu8yy_GbBuF6IK2dZwM-mqxzgekqVfI/view"
        ),
        name="cooking_quick_guide",
    ),
    path(
        "links/cooking-onboarding",
        RedirectView.as_view(
            url="https://drive.google.com/file/d/15ijQmXwx9vsJtXrUe0-K0DHaHTKMAW1k/view"
        ),
        name="cooking_onboarding",
    ),
    path(
        "links/delivery-guide",
        RedirectView.as_view(
            url="https://docs.google.com/document/d/1Kxf0Zz3dMO7vI410VMY5sTJX3PMh7Mt8dGQIgNmQwGs/edit"
        ),
        name="delivery_guide",
    ),
    path(
        "links/reimbursement",
        RedirectView.as_view(
            url="https://docs.google.com/forms/d/e/1FAIpQLSfuOiqDuuvngZhPRYhy5BpzFf5IwGvpYz4QYRQ3TzA18el9kA/viewform"
        ),
        name="reimbursement",
    ),
    path(
        "links/code-of-conduct",
        RedirectView.as_view(
            url="https://docs.google.com/document/d/1jJUnD8ZUWxM0Tkx6C-V2K-S2aYioY1LlIp3T9Yt-C5M/edit"
        ),
        name="code_of_conduct",
    ),
    path(
        "links/essential-service-letter",
        RedirectView.as_view(
            url="https://docs.google.com/document/d/1uu7pl_ID4XIQScVOyH8i2Xx0E7v8mV9mi14XLnPC2jo/edit"
        ),
        name="essential_service_letter",
    ),
    path(
        "links/logistics-teams-descriptions",
        RedirectView.as_view(
            url="https://docs.google.com/document/d/1V3R2bVRPOAaytM4h7UP7jXL7jHz-2MkLnN-9bhkPipk/edit"
        ),
        name="logistics_teams_descriptions",
    ),
    path(
        "links/caremongering-to",
        RedirectView.as_view(
            url="https://www.facebook.com/groups/TO.Community.Response.COVID19/"
        ),
        name="caremongering_to",
    ),
    path(
        "links/halal-resource",
        RedirectView.as_view(
            url="https://drive.google.com/file/d/1f3YewToGzFM9kpebBGKl3kddcoKwXlRv/view"
        ),
        name="halal_resource",
    ),
    path(
        "links/unity-kitchen",
        RedirectView.as_view(url="https://www.instagram.com/unitykitchento/"),
        name="unity_kitchen",
    ),
    path(
        "links/anti-racism",
        RedirectView.as_view(
            url="https://www.sundanceharvestfarm.com/learning-resources"
        ),
        name="anti_racism",
    ),
]
