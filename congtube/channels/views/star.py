from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin
from channels.models import Channel
from orders.models import Order


class StarDetailView(DetailView, MultipleObjectMixin): # paginate_by를 사용하기 위해 Multiple... 상속
    model = Channel
    paginate_by = 10 # 한 페이지에 오브젝트가 10개가 보이게 설정
    template_name = 'channels/star.html'

    def get_context_data(self, **kwargs):
        # Multiple을 사용하기 위해선 object_list로 선언해주어야 한다. ListView의 Default는 object_list 이기 때문에
        object_list = Order.objects.filter(Q(channel=self.get_object()) & Q(status=2)).order_by('id') # 주문완료이면서 channel = get_object()
        context = super(StarDetailView, self).get_context_data(object_list=object_list, **kwargs)
        # StarDetailView 위에 get_context_data의 object_list를 위에서 선언한 object_list로 변경
        paginator = context['paginator']
        page_numbers_range = 5  # 화면에 보이는 페이지 목록을 5개로 제한
        max_index = len(paginator.page_range) # 페이지의 총 길이를 카운트해서 max_index로 변경

        page = self.request.GET.get('page') # get으로 url에 맞는 page를 page에 저장
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range # 0부터 시작하기 때문에 설정
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context
