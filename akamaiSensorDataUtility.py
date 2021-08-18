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
    def __init__(self, sensor_data: str, ver = '1.7'):
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
        _, self.cpen, self.i1, self.dm, self.cwen, self.non, self.opc, self.fc, self.sc, self.wrc, self.isc, self.vib, self.bat, self.x11, self.x12, self.sumCharUA, self.k, self.halfStart, self.brv, self.loc = resto.split(',')

        if(self.testAB(self.useragent) != int(self.sumCharUA)):
            raise Exception("checksum error, bmak func: ab")
        

    def decodeFormInfo(self, string: str):
        infos = string.split(';')[0:-1]
        self.allFormInfo = []
        cnt = 0
        for info in infos:
            a = FormInfo(info)
            self.allFormInfo.append(a)

    def decode(self):
        roba, resto = self.sensor_data.split('-1,2,-94,-100,')
        roba = roba.replace(self.ver, '')

        gd, resto = resto.split('-1,2,-94,-101,')
        self.decodeGD(gd)
        
        i, resto = resto.split('-1,2,-94,-105,')
        self.device_orientation, self.device_motion, self.touch_event = i.split(',')

        if(any('dis' in s for s in [self.device_orientation, self.device_motion, self.touch_event])):
            print('maybe problem????')

        informinfo, resto = resto.split('-1,2,-94,-102,')

        getforminfo, resto = resto.split('-1,2,-94,-108,')
        kact, resto = resto.split('-1,2,-94,-110,')
        

        self.decodeFormInfo(getforminfo)

        kact = kact.replace(';', '\n')

        with open('resto.txt', 'w') as f:
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


if __name__ == '__main__':
    with open('sensorData//sensorData_acaso3.txt', 'r') as f:
        sensor_data = f.read()
    decoder = SensorDataDecoder(sensor_data)
    decoder.decode()
