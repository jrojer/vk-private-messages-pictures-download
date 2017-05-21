import requests
import vk

# USAGE:
# set credentials, count, offset

def GetAPI():
    # credentials :
    app_id  = 'your_app_id'
    login   = 'your_mail@somewhere'
    password = 'your_password'
    session = vk.AuthSession(app_id, login, password, scope='messages')
    return vk.API(session)

def GetMessages(api, count_ = 30, offset_ = 0):
    return api.messages.get(count = count_, offset = offset_)

def ProcessPhotos(att,picture_links):
    photo_sizes = ['src', 'src_small', 'src_big', 'src_xbig', 'src_xxbig', 'src_xxxbig']
    if 'photo' in att:
        # chose the biggest photo size
        for psize in photo_sizes[::-1]:
            if psize in att['photo']:
                picture_links.append(att['photo'][psize])
                break

def ProcessDocs(att,picture_links):
    if 'doc' in att:
        picture_links.append(att['doc']['url'])

def ProcessMessage(mes,picture_links):
    # there must be attachments
    if 'attachments' in mes:
        # iterate over attachments: newer at the end
        for att in mes['attachments']:
            ProcessPhotos(att,picture_links)
            ProcessDocs(att,picture_links)

def DownloadPictures(picture_links):

    print(len(picture_links), 'pictures found')

    num = 1
    for link in picture_links:
        print(num,'/',len(picture_links))
        print(link)
        r = requests.get(link)

        str_num = '%04d' % (num) # here is the number of zeros

        fd = open('./'+str_num+'.jpg','wb')
        fd.write(r.content)
        fd.close()
        num += 1

def main():
    
    api = GetAPI()
    messages = GetMessages(api);

    picture_links = []

    # iterate over messages: newer messages at the end
    for mes in messages[::-1]:     
        # message must be a dictionary
        if isinstance(mes,dict):
            if 'fwd_messages' in mes:
                for fwd_mes in mes['fwd_messages']:
                    ProcessMessage(fwd_mes, picture_links)
            ProcessMessage(mes, picture_links)

    DownloadPictures(picture_links)

if __name__ == '__main__':
    main()
