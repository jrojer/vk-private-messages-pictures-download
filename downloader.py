import requests
import vk

# USAGE:
# set credentials, count, offset

# credentials :
session = vk.AuthSession('your_app_id', 'your_mail@somewhere', 'your_password',scope='messages')
api = vk.API(session)

#count and offset
messages = api.messages.get(count = 30, offset = 0)

picture_links = []

for mes in messages[::-1]: 

    # iterate over messages: newer messages at the end
    if ( isinstance(mes,dict)):

        # message must be a dictionary
        if ('attachments' in mes):

            # there must be attachments
            for att in mes['attachments']:

                # iterate over attachments: newer at the end
                picture_links.append(att['photo']['src_xbig'])

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
