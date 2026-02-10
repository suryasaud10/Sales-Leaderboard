
from django.urls import path
from .views import LeaderboardView, SaleListView, SalesRecordCreateView, leaderboard_frontend, SaleCreateView, SaleUpdateView, SaleDeleteView


urlpatterns = [
    path("sales/", SalesRecordCreateView.as_view(), name="sales") ,
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path("leaderboard-ui/", leaderboard_frontend, name="leaderboard-ui"),


    path("sales/list/", SaleListView.as_view(), name="sale-list"),
    path("sales/add/", SaleCreateView.as_view(), name="sale-add"),
    path("sales/<int:pk>/edit/", SaleUpdateView.as_view(), name="sale-edit"),
    path("sales/<int:pk>/delete/", SaleDeleteView.as_view(), name="sale-delete"),
]

