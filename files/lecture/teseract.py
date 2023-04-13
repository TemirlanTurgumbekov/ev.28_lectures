# from PIL import Image
# import pytesseract
# import re


# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     print(string, type(string))
    
#     # list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    
#     # print(list_of_imei)
    
#     # with open('imei_codes.txt', 'w') as file:
#     #     file.writelines(f'{x}\n' for x in list_of_imei)   
# image = 'test.jpg'

# get_imei_code(image)

names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']

print(list(map(lambda name: name + ' Python' if len(name) > 5 else name + ' JavaScript', names)))