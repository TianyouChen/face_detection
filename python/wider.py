import re
import linecache
import os
import sys
import argparse

class Wider:
    def __init__(self,FileDir,OutDir):
        file = open(FileDir+'wider_face_all_bbx_gt.txt','rb')
        lines = count_line(file)
        file_txt = open(OutDir+'wider_all_data.txt','w')
        for a in range(lines):
            line = linecache.getline(FileDir+'wider_face_all_bbx_gt.txt',a)
            if re.search('jpg',line):
                position = line.index('/')
                file_name = line[position + 1: -5]
                folder_name =   line[:position]
    
                wider_path_txt = FileDir+'wider_all/' + file_name +'.jpg'
                wider_facebox_txt = OutDir+'wider_all_box/' +file_name +'.txt'
                file_txt.write(wider_path_txt + ' '+wider_facebox_txt +'\n')
                a += 1 
                face_count = int(linecache.getline(FileDir+'wider_face_all_bbx_gt.txt',a))
                for b in range(face_count):
                    cls =1
                    box_line = linecache.getline(FileDir+'wider_face_all_bbx_gt.txt',a+b+1)
                    po_x1 = box_line.index(' ')
                    x1 = box_line[:po_x1]
                    po_y1 =box_line.index(' ',po_x1 + 1)
                    y1 = box_line[po_x1:po_y1]
                    po_w = box_line.index(' ',po_y1 +1)
                    w = box_line[po_y1:po_w]
                    print("y1:", y1)
                    x2 = int(x1.strip()) + int(w.strip())
                    po_h = box_line.index(' ',po_w + 1)
                    h = box_line[po_w:po_h]
                    y2 = int(y1.strip()) + int(h.strip())
                    coordinates = str(cls)+' ' + x1 + y1 +' '+str(x2) +' '+ str(y2)
        
                    if not(os.path.exists(OutDir + 'wider_all_box/')):
                        os.makedirs(OutDir + 'wider_all_box/')
                    with open(OutDir +'wider_all_box/' + '/' +file_name + ".txt", 'a') as f1:
                        f1.write(coordinates + "\n")
                a += a + b + 1




def count_line(file):
    lines_quantity = 0
    while True:
	buffer = file.read(1024 * 8192)
        if not buffer:
            break
        lines_quantity += buffer.count('\n')
    file.close()
    return lines_quantity

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--FileDir",help="You should give FileDir")
    parser.add_argument("--OutDir",help="You should give OutDir")
    return parser.parse_args()

def main(args):
    Wider(args.FileDir,args.OutDir)



if __name__ == "__main__":
    main(parse_args())
