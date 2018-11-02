import re
import linecache
import os,cv2
from math import *
import numpy as np
import getopt
import sys
import argparse
def show_annotations(rootdir):
    imagesdir=rootdir+'face_data/fddb/images'
    origimagedir=rootdir+"/face_data/fddb/originalPics"
    annotationdir=rootdir+"/face_data/fddb/FDDB-folds"
    labelsdir=rootdir+"/mAP/ground_truth_labels"
    convert2rects=True
    file_txt = open(rootdir +"/face_data/fddb/"+'fddb_all_data.txt','w')
    for i in range(10):
        annotationfilepath=annotationdir+"/FDDB-fold-%0*d-ellipseList.txt"%(2,i+1)
	print(annotationfilepath)
        annotationfile=open(annotationfilepath)
        while(True):
            filename=annotationfile.readline()[:-1]+".jpg"
            if not filename:
                break
            line=annotationfile.readline()
            if not line:
                break
            #print filename
            facenum=(int)(line)
	    #print facenum
            img=cv2.imread(origimagedir+"/"+filename)
            filename=filename.replace('/','_')
            cv2.imwrite(imagesdir+"/"+filename,img)
            w = img.shape[1]
            h = img.shape[0]
	    #print w,h 
	    labelpath=labelsdir+"/"+filename.replace('/','_')[:-3]+"txt"
	    txt_path= rootdir+'face_data/fddb/'+'ground_truth_labels/'+filename.replace('/','_')[:-3]+"txt"
	    print filename
	    print txt_path
	    #print labelpath
	    file_txt.write(rootdir+'/face_data/fddb/images/'+filename+' '+txt_path+'\n')
            labelfile=open(labelpath,'w')   
            for j in range(facenum):
                line=annotationfile.readline().strip().split()
                major_axis_radius=(float)(line[0])
                minor_axis_radius=(float)(line[1])
                angle=(float)(line[2])
                center_x=(float)(line[3])
                center_y=(float)(line[4])
                score=(float)(line[5])
                angle = angle / 3.1415926*180
                cv2.ellipse(img, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 0, 0)) 
                if convert2rects:
                    mask=np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8)
                    cv2.ellipse(mask, ((int)(center_x), (int)(center_y)), ((int)(major_axis_radius), (int)(minor_axis_radius)), angle, 0., 360.,(255, 255, 255))
                    contours=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
		    for k in range(len(contours)-2):
                        r=cv2.boundingRect(contours[k])
                        x_min=r[0]
                        y_min=r[1]
                        x_max=r[0]+r[2]
                        y_max=r[1]+r[3]
                        xcenter=r[0]+r[2]/2
                        ycenter=r[1]+r[3]/2
                        labelline="1"+"\t"+str(x_min) + '\t' + str(y_min) + '\t' + str(x_max) + '\t' + str(y_max)    + '\n'
                        print labelline
			labelfile.write(labelline)
                        cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,0,255))
            cv2.waitKey(1)
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rootdir",help="path of rootdir")
    return parser.parse_args()

def main(args):
    show_annotations(args.rootdir)

if __name__=="__main__":
    main(parse_args()) 
