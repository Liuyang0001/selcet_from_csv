import re
import os
import pandas as pd


def selcet(rule, read_path, write_path):
    '''
    rule: 匹配规则(正则)
    read_path: 输入文件路径
    write_path: 输出文件路径
    '''
    with open(read_path, encoding="gbk") as file:
        data = pd.read_csv(file)
        cnt = 0
        for i in range(len(data)):
            # 取到15位准考证号
            number = data.iloc[[i], 0].to_string()[-15:]
            if re.match(rule, number):
                cnt += 1  # 计数
                df = data.iloc[[i], :]
                # 打印到控制台
                # print(df)
                # 输出到csv文件,index要设置为False,否则会多一列索引值
                df.to_csv(write_path, mode="a", index=False,
                          header=None, encoding="gbk")
        print("一共找到了{}个数据".format(cnt))


if __name__ == "__main__":
    # 【计算机专硕】匹配规则
    pat1 = "^10033[0-9]{4}16[123]0[0-9]{2}$"
    # 输入,输出文件目录
    read_path = os.getcwd() + r'\data\indata.csv'
    write_path = os.getcwd() + r'\data\outdata.csv'
    # 根据需要改三个参数
    selcet(pat1, read_path, write_path)
