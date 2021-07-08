from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('architecture', ArchViewSet, basename='api_arch')
router.register('architecture_shot', ArchShotViewSet, basename='api_arch_shot')
router.register('architect', ArchitectViewSet, basename='api_architect')
router.register('style', StyleViewSet, basename='api_style')
router.register('blog', BlogViewSet, basename='api_blog')
router.register('blog_shot', BlogShotViewSet, basename='api_blog_shot')
router.register('blog_file', BlogFileViewSet, basename='api_blog_file')
router.register('work', WorkViewSet, basename='api_work')
router.register('work_shot', WorkShotViewSet, basename='api_work_shot')
router.register('work_file', WorkFileViewSet, basename='api_work_file')
router.register('news', NewsViewSet, basename='api_news')
router.register('news_shot', NewsShotViewSet, basename='api_news_shot')
router.register('news_file', NewsFileViewSet, basename='api_news_file')
urlpatterns = router.urls

