import itchat

itchat.auto_login(enableCmdQR=True)

print(itchat.search_friends(name = '何雨菲'))
users = itchat.search_friends(name = '何雨菲')
#contact = u'ai'
contact_person = users[0]['UserName']
print(contact_person)

#Location =
#Videolink =
#itchat.send(u'FIXME%d, %s, be careful'%(Location, Videolink), toUserName='username')\

#Modify here
message_content = 'Hey,dude'
itchat.send(message_content, toUserName = contact_person)


itchat.run()
