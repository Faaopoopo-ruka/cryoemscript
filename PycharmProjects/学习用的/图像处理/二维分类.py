#Author：Alex.Zhang
'''
1.图片统一大小
2.图片对齐
3.K-MENAS聚类分析
4.显示图像
'''
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=128,height=128):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("E:\\img\\*.jpg"):
    convertjpg(jpgfile,"E:\\lianhua")
