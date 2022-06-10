import paddlehub as hub

senta = hub.Module(name="senta_gru")
print(senta.summary)

test_text = [
    "生态环境部、央行等九部门开启气候投融资试点 鼓励金融机构开展碳金融服务",
    "2021绿色金融发展怎样？2022发展态势如何？",
    "候投融资试点开启，引导促进更多资金投向这一领域" ,
    "金融如何精准支撑工业绿色发展，对两高项目设啥门槛，看这里！" ,
    "环保展原来可以“更环保”——中国国际环保展绿色搭建，使用绿色板材，循环再造等成为展会趋势",
    "女首善”激进拿下PPP项目，资金危机爆发四处找钱",
    "绍兴：抓服务促生产，累计指导帮扶复工复产企业647家"
]

input_dict = {"text": test_text}
results = senta.sentiment_classify(data=input_dict)

for result in results:
    print(result['text'])
    print(result['sentiment_label'])
    print(result['sentiment_key'])
    print(result['positive_probs'])
    print(result['negative_probs'])

