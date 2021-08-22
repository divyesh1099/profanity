import os, io
from google.cloud import vision
from PIL import Image,ImageFilter
from profanity_text.models import Cusslist

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'booming-coast-313509-bb494bed1251.json'
client=vision.ImageAnnotatorClient()

def check_for_special_character(a_word):
    for j in a_word:
        if j.isalpha()==False:
            return True


def check_if_actually_a_cussword(a_word,cuss_words_list):
    thatword=""
    for k in a_word:
        if k.isalpha()==True:
                thatword+=k
    if thatword in a_word and thatword in cuss_words_list:
        return True
    else:
        return False



def check_special_character(a_string, cuss_words_list):
    cuss_words_in_image = []
    list_of_words_from_string = a_string.split()
    for a_word in list_of_words_from_string:
        if a_word.lower() in cuss_words_list:
            cuss_words_in_image.append(list_of_words_from_string[list_of_words_from_string.index(a_word)])


        else:
            if check_for_special_character(a_word.lower())==True:
                if check_if_actually_a_cussword(a_word.lower(),cuss_words_list)==True:
                    cuss_words_in_image.append(list_of_words_from_string[list_of_words_from_string.index(a_word)])

    return cuss_words_in_image


def googleVision(fn):
    result_image_path = 'media/demoImages/'
    with io.open (os.path.join('media/demoImages/'+fn),'rb') as image_file:
        content=image_file.read()

    image=vision.Image(content=content)
    response=client.text_detection(image=image)   
    texts=response.text_annotations
    a = texts[0].description
    la=a.split()
    cuss_words_list=tuple(Cusslist.objects.all().values_list('cussword', flat=True))

    cuss_words_in_image = check_special_character(a, cuss_words_list)
    ogimage=Image.open('media/demoImages/'+fn)
    li = []
    for a_cuss_word in cuss_words_in_image:
        for i in range(len(la)):
            if la[i] == a_cuss_word:
                c = i
                a1=texts[c+1].bounding_poly.vertices[0].x
                a2=texts[c+1].bounding_poly.vertices[0].y
                b1=texts[c+1].bounding_poly.vertices[2].x
                b2=texts[c+1].bounding_poly.vertices[2].y

                cropped_image=ogimage.crop((a1,a2,b1,b2))
                blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))
                ogimage.paste(blurred_image,(a1,a2,b1,b2))
                ogimage.save(result_image_path+'im {}.jpeg'.format(i))
                ogimage.save()
                li.append(result_image_path+'im {}.jpeg'.format(i))
                ogimage = Image.open(result_image_path+'im {}.jpeg'.format(i))

    for j in range(len(li)-1):
        os.remove(li[j])
    return li[-1] if len(li)>0 else result_image_path + str(fn)