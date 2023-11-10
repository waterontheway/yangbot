from linebot.models import TextSendMessage, FlexSendMessage

def term_of_use():
    flex_template = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://github.com/BaiYangBot/assets/blob/main/term_of_use.png?raw=true",
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "กรุณายอมรับเงื่อนไขการใช้งาน",
            "weight": "bold",
            "size": "lg",
            "align": "start",
            "contents": []
        },
        {
            "type": "text",
            "text": "หากท่านกดยอมรับแล้วหมายถึงท่าน",
            "weight": "regular",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "contents": []
        },
        {
            "type": "text",
            "text": "เห็นด้วยกับการใช้งานรวมถึงการเก็บ",
            "weight": "regular",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "contents": []
        },
        {
            "type": "text",
            "text": "ข้อมูลส่วนตัวของท่าน",
            "weight": "regular",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
          "type": "message",
          "label": "ฉันยอมรับ",
          "text": "ฉันยอมรับ"
        },
            "color": "#3E6244",
            "style": "primary"
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def personal_information():
    flex_template = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://github.com/BaiYangBot/assets/blob/main/personal_information.png?raw=true",
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "กรุณากรอกข้อมูลส่วนบุคคล",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "contents": []
        },
        {
            "type": "text",
            "text": "ชื่อ-นามสกุล (ภาษาไทย)",
            "weight": "bold",
            "size": "md",
            "align": "center",
            "gravity": "center",
            "contents": []
        },
        {
            "type": "text",
            "text": "ตัวอย่าง : ใบยาง ทดสอบ",
            "weight": "regular",
            "size": "md",
            "align": "center",
            "style": "normal",
            "offsetTop": "5px",
            "contents": []
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def plantation_location():
    flex_template = {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
        "type": "image",
        "url": "https://github.com/BaiYangBot/assets/blob/main/share_location_place.png?raw=true",
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "กรุณาแชร์ตำแหน่งที่ตั้งของสวน",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "ตัวอย่างการระบุตำแหน่งที่ตั้ง :",
            "weight": "regular",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "style": "normal",
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "1. กดปุ่ม + ด้านล่างซ้าย",
            "style": "normal",
            "offsetTop": "3px",
            "contents": []
        },
        {
            "type": "text",
            "text": "2. เลือกตำแหน่งที่ตั้งแปลงสวนของท่าน",
            "style": "normal",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "image",
            "url": "https://github.com/BaiYangBot/Yangbot/blob/main/share_location_step.png?raw=true", ##
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def carousel_message():
    flex_template = {
    "type": "carousel",
    "contents": [
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://github.com/BaiYangBot/assets/blob/main/ask.png?raw=true",##
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "text",
                "text": "สอบถามโรคใบยาง",
                "weight": "bold",
                "size": "lg",
                "wrap": True,
                "contents": []
            },
            {
                "type": "text",
                "text": "รายละเอียดของโรคใบยาง",
                "color": "#909090FF",
                "contents": []
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "สอบถามโรคใบยาง",
                "text": "สอบถามโรคใบยาง"
                },
                "color": "#3E6244",
                "style": "primary"
            }
            ]
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://github.com/BaiYangBot/assets/blob/main/information.png?raw=true",##
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "text",
                "text": "ข้อมูลใบยาง",
                "weight": "bold",
                "size": "lg",
                "wrap": True,
                "contents": []
            },
            {
                "type": "text",
                "text": "ข้อมูลเกี่ยวกับใบยาง",
                "size": "md",
                "color": "#909090FF",
                "contents": []
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "ข้อมูลใบยาง",
                "uri": "https://linecorp.com"
                },
                "color": "#3E6244",
                "style": "primary"
            }
            ]
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://github.com/BaiYangBot/assets/blob/main/library.png?raw=true",##
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "text",
                "text": "ระบบคลังรูปภาพ",
                "weight": "bold",
                "size": "lg",
                "wrap": True,
                "contents": []
            },
            {
                "type": "text",
                "text": "คลังเก็บรูปภาพใบยาง",
                "color": "#909090FF",
                "contents": []
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "คลังรูปภาพ",
                "uri": "https://linecorp.com"
                },
                "color": "#3E6244",
                "style": "primary"
            }
            ]
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://github.com/BaiYangBot/assets/blob/main/aboutus.png?raw=true", ##
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "text",
                "text": "เกี่ยวกับเรา",
                "weight": "bold",
                "size": "lg",
                "wrap": True,
                "contents": []
            },
            {
                "type": "text",
                "text": "ช่องทางการติดต่อและข้อมูลของเรา",
                "color": "#909090FF",
                "contents": []
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "uri",
                "label": "เกี่ยวกับเรา",
                "uri": "https://linecorp.com"
                },
                "color": "#3E6244",
                "style": "primary"
            }
            ]
        }
        }
    ]
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def select_menu_flex():
    flex_template = {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": "https://github.com/BaiYangBot/assets/blob/main/select_menu.png?raw=true",##
      "size": "full",
      "aspectRatio": "18:6",
      "aspectMode": "fit"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "ลงทะเบียนเกษตรกร",
            "uri": "https://linecorp.com"
          }
        },
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "คุยกับน้องใบยาง",
            "text": "คุยกับน้องใบยาง"
          }
        }
      ]
    }
  }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def how_to_send_image():
    flex_template = {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
        "type": "image",
        "url": "https://raw.githubusercontent.com/BaiYangBot/Yangbot/main/sent_image.png",
        "margin": "none",
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFFFF",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "วิธีการส่งรูปภาพวิเคราะห์โรค",
            "weight": "bold",
            "size": "lg",
            "align": "start",
            "wrap": True,
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "ขั้นตอนดังต่อไปนี้ :)",
            "weight": "regular",
            "align": "start",
            "gravity": "center",
            "style": "normal",
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "1. กดปุ่มส่งรูปภาพด้านล่างซ้าย",
            "style": "normal",
            "contents": []
        },
        {
            "type": "text",
            "text": "2. เลือกรูปภาพใบยางของท่าน",
            "style": "normal",
            "contents": []
        },
        {
            "type": "text",
            "text": "3. กดส่งรูปภาพ",
            "style": "normal",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "image",
            "url": "https://github.com/BaiYangBot/Yangbot/blob/main/การส่งรูปภาพ.png?raw=true",
            "size": "4xl"
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def show_infomation_flex():
    flex_template = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "url": "https://github.com/BaiYangBot/assets/blob/main/show_information.png?raw=true",
      "size": "full",
      "aspectRatio": "18:6",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "md",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "เรียกดูขั้นตอนการแชร์ตำแหน่ง",
          "weight": "bold",
          "size": "lg",
          "align": "start",
          "contents": []
        },
        {
          "type": "text",
          "text": "หากท่านทราบถึงวิธีการแชร์ตำแหน่งอยู่แล้ว",
          "weight": "regular",
          "size": "sm",
          "align": "start",
          "gravity": "center",
          "contents": []
        },
        {
          "type": "text",
          "text": "ท่านสามารถกดแชร์ตำแหน่งเพื่อเก็บข้อมูลได้",
          "weight": "regular",
          "size": "sm",
          "align": "start",
          "gravity": "center",
          "contents": []
        },
        {
          "type": "text",
          "text": "โดยทันทีหากไม่ทราบโปรดกดที่ปุ่มด้านล่าง",
          "weight": "regular",
          "size": "sm",
          "align": "start",
          "gravity": "center",
          "contents": []
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "เรียกดูขั้นตอน",
            "text": "เรียกดูการแชร์ตำแหน่งที่ตั้ง"
          },
          "color": "#3E6244",
          "style": "primary"
        }
      ]
    }
  }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def image_location_flex():
    flex_template = {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
        "type": "image",
        "url": "https://github.com/BaiYangBot/assets/blob/main/share_location.png?raw=true",##
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "กรุณาแชร์ตำแหน่งที่ตั้งของรูปภาพ",
            "weight": "bold",
            "size": "lg",
            "align": "center",
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "ตัวอย่างการระบุตำแหน่งที่ตั้ง :",
            "weight": "regular",
            "size": "md",
            "align": "start",
            "gravity": "center",
            "style": "normal",
            "offsetTop": "5px",
            "contents": []
        },
        {
            "type": "text",
            "text": "1. กดปุ่ม + ด้านล่างซ้าย",
            "style": "normal",
            "offsetTop": "3px",
            "contents": []
        },
        {
            "type": "text",
            "text": "2. เลือกตำแหน่งที่ตั้งของรูปภาพ",
            "style": "normal",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "image",
            "url": "https://github.com/BaiYangBot/Yangbot/blob/main/share_location_step.png?raw=true", #
            "size": "4xl"
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)

def request_location():
    flex_template = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": "https://github.com/BaiYangBot/assets/blob/main/share_location.png?raw=true",
        "size": "full",
        "aspectRatio": "18:6",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
        },
        "contents": [
        {
            "type": "text",
            "text": "ตำแหน่งที่ตั้งของรูปภาพดังกล่าว",
            "weight": "bold",
            "size": "lg",
            "align": "start",
            "contents": []
        },
        {
            "type": "text",
            "text": "ขออนุญาติเก็บตำแหน่งที่ตั้งของรูปภาพนี้เพื่อ",
            "weight": "regular",
            "size": "sm",
            "align": "start",
            "gravity": "center",
            "contents": []
        },
        {
            "type": "text",
            "text": "นำไปวิเคราะห์ถึงความเสี่ยงของโรคระบาด",
            "weight": "regular",
            "size": "sm",
            "align": "start",
            "gravity": "center",
            "contents": []
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "ตกลง",
            "text": "ตกลง"
            },
            "color": "#3E6244",
            "style": "primary"
        }
        ]
    }
    }
    return FlexSendMessage(alt_text="คุณได้รับข้อความใหม่", contents=flex_template)
