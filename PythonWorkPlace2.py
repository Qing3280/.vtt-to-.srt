import os

read_file = open("E:/C++2019/script/01.vtt","r",encoding='utf-8')
out_file = open("E:/C++2019/script/text.txt","w+",encoding='utf-8')

print ('文件名：{}'.format(read_file.name))
print ('文件名：{}'.format(out_file.name))

line_number = 1
add_list_number = 1

def add_list(n,m):
    if( n/3 == m ):
            out_file.write(str(m)+"\n")
            #print("{}".format(m))
            global add_list_number
            add_list_number+=1

for line in read_file.readlines():
    #print ('读取到的数据为：{}'.format(line))
    #print ('{}'.format(line))
    if(line_number==1)or(line_number==2):
        line_number+=1
        continue
    else:
        replace_note = line.replace(".",",")
        add_list(line_number,add_list_number)
        out_file.write(replace_note)
        line_number+=1
 
print("处理完成！")

read_file.close()
out_file.close()

#1 2 3 4 5
#3 6 9 12 15