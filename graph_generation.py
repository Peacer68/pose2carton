from PIL import Image
import os
file_name = 'obj_seq_5_fbxCartoonMan014_3dmodel/CartoonMan014_intermediate.mtl'
dir = file_name.split('/')[0]
f = open(file_name,'r')
contents = f.readlines(0)
f.close()
# 重建原文件
os.remove(file_name)
f = open(file_name,'w')

# 生成纯色图片并保存
cnt = 0
for i in contents:
    i = i.strip('\n')
    if i[0:2] == 'Kd':
        png_dir = dir+'/'+str(cnt)+'.png'
        content = i.split(' ')
        color = [int(255*float(j)) for j in content[1:4]]
        color = tuple(color)
        img = Image.new('RGBA', (1024,1024),color)
        img.save(png_dir)
        cnt += 1

# 改写mtl文件
cnt = 0
for i in contents:
    f.write(i)
    if i[0] == 'N':
        f.write('map_Kd {}.png\n'.format(cnt))
        # print(cnt)
        cnt += 1
f.close()