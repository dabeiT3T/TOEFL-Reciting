#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = {
    'obsess': {
        'v.': ['迷住', '牵挂']
    },
    'atomic': {
        'a.': ['原子的', '原子能的']
    },
    'senior': {
        'a.': ['地位较高的', '较年长的'],
        'n.': ['较年长者', '四年级学生']
    },
    'finalize': {
        'vt.': ['使完成', '把...最后定下来', '定稿']
    },
    'utter': {
        'vt.': ['出声', '说'],
        'a.': ['完全的']
    },
    'outrageously': {
        'ad.': ['令人不能容忍地', '肆无忌惮地']
    },
    'mammal': {
        'n.': ['哺乳动物']
    },
    'bare': {
        'a.': ['赤裸的', '光秃的，无遮盖的', '最基本的'],
        'vt.': ['脱掉（衣服）', '显露']
    },
    'sticky': {
        'a.': ['黏的，黏性的', '（天气）闷热的', '棘手的']
    },
    'personnel': {
        'n.': ['全体人员，员工']
    },
    'inclination': {
        'n.': ['爱好，意愿', '趋向，趋势', '倾斜度']
    },
    'particle': {
        'n.': ['微粒，颗粒', '【语】小品词']
    },
    'notify': {
        'vt.': ['通报']
    },
    'survey': {
        'n.': ['调查', '概述'],
        'v.': ['调查', '概述']
    },
    'abortive': {
        'a.': ['落空的，失败的']
    },
    'catholic': {
        'a.': ['广泛的，包罗万象的', '天主教的'],
        'n.': ['天主教']
    },
    'offset': {
        'n.': ['分支', '补偿', '抵消'],
        'vt.': ['补偿', '抵消']
    },
    'stable': {
        'a.': ['稳定的，安定的', '牢固的', '沉稳的'],
        'n.': ['马厩']
    },
    'ambiguity': {
        'n.': ['模凌两可的话', '歧义（现象）']
    },
    'retrospective': {
        'a.': ['回顾的，追想的', '有追溯效力的']
    },
    'overt': {
        'a.': ['公开的，非秘密的']
    },
    'contributory': {
        'a.': ['贡献的', '捐助的', '促进的']
    },
    'strenuous': {
        'a.': ['费劲的，费力的，艰苦的', '精力充沛的', '奋力的']
    },
    'puff': {
        'v.': ['喘气，喘息', '（使）喷出（烟等）'],
        'n.': ['吸', '（烟等的）一缕', '喘息']
    },
    'instill': {
        'vt.': ['慢慢灌输', '逐渐培养']
    },
    'depress': {
        'vt.': ['降低，削弱', '使沮丧', '使萧条']
    },
    'avenge': {
        'vt.': ['复仇，报仇', '向...报仇']
    },
    'meditate': {
        'v.': ['沉思，冥想', '考虑', '谋划']
    },
    'ensure': {
        'vt.': ['确保，担保，保证']
    },
    'gush': {
        'v.': ['滔滔不绝地说（话）', '喷涌'],
        'n.': ['喷出，涌出', '迸发，发作']
    },
    'predispose': {
        'v.': ['事先（在某方面）影响某人', '（使）易受感染（或患病）']
    },
    'languish': {
        'vi.': ['憔悴', '凋谢，枯萎', '受煎熬']
    },
    'ravage': {
        'vt.': ['毁坏', '（尤指军队等）抢劫，掠夺']
    },
    'exodus': {
        'n.': ['大批离去，成群外出']
    },
    'compound': {
        'n.': ['化合物，复合物'],
        'a.': ['化合的，复合的'],
        'vt.': ['使恶化，使加重', '混合']
    },
    'subject': {
        'n.': ['主体', '对象'],
        'a.': ['受...支配的'],
        'vt.': ['使服从']
    },
    'couple': {
        'n.': ['（一）对，（一）双', '夫妇，情侣', '几个人，几件事'],
        'vt.': ['连接，结合']
    },
    'downtown': {
        'a.': ['市中心'],
        'ad.': ['在市中心', '往市中心']
    },
    'backlighting': {
        'n.': ['逆光']
    },
    'mild': {
        'a.': ['轻微的', '温和的', '随和的']
    },
    'consistency': {
        'n.': ['浓度，密度', '一致性，协调', '连接，结合']
    },
    'exalt': {
        'vt.': ['高度赞扬，褒扬', '提升，提拔']
    },
    'soluble': {
        'a.': ['可容的', '可解决的']
    },
    'academy': {
        'n.': ['学会，研究院', '专科院校']
    },
    'prodigious': {
        'a.': ['巨大的']
    },
    'brief': {
        'a.': ['简短的，短暂的', '简洁的'],
        'vt.': ['向...介绍基本情况'],
        'n.': ['指示', '摘要']
    },
    'optimistic': {
        'a.': ['乐观的']
    },
    'marked': {
        'a.': ['显著的', '有记号的', '被监视的']
    },
    'typify': {
        'vt.': ['是...的典范', '成为...的特征']
    },
    'imitation': {
        'n.': ['模仿，仿效', '仿制', '仿造品']
    },
    'gallery': {
        'n.': ['画廊，美术馆']
    },
    'compile': {
        'vt.': ['汇编', '编辑，编纂']
    },
    'propel': {
        'vt.': ['推进，驱使', '激励']
    },
    'hoe': {
        'vt.': ['用锄头锄'],
        'n.': ['锄头']
    },
    'stride': {
        'n.': ['大步', '步法', '进展'],
        'vi.': ['大步走']
    },
    'fade': {
        'v.': ['褪色', '凋谢', '逐渐消失']
    },
    'tunnel': {
        'n.': ['隧道', '地道'],
        'v.': ['开凿隧道', '挖地道']
    },
    'highlight': {
        'vt.': ['强调，突出', '以强烈光线照射'],
        'n.': ['最精彩部分']
    },
    'friction': {
        'n.': ['摩擦', '摩擦力', '矛盾，冲突']
    },
    'calm': {
        'a.': ['（天气、海洋等）平静的', '镇静的，沉着的'],
        'vt.': ['使平静，使镇定，平息']
    },
    'wrinkle': {
        'n.': ['皱纹'],
        'v.': ['（使）起皱纹']
    },
    'cube': {
        'n.': ['立方体', '立方形的东西（尤指食物）', '立方']
    },
    'plank': {
        'n.': ['木板', '政策要点，政纲的核心']
    },
    'transfer': {
        'v.': ['转移', '转学', '转让', '换乘'],
        'n.': ['转移', '转学', '转让', '换乘']
    },
    'situated': {
        'a.': ['坐落在...的', '处于...境地的']
    },
    'eclecticism': {
        'n.': ['折中主义']
    },
    'piracy': {
        'n.': ['海盗行为', '抢劫行为', '剽窃行为']
    },
    'deception': {
        'n.': ['骗局', '诡计', '欺骗，欺诈']
    },
    'blanket': {
        'n.': ['毯子', '覆盖物']
    },
    'subtle': {
        'a.': ['微细的，微妙的', '精巧的，巧妙的', '狡猾的', '敏锐的']
    },
    'dissenter': {
        'n.': ['不同意者，反对者']
    },
    'habit': {
        'n.': ['习惯', '习性，脾性']
    },
    'dictate': {
        'v.': ['规定', '决定', '口述', '支配'],
        'n.': ['命令，规定']
    },
    'subway': {
        'n.': ['地铁']
    },
    'aroma': {
        'n.': ['芳香，香味', '气氛，氛围']
    },
    'niche': {
        'n.': ['生态位', '壁龛']
    },
    'rush': {
        'v.': ['（使）冲，（使）突进', '奔，急速流动', '（使）仓促从事', '突袭'],
        'n.': ['冲，急速行进', '匆忙', '（交通等的）繁忙'],
        'a.': ['（交通）繁忙的']
    },
    'embody': {
        'vt.': ['表达，体现', '含有']
    },
    'inviting': {
        'a.': ['动人的，诱人的', '引人注目的']
    },
    'elective': {
        'a.': ['选举的', '可选择的', '选修的']
    },
    'benefit': {
        'n.': ['益处，好处', '恩惠', '津贴'],
        'v.': ['（使）受益', '得益于']
    }
}
