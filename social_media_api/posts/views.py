from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from .models import Post, Like
from notifications.models import Notification

from .models import Post, Like
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(
            author__in=followed_users
        ).order_by('-created_at')
Post.objects.filter(author__in=following_users).order_by

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    """
    Returns posts from users the current user follows,
    ordered by most recent first.
    """
    user = request.user
    following_users = user.following.all()

    posts = Post.objects.filter(
        author__in=following_users
    ).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    like, created = Like.objects.get_or_create(user=user, post=post)

    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )

    return Response({'status': 'post liked'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    Like.objects.filter(user=user, post=post).delete()

    return Response({'status': 'post unliked'})
