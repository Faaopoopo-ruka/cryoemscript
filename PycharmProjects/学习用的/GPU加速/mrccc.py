#Author：Alex.Zhang
import mrcfile
from PIL import Image
import numpy as np

# aa=mrcfile.validate('postprocess_masked.mrc')
# print(aa)
# example_data = np.arange( 12 , dtype=np.int8 ).reshape( 3 , 4 )
with mrcfile.open('emd_10156.mrc') as mrc:
    mrc.print_header()
    with open('mes.txt','w') as f:
        aa=str(mrc.data)
        f.write(aa)
        print(mrcfile.validate('postprocess_masked.mrc'))
        ss=mrc.header
        f.write(str(ss))
        print(mrc.is_volume)
    print(mrc.header.dmax)

# im=Image.open('aaa.png')
# na=np.array(im)
# print(na.shape)
# print(na)
