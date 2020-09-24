from requests import get
import json
from enum import Enum
from time import sleep as sleep

class _serviceSim(Enum):
    getBalance = 'getBalance'
    getRepeat = 'getRepeat'
    getNumber = 'getNumber'
    setStatus = 'setStatus'
    getStatus = 'getStatus'

class _beyService(Enum):
    adidas = 'adidas'
    airbnb = 'airbnb'
    airtel = 'airtel'
    akelni = 'akelni'
    alibaba = 'alibaba'
    aliexpress = 'aliexpress'
    alipay = 'alipay'
    amazon = 'amazon'
    aol = 'aol'
    avito = 'avito'
    azino = 'azino'
    bittube = 'bittube'
    blablacar = 'blablacar'
    blizzard = 'blizzard'
    blockchain = 'blockchain'
    burgerking = 'burgerking'
    careem = 'careem'
    cdkeys = 'cdkeys'
    cekkazan = 'cekkazan'
    citymobil = 'citymobil'
    craigslist = 'craigslist'
    delivery = 'delivery'
    dent = 'dent'
    discord = 'discord'
    dixy = 'dixy'
    dodopizza = 'dodopizza'
    domdara = 'domdara'
    dostavista = 'dostavista'
    douyu = 'douyu'
    drom = 'drom'
    drugvokrug = 'drugvokrug'
    dukascopy = 'dukascopy'
    ebay = 'ebay'
    edgeless = 'edgeless'
    electroneum = 'electroneum'
    facebook = 'facebook'
    fiverr = 'fiverr'
    foodpanda = 'foodpanda'
    forwarding = 'forwarding'
    gameflip = 'gameflip'
    gcash = 'gcash'
    get = 'get'
    gett = 'gett'
    globus = 'globus'
    glovo = 'glovo'
    google = 'google'
    grabtaxi = 'grabtaxi'
    green = 'green'
    haraj = 'haraj'
    hopi = 'hopi'
    hqtrivia = 'hqtrivia'
    icard = 'icard'
    icq = 'icq'
    imo = 'imo'
    ininal = 'ininal'
    instagram = 'instagram'
    iost = 'iost'
    jd = 'jd'
    justdating = 'justdating'
    kakaotalk = 'kakaotalk'
    keybase = 'keybase'
    komandacard = 'komandacard'
    kotak811 = 'kotak811'
    kufarby = 'kufarby'
    lazada = 'lazada'
    lbry = 'lbry'
    lenta = 'lenta'
    lianxin = 'lianxin'
    line = 'line'
    linkedin = 'linkedin'
    livescore = 'livescore'
    magnit = 'magnit'
    magnolia = 'magnolia'
    mailru = 'mailru'
    mamba = 'mamba'
    mcdonalds = 'mcdonalds'
    meetme = 'meetme'
    mega = 'mega'
    mercado = 'mercado'
    michat = 'michat'
    microsoft = 'microsoft'
    miratorg = 'miratorg'
    mtscashback = 'mtscashback'
    naver = 'naver'
    netflix = 'netflix'
    nike = 'nike'
    nimses = 'nimses'
    nttgame = 'nttgame'
    odnoklassniki = 'odnoklassniki'
    offerup = 'offerup'
    okcupid = 'okcupid'
    okey = 'okey'
    olx = 'olx'
    openpoint = 'openpoint'
    oraclecloud = 'oraclecloud'
    other = 'other'
    ozon = 'ozon'
    pairs = 'pairs'
    papara = 'papara'
    paycell = 'paycell'
    paymaya = 'paymaya'
    paypal = 'paypal'
    paysend = 'paysend'
    perekrestok = 'perekrestok'
    pof = 'pof'
    pokec = 'pokec'
    pokermaster = 'pokermaster'
    potato = 'potato'
    proton = 'proton'
    pubg = 'pubg'
    pyaterochka = 'pyaterochka'
    qiwiwallet = 'qiwiwallet'
    quipp = 'quipp'
    reuse = 'reuse'
    ripkord = 'ripkord'
    seosprint = 'seosprint'
    shopee = 'shopee'
    signal = 'signal'
    skout = 'skout'
    snapchat = 'snapchat'
    steam = 'steam'
    swvl = 'swvl'
    taksheel = 'taksheel'
    tango = 'tango'
    tantan = 'tantan'
    telegram = 'telegram'
    tencentqq = 'tencentqq'
    tiktok = 'tiktok'
    tinder = 'tinder'
    tosla = 'tosla'
    totalcoin = 'totalcoin'
    touchance = 'touchance'
    trendyol = 'trendyol'
    truecaller = 'truecaller'
    twitter = 'twitter'
    uber = 'uber'
    uploaded = 'uploaded'
    vernyi = 'vernyi'
    viber = 'viber'
    vkontakte = 'vkontakte'
    voopee = 'voopee'
    wechat = 'wechat'
    weibo = 'weibo'
    weku = 'weku'
    whatsapp = 'whatsapp'
    winston = 'winston'
    yahoo = 'yahoo'
    yalla = 'yalla'
    yandex = 'yandex'
    youdo = 'youdo'
    youla = 'youla'
    zoho = 'zoho'

class _operator(Enum):
    o19 = '19'
    activ = 'activ'
    altel = 'altel'
    beeline = 'beeline'
    claro = 'claro'
    globe = 'globe'
    kcell = 'kcell'
    kyivstar = 'kyivstar'
    lycamobile = 'lycamobile'
    matrix = 'matrix'
    megafon = 'megafon'
    movistar = 'movistar'
    mts = 'mts'
    orange = 'orange'
    play = 'play'
    range1 = 'range1'
    redbull = 'redbull'
    redbullmobile = 'redbullmobile'
    rostelecom = 'rostelecom'
    smart = 'smart'
    sun = 'sun'
    tele2 = 'tele2'
    three = 'three'
    tigo = 'tigo'
    tmobile = 'tmobile'
    tnt = 'tnt'
    virginmobile = 'virginmobile'
    vodafone = 'vodafone'
    yota = 'yota'

class _country(Enum):
    afghanistan = 'afghanistan'
    albania = 'albania'
    algeria = 'algeria'
    angola = 'angola'
    antiguaandbarbuda = 'antiguaandbarbuda'
    argentina = 'argentina'
    armenia = 'armenia'
    australia = 'australia'
    austria = 'austria'
    azerbaijan = 'azerbaijan'
    bahrain = 'bahrain'
    bangladesh = 'bangladesh'
    barbados = 'barbados'
    belarus = 'belarus'
    belgium = 'belgium'
    benin = 'benin'
    bhutane = 'bhutane'
    bih = 'bih'
    bolivia = 'bolivia'
    botswana = 'botswana'
    brazil = 'brazil'
    bulgaria = 'bulgaria'
    burkinafaso = 'burkinafaso'
    burundi = 'burundi'
    cambodia = 'cambodia'
    cameroon = 'cameroon'
    canada = 'canada'
    caymanislands = 'caymanislands'
    chad = 'chad'
    china = 'china'
    colombia = 'colombia'
    congo = 'congo'
    costarica = 'costarica'
    croatia = 'croatia'
    cyprus = 'cyprus'
    czech = 'czech'
    djibouti = 'djibouti'
    dominicana = 'dominicana'
    easttimor = 'easttimor'
    ecuador = 'ecuador'
    egypt = 'egypt'
    england = 'england'
    equatorialguinea = 'equatorialguinea'
    estonia = 'estonia'
    ethiopia = 'ethiopia'
    finland = 'finland'
    france = 'france'
    frenchguiana = 'frenchguiana'
    gabon = 'gabon'
    gambia = 'gambia'
    georgia = 'georgia'
    germany = 'germany'
    ghana = 'ghana'
    guadeloupe = 'guadeloupe'
    guatemala = 'guatemala'
    guinea = 'guinea'
    guineabissau = 'guineabissau'
    guyana = 'guyana'
    haiti = 'haiti'
    honduras = 'honduras'
    hungary = 'hungary'
    india = 'india'
    indonesia = 'indonesia'
    iran = 'iran'
    iraq = 'iraq'
    ireland = 'ireland'
    israel = 'israel'
    italy = 'italy'
    ivorycoast = 'ivorycoast'
    jamaica = 'jamaica'
    jordan = 'jordan'
    kazakhstan = 'kazakhstan'
    kenya = 'kenya'
    kuwait = 'kuwait'
    laos = 'laos'
    latvia = 'latvia'
    lesotho = 'lesotho'
    libya = 'libya'
    lithuania = 'lithuania'
    luxembourg = 'luxembourg'
    macau = 'macau'
    madagascar = 'madagascar'
    malawi = 'malawi'
    malaysia = 'malaysia'
    maldives = 'maldives'
    mali = 'mali'
    mauritania = 'mauritania'
    mauritius = 'mauritius'
    mexico = 'mexico'
    moldova = 'moldova'
    mongolia = 'mongolia'
    montenegro = 'montenegro'
    morocco = 'morocco'
    mozambique = 'mozambique'
    myanmar = 'myanmar'
    namibia = 'namibia'
    nepal = 'nepal'
    netherlands = 'netherlands'
    newzealand = 'newzealand'
    nicaragua = 'nicaragua'
    nigeria = 'nigeria'
    norway = 'norway'
    oman = 'oman'
    pakistan = 'pakistan'
    panama = 'panama'
    papuanewguinea = 'papuanewguinea'
    paraguay = 'paraguay'
    peru = 'peru'
    philippines = 'philippines'
    poland = 'poland'
    portugal = 'portugal'
    puertorico = 'puertorico'
    qatar = 'qatar'
    reunion = 'reunion'
    romania = 'romania'
    russia = 'russia'
    rwanda = 'rwanda'
    saintkittsandnevis = 'saintkittsandnevis'
    saintlucia = 'saintlucia'
    saintvincentandgrenadines = 'saintvincentandgrenadines'
    salvador = 'salvador'
    saudiarabia = 'saudiarabia'
    senegal = 'senegal'
    serbia = 'serbia'
    sierraleone = 'sierraleone'
    slovakia = 'slovakia'
    slovenia = 'slovenia'
    somalia = 'somalia'
    southafrica = 'southafrica'
    spain = 'spain'
    srilanka = 'srilanka'
    sudan = 'sudan'
    suriname = 'suriname'
    swaziland = 'swaziland'
    sweden = 'sweden'
    switzerland = 'switzerland'
    syria = 'syria'
    taiwan = 'taiwan'
    tajikistan = 'tajikistan'
    tanzania = 'tanzania'
    thailand = 'thailand'
    tit = 'tit'
    togo = 'togo'
    tunisia = 'tunisia'
    turkey = 'turkey'
    turkmenistan = 'turkmenistan'
    uae = 'uae'
    uganda = 'uganda'
    ukraine = 'ukraine'
    uruguay = 'uruguay'
    usa = 'usa'
    uzbekistan = 'uzbekistan'
    venezuela = 'venezuela'
    vietnam = 'vietnam'
    yemen = 'yemen'
    zambia = 'zambia'
    zimbabwe = 'zimbabwe'

class statusSim(Enum):
    """ ожидание готовности """
    waitReady = 0
    """Ожидания кода для активации сервиса"""
    waitCode = 1
    """ ожидание проверки """
    waitCheck = 2
    """Ожидание уточнения"""
    waitCurrenty = 3
    """ ожидание скрина """
    waitScreen = 4
    """ Ожидание переотправки SMS """
    waitSmsSend_repeat = 5


class _sim():
    def __init__(self, api):
        self.api = api
        self.url = "http://api2.5sim.net/stubs/handler_api.php?api_key={}&action={}"


class getInfo(_sim):
    def __init__(self):
        super().__init__()
        self.acess_number = ''
        self.idActivation = ''
        self.telNumber = ''
        self.codeActivation = ''

    """ баланс api """
    def balance(self):
        command = _serviceSim.getBalance.value
        self.url = self.url.format(self.api, command)
        print(get(self.url).text)

    """ получить статус номера """
    def getStatus(self):
        command = _serviceSim.getStatus.value
        url_new = self.url.format(self.api, command)
        if self.idActivation is None:
            print("сначала получите номер, id активации отстутствует.")
            return
        url_new += f'&id={self.idActivation}'
        status = get(url_new).text
        while not('STATUS_OK' in status):
            status = get(url_new).text
            print(status)
            sleep(1)
        self.codeActivation = status.split(':')[1]
        return self.codeActivation

    """ получить номер, статус "ожидание смс" """
    def getMeNumber(self, _country, _beyService, count_sms):
        count_sms = str(count_sms)
        command = _serviceSim.getNumber.value
        url_new = self.url.format(self.api, command)
        url_new += f'&country={_country}&service={_beyService}&count={count_sms}'
        print(url_new)
        js_answ = (str(get(url_new).text))
        print(js_answ)
        self.acess_number, self.idActivation, self.telNumber = js_answ.split(':')
        print(' получили номер ', self.telNumber)
        print('сразу переводим в статус ожидания ')
        command = _serviceSim.setStatus.value
        url_new = self.url.format(self.api, command)
        url_new += f'&id={self.idActivation}&status=1'
        return print(get(url_new).text)

    """ переключить статус """
    def setStatus(self, statusSim):
        command = _serviceSim.setStatus.value
        url_new = self.url.format(self.api, command)
        url_new += f'&id={self.idActivation}&status={statusSim}'
        return print(get(url_new).text)

    """ Получить номер и ожидать смс сразу """
    def getMeNumber_waitSms(self, _country, _beyService, count_sms):
        self.getMeNumber(_country, _beyService, count_sms)
        print(self.acess_number, " получили номер ")
        print(' ждём смс ')
        self.getStatus()
        return self.codeActivation

""" ошибки при активации """
class printErr():
    def __init__(self):
        self.msgActiveErr = "сначала получите номер, id активации отстутствует."

    def activation(self):
        print(self.msgActiveErr)
        return


if __name__ == '__main__':
    getInfo().getMeNumber_waitSms(_country=_country.russia.value, _beyService=_beyService.tiktok.value, count_sms=1)
