def MostCommonWord(a):
    from collections import Counter
    from konlpy.tag import Kkma
    import matplotlib.pyplot as pyplot
    import matplotlib
    from matplotlib import font_manager, rc

    font_name = font_manager.FontProperties(fname='c:/windows/fonts/KoPubWorld Dotum_Pro Medium.otf').get_name()
    matplotlib.rc('font',family=font_name)

    kkma = Kkma()
    results = []

    file = open('bloglist.txt','r',encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        results.append(line)
    file.close()

    sentences_tag = []
    for sentence in results:
        morph = kkma.pos(sentence)
        sentences_tag.append(morph)

    noun_adj_list = []
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['NNG', 'NP','VV', 'MAG']:
                noun_adj_list.append(word)

    #print(noun_adj_list)
    counts = Counter(noun_adj_list)
    return print(counts.most_common(a))
    # counts = dict(counts)
    # pyplot.xticks(range(len(counts)),counts)
    # pyplot.bar(range(len(counts.values())),counts.values,align='center')
    # pyplot.xlabel('주요단어')
    # pyplot.ylabel('출현빈도')
    # pyplot.title('주요 단어 별 출현 빈도 분석')
    # pyplot.show()

#MostCommonWord(10)

#
# #! /usr/bin/python2.7
# # -*- coding: utf-8 -*-
#
# from time import time
#
# from konlpy import tag
# from konlpy.corpus import kolaw
# from konlpy.utils import csvwrite
# from konlpy.utils import pprint
#
#
# def tagging(tagger, text):
#     r = []
#     try:
#         r = getattr(tag, tagger)().pos(text)
#     except Exception as e:
#         print("Uhoh,", e)
#     return r
#
#
# def measure_time(taggers, mult=6):
#     doc = kolaw.open('bloglist.txt').read()*6
#     data = [['n'] + taggers]
#     for i in range(mult):
#         doclen = 10**i
#         times = [time()]
#         diffs = [doclen]
#         for tagger in taggers:
#             r = tagging(tagger, doc[:doclen])
#             times.append(time())
#             diffs.append(times[-1] - times[-2])
#             print('%s\t%s\t%s' % (tagger[:5], doclen, diffs[-1]))
#             pprint(r[:5])
#         data.append(diffs)
#         print
#     return data
#
#
# def measure_accuracy(taggers, text):
#     print('\n%s' % text)
#     result = []
#     for tagger in taggers:
#         print(tagger)
#         r = tagging(tagger, text)
#         pprint(r)
#         result.append([tagger] + map(lambda s: ' / '.join(s), r))
#     return result
#
#
# def plot(result):
#
#     from matplotlib import pylab as pl
#     import scipy as sp
#
#     if not result:
#         result = sp.loadtxt('morph.csv', delimiter=',', skiprows=1).T
#
#     x, y = result[0], result[1:]
#
#     for i in y:
#         pl.plot(x, i)
#
#     pl.xlabel('Number of characters')
#     pl.ylabel('Time (sec)')
#     pl.xscale('log')
#     pl.grid(True)
#     pl.savefig("images/time.png")
#     pl.show()
#
#
# if __name__=='__main__':
#
#     PLOT = False
#     MULT = 6
#
#     examples = [u'아버지가방에들어가신다',  # 띄어쓰기
#             u'나는 밥을 먹는다', u'하늘을 나는 자동차', # 중의성 해소
#             u'아이폰 기다리다 지쳐 애플공홈에서 언락폰질러버렸다 6+ 128기가실버ㅋ'] # 속어
#
#     taggers = [t for t in dir(tag) if t[0].isupper()]
#
#     # Time
#     data = measure_time(taggers, mult=MULT)
#     with open('morph.csv', 'w') as f:
#         csvwrite(data, f)
#
#     # Accuracy
#     for i, example in enumerate(examples):
#         result = measure_accuracy(taggers, example)
#         result = map(lambda *row: [i or '' for i in row], *result)
#         with open('morph-%s.csv' % i, 'w') as f:
#             csvwrite(result, f)
#
#     # Plot
#     if PLOT:
#         plot(result)


