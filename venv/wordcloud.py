from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import  jieba                    #jieba分词

path_txt='C://Users/Administrator/Desktop/天猫评论.txt'
f = open(path_txt,'r',encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云
cut_text = " ".join(jieba.cut(f))

wordcloud = WordCloud(

   font_path="C:/Windows/Fonts/simfang.ttf",

   background_color="white",width=1000,height=880).generate(cut_text)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
