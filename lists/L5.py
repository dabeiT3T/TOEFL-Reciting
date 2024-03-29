#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = {
    'deposit': {
        'v.': ['沉淀', '堆积', '储蓄', '寄存'],
        'n.': ['沉淀物，堆积物', '存款']
    },
    'reunion': {
        'n.': ['团圆，重聚']
    },
    'lay': {
        'v.': ['产（卵）', '放置', '铺', '筹划，设置', '提出，提交']
    },
    'occupy': {
        'vt.': ['占用', '占据，占领', '使忙于（做某事）']
    },
    'envelop': {
        'vt.': ['包围']
    },
    'storage': {
        'n.': ['库房', '贮藏', '存储']
    },
    'proactive': {
        'a.': ['积极主动的', '先发制人的']
    },
    'fantasy': {
        'n.': ['想象，幻想']
    },
    'posit': {
        'vt.': ['安排', '假定']
    },
    'disguise': {
        'vt./n.': ['掩饰', '伪装，假装']
    },
    'psychology': {
        'n.': ['心理学', '心理，心理特征']
    },
    'embellish': {
        'vt.': ['装饰', '对...添枝加叶，渲染']
    },
    'weird': {
        'a.': ['怪异的，神秘的']
    },
    'diverge': {
        'vi.': ['（道路、线条等）分开，叉开', '（意见等）分歧', '分离']
    },
    'infuriate': {
        'vt.': ['激怒']
    },
    'spear': {
        'v.': ['刺，戳'],
        'n.': ['矛，枪', '嫩叶']
    },
    'repress': {
        'vt.': ['克制，抑制', '镇压，压制']
    },
    'conquer': {
        'vt.': ['战胜，征服', '克服']
    },
    'thrust': {
        'v.': ['挤', '插', '戳，刺'],
        'n.': ['戳，刺', '要旨', '驱动力']
    },
    'casualty': {
        'n.': ['伤亡事故', '伤亡（人员）']
    },
    'incidental': {
        'a.': ['偶然的', '附带发生的，伴随而来的']
    },
    'superb': {
        'a.': ['极好的，高质量的，上乘的', '华丽的']
    },
    'bestow': {
        'vt.': ['赠与，授予，献给']
    },
    'adventitious': {
        'a.': ['偶然的，偶发的']
    },
    'dissipate': {
        'v.': ['（使）消散，（使）消失', '挥霍，浪费（时间、金钱等）']
    },
    'resolute': {
        'a.': ['坚决的，果断的']
    },
    'cranial': {
        'a.': ['头盖骨的，颅骨的']
    },
    'lineage': {
        'n.': ['宗系，世系，血统']
    },
    'balk': {
        'n.': ['障碍'],
        'v.': ['畏缩', '阻止', '妨碍']
    },
    'irritate': {
        'vt.': ['激怒，使烦躁', '刺激']
    },
    'consolidate': {
        'v.': ['巩固', '（使）合并']
    },
    'intervening': {
        'a.': ['介于中间的，发生于其间的']
    },
    'corrosion': {
        'n.': ['腐蚀（状态），侵蚀']
    },
    'mental': {
        'a.': ['精神的', '智力的', '精神健康的']
    },
    'plump': {
        'a.': ['微胖的', '丰满的']
    },
    'readily': {
        'ad.': ['欣然地', '容易地']
    },
    'cooperative': {
        'a.': ['合作的，协作的', '配合的'],
        'n.': ['合作企业']
    },
    'pave': {
        'v.': ['铺', '密布']
    },
    'contamination': {
        'n.': ['污染', '玷污']
    },
    'shrink': {
        'v.': ['（使）收缩，缩小', '退缩，畏缩']
    },
    'pretentious': {
        'a.': ['自负的']
    },
    'laser': {
        'n.': ['激光', '激光器']
    },
    'identify': {
        'v.': ['识别', '鉴定', '找到，发现']
    },
    'barter': {
        'n./v.': ['实物交易，以物易物']
    },
    'cue': {
        'n.': ['暗示，提示']
    },
    'tenant': {
        'n.': ['房客，承租人'],
        'vt.': ['（作为租赁者）居住']
    },
    'medal': {
        'n.': ['奖牌，奖章']
    },
    'inscribe': {
        'v.': ['（在某物上）写、题、铭刻', '铭记']
    },
    'flake': {
        'v.': ['使成薄片', '雪片般落下'],
        'n.': ['薄片']
    },
    'concert': {
        'n.': ['音乐会，演奏会', '一致']
    },
    'supreme': {
        'a.': ['至高无上的']
    },
    'encounter': {
        'vt./v.': ['偶然碰到', '遭遇']
    },
    'lease': {
        'n.': ['租约', '租期'],
        'vt.': ['出租']
    },
    'downward': {
        'ad.': ['向下，往下'],
        'a.': ['向下的']
    },
    'courteous': {
        'a.': ['谦恭的，有礼貌的']
    },
    'evolve': {
        'v.': ['发展', '（使）进化']
    },
    'jeopardize': {
        'vt.': ['破坏，危及']
    },
    'detergent': {
        'n.': ['清洁剂'],
        'a.': ['净化的，清洁的']
    },
    'parking': {
        'n.': ['机动车停放', '停车场']
    },
    'imprint': {
        'vt.': ['使铭记，使牢记', '压印'],
        'n.': ['印记，印痕', '持久的影响']
    },
    'degree': {
        'n.': ['程度', '度数', '学位', '等级']
    },
    'bulk': {
        'n.': ['容积，体积', '主体，大部分']
    },
    'spontaneity': {
        'n.': ['自发性', '自发行为']
    },
    'mast': {
        'n.': ['船桅', '旗杆', '天线塔']
    },
    'inanimate': {
        'a.': ['无生命的', '无生气的']
    },
    'exhale': {
        'v.': ['呼出（气）', '散发']
    },
    'comply': {
        'vi.': ['服从', '遵守']
    },
    'plantation': {
        'n.': ['种植园', '人造林']
    },
    'request': {
        'n./vt.': ['要求，请求']
    },
    'penetrate': {
        'v.': ['刺穿', '渗透，洞察']
    },
    'diversion': {
        'n.': ['消遣，娱乐', '转移，转换']
    },
    'endure': {
        'vt.': ['忍受，忍耐', '持久，持续']
    },
    'reserve': {
        'n.': ['储备（物）', '自然保护区', '谨慎', '替补队员', '后备部队'],
        'vt.': ['保留', '预定']
    },
    'overload': {
        'vt.': ['使超载，使过载', '使（电路等）超负荷', '给...增加负担'],
        'n.': ['超载（量）', '超负荷']
    },
    'region': {
        'n.': ['（大气等的）层', '地区，区域', '范围']
    },
    'absurd': {
        'a.': ['可笑的，荒唐的']
    },
    'exemplary': {
        'a.': ['模范的', '典型的']
    },
    'leftover': {
        'n.': ['残留物', '吃剩下的食物'],
        'a.': ['剩余的']
    },
    'conservationist': {
        'n.': ['自然环境保护论者']
    },
    'suspect': {
        'v.': ['怀疑，猜想'],
        'a.': ['可疑的', '不信任的'],
        'n.': ['嫌疑犯，可疑分子']
    },
    'adhesive': {
        'n.': ['胶合剂'],
        'a.': ['带黏性的']
    },
    'gravitational': {
        'a.': ['重力的，万有引力的']
    },
    'hydrogen': {
        'n.': ['氢']
    },
    'celebrate': {
        'v.': ['赞美', '庆祝']
    }
}
