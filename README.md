# vk-private-messages-pictures-download
python script for downloading pictures from your private messages

To use the script:
1. Go to  https://vk.com/dev/standalone
2. Create a standalone application
3. In your application's setting find and copy "Application ID"
4. Edit the "downloader.py" file:

 * Give the "Application ID" and your credentials in vk.AuthSession method

 * In the api.messages.get method set: count -- number of messages to get, offset -- the offset.

6. cd to the script's folder
7. launch the script 

the pictures will be saved at the same folder

Скачать картинки и документы из своих личных сообщений вконтакте (vk.com). Python скрипт.
