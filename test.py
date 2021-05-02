

front_data="{'words_result': {'姓名': {'words': '管小康', 'location': {'top': 637, 'left': 908, 'width': 309, 'height': 121}}, '民族': {'words': '汉', 'location': {'top': 851, 'left': 1364, 'width': 86, 'height': 95}}, '住址': {'words': '广东省大埔县高陂镇北坑村坝仔下', 'location': {'top': 1217, 'left': 879, 'width': 943, 'height': 229}}, '公民身份号码': {'words': '441422198908293413', 'location': {'top': 1683, 'left': 1278, 'width': 1227, 'height': 108}}, '出生': {'words': '19890829', 'location': {'top': 1020, 'left': 886, 'width': 765, 'height': 98}}, '性别': {'words': '男', 'location': {'top': 844, 'left': 895, 'width': 86, 'height': 98}}}, 'log_id': 1388497679239086080, 'words_result_num': 6, 'idcard_number_type': 1, 'image_status': 'normal'}"
import  json
res=json.load(front_data)
print(res)
print(type(res))
print(res['words_result'])