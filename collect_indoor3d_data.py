import os
import sys
# 这里是拿到这个basedir 的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 他在这里改变了系统参数 sys.path （不建议学习，这是不好的操作）
sys.path.append(BASE_DIR)
# 这里他把自己写的indoor3d_util.py 这个module import 进来就可以使用里面的object了。 
import indoor3d_util

# 他先join了BASE_DIR, 'meta/anno_paths.txt'，然后去掉右边的空格。
anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/anno_paths.txt'))]
# 然后这里他用到了indoor3d_util.py 里面定义的DATA_PATH这个object，然后和anno_paths 里面的每一个join在一起了。 
anno_paths = [os.path.join(indoor3d_util.DATA_PATH, p) for p in anno_paths]

# 这里还是为了设置输出文件的path。 
output_folder = os.path.join(BASE_DIR, 'data/stanford_indoor3d_ins.sem') 
# 如果上述output_folder dir 不存在的话，就直接mkdir。 
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
for anno_path in anno_paths:
    print(anno_path)
    try:
        # 这里就是为了用“/”split开anno_path（就是anno_paths里面的每一个，这里的命名真的是很不好。 
        elements = anno_path.split('/')
        # 产生output file的名字。 
        out_filename = elements[-3]+'_'+elements[-2]+'.npy' # Area_1_hallway_1.npy
        # 这里又调用了indoor3d_util.py 里面的collect_point_label 函数。 （具体这个函数是做什么的我还没有看）
        indoor3d_util.collect_point_label(anno_path, os.path.join(output_folder, out_filename), 'numpy')
    except:
        # 如果上述过程failed，就只是print下面这个（这个操作也是很不好的，因为这样不会返回错误的原因）
        # 看这个 改写他的except https://codeday.me/bug/20171004/80750.html
        # 或者是 这个 https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e-in-python
        print(anno_path, 'ERROR!!')
# 我暂时看了这么多，抽时间我再看看，你看还有什么问题。 
