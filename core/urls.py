from django.urls import path
from core.views import (deletePost, home, followView,
    unfollowView, createPost, deletePost,
    postDetail, likePost, unlikePost,
    commentPost,savePost,unsavePost ,
    likePost, explorePost,savedPost)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('feed/',login_required(home.as_view()),name='home_feed_view'),
    
    path('follow/done/',login_required(followView.as_view()),name='follow_done_view'),
    path('unfollow/done/',login_required(unfollowView.as_view()),name='unfollow_done_view'),
    
    path('post/create/',login_required(createPost.as_view()),name='post_create_view'),
    path('post/delete/<int:id>/',login_required(deletePost.as_view()),name='post_delete_view'),
    path('post/save/<int:id>/',login_required(savePost.as_view()),name='post_save_view'),
    path('post/unsave/<int:id>/',login_required(unsavePost.as_view()),name='post_unsave_view'),
    
    path('post/like/',login_required(likePost.as_view()),name='liked_posts_view'),
    path('post/explore/',login_required(explorePost.as_view()),name='explore_posts_view'),
    path('post/save/',login_required(savedPost.as_view()),name='saved_posts_view'),
    
    path('post/<int:id>/',login_required(postDetail.as_view()),name='post_detail_view'),
    path('post/like/<int:id>/',login_required(likePost.as_view()),name='post_like_view'),
    path('post/unlike/<int:id>/',login_required(unlikePost.as_view()),name='post_unlike_view'),
    path('post/comment/<int:id>/',login_required(commentPost.as_view()),name='post_comment_view'),
    
    
  
]
