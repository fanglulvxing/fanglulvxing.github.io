from email.policy import default
from django.db import models
from django.urls import reverse

class Order(models.Model):
    # stay_duration=models.CharField(max_length=100, default='-')
    starting_airport = models.CharField(max_length=100, default='-')
    destination_airport = models.CharField(max_length=100, default='-')
    #airlines = models.CharField(max_length=100, choices=AIRLINE_CHOICES)
    airlines = models.CharField(max_length=100, default='-')
    flight = models.CharField(max_length=100, default='-')
    aircraft_type = models.CharField(max_length=100, default='-')
    departure_time = models.CharField(blank=True, null=True,max_length=10)
    arrival_time = models.CharField(blank=True, null=True,max_length=10)
    punctuality_rate = models.CharField(max_length=100,default='-')
    seat_number = models.CharField(max_length=100,default='-')
    check_bag = models.CharField(max_length=100,default='-')
    price = models.CharField(max_length=10,default='-')
    total_price = models.CharField(max_length=10,default='-')
    carbon_choice = models.CharField(max_length=10,default='-')
    
    subject_gender = models.CharField(max_length=10,default='-')
    subject_age = models.CharField(max_length=10,default='-')
    subject_marital = models.CharField(max_length=10,default='-')
    subject_education = models.CharField(max_length=10,default='-')
    subject_income = models.CharField(max_length=10,default='-')

    survery_Q1_a = models.CharField(max_length=30,default='-')
    survery_Q1_b = models.CharField(max_length=30,default='-')
    survery_Q1_c = models.CharField(max_length=30,default='-')
    survery_Q1_d = models.CharField(max_length=30,default='-')
    survery_Q1_e = models.CharField(max_length=30,default='-')

    survery_Q2 = models.CharField(max_length=30,default='-')
    
    survery_Q3_a = models.CharField(max_length=30,default='-')
    survery_Q3_b = models.CharField(max_length=30,default='-')
    survery_Q3_c = models.CharField(max_length=30,default='-')
    survery_Q3_d = models.CharField(max_length=30,default='-')
    
    survery_Q4_a = models.CharField(max_length=30,blank=True)
    survery_Q4_b = models.CharField(max_length=30,blank=True)
    survery_Q4_c = models.CharField(max_length=30,blank=True)
    survery_Q4_d = models.CharField(max_length=30,blank=True)
    survery_Q4_e = models.CharField(max_length=30,blank=True)

    survery_Q5_a = models.CharField(max_length=30,blank=True)
    survery_Q5_b = models.CharField(max_length=30,blank=True)
    survery_Q5_c = models.CharField(max_length=30,blank=True)
    survery_Q5_d = models.CharField(max_length=30,blank=True)
    survery_Q5_e = models.CharField(max_length=30,blank=True)
    survery_Q5_f = models.CharField(max_length=30,blank=True)
    survery_Q5_g = models.CharField(max_length=30,blank=True)
    
    survery_Q6 = models.CharField(max_length=30,default='-',blank=True)
    
    def get_absolute_url(self):
    # set success url
        return reverse("search", kwargs={'pk': self.pk})


class Airline(models.Model):

        AIRLINE_CHOICES = (
            ("金鹏航空","金鹏航空"),
            ("中国国航","中国国航"),
            ("昆明航空","昆明航空"),
            ("深圳航空","深圳航空"),
            ("海南航空","海南航空"),
            ("南方航空","南方航空"),
            ("厦门航空","厦门航空"),
            ("祥鹏航空","祥鹏航空"),
            ("东方航空","东方航空"),
            ("多彩航空","多彩航空"),
            ("天津航空","天津航空"),
            ("华夏航空","华夏航空"),
            ("山东航空","山东航空"),
            ("长龙航空","长龙航空"),
            ("中国联航","中国联航"),
            ("河北航空","河北航空"),
            ("首都航空","首都航空"),
            ("四川航空","四川航空"),
            ("西藏航空","西藏航空"),
            ("成都航空","成都航空"),
            ("吉祥航空","吉祥航空"),
            ("上海航空","上海航空"),
            ("东海航空","东海航空"),
            ("重庆航空","重庆航空"),
            ("西部航空","西部航空"),
            ("幸福航空","幸福航空"),
            ("福州航空","福州航空"),
            ("瑞丽航空","瑞丽航空"),
            ("桂林航空","桂林航空"),
            ("青岛航空","青岛航空"),
            ("北部湾航空","北部湾航空"),
            ("长安航空","长安航空"),
            ("江西航空","江西航空"),
            ("乌鲁木齐航空","乌鲁木齐航空"),
        
    )
        START_CHOICES = (
    ("深圳", "深圳"),
    ("武汉", "武汉"),
    ("贵阳", "贵阳"),
    ("威海", "威海"),
    ("海口", "海口"),
    ("遵义", "遵义"),
    ("西宁", "西宁"),
    ("阜阳", "阜阳"),
    ("西安", "西安"),
    ("临沂", "临沂"),
    ("福州", "福州"),
    ("昆明", "昆明"),
    ("西昌", "西昌"),
    ("杭州", "杭州"),
    ("烟台", "烟台"),
    ("成都", "成都"),
    ("锦州", "锦州"),
    ("大庆", "大庆"),
    ("南京", "南京"),
    ("延吉", "延吉"),
    ("重庆", "重庆"),
    ("固原", "固原"),
    ("大理", "大理"),
    ("郑州", "郑州"),
    ("哈密", "哈密"),
    ("北海", "北海"),
    ("沈阳", "沈阳"),
    ("张家界", "张家界"),
    ("抚远", "抚远"),
    ("台州", "台州"),
    ("哈尔滨", "哈尔滨"),
    ("泉州", "泉州"),
    ("大同", "大同"),
    ("秦皇岛", "秦皇岛"),
    ("怀化", "怀化"),
    ("舟山", "舟山"),
    ("大连", "大连"),
    ("湛江", "湛江"),
    ("衢州", "衢州"),
    ("西双版纳", "西双版纳"),
    ("鄂尔多斯", "鄂尔多斯"),
    ("广州", "广州"),
    ("吐鲁番", "吐鲁番"),
    ("济南", "济南"),
    ("日喀则", "日喀则"),
    ("乌鲁木齐", "乌鲁木齐"),
    ("朝阳", "朝阳"),
    ("陇南", "陇南"),
)

        DESTINATION_CHOICES = (
            ("呼和浩特","呼和浩特"),
            ("十堰","十堰"),
            ("南阳","南阳"),
            ("昆明","昆明"),
            ("琼海","琼海"),
            ("上海","上海"),
            ("天津","天津"),
            ("西双版纳","西双版纳"),   
    )
        DESTINATION_CHOICES1 = (
            ("呼和浩特","呼和浩特"),
            ("广州","广州"),
            ("满洲里","满洲里"),
            ("乌兰浩特","乌兰浩特"),
            ("昆明","昆明"),
            ("西安","西安"),
            ("北京","北京"),
    )
        DESTINATION_CHOICES2 = (

        ("杭州", "杭州"),
        ("乌鲁木齐", "乌鲁木齐"),
        ("北京", "北京"),
        ("青岛", "青岛"),
        ("郑州", "郑州"),
        ("西安", "西安"),
        ("成都", "成都"),
    )

        DESTINATION_CHOICES3 = (
    ("阿拉善左旗", "阿拉善左旗"),
)
        DESTINATION_CHOICES4 = (
    ("杭州", "杭州"),
    ("西安", "西安"),
)
        DESTINATION_CHOICES5 = (
        ("石家庄", "石家庄"),
        ("十堰", "十堰"),
        ("张家界", "张家界"),
        )
        DESTINATION_CHOICES6 = (
        ("昆明", "昆明"),
        ("银川", "银川"),
        )

        # DESTINATION_CHOICES10
        DESTINATION_CHOICES7 = (
        ("成都", "成都"),
        )

        # DESTINATION_CHOICES11
        DESTINATION_CHOICES8 = (
        ("舟山", "舟山"),
        )

        # DESTINATION_CHOICES12
        DESTINATION_CHOICES9 = (
        ("林芝", "林芝"),
        )

        # DESTINATION_CHOICES13
        DESTINATION_CHOICES10 = (
        ("桂林", "桂林"),
        ("天津", "天津"),
        ("深圳", "深圳"),
        ("珠海", "珠海"),
        )

        # DESTINATION_CHOICES14
        DESTINATION_CHOICES11= (
        ("六盘", "六盘"),
        )

        # DESTINATION_CHOICES15
        DESTINATION_CHOICES12 = (
        ("澜沧", "澜沧"),
        ("兰州", "兰州"),
        )

        # DESTINATION_CHOICES16
        DESTINATION_CHOICES13 = (
        ("南京", "南京"),
        ("重庆", "重庆"),
        )

        # DESTINATION_CHOICES17
        DESTINATION_CHOICES14 = (
        ("阿克苏", "阿克苏"),
        ("柳州", "柳州"),
        ("北京", "北京"),
        )

        # DESTINATION_CHOICES18
        DESTINATION_CHOICES15 = (
        ("盐城", "盐城"),
        ("大连", "大连"),
        )

        # DESTINATION_CHOICES19
        DESTINATION_CHOICES16 = (
        ("威海", "威海"),
        )

        # DESTINATION_CHOICES20
        DESTINATION_CHOICES17 = (
        ("深圳", "深圳"),
        )

        # DESTINATION_CHOICES21
        DESTINATION_CHOICES18 = (
        ("沈阳", "沈阳"),
        )

        # DESTINATION_CHOICES22
        DESTINATION_CHOICES19 = (
        ("盐城", "盐城"),
        ("兰州", "兰州"),
        )

        # DESTINATION_CHOICES23
        DESTINATION_CHOICES20 = (
        ("青岛", "青岛"),
        )

        # DESTINATION_CHOICES24
        DESTINATION_CHOICES21 = (
        ("南京", "南京"),
        ("巴彦", "巴彦"),
        )

        # DESTINATION_CHOICES25
        DESTINATION_CHOICES22 = (
        ("天津", "天津"),
        )

        # DESTINATION_CHOICES26
        DESTINATION_CHOICES23 = (
        ("绵阳", "绵阳"),
        )

        # DESTINATION_CHOICES27
        DESTINATION_CHOICES24 = (
        ("黄山", "黄山"),
        ("福州", "福州"),
        )

        # DESTINATION_CHOICES28
        DESTINATION_CHOICES25 = (
        ("郑州", "郑州"),
        )

        # DESTINATION_CHOICES29
        DESTINATION_CHOICES26 = (
        ("深圳", "深圳"),
        ("宁波", "宁波"),
        )

        # DESTINATION_CHOICES30
        DESTINATION_CHOICES27 = (
        ("南通", "南通"),
        )

        # DESTINATION_CHOICES31
        DESTINATION_CHOICES28 = (
        ("海口", "海口"),
        )

        # DESTINATION_CHOICES32
        DESTINATION_CHOICES29 = (
        ("上海", "上海"),
        )

        # DESTINATION_CHOICES33
        DESTINATION_CHOICES30 = (
        ("广州", "广州"),
        )

        # DESTINATION_CHOICES34
        DESTINATION_CHOICES31 = (
        ("安庆", "安庆"),
        ("常州", "常州"),
        )

        # DESTINATION_CHOICES35
        DESTINATION_CHOICES32 = (
        ("贵阳", "贵阳"),
        ("青岛", "青岛"),
        )

        # DESTINATION_CHOICES36
        DESTINATION_CHOICES33 = (
        ("哈尔滨", "哈尔滨"),
        )

        # DESTINATION_CHOICES37
        DESTINATION_CHOICES34 = (
        ("青岛", "青岛"),
        )

        # DESTINATION_CHOICES38
        DESTINATION_CHOICES35 = (
        ("天津", "天津"),
        )

        # DESTINATION_CHOICES39
        DESTINATION_CHOICES36 = (
        ("上饶", "上饶"),
        )
        DESTINATION_CHOICES37 = (
        ("连云港", "连云港"),
        ("广州", "广州"),
        )
        DESTINATION_CHOICES38 = (
        ("成都", "成都"),
        )
        DESTINATION_CHOICES39 = (
        ("青岛", "青岛"),
        )
        DESTINATION_CHOICES40 = (
        ("南京", "南京"),
        ("重庆", "重庆"),
        )
        DESTINATION_CHOICES41 = (
        ("三亚", "三亚"),
        )
        DESTINATION_CHOICES42 = (
        ("广元", "广元"),
        )
        DESTINATION_CHOICES43 = (
        ("伊宁", "伊宁"),
        )
        DESTINATION_CHOICES44 = (
        ("怀化", "怀化"),
        ("南宁", "南宁"),
        )
        DESTINATION_CHOICES45 = (
        ("成都", "成都"),
        )
        DESTINATION_CHOICES46 = (
        ("温州", "温州"),
        )
        DESTINATION_CHOICES47 = (
        ("北京", "北京"),
        )
        DESTINATION_CHOICES48 = (
        ("重庆", "重庆"),
        )
        
        START_CHOICES1 = (
        ("深圳", "深圳"),
        )
        START_CHOICES2 = (
        ("深圳", "深圳"),
        ("海口", "海口"),
        )
        START_CHOICES3 = (
        ("深圳", "深圳"),
        )
        START_CHOICES4 = (
        ("武汉", "武汉"),
        ("遵义", "遵义"),
        )
        START_CHOICES5 = (
        ("武汉", "武汉"),
        )
        START_CHOICES6 = (
        ("武汉", "武汉"),
        ("抚远", "抚远"),
        )
        START_CHOICES7 = (
        ("贵阳", "贵阳"),
        ("临沂", "临沂"),
        ("固原", "固原"),
        ("怀化", "怀化"),
        )
        START_CHOICES8 = (
        ("贵阳", "贵阳"),
        )
        START_CHOICES9 = (
        ("贵阳", "贵阳"),
        )
        START_CHOICES10 = (
        ("贵阳", "贵阳"),
        )
        START_CHOICES11 = (
        ("威海", "威海"),
        )
        START_CHOICES12 = (
        ("威海", "威海"),
        )
        START_CHOICES13 = (
        ("海口", "海口"),
        )
        START_CHOICES14 = (
        ("海口", "海口"),
        )
        START_CHOICES15 = (
        ("遵义", "遵义"),
        )
        START_CHOICES16 = (
        ("西安", "西安"),
        )
        START_CHOICES17 = (
        ("临沂", "临沂"),
        )
        START_CHOICES18 = (
        ("临沂", "临沂"),
        ("锦州", "锦州"),
        ("北海", "北海"),
        )
        START_CHOICES19 = (
        ("临沂", "临沂"),
        )
        START_CHOICES20 = (
        ("福州", "福州"),
        )
        START_CHOICES21 = (
        ("昆明", "昆明"),
        )
        START_CHOICES22 = (
        ("昆明", "昆明"),
        ("南京", "南京"),
        )
        START_CHOICES23 = (
        ("西昌", "西昌"),
        ("重庆", "重庆"),
        ("西双版纳", "西双版纳"),
        )
        START_CHOICES24 = (
        ("杭州", "杭州"),
        )
        START_CHOICES25 = (
        ("杭州", "杭州"),
        )
        START_CHOICES26 = (
        ("杭州", "杭州"),
        ("朝阳", "朝阳"),
        )
        START_CHOICES27 = (
        ("烟台", "烟台"),
        ("南京", "南京"),
        )
        START_CHOICES28 = (
        ("烟台", "烟台"),
        )
        START_CHOICES29 = (
        ("成都", "成都"),
        )
        START_CHOICES30 = (
        ("大庆", "大庆"),
        )
        START_CHOICES31 = (
        ("延吉", "延吉"),
        ("泉州", "泉州"),
        ("秦皇岛", "秦皇岛"),
        ("衢州", "衢州"),
        )
        START_CHOICES32 = (
        ("重庆", "重庆"),
        )
        START_CHOICES33 = (
        ("大理", "大理"),
        )
        START_CHOICES34 = (
        ("郑州", "郑州"),
        )
        START_CHOICES35 = (
        ("郑州", "郑州"),
        )
        START_CHOICES36 = (
        ("哈密", "哈密"),
        )
        START_CHOICES37 = (
        ("北海", "北海"),
        )
        START_CHOICES38 = (
        ("沈阳", "沈阳"),
        )
        START_CHOICES39 = (
        ("张家界", "张家界"),
        )
        START_CHOICES40 = (
        ("台州", "台州"),
        ("大连", "大连"),
        )
        START_CHOICES41 = (
        ("哈尔滨", "哈尔滨"),
        )
        START_CHOICES42 = (
        ("哈尔滨", "哈尔滨"),
        )
        START_CHOICES43 = (
        ("泉州", "泉州"),
        )
        START_CHOICES44 = (
        ("大同", "大同"),
        )
        START_CHOICES45 = (
        ("西双版纳", "西双版纳"),
        ("陇南", "陇南"),
        ("西昌", "西昌"),
        )
        START_CHOICES46 = (
        ("鄂尔多斯", "鄂尔多斯"),
        )
        START_CHOICES47 = (
        ("广州", "广州"),
        )
        START_CHOICES48 = (
        ("吐鲁番", "吐鲁番"),
        )
        START_CHOICES49 = (
        ("济南", "济南"),
        )
        START_CHOICES50 = (
        ("济南", "济南"),
        )
        START_CHOICES51 = (
        ("舟山", "舟山"),
        )
        START_CHOICES52 = (
        ("大连", "大连"),
        )
        START_CHOICES53 = (
        ("湛江", "湛江"),
        ("日喀则", "日喀则"),
        )
        START_CHOICES54 = (
        ("乌鲁木齐", "乌鲁木齐"),
        )
        airline_id = models.IntegerField(default=0)
        starting_airport = models.CharField(max_length=100)
        destination_airport = models.CharField(max_length=100)
        #airlines = models.CharField(max_length=100, choices=AIRLINE_CHOICES)
        airlines = models.CharField(max_length=100)
        flight = models.CharField(max_length=100)
        aircraft_type = models.CharField(max_length=100, default='-')
        departure_time = models.TimeField()
        arrival_time = models.TimeField()
        punctuality_rate = models.CharField(max_length=100,default='-')
        price = models.CharField(max_length=10,default='-')

        def get_absolute_url(self):
        #return reverse("article_detail", args=(str(self.pk)))
        #return reverse('home')
                return reverse("arline_detail", kwargs={'pk': self.pk})
    
    
