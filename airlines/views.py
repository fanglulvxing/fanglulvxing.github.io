from django.shortcuts import render, get_object_or_404,redirect
from .models import Airline, Order
from .filters import AirlineFilter
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

import random
from .forms import ChooseSeatForm, CheckBagForm, AddOrderForm, SubmitOrderForm, SurveyForm
import time
import json
from django.http import JsonResponse

def get_destination_choices(request):
    starting_airport = request.GET.get('starting_airport', None)
    
    # 根据选择的出发地更新目的地选项
    if starting_airport == '阿尔山':
        destination_choices = Airline.DESTINATION_CHOICES1
    elif starting_airport == '阿克苏':
        destination_choices = Airline.DESTINATION_CHOICES2
    elif starting_airport == '阿拉善右旗':
        destination_choices = Airline.DESTINATION_CHOICES3
#     elif starting_airport == '阿拉善左旗':
#         destination_choices = Airline.DESTINATION_CHOICES4
#     elif starting_airport == '海口':
#         destination_choices = Airline.DESTINATION_CHOICES5
#     elif starting_airport == '遵义':
#         destination_choices = Airline.DESTINATION_CHOICES6
#     elif starting_airport == '西宁':
#         destination_choices = Airline.DESTINATION_CHOICES7
#     elif starting_airport == '阜阳':
#         destination_choices = Airline.DESTINATION_CHOICES8
#     elif starting_airport == '西安':
#         destination_choices = Airline.DESTINATION_CHOICES9
#     elif starting_airport == '临沂':
#         destination_choices = Airline.DESTINATION_CHOICES10
#     elif starting_airport == '福州':
#         destination_choices = Airline.DESTINATION_CHOICES11
#     elif starting_airport == '昆明':
#         destination_choices = Airline.DESTINATION_CHOICES12
#     elif starting_airport == '西昌':
#         destination_choices = Airline.DESTINATION_CHOICES13
#     elif starting_airport == '杭州':
#         destination_choices = Airline.DESTINATION_CHOICES14
#     elif starting_airport == '烟台':
#         destination_choices = Airline.DESTINATION_CHOICES15
#     elif starting_airport == '成都':
#         destination_choices = Airline.DESTINATION_CHOICES16
#     elif starting_airport == '锦州':
#         destination_choices = Airline.DESTINATION_CHOICES17
#     elif starting_airport == '大庆':
#         destination_choices = Airline.DESTINATION_CHOICES18
#     elif starting_airport == '南京':
#         destination_choices = Airline.DESTINATION_CHOICES19
#     elif starting_airport == '延吉':
#         destination_choices = Airline.DESTINATION_CHOICES20
#     elif starting_airport == '重庆':
#         destination_choices = Airline.DESTINATION_CHOICES21
#     elif starting_airport == '固原':
#         destination_choices = Airline.DESTINATION_CHOICES22
#     elif starting_airport == '大理':
#         destination_choices = Airline.DESTINATION_CHOICES23
#     elif starting_airport == '郑州':
#         destination_choices = Airline.DESTINATION_CHOICES24
#     elif starting_airport == '哈密':
#         destination_choices = Airline.DESTINATION_CHOICES25
#     elif starting_airport == '北海':
#         destination_choices = Airline.DESTINATION_CHOICES26
#     elif starting_airport == '沈阳':
#         destination_choices = Airline.DESTINATION_CHOICES27
#     elif starting_airport == '张家界':
#         destination_choices = Airline.DESTINATION_CHOICES28
#     elif starting_airport == '抚远':
#         destination_choices = Airline.DESTINATION_CHOICES29
#     elif starting_airport == '台州':
#         destination_choices = Airline.DESTINATION_CHOICES30
#     elif starting_airport == '哈尔滨':
#         destination_choices = Airline.DESTINATION_CHOICES31
#     elif starting_airport == '泉州':
#         destination_choices = Airline.DESTINATION_CHOICES32
#     elif starting_airport == '大同':
#         destination_choices = Airline.DESTINATION_CHOICES33
#     elif starting_airport == '秦皇岛':
#         destination_choices = Airline.DESTINATION_CHOICES34
#     elif starting_airport == '怀化':
#         destination_choices = Airline.DESTINATION_CHOICES35
#     elif starting_airport == '舟山':
#         destination_choices = Airline.DESTINATION_CHOICES36
#     elif starting_airport == '大连':
#         destination_choices = Airline.DESTINATION_CHOICES37
#     elif starting_airport == '湛江':
#         destination_choices = Airline.DESTINATION_CHOICES38
#     elif starting_airport == '衢州':
#         destination_choices = Airline.DESTINATION_CHOICES39
#     elif starting_airport == '西双版纳':
#         destination_choices = Airline.DESTINATION_CHOICES40
#     elif starting_airport == '鄂尔多斯':
#         destination_choices = Airline.DESTINATION_CHOICES41
#     elif starting_airport == '广州':
#         destination_choices = Airline.DESTINATION_CHOICES42
#     elif starting_airport == '吐鲁番':
#         destination_choices = Airline.DESTINATION_CHOICES43
#     elif starting_airport == '济南':
#         destination_choices = Airline.DESTINATION_CHOICES44
#     elif starting_airport == '日喀则':
#         destination_choices = Airline.DESTINATION_CHOICES45
#     elif starting_airport == '乌鲁木齐':
#         destination_choices = Airline.DESTINATION_CHOICES46
#     elif starting_airport == '朝阳':
#         destination_choices = Airline.DESTINATION_CHOICES47
#     elif starting_airport == '陇南':
#         destination_choices = Airline.DESTINATION_CHOICES48
#     else:
#         destination_choices = Airline.DESTINATION_CHOICES
    
    return JsonResponse(destination_choices, safe=False)

# def get_starting_choices(request):
#     destination_airport = request.GET.get('destination_airport', None)
    
#     # 根据选择的出发地更新目的地选项
#     if destination_airport == '呼和浩特':
#         starting_choices = Airline.START_CHOICES1
#     elif destination_airport == '十堰':
#         starting_choices = Airline.START_CHOICES2
#     elif destination_airport == '南阳':
#         starting_choices = Airline.START_CHOICES3
#     elif destination_airport == '昆明':
#         starting_choices = Airline.START_CHOICES4
#     elif destination_airport == '琼海':
#         starting_choices = Airline.START_CHOICES5
#     elif destination_airport == '上海':
#         starting_choices = Airline.START_CHOICES6
#     elif destination_airport == '天津':
#         starting_choices = Airline.START_CHOICES7
#     elif destination_airport == '西双版纳':
#         starting_choices = Airline.START_CHOICES8
#     elif destination_airport == '惠州':
#         starting_choices = Airline.START_CHOICES9
#     elif destination_airport == '烟台':
#         starting_choices = Airline.START_CHOICES10
#     elif destination_airport == '杭州':
#         starting_choices = Airline.START_CHOICES11
#     elif destination_airport == '西安':
#         starting_choices = Airline.START_CHOICES12
#     elif destination_airport == '石家庄':
#         starting_choices = Airline.START_CHOICES13
#     elif destination_airport == '张家界':
#         starting_choices = Airline.START_CHOICES14
#     elif destination_airport == '银川':
#         starting_choices = Airline.START_CHOICES15
#     elif destination_airport == '林芝':
#         starting_choices = Airline.START_CHOICES16
#     elif destination_airport == '桂林':
#         starting_choices = Airline.START_CHOICES17
#     elif destination_airport == '深圳':
#         starting_choices = Airline.START_CHOICES18
#     elif destination_airport == '珠海':
#         starting_choices = Airline.START_CHOICES19
#     elif destination_airport == '六盘':
#         starting_choices = Airline.START_CHOICES20
#     elif destination_airport == '澜沧':
#         starting_choices = Airline.START_CHOICES21
#     elif destination_airport == '兰州':
#         starting_choices = Airline.START_CHOICES22
#     elif destination_airport == '南京':
#         starting_choices = Airline.START_CHOICES23
#     elif destination_airport == '阿克苏':
#         starting_choices = Airline.START_CHOICES24
#     elif destination_airport == '柳州':
#         starting_choices = Airline.START_CHOICES25
#     elif destination_airport == '北京':
#         starting_choices = Airline.START_CHOICES26
#     elif destination_airport == '盐城':
#         starting_choices = Airline.START_CHOICES27
#     elif destination_airport == '大连':
#         starting_choices = Airline.START_CHOICES28
#     elif destination_airport == '威海':
#         starting_choices = Airline.START_CHOICES29
#     elif destination_airport == '沈阳':
#         starting_choices = Airline.START_CHOICES30
#     elif destination_airport == '青岛':
#         starting_choices = Airline.START_CHOICES31
#     elif destination_airport == '巴彦':
#         starting_choices = Airline.START_CHOICES32
#     elif destination_airport == '绵阳':
#         starting_choices = Airline.START_CHOICES33
#     elif destination_airport == '黄山':
#         starting_choices = Airline.START_CHOICES34
#     elif destination_airport == '福州':
#         starting_choices = Airline.START_CHOICES35
#     elif destination_airport == '郑州':
#         starting_choices = Airline.START_CHOICES36
#     elif destination_airport == '宁波':
#         starting_choices = Airline.START_CHOICES37
#     elif destination_airport == '南通':
#         starting_choices = Airline.START_CHOICES38
#     elif destination_airport == '海口':
#         starting_choices = Airline.START_CHOICES39
#     elif destination_airport == '广州':
#         starting_choices = Airline.START_CHOICES40
#     elif destination_airport == '安庆':
#         starting_choices = Airline.START_CHOICES41
#     elif destination_airport == '常州':
#         starting_choices = Airline.START_CHOICES42
#     elif destination_airport == '贵阳':
#         starting_choices = Airline.START_CHOICES43
#     elif destination_airport == '哈尔滨':
#         starting_choices = Airline.START_CHOICES44
#     elif destination_airport == '重庆':
#         starting_choices = Airline.START_CHOICES45
#     elif destination_airport == '三亚':
#         starting_choices = Airline.START_CHOICES46
#     elif destination_airport == '广元':
#         starting_choices = Airline.START_CHOICES47
#     elif destination_airport == '伊宁':
#         starting_choices = Airline.START_CHOICES48
#     elif destination_airport == '怀化':
#         starting_choices = Airline.START_CHOICES49
#     elif destination_airport == '南宁':
#         starting_choices = Airline.START_CHOICES50
#     elif destination_airport == '上饶':
#         starting_choices = Airline.START_CHOICES51
#     elif destination_airport == '连云港':
#         starting_choices = Airline.START_CHOICES52
#     elif destination_airport == '成都':
#         starting_choices = Airline.START_CHOICES53
#     elif destination_airport == '温州':
#         starting_choices = Airline.START_CHOICES54

#     else:
#         starting_choices = Airline.START_CHOICES
    
#     return JsonResponse(starting_choices, safe=False)

        
def welcome(request):
    return render(request,'airlines/welcome.html')
def thank(request):
    return render(request,'airlines/thank.html')

def search(request, pk):
    airlines = Airline.objects.none()
    airlineFilter = AirlineFilter(queryset=airlines)

    if request.method == "POST":
        airlineFilter = AirlineFilter(request.POST, queryset=Airline.objects.all())
        
    context = {
        'airlineFilter': airlineFilter,
        'order_id': pk
    }

    return render(request, 'airlines/search.html', context)


def AirlineDetailView(request, aid, oid):
    print(aid)
    print(oid)
    airline = get_object_or_404(Airline, id=aid)

    current_order =get_object_or_404(Order, id=oid)
    carbon_offset_choice = current_order.carbon_choice
    print(carbon_offset_choice)

    context = {
        "airline":airline,
        "carbon_offset_choice":int(carbon_offset_choice),
        "current_order":current_order.pk,
        "carbon_offset_fee":50,
        "choice_0":0,
        "choice_1":1,
        "choice_2":2,
        "choice_3":3
        

    }
    return render(request, 'airlines/airline_detail.html', context)

class AddOrderView(CreateView):
    model = Order
    template_name = 'airlines/index.html'
    form_class = AddOrderForm
    

class SubmitOrderView(UpdateView):
    model = Order
    template_name = 'airlines/comfirm_order.html'
    # fields = '__all__'
    form_class = SubmitOrderForm
    pk_url_kwarg = 'oid'
    
    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])

    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        return reverse_lazy("survey", kwargs={'pk': current_order.pk})

    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(SubmitOrderView, self).get_context_data(
            *args, **kwargs)
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice

        # context data
        context['current_order'] = current_order.pk
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['carbon_offset_fee'] = 50
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context  

# class ChooseSeatView(UpdateView):
#     model = Order
#     template_name = 'airlines/choose_seat.html'
#     form_class = ChooseSeatForm
#     pk_url_kwarg = 'oid'

#     def get_queryset(self):
#         return super().get_queryset().filter(id=self.kwargs['oid'])
    
#     def get_success_url(self):
#         current_order = Order.objects.get(id=self.kwargs["oid"])
#         return reverse_lazy("check_bag", kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})
    
#     def get_context_data(self, *args, **kwargs):
#         #cat_menu = Category.objects.all()
#         context = super(ChooseSeatView, self).get_context_data(
#             *args, **kwargs)
#         current_order = Order.objects.get(id=self.kwargs["oid"])
        
#         # context data
#         context['current_order'] = current_order.pk
#         context['airline_id'] = self.kwargs["aid"]

        
#         # context['post'] = current_post
#         return context  
    
class CheckBagView(UpdateView):
    model = Order
    template_name = 'airlines/check_bag.html'
    form_class = CheckBagForm
    pk_url_kwarg = 'oid'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])
    

    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = int(current_order.carbon_choice)
        return_page = "carbon_offset"
        if carbon_offset_choice == 0 or carbon_offset_choice == 3: # control group &  compulsory fee group
            return_page = "submit_order"

        return reverse_lazy(return_page, kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})


    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(CheckBagView, self).get_context_data(
            *args, **kwargs)
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice
        
        airline = get_object_or_404(Airline, id=self.kwargs['aid'])#这两句我后加的
        context['airline'] = airline
        # context data
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['current_order'] = current_order.pk
        context['carbon_offset_fee'] = 50
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context     


class CarbonOffsetView(UpdateView):
    model = Order
    template_name = 'airlines/carbon_offset.html'
    fields = ()
    pk_url_kwarg = 'oid'
    
    # start_time = None
    # stay_duration = 0

    # def get(self, request, *args, **kwargs):
    #     self.start_time = time.time()  # 记录开始时间
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.stop_timer()  # 停止计时
    #     self.send_stay_duration()  # 发送停留时间数据
    #     return super().post(request, *args, **kwargs)

    # def stop_timer(self):
    #     end_time = time.time()  # 记录结束时间
    #     self.stay_duration += end_time - self.start_time  # 累计停留时间

    # def send_stay_duration(self):
    #     # 在这里发送停留时间数据到后端进行处理
    #     current_order = Order.objects.get(id=self.kwargs["oid"])
    #     stay_duration_data = {
    #         'stayDuration': self.stay_duration,
    #         'orderId': current_order.pk
    #     }

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])


    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        return reverse_lazy("submit_order", kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})

    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(CarbonOffsetView, self).get_context_data(
            *args, **kwargs) 
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice
        airline = get_object_or_404(Airline, id=self.kwargs['aid'])#这两句我后加的
        context['airline'] = airline

        # context data
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['choice_0'] = 0
        context['choice_1'] = 1
        context['choice_2'] = 2
        context['choice_3'] = 3
        context['carbon_offset_fee'] = 50
        context['current_order'] = current_order.pk
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context                

class SurveyView(UpdateView):
    model = Order
    template_name = 'airlines/survey.html'
    form_class = SurveyForm
    success_url = reverse_lazy('new_order')
