from django.db.models import Q
from django.views.generic import ListView
from orders.models.order import Order


class ProfileListView(ListView):
    model = Order
    paginate_by = 8
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # 화면에 보이는 페이지 목록을 5개로 제한
        max_index = len(paginator.page_range)  # 페이지의 총 길이를 카운트해서 max_index로 변경

        page = self.request.GET.get('page')  # get으로 url에 맞는 page를 page에 저장
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range  # 0부터 시작하기 때문에 설정
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        context['orders'] = self.request.user.order_set.is_display()
        return context

    def get_queryset(self):
        return Order.objects.filter(Q(user=self.request.user) & Q(status__gt=1))


# from django.views.generic.base import TemplateView
#
#
# class ProfileView(TemplateView):
#     template_name = 'account/profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)
#         context['orders'] = self.request.user.order_set.is_display()
#         return context
