from __future__ import unicode_literals
from flask import (
    Flask,
    request,
    abort, 
    send_from_directory
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, LocationMessage,
    ImageMessage, QuickReply, QuickReplyButton, 
    LocationAction, TextSendMessage, MessageAction,
    ImageSendMessage
)
from flexmessage import (
    term_of_use,
    personal_information,
    plantation_location,
    carousel_message,
    select_menu_flex,
    how_to_send_image,
    show_infomation_flex,
    image_location_flex,
    request_location
)
from werkzeug.middleware.proxy_fix import ProxyFix
from pathlib import Path
import cv2
import torch
from dotenv import load_dotenv
import os, sys, warnings, errno, tempfile
from google.cloud import dialogflow_v2
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import mysql.connector
from datetime import datetime
from utils.plots import Annotator, colors



current = datetime.now()
date = str(current.strftime('%Y-%m-%d'))
time = str(current.strftime('%H:%M:%S'))
datetime =  date + " " + time
warnings.filterwarnings('ignore')

path_to_upload_file = '/Users/waterondaway/Desktop/chatbotv2/static/img_from_user'
SERVICE_ACCOUNT_FILE = '/Users/waterondaway/chatbot/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

image_location_request = {
    # UserID : Google Drive
}

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

# reads the key-value pair from .env file and adds them to environment variable.
load_dotenv()

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('CHANNEL_SECRET', None)
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None or channel_access_token is None:
    print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# Set up Dialogflow client
credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'chatbot-credentials.json'
dialogflow_session_client = dialogflow_v2.SessionsClient(credentials=credentials)

# Dialogflow credentials
dialogflow_session_client = dialogflow_v2.SessionsClient()
PROJECT_ID = "chatbot-ufqy"

### YOLOv5 ###
# Setup
# weights, view_img, save_txt, imgsz = 'yolov5s.pt', False, False, 640
conf_thres = 0.25
iou_thres = 0.45
classes = None
agnostic_nms = False
save_conf = False
save_img = True
line_thickness = 3

# Directories
save_dir = 'static/tmp/'

# Load model
model = torch.hub.load('./', 'custom', path='best.pt', source='local', force_reload=True)

# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise

# Detect Intent Dialogflow
def detect_intent_from_text(text, session_id, language_code="th"):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow_v2.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow_v2.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

# MYSQL Tools --------------
def insert_db(table_name,columns,values):
    database = active_db()
    mycursor = database.cursor()
    SQL = f"INSERT INTO {table_name} {columns} VALUES {values}"
    mycursor.execute(SQL)
    database.commit()
    mycursor.close()
    database.close()

def get_value_db(table_name,columns,condition):
    database = active_db()
    mycursor = database.cursor()
    SQL = f'SELECT {columns} FROM {table_name} WHERE {condition}'
    mycursor.execute(SQL)
    data_from_db = mycursor.fetchall()
    database.commit()
    mycursor.close()
    database.close()
    if not data_from_db:
        return None
    return data_from_db

def update_db(table_name,command,column_index,column_val):
    database = active_db()
    mycursor = database.cursor()
    SQL = f"UPDATE {table_name} SET {command} WHERE {column_index} = '{column_val}'"
    mycursor.execute(SQL)
    database.commit()
    mycursor.close()
    database.close()

def active_db():
    database = mysql.connector.connect(host="127.0.0.1",
                               user="root",
                               password="",
                               database="mybot")
    return database

# Database `User-Interrupt`
def statusdb(event):
    userid = event.source.user_id
    displayname = line_bot_api.get_profile(event.source.user_id).display_name
    messagetype = event.message.type
    if(messagetype == 'text'):
        message = event.message.text
    if(get_value_db('linebot_user','*',f"UserID = '{userid}'") == None):
        status = 0
        columns = '(DateTime,UserID,DisplayName,Status)'
        values = f"('{datetime}','{userid}','{displayname}','{status}')"
        insert_db('linebot_user',columns,values)
        line_bot_api.push_message(userid,term_of_use())
    else:
        for row in get_value_db('linebot_user','*',f'UserID = "{userid}"'):
            userid = row[2]
            displayname = row[3]
            status = row[4]
            fullname = row[5]
            address = row[6]
            latitude = row[7]
            longitude = row[8]
        if(status == 0 and message == 'ฉันยอมรับ'):
            update_db('linebot_user',f'status = 1','UserID',userid)
            line_bot_api.push_message(userid,personal_information())
        elif(status == 0 and message != 'ฉันยอมรับ'):
            line_bot_api.push_message(userid,term_of_use())
        elif(status == 1 and fullname == None and messagetype == 'text'):
            update_db('linebot_user',f"FullName = '{message}'",'UserID',userid)
            line_bot_api.push_message(userid,plantation_location())
            quick_reply = QuickReply(
                items = [
                        QuickReplyButton(action=LocationAction(label = 'ส่งตำแหน่งที่ตั้ง'))
                    ]
            )
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text="โปรดกด 'ส่งตำแหน่งที่ตั้ง' เพื่อส่งตำแหน่งของคุณ",quick_reply=quick_reply))
        elif(status == 1 and fullname == None and messagetype != 'text'):
            line_bot_api.push_message(userid, TextSendMessage(text="บอกน้องใบยางหน่อยน่า ว่าชื่ออะไรค้าบ!?"))
            line_bot_api.push_message(userid, personal_information())
        elif(status == 1 and address == None and messagetype == 'location'):
            address = event.message.address
            latitude = event.message.latitude
            longitude = event.message.longitude
            update_db('linebot_user',f"Address = '{address}'",'UserID',userid)
            update_db('linebot_user',f"Latitude = '{latitude}'",'UserID',userid)
            update_db('linebot_user',f"Longitude = '{longitude}'",'UserID',userid)
            line_bot_api.push_message(userid, TextSendMessage(text="ลงทะเบียนใช้งานเสร็จสมบูรณ์ มีอะไรให้น้องใบยางช่วยค้าบ!"))
        elif(status == 1 and address == None and messagetype != 'location'):
            line_bot_api.push_message(userid, TextSendMessage(text="น้องใบยาง ขอทราบที่อยู่ของสวนยางหน่อยน้าค้าบ"))
            line_bot_api.push_message(userid, plantation_location())
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(action=LocationAction(label="ส่งตำแหน่งที่ตั้ง"))
                ]
            )
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text="โปรดกด 'ส่งตำแหน่งที่ตั้ง' เพื่อส่งตำแหน่งของคุณ",quick_reply=quick_reply))
        else:
            return True
        
# Database `Log-Interrupt`
def logdb(event,reply_message):
    userid = event.source.user_id
    displayname = line_bot_api.get_profile(event.source.user_id).display_name
    messagetype = event.message.type
    if(messagetype == "text"):
        message = event.message.text
        messagetype = 'TextMessage'
        columns = '(DateTime,UserID,DisplayName,Message,MessageType,ReplyMessage)'
        value = f"('{datetime}','{userid}','{displayname}','{message}','{messagetype}','{reply_message}')"
        insert_db('linebot_log',columns,value)
    if(messagetype == 'location'):
        address = event.message.address
        latitude = str(event.message.latitude)
        longitude = str(event.message.longitude)
        message = address + " (" + latitude + " " + longitude +")"
        messagetype = 'LocationMessage'
        columns = '(DateTime,UserID,DisplayName,Message,MessageType,ReplyMessage)'
        value = f"('{datetime}','{userid}','{displayname}','{message}','{messagetype}','{reply_message}')"
        insert_db('linebot_log',columns,value)
    if(messagetype == 'image'):
        messagetype = "ImageMessage"
        message_id = event.message.id
        message_content = line_bot_api.get_message_content(message_id)
        file_name = f"{displayname}_{str(event.timestamp)}.jpg"
        file_path = os.path.join(path_to_upload_file , file_name)
        with open(file_path, 'wb') as f:
            for chunk in message_content.iter_content():
                f.write(chunk)
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': file_name,
            'parents': ['1Bo9riv4Ty8G8vs_lnl21ifN5yroj8pmP']
        }
        media = MediaFileUpload(file_path, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        linkaccess = 'https://drive.google.com/file/d/'+file.get('id')
        message = linkaccess
        columns = '(DateTime,UserID,DisplayName,Message,MessageType,ReplyMessage)'
        value = f"('{datetime}','{userid}','{displayname}','{message}','{messagetype}','{reply_message}')"
        insert_db('linebot_log',columns,value)
        columns = '(DateTime,UserID,DisplayName,FileName,FilePath,GoogleDrive)'
        value = f"('{datetime}','{userid}','{displayname}','{file_name}','{file_path}','{message}')"
        insert_db('linebot_image',columns,value)
        image_location_request[userid] = message
        line_bot_api.push_message(event.source.user_id, request_location())

@app.route("/",methods=['GET'])
def default():
    return f"#%&^@!%^!%* LINE Messaging API #!@(#&)"

@app.route("/callback",methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except Exception as error:
        print(error)
        abort(400)
    return 'OK', 200

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    displayname = line_bot_api.get_profile(event.source.user_id).display_name
    print(f"Handle Text Message # {displayname}")
    text = event.message.text
    userid = event.source.user_id
    if(statusdb(event) == True):
        if(userid in image_location_request and text == 'ตกลง'):
            line_bot_api.push_message(event.source.user_id, show_infomation_flex())
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(action=LocationAction(label="ส่งตำแหน่งที่ตั้ง")
                    ),
                ]
            )
            reply_message = "โปรดกด (ส่งตำแหน่งที่ตั้ง) เพื่อส่งตำแหน่งของคุณ"
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message,quick_reply=quick_reply))
        elif(userid in image_location_request and text == 'เรียกดูการแชร์ตำแหน่งที่ตั้ง'):
            line_bot_api.push_message(event.source.user_id, image_location_flex())
            reply_message = "ขั้นตอนการแชร์ตำแหน่งที่ตั้ง (FlexMessage)"
        elif(userid in image_location_request and text != 'ตกลง'):
            image_location_request.pop(event.source.user_id)
        elif(text == 'คุยกับน้องใบยาง'):
            line_bot_api.push_message(event.source.user_id, carousel_message())
            reply_message = "เมนูคุยกับน้องใบยาง (CarouselMessage)"
        elif(event.message.text == 'เมนูเข้าใช้งาน'):
            line_bot_api.push_message(event.source.user_id, select_menu_flex())
            reply_message = "เมนูเข้าใช้งานเริ่มต้น (FlexMessage)"
        elif(event.message.text == 'ส่งรูปภาพวิเคราะห์โรคใบยาง'):
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="ขั้นตอนการส่งรูปภาพ", text="ขั้นตอนการส่งรูปภาพ"))
                ]
            )
            reply_message = 'สามารถส่งรูปภาพใบยางของท่านให้กับเราเพื่อวิเคราะห์โรคใบยางได้เลยครับ!'
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message,quick_reply=quick_reply))
        elif(event.message.text == 'ขั้นตอนการส่งรูปภาพ'):
            line_bot_api.push_message(event.source.user_id, how_to_send_image())
            reply_message = 'วิธีการและขั้นตอนการส่งรูปภาพ (FlexMessage)'
        elif(event.message.text == 'สอบถามโรคใบยาง'):
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="โรคราแป้ง", text="โรคราแป้ง")),
                    QuickReplyButton(action=MessageAction(label="โรคใบจุดนูน", text="โรคใบจุดนูน")),
                    QuickReplyButton(action=MessageAction(label="โรคใบจุดก้างปลา", text="โรคใบจุดก้างปลา")
                    ),
                ]
            )
            reply_message = 'เลือกโรคใบยางที่ต้องการข้อมูลได้เลยครับ'
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message,quick_reply=quick_reply))
        elif(event.message.text == 'โรคราแป้ง'):
            reply_message = "รายละเอียดทั้งหมดของโรคราแป้งในใบยาง สามารถอ่านได้ด่านล่างเลยครับผม"
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message))
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/Powder%20table.png?raw=true', 
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/Powder%20table.png?raw=true'  
            )
            line_bot_api.push_message(event.source.user_id, image_message)
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/Powder%20disease.png?raw=true',  
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/Powder%20disease.png?raw=true'
            )
            line_bot_api.push_message(event.source.user_id, image_message)
        elif(event.message.text == 'โรคใบจุดนูน'):
            reply_message = "รายละเอียดทั้งหมดของโรคใบจุดนูนในใบยาง สามารถอ่านได้ด่านล่างเลยครับผม"
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message))
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/fishbone%20table.png?raw=true', 
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/fishbone%20table.png?raw=true'  
            )
            line_bot_api.push_message(event.source.user_id, image_message)
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/Leaf%20spot%20disease.png?raw=true', 
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/Leaf%20spot%20disease.png?raw=true' 
            )
            line_bot_api.push_message(event.source.user_id, image_message)
        elif(event.message.text == 'โรคใบจุดก้างปลา'):
            reply_message = "รายละเอียดทั้งหมดของโรคใบจุดก้างปลาในใบยาง สามารถอ่านได้ด่านล่างเลยครับผม"
            line_bot_api.push_message(event.source.user_id,TextSendMessage(text=reply_message))
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/leaf%20spot%20table.png?raw=true',
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/leaf%20spot%20table.png?raw=true' 
            )
            line_bot_api.push_message(event.source.user_id, image_message)
            image_message = ImageSendMessage(
                original_content_url='https://github.com/BaiYangBot/Yangbot/blob/main/fishbone%20disease.png?raw=true', 
                preview_image_url='https://github.com/BaiYangBot/Yangbot/blob/main/fishbone%20disease.png?raw=true' 
            )
            line_bot_api.push_message(event.source.user_id, image_message)
        else:
            session_id = userid
            response = detect_intent_from_text(text,session_id)
            reply_message = response.fulfillment_text
            line_bot_api.push_message(event.source.user_id, TextSendMessage(reply_message))
        logdb(event,reply_message)

@handler.add(MessageEvent,message=LocationMessage)
def handle_message(event):
    userid = event.source.user_id
    displayname = line_bot_api.get_profile(event.source.user_id).display_name
    print(f"Handle Location Message # {displayname}")
    reply_message = 'ได้รับข้อมูลเรียบร้อยแล้ว ขอบคุณครับ'
    if(statusdb(event) == True):
        if(userid in image_location_request):
            google_drive_url = image_location_request[userid]
            update_db('linebot_image',f"Address = '{event.message.address}'",'GoogleDrive',google_drive_url)
            update_db('linebot_image',f"Latitude = '{event.message.latitude}'",'GoogleDrive',google_drive_url)
            update_db('linebot_image',f"Longitude = '{event.message.longitude}'",'GoogleDrive',google_drive_url)
            image_location_request.pop(userid)
            reply_message = 'ขอบคุณที่ให้ข้อมูลกับน้องใบยางค้าบ'
            line_bot_api.push_message(event.source.user_id, TextSendMessage(reply_message))
        logdb(event,reply_message)

@handler.add(MessageEvent,message=ImageMessage)
def handle_message(event):
    displayname = line_bot_api.get_profile(event.source.user_id).display_name
    print(f"Handle Image Message # {displayname}")
    reply_message = 'ได้รับข้อมูลเรียบร้อยแล้ว ขอบคุณครับ'
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    else:
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    os.rename(tempfile_path, dist_path)

    im_file = open(dist_path, "rb")
    im = cv2.imread(im_file)
    im0 = im.copy()

    results = model(im, size=640)  # reduce size=320 for faster inference
    print(results)
    annotator = Annotator(im0, line_width=line_thickness)
    # Write results 
    df = results.pandas().xyxy[0]
    for idx, r in df.iterrows():
        c = int(r['class'])  # integer class
        name = r['name']
        label = f'{name} {r.confidence:.2f}'
        annotator.box_label((r.xmin, r.ymin, r.xmax, r.ymax), label, color=colors(c, True))

    save_path = str(save_dir + os.path.basename(tempfile_path) + '_result.' + ext) 
    cv2.imwrite(save_path, im0)

    url = request.url_root + '/' + save_path

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='น้องใบยางวิเคราะห์รูปภาพได้ดังนี้ครับ : '),
            ImageSendMessage(url,url)
        ])
    if(statusdb(event) == True):
        logdb(event,reply_message)

@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)

# create tmp dir for download content
make_static_tmp_dir()

if __name__ == "__main__":
    app.run(port=8000, debug=True)