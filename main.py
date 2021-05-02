# encoding:utf-8

import requests
import base64
from flask import Flask, request, render_template,session
import json
'''
身份证识别
'''
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.request_class.charset.encode("utf-8")
#封装百度API识别接口，返回识别内容
def discern(img_base64):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    params = {"id_card_side": "front", "image": img_base64}
    access_token = '24.f48c5731bc7b66c9c7c0ab17c6f91255.2592000.1621926281.282335-24061737'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    return response
#封装图片转base64
def from_img_to_base64(path):
    with open(path, "rb") as file_photo:  # 转为二进制格式
        ret = file_photo.read()
    base64_data = base64.b64encode(ret)  # 使用base64进行加密
    return base64_data

@app.route("/")
def main():
    return render_template('index.html')
#
@app.route('/api', methods=["POST"])
def form():
    #身份证正面
    host=request.host_url
    file = request.files["front"]
    path = "./static/"
    img_name = file.filename
    file_path = path + img_name
    file.save(file_path)
    front_card_path=host+file_path[1:]
    front_card = discern(from_img_to_base64(file_path))
    #身份证反面
    file = request.files["back"]
    img_name = file.filename
    file_path = path + img_name
    file.save(file_path)
    back_card_path = host+file_path[1:]
    back_card = discern(from_img_to_base64(file_path))
    # name:姓名  gender：性别   nation：民族  birth：出生日期  address：家庭地址  no：身份证号码  issue：签发机关  date：有效日期
    front_card=json.loads(front_card.text).get('words_result')
    back_card=json.loads(back_card.text).get('words_result')
    name=front_card.get('姓名').get('words')
    gender = front_card.get('性别').get('words')
    nation = front_card.get('民族').get('words')
    birth = front_card.get('出生').get('words')
    address = front_card.get('住址').get('words')
    no = front_card.get('公民身份号码').get('words')
    issue=back_card.get('签发机关').get('words')
    date=back_card.get('签发日期').get('words')+"-"+back_card.get('失效日期').get('words')

    return render_template('index.html',name=name,gender=gender,nation=nation,birth=birth,address=address,
                           no=no,issue=issue,date=date,back=back_card_path,front=front_card_path)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)