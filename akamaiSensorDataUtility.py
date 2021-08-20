import time


class SensorDataGenerator:

    def __init__(self, protocol='https://', hostname='www.nike.com"', api_public_key='afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq'):
        self.ver = 1.7
        # keyboard event
        self.ke_cnt_lmt = 150
        self.mme_cnt_lmt = 100
        self.mduce_cnt_lmt = 75
        self.pme_cnt_lmt = 25
        self.pduce_cnt_lmt = 25
        self.tme_cnt_lmt = 25
        self.tduce_cnt_lmt = 25
        self.doe_cnt_lmt = 10
        self.dme_cnt_lmt = 10
        self.vc_cnt_lmt = 100
        self.doa_throttle = 0
        self.dma_throttle = 0
        self.session_id = 'default_session'
        self.js_post = False
        self.loc = ''
        self.cf_url = protocol
        self.params_url = self.cf_url + hostname + '/get_params'
        self.auth = ''
        self.api_public_key = api_public_key
        self.aj_lmt_doact = 1
        self.aj_lmt_dmact = 1
        self.aj_lmt_tact = 1
        self.ce_js_post = 0
        self.init_time = 0
        self.informinfo = ''
        self.prevfid = -1
        self.fidcnt = 0
        self.sensor_data = 0
        self.ins = None
        self.cns = None
        self.enGetLoc = 0
        self.enReadDocUrl = 1
        self.disFpCalOnTimeout = 0
        self.xagg = -1
        self.pen = -1
        self.brow = ''
        self.browver = ''
        self.psub = '-'
        self.lang = '-'
        self.prod = '-'
        self.plen = -1
        self.doadma_en = 0
        self.sdfn = []
        self.d2 = 0
        self.d3 = 0
        self.thr = 0
        self.cs = '0a46G5m17Vrp4o4c'
        self.hn = 'unk'
        self.z1 = 0
        self.o9 = 0
        self.vc = ''
        self.y1 = 2016
        self.ta = 0
        self.tst = -1
        self.t_tst = 0
        self.ckie = '_abck'
        self.n_ck = '0'
        self.ckurl = 0
        self.bm = False
        self.mr = '-1'
        self.altFonts = False
        self.rst = False
        self.runFonts = False
        self.fsp = False
        self.firstLoad = True
        self.pstate = False
        self.mn_mc_lmt = 10
        self.mn_state = 0
        self.mn_mc_indx = 0
        self.mn_sen = 0
        self.mn_tout = 100
        self.mn_stout = 1e3
        self.mn_ct = 1
        self.mn_cc = ''
        self.mn_cd = 1e4
        self.mn_lc = []
        self.mn_ld = []
        self.mn_lcl = 0
        self.mn_al = []
        self.mn_il = []
        self.mn_tcl = []
        self.mn_r = []
        self.mn_rt = 0
        self.mn_wt = 0
        self.mn_abck = ''
        self.mn_psn = ''
        self.mn_ts = ''
        self.mn_lg = []
        self.loap = 1
        self.dcs = 0

    def get_cf_date(self):
        '''
        returns unix time
        '''
        return int(time.time())

    def ab(self, t: str) -> int:
        '''
            sums all chars in a string
        '''
        if t == None:
            return -1
        elif type(t) != str:
            return -2

        a = 0
        for char in t:
            temp = ord(char)
            if(temp < 128):
                a += temp
        return a


class SensorDataDecoder:
    def __init__(self, sensor_data: str, ver='1.7'):
        self.sensor_data = sensor_data
        self.ver = ver
        self.decode()

    def testAB(self, string):
        if(string == None):
            return -1
        if type(string) != str:
            return -2

        a = 0
        for char in string:
            a += ord(char)
        return a

    def decodeGD(self, n):
        self.useragent, resto = n.split(',uaend,')

        self.xagg, self.psub, self.lang, self.prod, self.plen, self.pen, self.wen, self.den, self.z1, self.d3, self.availWidth, self.availHeight, self.width, self.height, self.innerWidth, self.innerHeight, self.outerWidth, \
        _, self.cpen, self.i1, self.dm, self.cwen, self.non, self.opc, self.fc, self.sc, self.wrc, self.isc, self.vib, self.bat, self.x11, self.x12, self.sumCharUA, self.k, self.halfStart, self.brv, self.loc = resto.split(
            ',')

        if(self.testAB(self.useragent) != int(self.sumCharUA)):
            raise Exception("checksum error, bmak func: ab")

    def decodeFormInfo(self, string: str):
        infos = string.split(';')[0:-1]
        self.allFormInfo = []
        for info in infos:
            a = FormInfo(info)
            self.allFormInfo.append(a)

    def decodeKact(self, string: str):
        infos = string.split(';')[0:-1]
        self.allKeyboardInfo = []

        for info in infos:
            a = KeyboardAction(info)
            self.allKeyboardInfo.append(a)
            # with open('resto2.txt', 'a+') as f:
            #     f.write(str(a() + '\n')
        
    def decodeMact(self, string: str):
        infos = string.split(';')[0:-1]
        self.allMouseInfo = []

        with open('resto_mouse.txt', 'w') as f:
            f.write('')
        for info in infos:
            with open('resto_mouse.txt', 'a+') as f:

                f.write(str(info) + '\n')

    def decode(self):
        roba, resto = self.sensor_data.split('-1,2,-94,-100,')
        #! da sistemare roba piu avanti

        gd, resto = resto.split('-1,2,-94,-101,')
        self.decodeGD(gd)
        
        i, resto = resto.split('-1,2,-94,-105,')
        self.device_orientation, self.device_motion, self.touch_event = i.split(',')

        if(any('dis' in s for s in [self.device_orientation, self.device_motion, self.touch_event])):
            print('maybe problem????')

        informinfo, resto = resto.split('-1,2,-94,-102,')

        getforminfo, resto = resto.split('-1,2,-94,-108,')
        self.decodeFormInfo(getforminfo)

        kact, resto = resto.split('-1,2,-94,-110,')
        self.decodeKact(kact)

        mact, resto = resto.split('-1,2,-94,-117,')
        self.decodeMact(mact)

        with open('resto.txt', 'w') as f:
            kact = kact.replace(';', '\n')
            f.write(kact)
        


class FormInfo:
    def __init__(self, string: str):
        '''
            self.typee, -1 if null, 1 if type == [text, search, url, email, tel, number, password] otherwise 2
            self.autocomplete -1 if null, 0 off, 1 on otherwise 2
            self.value 1 if value empty OR value == default value
            self.index index of the input box
            self.isRequired 1 if attribute Required exists in that input box or 0
            self.sumCharId call bmak.ab (u can see it above SensorDataDecoder.testAB) with attribute id
            self.sumCharName call bmak.ab (u can see it above SensorDataDecoder.testAB) with attribute name
            self.f 1 if default value is not '' otherwise 0


            Know sumCharName:
                emailAddress: 1230
                password: 883
                pid: 312

            Know sumCharId:
                emailAddress: 2500 
                password: 2290
                pid: -1
        '''
        self.typee, self.autocomplete, self.value, self.isRequired, self.sumCharId, self.sumCharName, self.f = string.split(',')
    def __str__(self):
        return f'FormInfo   type={self.typee} | autocomplete={self.autocomplete} | isRequired={self.isRequired} | sumCharId={self.sumCharId} | sumCharName={self.sumCharName} | f={self.f}'

class KeyboardAction:
    '''
        self.cnt counter, indicates how many keys have been pressed so far
        self.type, the method that logs keyboard action (cka) is called by 3 possibile Events, keyboardDown, keyboardUp, keyboardPress each one has a code respectively 1, 2, 3
        self.time time between current time and bmak.start_ts, bmak.start_ts is inizialized at the start
        self.n value based on the key you have pressed, -2 if (it's called by keyboard press && keycode >= 32 && <=126), -3 if(n >= 33 && n <= 47 and called by keyboarddown or keyup), -4 if(n >= 122 && n <= 123) all other cases -2
        self.l always 0
        self.specialKeys indicites if shift, ctrl, meta or alt key are pressed, formula =
        self.sumChar bmak.ab is called with the name of input box where the character have been typed, if name is not defined it's bmak.ab is called with the paramam id instead of name, -1 if no active element or name and id not defined

        Know sumChar of name:
                emailAddress: 1230
                password: 883
                pid: 312 
                search: 630
        
        notes: 
            - they check by event.isTrusted() if the event is genereted by a script or not
                if it's genereted by script it appends '0,' at the end
    '''

    def __init__(self, string: str):
        if string[-2:] == ',0':
            print('keyboard event genereted by script, problem???')
            self.cnt, self.typee, self.time, self.n, self.l, self.specialKeys, self.sumChar = string.split(',')[0:7]
            self.isTrusted = False
        else:
            self.cnt, self.typee, self.time, self.n, self.l, self.specialKeys, self.sumChar = string.split(',')
            self.isTrusted = True

        self.whichSpecialKeyArePressed()

    def whichSpecialKeyArePressed(self):
        # bmak check if special keys are pressed and assign 1 or 0 to variables for each special key
        # r = e.shiftKey ? 1 : 0 is one exemple for shiftkey, variable name for ctrl, meta and alt are respectively i, c and b
        # then they calculate a number by multiplying power of 2 by the variables
        # 8 * shiftkey + 4 * ctrlKey + 2 * metaKey + alt

        binNum = int(self.specialKeys)
        binList = [char for char in format(binNum, 'b').zfill(4)]
        self.shiftKey = True if binList[0] == '1' else False 
        self.ctrlKey = True if binList[1] == '1' else False
        self.metaKey = True if binList[2] == '1' else False
        self.altKey = True if binList[3] == '1' else False
    
    def __str__(self) -> str:
        return f'Keyboard    isT:{self.isTrusted}|| cnt:{self.cnt} || typee:{self.typee} || time:{self.time} || n:{self.n} || l:{self.l} || specialKeys:{self.specialKeys} || sumChar:{self.sumChar} || shift:{self.shiftKey} || ctrl:{self.ctrlKey} || meta:{self.metaKey} || alt:{self.altKey}'

if __name__ == '__main__':
    with open('sensorData//sensorData_acaso4.txt', 'r') as f:
        sensor_data = f.read()
    decoder = SensorDataDecoder(sensor_data)
    decoder.decode()
