import matplotlib.pyplot as plt

def show1plt(img,n=""):
    plt.figure(figsize=(2,2));
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    
def show2plt(img,img2,n1="",n2=""):
    plt.figure(figsize=(4,2));
    plt.subplot(121)
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(122)
    plt.imshow(img2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);

def show3plt(img,img2,img3,n1="",n2="",n3=""):
    plt.figure(figsize=(6,2));
    plt.subplot(131)
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(132)
    plt.imshow(img2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(133)
    plt.imshow(img3)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    
def show4plt(img,img2,img3,img4,n1="",n2="",n3="",n4=""):
    plt.figure(figsize=(8,2));
    plt.subplot(141)
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(142)
    plt.imshow(img2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(143)
    plt.imshow(img3)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(144)
    plt.imshow(img4)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    
def show5plt(img,img2,img3,img4,img5,n1="",n2="",n3="",n4="",n5=""):
    plt.figure(figsize=(10,2));
    plt.subplot(151)
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(152)
    plt.imshow(img2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(153)
    plt.imshow(img3)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(154)
    plt.imshow(img4)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(155)
    plt.imshow(img5)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    
def show6plt(img,img2,img3,img4,img5,img6,n1="",n2="",n3="",n4="",n5="",n6=""):
    plt.figure(figsize=(12,2));
    plt.subplot(161)
    plt.imshow(img)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(162)
    plt.imshow(img2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(163)
    plt.imshow(img3)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(164)
    plt.imshow(img4)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(165)
    plt.imshow(img5)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    plt.subplot(166)
    plt.imshow(img6)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n6);