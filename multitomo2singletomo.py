import starfile
def read_starfile(file):
    df = starfile.open(file)
    return df
def classification(data,tomo):
    df=data
    v_want = df.loc[df['rlnMicrographName'] == tomo]
    return v_want
def write_starfile(df,tomo):
    starfile.new(df, tomo+'.star')
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='把warp产生的star文件根据tomo分开，为了做map back' ,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input', help='输入你的run_it025_data.star')
    parser.add_argument('-t', '--tomo', help='想提取哪套tomo')
    parser.add_argument('-v', '--version', action='version', version='v. 1.0')
    parser.add_argument('-o', '--output', help='起个名')
    args = parser.parse_args()
    data=read_starfile(args.input)
    for_write=classification(data,args.tomo)
    write_starfile(for_write,args.output)