def function(argument):
      a = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
      b = ['1409876','3709865','61098765434567','836543237','259876543','440987654','519876','22876543','83987654','4487654','96987654',
      '50987654','232408','4','8443434','434343','59876','098652347','8876542345','069588884','0987654','8876543','723478','28763',
      '82345','365432','83487','733456','6987654','5344567','1987654','3765432','635677','887654','26543','476543','576543','765432','8765438',
      '87654','9876549','654325','54328','7654324','65438','76544','54325','98765430','89876543','009876543','00987654','86798765','45678876547',
      '27784636225','809876543','65433','654314','654337','654361','7654383','7654365425','44876543','51765432','987654322','4567876583','8765444',
      '96','5','8','4','8','4','5','0','8','0','0','8',
      '7','2','8','3','8','7','6','5','1','3','6','14','37','61','83','25','44','51','22','83','44','96','5','8','4','8','4','5','0','8','0',
      '0','8','7','2','8','14','37','61','83','25','44','51','22','83','44','96','5','8','4','8','4','5','0','8','0','0','8','7','2','8','14',
      '37','61','83','25','44','51','22','83','44','96','5','8','4','8','4','5','0','8','0','0','8','7','2','8','14','37','61','83','25','44',
      '51','22','83','44','96','5','8','4','8','4','5','0','8','0','0','8','7','2','8','14','37','61','83','25','44','51','22','83','44','96',
      '5','8','4','8','4','5','0','8','0','0','8','7','2','8','14','37','61','83','25','44','51','22','83','44','96','5','8','4','8','4','5','0',
      '8','0','0','8','7','2','8']
      f= open('D:\sf\читать.txt')
      s = f.read()
      c = ''
      for i in s:
            try:
                  h = a.index(i)
                  g = b[h]
            except ValueError:
                  c = c + i
            else: 
                  c = c + g + "-"  
      f.close()
      f = open("D:\sf\записать.txt", "w")
      f.write(c)
      f.close()
function("abracadabra")















