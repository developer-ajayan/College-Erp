from django.urls import path
from boards import views

urlpatterns=[
    # path('',views.LandingPageView.as_view(),name="home"),
    path('new/',views.newboard,name='new_board'),
    path('list', views.BoardListView.as_view(), name='boards_list'),
    path('<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),
    path('<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/delete/', views.PostDeleteView,
        name="deletepost"),

]