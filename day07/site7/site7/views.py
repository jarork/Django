from django.http import HttpResponse
import time

# 导入缓存
from django.views.decorators.cache import cache_page

# 页面缓存n秒
@cache_page(20)
def test_cache(request):
    # 1. 模拟生成页面是消耗时间的（如复杂计算和复杂查询）
    time.sleep(3)

    # 2. 如果时间变了，表示没有使用缓存
    t1 = time.time()
    return HttpResponse(f"t1 : {t1}")

