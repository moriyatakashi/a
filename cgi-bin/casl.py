__all__ = ['casl']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['LabelTableItem', 'instNOP', 'installAsmErrorHandlers', 'getHex', 'instJOV', 'signedDec', 'alNone', 'gr', 'STATE_BREAK', 'isLabel', 'instCPA', 'referLabelSub', 'scrollProgToShowLine', 'instCALL', 'referGlobalLabel', 'defineGlobalLabel', 'initializeRegMem', 'errorShown', 'instJNZ', 'outputRegMem', 'setState', 'inputRegMem', 'defineLabelSub', 'aITable', 'scriptAllowed', 'onClickedError', 'ParsedLine', 'instLD', 'breakPointData', 'getGRCheck', 'alInOut', 'stepOut', 'executeOneInstruction', 'lineNumber', 'op2m', 'instJPL', 'resolveGlobalReferences', 'getAddrCheck', 'i', 'alEnd', 'alDC', 'sf', 'instAND', 'zxt', 'op2r', 'INST', 'sxt', 'instSUBA', 'startLine', 'instSRL', 'macroFlag', 'errorMessages', 'onClickRadix', 'getDec', 'instJMI', 'alRPop', 'STATE_UNSTARTED', 'address', 'setFRC', 'instInvalid', 'startOperand', 'installBreakPointHandlers', 'enableElement', 'instSUBL', 'setReadOnly', 'instJUMP', 'setFROSigned', 'isSpace', 'onClickedBreakPoint', 'unsignedDec', 'alRM', 'getXRCheck', 'stepIn', 'globalLabelTable', 'instADDL', 'findOrCreateLabelTableItem', 'stepOver', 'alRMR', 'instPUSH', 'markPR', 'instSVC', 'stop', 'sp', 'consoleView', 'alDS', 'pr', 'fromHex', 'enableButton', 'jis8ToCharCode', 'InstTableItem', 'callNest', 'alStart', 'parseLine', 'STATE_NONE', 'markedAddress', 'instSLA', 'outputMem', 'startLabel', 'STATE_RUNNING', 'referLabel', 'assemble', 'radix', 'instLAD', 'hex4', 'go', 'instADDA', 'inputReg', 'getGR', 'mem', 'instSLL', 'instPOP', 'charCodeToJis8', 'startLocation', 'entryPoint', 'instTable', 'outputReg', 'alRPush', 'nonExecutableTable', 'assembleOneLine', 'alR', 'setFR', 'instOR', 'instST', 'pause', 'logError', 'instRET', 'instSRA', 'processEnd', 'allocConstant', 'Token', 'AITableItem', 'fromDec', 'cont', 'setFROUnsigned', 'processStart', 'stateCurrent', 'instXOR', 'alRMR2', 'ConsoleView', 'getAddress', 'instCPL', 'zf', 'localLabelTable', 'ea', 'ErrorItem', 'locationCounter', 'addressTable', 'of', 'inputMem', 'instJZE', 'Bits64K', 'getStr', 'getRadix', 'objectcode', 'breakOnRet', 'onChangeAddress', 'defineLabel', 'clearAllBreakPoints', 'v', 'singleStep', 'alM'])
@Js
def PyJsHoisted_hex4_(val, this, arguments, var=var):
    var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'val'])
    var.put('str', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        var.put('str', Js('0123456789ABCDEF').callprop('charAt', (PyJsBshift(var.get('val'),(Js(12.0)-(var.get('i')*Js(4.0))))&Js(15))), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('str')
PyJsHoisted_hex4_.func_name = 'hex4'
var.put('hex4', PyJsHoisted_hex4_)
@Js
def PyJsHoisted_unsignedDec_(val, this, arguments, var=var):
    var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
    var.registers(['val'])
    return (Js('')+(var.get('val')&Js(65535)))
PyJsHoisted_unsignedDec_.func_name = 'unsignedDec'
var.put('unsignedDec', PyJsHoisted_unsignedDec_)
@Js
def PyJsHoisted_signedDec_(val, this, arguments, var=var):
    var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
    var.registers(['val'])
    return (Js('')+var.get('sxt')((var.get('val')&Js(65535))))
PyJsHoisted_signedDec_.func_name = 'signedDec'
var.put('signedDec', PyJsHoisted_signedDec_)
@Js
def PyJsHoisted_ea_(val1, val2, this, arguments, var=var):
    var = Scope({'val1':val1, 'val2':val2, 'this':this, 'arguments':arguments}, var)
    var.registers(['val1', 'val2'])
    return ((var.get('val1')+var.get('val2'))&Js(65535))
PyJsHoisted_ea_.func_name = 'ea'
var.put('ea', PyJsHoisted_ea_)
@Js
def PyJsHoisted_sxt_(val, this, arguments, var=var):
    var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
    var.registers(['val'])
    var.put('val', Js(65535), '&')
    return (var.get('val') if (var.get('val')<Js(32768)) else (var.get('val')-Js(65536.0)))
PyJsHoisted_sxt_.func_name = 'sxt'
var.put('sxt', PyJsHoisted_sxt_)
@Js
def PyJsHoisted_zxt_(val, this, arguments, var=var):
    var = Scope({'val':val, 'this':this, 'arguments':arguments}, var)
    var.registers(['val'])
    return var.put('val', Js(65535), '&')
PyJsHoisted_zxt_.func_name = 'zxt'
var.put('zxt', PyJsHoisted_zxt_)
@Js
def PyJsHoisted_charCodeToJis8_(charcode, this, arguments, var=var):
    var = Scope({'charcode':charcode, 'this':this, 'arguments':arguments}, var)
    var.registers(['charcode'])
    if ((var.get('charcode')>=Js(0.0)) and (var.get('charcode')<=Js(127))):
        return var.get('charcode')
    if ((var.get('charcode')>=Js(65377)) and (var.get('charcode')<=Js(65439))):
        return ((var.get('charcode')-Js(65377))+Js(161))
    return (-Js(1.0))
PyJsHoisted_charCodeToJis8_.func_name = 'charCodeToJis8'
var.put('charCodeToJis8', PyJsHoisted_charCodeToJis8_)
@Js
def PyJsHoisted_jis8ToCharCode_(jis8, this, arguments, var=var):
    var = Scope({'jis8':jis8, 'this':this, 'arguments':arguments}, var)
    var.registers(['jis8'])
    if ((var.get('jis8')>=Js(0.0)) and (var.get('jis8')<=Js(127))):
        return var.get('jis8')
    if ((var.get('jis8')>=Js(161)) and (var.get('jis8')<=Js(223))):
        return ((var.get('jis8')-Js(161))+Js(65377))
    return (-Js(1.0))
PyJsHoisted_jis8ToCharCode_.func_name = 'jis8ToCharCode'
var.put('jis8ToCharCode', PyJsHoisted_jis8ToCharCode_)
@Js
def PyJsHoisted_Bits64K_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('ar', var.get('Array').create((Js(65536.0)/Js(32.0))))
    var.get(u"this").put('count', Js(0.0))
    @Js
    def PyJs_anonymous_0_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i'])
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get(u"this").get('ar').get('length')):
            var.get(u"this").get('ar').put(var.get('i'), Js(0.0))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.get(u"this").put('count', Js(0.0))
    PyJs_anonymous_0_._set_name('anonymous')
    var.get(u"this").put('initialize', PyJs_anonymous_0_)
    @Js
    def PyJs_anonymous_1_(addr, this, arguments, var=var):
        var = Scope({'addr':addr, 'this':this, 'arguments':arguments}, var)
        var.registers(['mask', 'offset', 'addr'])
        var.put('offset', PyJsBshift(var.get('addr'),Js(5.0)))
        var.put('mask', (Js(1.0)<<(var.get('addr')%Js(32.0))))
        if (var.get(u"this").get('ar').get(var.get('offset'))&var.get('mask')).neg():
            var.get(u"this").get('ar').put(var.get('offset'), var.get('mask'), '|')
            (var.get(u"this").put('count',Js(var.get(u"this").get('count').to_number())+Js(1))-Js(1))
    PyJs_anonymous_1_._set_name('anonymous')
    var.get(u"this").put('set', PyJs_anonymous_1_)
    @Js
    def PyJs_anonymous_2_(addr, this, arguments, var=var):
        var = Scope({'addr':addr, 'this':this, 'arguments':arguments}, var)
        var.registers(['mask', 'offset', 'addr'])
        var.put('offset', PyJsBshift(var.get('addr'),Js(5.0)))
        var.put('mask', (Js(1.0)<<(var.get('addr')%Js(32.0))))
        if (var.get(u"this").get('ar').get(var.get('offset'))&var.get('mask')):
            var.get(u"this").get('ar').put(var.get('offset'), (~var.get('mask')), '&')
            (var.get(u"this").put('count',Js(var.get(u"this").get('count').to_number())-Js(1))+Js(1))
    PyJs_anonymous_2_._set_name('anonymous')
    var.get(u"this").put('clear', PyJs_anonymous_2_)
    @Js
    def PyJs_anonymous_3_(addr, this, arguments, var=var):
        var = Scope({'addr':addr, 'this':this, 'arguments':arguments}, var)
        var.registers(['mask', 'offset', 'addr'])
        var.put('offset', PyJsBshift(var.get('addr'),Js(5.0)))
        var.put('mask', (Js(1.0)<<(var.get('addr')%Js(32.0))))
        return (Js(True) if (var.get(u"this").get('ar').get(var.get('offset'))&var.get('mask')) else Js(False))
    PyJs_anonymous_3_._set_name('anonymous')
    var.get(u"this").put('isSet', PyJs_anonymous_3_)
    @Js
    def PyJs_anonymous_4_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get(u"this").get('count')
    PyJs_anonymous_4_._set_name('anonymous')
    var.get(u"this").put('getCount', PyJs_anonymous_4_)
    var.get(u"this").callprop('initialize')
PyJsHoisted_Bits64K_.func_name = 'Bits64K'
var.put('Bits64K', PyJsHoisted_Bits64K_)
@Js
def PyJsHoisted_AITableItem_(code, fnc, this, arguments, var=var):
    var = Scope({'code':code, 'fnc':fnc, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'fnc'])
    var.get(u"this").put('code', var.get('code'))
    var.get(u"this").put('fnc', var.get('fnc'))
    @Js
    def PyJs_anonymous_5_(parsedLine, this, arguments, var=var):
        var = Scope({'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
        var.registers(['parsedLine'])
        var.get(u"this").callprop('fnc', var.get(u"this").get('code'), var.get('parsedLine'))
    PyJs_anonymous_5_._set_name('anonymous')
    var.get(u"this").put('callFnc', PyJs_anonymous_5_)
PyJsHoisted_AITableItem_.func_name = 'AITableItem'
var.put('AITableItem', PyJsHoisted_AITableItem_)
@Js
def PyJsHoisted_LabelTableItem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('value', (-Js(1.0)))
    var.get(u"this").put('defLine', (-Js(1.0)))
    var.get(u"this").put('refAddr', var.get('Array').create())
    var.get(u"this").put('refLine', var.get('Array').create())
    var.get(u"this").put('multiDefined', Js(False))
PyJsHoisted_LabelTableItem_.func_name = 'LabelTableItem'
var.put('LabelTableItem', PyJsHoisted_LabelTableItem_)
@Js
def PyJsHoisted_defineLabel_(label, this, arguments, var=var):
    var = Scope({'label':label, 'this':this, 'arguments':arguments}, var)
    var.registers(['label'])
    var.get('defineLabelSub')(var.get('localLabelTable'), var.get('label'), var.get('locationCounter'), var.get('lineNumber'))
PyJsHoisted_defineLabel_.func_name = 'defineLabel'
var.put('defineLabel', PyJsHoisted_defineLabel_)
@Js
def PyJsHoisted_defineGlobalLabel_(label, value, line, this, arguments, var=var):
    var = Scope({'label':label, 'value':value, 'line':line, 'this':this, 'arguments':arguments}, var)
    var.registers(['label', 'value', 'line'])
    var.get('defineLabelSub')(var.get('globalLabelTable'), var.get('label'), var.get('value'), var.get('line'))
PyJsHoisted_defineGlobalLabel_.func_name = 'defineGlobalLabel'
var.put('defineGlobalLabel', PyJsHoisted_defineGlobalLabel_)
@Js
def PyJsHoisted_defineLabelSub_(table, label, value, line, this, arguments, var=var):
    var = Scope({'table':table, 'label':label, 'value':value, 'line':line, 'this':this, 'arguments':arguments}, var)
    var.registers(['line', 'item', 'label', 'value', 'table'])
    var.put('item', var.get('findOrCreateLabelTableItem')(var.get('table'), var.get('label')))
    if (var.get('item').get('value')>=Js(0.0)):
        var.get('item').put('multiDefined', Js(True))
        var.get('logError')(var.get('line'), (Js('多重定義されています - ')+var.get('label')))
    else:
        var.get('item').put('value', var.get('value'))
        var.get('item').put('defLine', var.get('line'))
PyJsHoisted_defineLabelSub_.func_name = 'defineLabelSub'
var.put('defineLabelSub', PyJsHoisted_defineLabelSub_)
@Js
def PyJsHoisted_referLabel_(label, location, this, arguments, var=var):
    var = Scope({'label':label, 'location':location, 'this':this, 'arguments':arguments}, var)
    var.registers(['location', 'label'])
    var.get('referLabelSub')(var.get('localLabelTable'), var.get('label'), var.get('location'), var.get('lineNumber'))
PyJsHoisted_referLabel_.func_name = 'referLabel'
var.put('referLabel', PyJsHoisted_referLabel_)
@Js
def PyJsHoisted_referGlobalLabel_(label, location, line, this, arguments, var=var):
    var = Scope({'label':label, 'location':location, 'line':line, 'this':this, 'arguments':arguments}, var)
    var.registers(['location', 'label', 'line'])
    var.get('referLabelSub')(var.get('globalLabelTable'), var.get('label'), var.get('location'), var.get('line'))
PyJsHoisted_referGlobalLabel_.func_name = 'referGlobalLabel'
var.put('referGlobalLabel', PyJsHoisted_referGlobalLabel_)
@Js
def PyJsHoisted_referLabelSub_(table, label, location, line, this, arguments, var=var):
    var = Scope({'table':table, 'label':label, 'location':location, 'line':line, 'this':this, 'arguments':arguments}, var)
    var.registers(['line', 'location', 'item', 'label', 'table'])
    var.put('item', var.get('findOrCreateLabelTableItem')(var.get('table'), var.get('label')))
    var.get('item').get('refAddr').callprop('push', var.get('location'))
    var.get('item').get('refLine').callprop('push', var.get('line'))
PyJsHoisted_referLabelSub_.func_name = 'referLabelSub'
var.put('referLabelSub', PyJsHoisted_referLabelSub_)
@Js
def PyJsHoisted_findOrCreateLabelTableItem_(table, label, this, arguments, var=var):
    var = Scope({'table':table, 'label':label, 'this':this, 'arguments':arguments}, var)
    var.registers(['item', 'label', 'table'])
    var.put('item', var.get('table').get(var.get('label')))
    if var.get('item').neg():
        var.put('item', var.get('LabelTableItem').create())
        var.get('table').put(var.get('label'), var.get('item'))
    return var.get('item')
PyJsHoisted_findOrCreateLabelTableItem_.func_name = 'findOrCreateLabelTableItem'
var.put('findOrCreateLabelTableItem', PyJsHoisted_findOrCreateLabelTableItem_)
@Js
def PyJsHoisted_ParsedLine_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('label', Js(''))
    var.get(u"this").put('inst', Js(''))
    var.get(u"this").put('operands', var.get('Array').create())
    var.get(u"this").put('endcol', (-Js(1.0)))
    @Js
    def PyJs_anonymous_6_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if (((var.get(u"this").get('label')==Js('')) and (var.get(u"this").get('inst')==Js(''))) and (var.get(u"this").get('operands').get('length')==Js(0.0))):
            return Js(True)
        else:
            return Js(False)
    PyJs_anonymous_6_._set_name('anonymous')
    var.get(u"this").put('isEmpty', PyJs_anonymous_6_)
PyJsHoisted_ParsedLine_.func_name = 'ParsedLine'
var.put('ParsedLine', PyJsHoisted_ParsedLine_)
@Js
def PyJsHoisted_ErrorItem_(lineNumber, message, this, arguments, var=var):
    var = Scope({'lineNumber':lineNumber, 'message':message, 'this':this, 'arguments':arguments}, var)
    var.registers(['message', 'lineNumber'])
    var.get(u"this").put('lineNumber', var.get('lineNumber'))
    var.get(u"this").put('message', var.get('message'))
PyJsHoisted_ErrorItem_.func_name = 'ErrorItem'
var.put('ErrorItem', PyJsHoisted_ErrorItem_)
@Js
def PyJsHoisted_assemble_(arrayLines, initialLocation, tabWidth, entryPointName, this, arguments, var=var):
    var = Scope({'arrayLines':arrayLines, 'initialLocation':initialLocation, 'tabWidth':tabWidth, 'entryPointName':entryPointName, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'lineAddr', 'entryPointName', 'endColTable', 'parsedLine', 'item', 'nErrors', 'initialLocation', 'arOut', 'arrayLines', 'n', 'tabWidth', 'str', 'arErrors', 'len'])
    var.put('globalLabelTable', var.get('Object').create())
    var.put('errorMessages', var.get('Array').create())
    var.put('addressTable', var.get('Array').create(var.get('arrayLines').get('length')))
    var.put('nonExecutableTable', var.get('Array').create(var.get('arrayLines').get('length')))
    var.get('breakPointData').callprop('initialize')
    var.get('macroFlag').callprop('initialize')
    var.get('enableElement')(Js('button_clear_break'), var.get('breakPointData').callprop('getCount'))
    var.put('startLabel', var.get(u"null"))
    var.put('startOperand', var.get(u"null"))
    var.put('startLine', (-Js(1.0)))
    var.put('errorShown', (-Js(1.0)))
    var.put('objectcode', var.get('Array').create(Js(65536.0)))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('objectcode')):
        var.get('objectcode').put(var.get('i'), Js(0.0))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('entryPoint', (-Js(1.0)))
    var.put('locationCounter', var.get('initialLocation'))
    var.put('endColTable', var.get('Array').create(var.get('arrayLines').get('length')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('arrayLines').get('length')):
        var.get('arrayLines').put(var.get('i'), var.get('formatSourceLine')(var.get('arrayLines').get(var.get('i')), var.get('tabWidth')))
        var.get('addressTable').put(var.get('i'), (-Js(1.0)))
        var.get('nonExecutableTable').put(var.get('i'), Js(False))
        var.put('lineNumber', var.get('i'))
        var.put('parsedLine', var.get('parseLine')(var.get('arrayLines').get(var.get('i'))))
        var.get('endColTable').put(var.get('i'), var.get('parsedLine').get('endcol'))
        if (var.get('parsedLine').get('inst')==Js('IN')):
            if ((var.get('defined')(var.get('window').get('opera')).neg() and var.get('defined')(var.get('document').get('all'))) and var.get('defined')(var.get('window').get('XMLHttpRequest'))):
                if var.get('scriptAllowed').neg():
                    var.put('str', var.get('prompt')(Js('IN命令が実行可能な環境になっているかの確認です。\r\nお手数ですが [OK] を押してください。入力欄は空でかまいません。'), Js('')))
                    if (var.get('str')!=var.get(u"null")):
                        var.put('scriptAllowed', Js(True))
                    else:
                        var.get('alert')(Js('情報バーに「スクリプト化されたウィンドウ」云々が出ていたら、お手数ですが、許可してから、[アセンブル] ボタンを押しなおしてください。IN命令の動作にはこの許可が必要です。'))
                        return (-Js(1.0))
            else:
                var.put('scriptAllowed', Js(True))
        if var.get('parsedLine').callprop('isEmpty').neg():
            if (var.get('parsedLine').get('label')!=Js('')):
                if var.get('isLabel')(var.get('parsedLine').get('label')).neg():
                    var.get('logError')(var.get('i'), (Js('ラベル欄が不正です - ')+var.get('parsedLine').get('label')))
                    var.get('parsedLine').put('label', Js(''))
            var.get('assembleOneLine')(var.get('parsedLine'))
        if (var.get('locationCounter')>Js(65536)):
            var.get('logError')(var.get('i'), Js('COMET II コンピュータのメモリに入りきりません。アセンブルを中止します'))
            break
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('locationCounter')<=Js(65536)):
        if (var.get('startLabel')!=var.get(u"null")):
            var.get('logError')((var.get('arrayLines').get('length')-Js(1.0)), Js('END命令がありません'))
            var.get('processEnd')()
        var.get('resolveGlobalReferences')(var.get('entryPointName'))
    var.put('nErrors', var.get('errorMessages').get('length'))
    @Js
    def PyJs_anonymous_7_(item1, item2, this, arguments, var=var):
        var = Scope({'item1':item1, 'item2':item2, 'this':this, 'arguments':arguments}, var)
        var.registers(['item1', 'item2'])
        return (var.get('item1').get('lineNumber')-var.get('item2').get('lineNumber'))
    PyJs_anonymous_7_._set_name('anonymous')
    var.get('errorMessages').callprop('sort', PyJs_anonymous_7_)
    var.put('arErrors', var.get('Array').create())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('errorMessages').get('length')):
        var.put('item', var.get('errorMessages').get(var.get('i')))
        var.get('arErrors').callprop('push', Js('<a href="#" class="asm_error">'))
        var.get('arErrors').callprop('push', ((Js(1.0)+var.get('item').get('lineNumber'))+Js('行目')))
        var.get('arErrors').callprop('push', Js('</a>'))
        var.get('arErrors').callprop('push', var.get('enCER')((Js(' ')+var.get('item').get('message'))))
        var.get('arErrors').callprop('push', Js('<br />'))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('top').get('conframe').get('document').callprop('getElementById', Js('errorlog')).put('innerHTML', var.get('arErrors').callprop('join', Js('')))
    var.get('installAsmErrorHandlers')()
    var.put('arOut', var.get('Array').create())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('arrayLines').get('length')):
        def PyJs_LONG_8_(var=var):
            return var.get('arOut').callprop('push', (((((((((((((((((((Js('<div ')+Js('id="line_'))+var.get('i'))+Js('" '))+Js('style="position:absolute; '))+Js('top:'))+(var.get('i')*var.get('lineHeight')))+Js('px; '))+Js('left:0px; '))+Js('width:'))+(var.get('lineHeight')*Js(100.0)))+Js('px; '))+Js('height:'))+var.get('lineHeight'))+Js('px; '))+Js('font-size: '))+(var.get('lineHeight')-Js(1.0)))+Js('px;'))+Js('overflow: hidden; '))+Js('">')))
        PyJs_LONG_8_()
        var.put('lineAddr', var.get('addressTable').get(var.get('i')))
        if ((var.get('lineAddr')>=Js(0.0)) and var.get('nonExecutableTable').get(var.get('i')).neg()):
            var.get('arOut').callprop('push', ((Js('<span id="line_addr_')+var.get('hex4')(var.get('lineAddr')))+Js('">')))
        if ((var.get('lineAddr')>=Js(0.0)) and var.get('nonExecutableTable').get(var.get('i')).neg()):
            var.get('arOut').callprop('push', ((Js('<a href="#" class="addr" id="addr_addr_')+var.get('hex4')(var.get('lineAddr')))+Js('">')))
            var.get('arOut').callprop('push', ((Js('<span style="color: #804000; " class="addr_mark" id="addr_mark_')+var.get('hex4')(var.get('lineAddr')))+Js('">\u3000</span>')))
            var.get('arOut').callprop('push', var.get('hex4')(var.get('lineAddr')))
            var.get('arOut').callprop('push', Js('</a>'))
        else:
            if (var.get('lineAddr')>=Js(0.0)):
                var.get('arOut').callprop('push', (Js('\u3000')+var.get('hex4')(var.get('lineAddr'))))
            else:
                var.get('arOut').callprop('push', Js('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'))
        var.get('arOut').callprop('push', Js('&nbsp;'))
        var.put('str', var.get('arrayLines').get(var.get('i')))
        var.put('len', var.get('str').get('length'))
        var.put('n', var.get('endColTable').get(var.get('i')))
        if ((var.get('n')>=Js(0.0)) and (var.get('n')<var.get('len'))):
            var.get('arOut').callprop('push', var.get('enCER')(var.get('str').callprop('substring', Js(0.0), var.get('n'))))
            var.get('arOut').callprop('push', Js('<span style="color:#008000">'))
            var.get('arOut').callprop('push', var.get('enCER')(var.get('str').callprop('substring', var.get('n'))))
            var.get('arOut').callprop('push', Js('</span>'))
        else:
            var.get('arOut').callprop('push', var.get('enCER')(var.get('arrayLines').get(var.get('i'))))
        if ((var.get('lineAddr')>=Js(0.0)) and var.get('nonExecutableTable').get(var.get('i')).neg()):
            var.get('arOut').callprop('push', Js('</span>'))
        var.get('arOut').callprop('push', Js('</div>'))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('top').get('progframe').get('document').callprop('getElementById', Js('progblock')).put('innerHTML', var.get('arOut').callprop('join', Js('')))
    var.get('installBreakPointHandlers')()
    if (var.get('entryPoint')<Js(0.0)):
        var.get('alert')(Js('ソースプログラムがありません。'))
        return (-Js(1.0))
    return var.get('nErrors')
PyJsHoisted_assemble_.func_name = 'assemble'
var.put('assemble', PyJsHoisted_assemble_)
@Js
def PyJsHoisted_assembleOneLine_(parsedLine, this, arguments, var=var):
    var = Scope({'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedLine', 'aiTableItem'])
    if (var.get('parsedLine').get('inst')==Js('')):
        var.get('logError')(var.get('lineNumber'), Js('命令がありません'))
        return var.get('undefined')
    var.put('aiTableItem', var.get('aITable').get(var.get('parsedLine').get('inst')))
    if var.get('aiTableItem').neg():
        var.get('logError')(var.get('lineNumber'), (Js('命令欄が不正です - ')+var.get('parsedLine').get('inst')))
        return var.get('undefined')
    if (var.get('parsedLine').get('inst')==Js('START')):
        var.get('aiTableItem').callprop('callFnc', var.get('parsedLine'))
    else:
        if (var.get('parsedLine').get('inst')==Js('END')):
            var.get('aiTableItem').callprop('callFnc', var.get('parsedLine'))
        else:
            if (var.get('startLabel')==var.get(u"null")):
                var.get('logError')(var.get('lineNumber'), Js('STARTがありません'))
                var.get('processStart')(Js(''), Js(''))
            if (var.get('parsedLine').get('label')!=Js('')):
                var.get('defineLabel')(var.get('parsedLine').get('label'))
            var.get('aiTableItem').callprop('callFnc', var.get('parsedLine'))
PyJsHoisted_assembleOneLine_.func_name = 'assembleOneLine'
var.put('assembleOneLine', PyJsHoisted_assembleOneLine_)
@Js
def PyJsHoisted_alStart_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'label', 'parsedLine', 'operand'])
    if (var.get('startLabel')!=var.get(u"null")):
        var.get('logError')(var.get('lineNumber'), Js('END命令がありません'))
        var.get('processEnd')()
    var.put('label', Js(''))
    var.put('operand', Js(''))
    if (var.get('parsedLine').get('label')==Js('')):
        var.get('logError')(var.get('lineNumber'), Js('START命令にはラベルが必要です'))
        var.put('label', Js(''))
    else:
        if var.get('isLabel')(var.get('parsedLine').get('label')):
            var.put('label', var.get('parsedLine').get('label'))
    if (var.get('parsedLine').get('operands').get('length')>=Js(1.0)):
        if var.get('isLabel')(var.get('parsedLine').get('operands').get('0')):
            var.put('operand', var.get('parsedLine').get('operands').get('0'))
        else:
            var.get('logError')(var.get('lineNumber'), (Js('オペランドが不正です - ')+var.get('parsedLine').get('operands').get('0')))
        if (var.get('parsedLine').get('operands').get('length')>Js(1.0)):
            var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('processStart')(var.get('label'), var.get('operand'))
PyJsHoisted_alStart_.func_name = 'alStart'
var.put('alStart', PyJsHoisted_alStart_)
@Js
def PyJsHoisted_processStart_(label, operand, this, arguments, var=var):
    var = Scope({'label':label, 'operand':operand, 'this':this, 'arguments':arguments}, var)
    var.registers(['label', 'operand'])
    var.put('startLabel', var.get('label'))
    var.put('startLocation', var.get('locationCounter'))
    var.put('startOperand', var.get('operand'))
    var.put('startLine', var.get('lineNumber'))
    var.get('nonExecutableTable').put(var.get('lineNumber'), Js(True))
    var.put('localLabelTable', var.get('Object').create())
PyJsHoisted_processStart_.func_name = 'processStart'
var.put('processStart', PyJsHoisted_processStart_)
@Js
def PyJsHoisted_alEnd_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine'])
    if (var.get('startLabel')==var.get(u"null")):
        var.get('logError')(var.get('lineNumber'), Js('END命令が余計です'))
        return var.get('undefined')
    if (var.get('parsedLine').get('label')!=Js('')):
        var.get('logError')(var.get('lineNumber'), Js('END命令にはラベルはつけられません'))
    if (var.get('parsedLine').get('operands').get('length')!=Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('processEnd')()
PyJsHoisted_alEnd_.func_name = 'alEnd'
var.put('alEnd', PyJsHoisted_alEnd_)
@Js
def PyJsHoisted_processEnd_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['item', 'itemname', 'i'])
    for PyJsTemp in var.get('localLabelTable'):
        var.put('itemname', PyJsTemp)
        var.put('item', var.get('localLabelTable').get(var.get('itemname')))
        if (var.get('itemname').callprop('charAt', Js(0.0))==Js('=')):
            var.get('defineLabel')(var.get('itemname'))
            var.get('allocConstant')(var.get('itemname').callprop('substring', Js(1.0)))
    if (var.get('startLabel')!=Js('')):
        var.get('defineLabelSub')(var.get('localLabelTable'), var.get('startLabel'), var.get('startLocation'), var.get('startLine'))
        if (var.get('startOperand')!=Js('')):
            var.put('item', var.get('localLabelTable').get(var.get('startOperand')))
            if (var.get('item') and (var.get('item').get('value')>=Js(0.0))):
                var.put('startLocation', var.get('item').get('value'))
                var.get('localLabelTable').get(var.get('startLabel')).put('value', var.get('item').get('value'))
            else:
                var.get('logError')(var.get('startLine'), (Js('未定義です - ')+var.get('startOperand')))
        var.get('addressTable').put(var.get('startLine'), var.get('startLocation'))
        var.get('defineGlobalLabel')(var.get('startLabel'), var.get('startLocation'), var.get('startLine'))
        if (var.get('entryPoint')<Js(0.0)):
            var.put('entryPoint', var.get('startLocation'))
    for PyJsTemp in var.get('localLabelTable'):
        var.put('itemname', PyJsTemp)
        var.put('item', var.get('localLabelTable').get(var.get('itemname')))
        if (var.get('item').get('value')<Js(0.0)):
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('item').get('refAddr').get('length')):
                var.get('referGlobalLabel')(var.get('itemname'), var.get('item').get('refAddr').get(var.get('i')), var.get('item').get('refLine').get(var.get('i')))
                # update
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        else:
            if var.get('item').get('multiDefined'):
                var.get('logError')(var.get('item').get('defLine'), (Js('多重定義されています - ')+var.get('itemname')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('item').get('refLine').get('length')):
                    var.get('logError')(var.get('item').get('refLine').get(var.get('i')), (Js('多重定義ラベルを参照しています - ')+var.get('itemname')))
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            else:
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('item').get('refAddr').get('length')):
                    var.get('objectcode').put(var.get('item').get('refAddr').get(var.get('i')), var.get('item').get('value'))
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('startLabel', var.get(u"null"))
    var.put('startOperand', var.get(u"null"))
    var.put('startLine', (-Js(1.0)))
PyJsHoisted_processEnd_.func_name = 'processEnd'
var.put('processEnd', PyJsHoisted_processEnd_)
@Js
def PyJsHoisted_resolveGlobalReferences_(entryPointName, this, arguments, var=var):
    var = Scope({'entryPointName':entryPointName, 'this':this, 'arguments':arguments}, var)
    var.registers(['item', 'entryPointName', 'itemname', 'i'])
    for PyJsTemp in var.get('globalLabelTable'):
        var.put('itemname', PyJsTemp)
        var.put('item', var.get('globalLabelTable').get(var.get('itemname')))
        if (var.get('item').get('value')<Js(0.0)):
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('item').get('refLine').get('length')):
                var.get('logError')(var.get('item').get('refLine').get(var.get('i')), (Js('未定義です - ')+var.get('itemname')))
                # update
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        else:
            if var.get('item').get('multiDefined'):
                var.get('logError')(var.get('item').get('defLine'), (Js('多重定義されています - ')+var.get('itemname')))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('item').get('refLine').get('length')):
                    var.get('logError')(var.get('item').get('refLine').get(var.get('i')), (Js('多重定義ラベルを参照しています - ')+var.get('itemname')))
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            else:
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('item').get('refAddr').get('length')):
                    var.get('objectcode').put(var.get('item').get('refAddr').get(var.get('i')), var.get('item').get('value'))
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('entryPointName')!=Js('')):
        var.put('item', var.get('globalLabelTable').get(var.get('entryPointName').callprop('toUpperCase')))
        if (var.get('item').neg() or (var.get('item').get('value')<Js(0.0))):
            var.get('alert')(((Js('実行開始ラベル欄で指定された')+var.get('entryPointName'))+Js('がプログラム中に存在しません')))
        if var.get('item'):
            var.put('entryPoint', var.get('item').get('value'))
PyJsHoisted_resolveGlobalReferences_.func_name = 'resolveGlobalReferences'
var.put('resolveGlobalReferences', PyJsHoisted_resolveGlobalReferences_)
@Js
def PyJsHoisted_alNone_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine'])
    if (var.get('parsedLine').get('operands').get('length')!=Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), (var.get('code')<<Js(8.0)))
PyJsHoisted_alNone_.func_name = 'alNone'
var.put('alNone', PyJsHoisted_alNone_)
@Js
def PyJsHoisted_alRM_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine'])
    var.get('alRMR2')(var.get('code'), var.get('parsedLine'), Js(False))
PyJsHoisted_alRM_.func_name = 'alRM'
var.put('alRM', PyJsHoisted_alRM_)
@Js
def PyJsHoisted_alRMR_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine'])
    var.get('alRMR2')(var.get('code'), var.get('parsedLine'), Js(True))
PyJsHoisted_alRMR_.func_name = 'alRMR'
var.put('alRMR', PyJsHoisted_alRMR_)
@Js
def PyJsHoisted_alRMR2_(code, parsedLine, rrOK, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'rrOK':rrOK, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine', 'gr', 'addr', 'xr', 'rrOK'])
    var.put('gr', Js(0.0))
    var.put('addr', Js(0.0))
    var.put('xr', Js(0.0))
    if (var.get('parsedLine').get('operands').get('length')<Js(2.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドの数が不足です'))
    else:
        var.put('gr', var.get('getGRCheck')(var.get('parsedLine').get('operands').get('0')))
        if var.get('rrOK'):
            var.put('gr2', var.get('getGR')(var.get('parsedLine').get('operands').get('1')))
            if (var.get('gr2')>=Js(0.0)):
                var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
                var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), ((((var.get('code')|Js(4))<<Js(8.0))|(var.get('gr')<<Js(4.0)))|var.get('gr2')))
                return var.get('undefined')
        var.put('addr', var.get('getAddrCheck')(var.get('parsedLine').get('operands').get('1')))
        var.put('xr', var.get('getXRCheck')(var.get('parsedLine').get('operands'), Js(2.0)))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), (((var.get('code')<<Js(8.0))|(var.get('gr')<<Js(4.0)))|var.get('xr')))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('addr'))
PyJsHoisted_alRMR2_.func_name = 'alRMR2'
var.put('alRMR2', PyJsHoisted_alRMR2_)
@Js
def PyJsHoisted_alM_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'xr', 'parsedLine', 'addr'])
    var.put('addr', Js(0.0))
    var.put('xr', Js(0.0))
    if (var.get('parsedLine').get('operands').get('length')<Js(1.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドの数が不足です'))
    else:
        var.put('addr', var.get('getAddrCheck')(var.get('parsedLine').get('operands').get('0')))
        var.put('xr', var.get('getXRCheck')(var.get('parsedLine').get('operands'), Js(1.0)))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), ((var.get('code')<<Js(8.0))|var.get('xr')))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('addr'))
PyJsHoisted_alM_.func_name = 'alM'
var.put('alM', PyJsHoisted_alM_)
@Js
def PyJsHoisted_alR_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'parsedLine', 'gr'])
    var.put('gr', Js(0.0))
    if (var.get('parsedLine').get('operands').get('length')<Js(1.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドの数が不足です'))
    else:
        var.put('gr', var.get('getGRCheck')(var.get('parsedLine').get('operands').get('0')))
        if (var.get('parsedLine').get('operands').get('length')>Js(1.0)):
            var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), ((var.get('code')<<Js(8.0))|(var.get('gr')<<Js(4.0))))
PyJsHoisted_alR_.func_name = 'alR'
var.put('alR', PyJsHoisted_alR_)
@Js
def PyJsHoisted_alDS_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'str', 'parsedLine', 'count'])
    var.put('count', Js(0.0))
    if (var.get('parsedLine').get('operands').get('length')!=Js(1.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドの数が不正です'))
    else:
        var.put('str', var.get('parsedLine').get('operands').get('0'))
        if var.get('str').callprop('match', JsRegExp('/^[0-9]+$/')):
            var.put('count', (var.get('str')-Js(0.0)))
        else:
            var.get('logError')(var.get('lineNumber'), (Js('オペランドが不正です - ')+var.get('str')))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('nonExecutableTable').put(var.get('lineNumber'), Js(True))
    var.put('locationCounter', var.get('count'), '+')
PyJsHoisted_alDS_.func_name = 'alDS'
var.put('alDS', PyJsHoisted_alDS_)
@Js
def PyJsHoisted_alDC_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'str', 'i', 'parsedLine'])
    if (var.get('parsedLine').get('operands').get('length')==Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドがありません'))
    else:
        var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
        var.get('nonExecutableTable').put(var.get('lineNumber'), Js(True))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('parsedLine').get('operands').get('length')):
            var.put('str', var.get('parsedLine').get('operands').get(var.get('i')))
            if (var.get('str').get('length')==Js(0.0)):
                var.get('logError')(var.get('lineNumber'), Js('オペランドが不正です'))
            else:
                if var.get('allocConstant')(var.get('str')).neg():
                    var.get('logError')(var.get('lineNumber'), (Js('オペランドが不正です - ')+var.get('str')))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_alDC_.func_name = 'alDC'
var.put('alDC', PyJsHoisted_alDC_)
@Js
def PyJsHoisted_allocConstant_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'str', 'val', 'ar'])
    var.put('val', Js(0.0))
    if var.get('isLabel')(var.get('str')):
        var.get('referLabel')(var.get('str'), var.get('locationCounter'))
    else:
        var.put('val', var.get('getDec')(var.get('str')))
        if (var.get('val')<Js(0.0)):
            var.put('val', var.get('getHex')(var.get('str')))
    if (var.get('val')>=Js(0.0)):
        var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('val'))
        return Js(True)
    var.put('ar', var.get('getStr')(var.get('str')))
    if var.get('ar'):
        #for JS loop
        var.put('j', Js(0.0))
        while (var.get('j')<var.get('ar').get('length')):
            var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('ar').get(var.get('j')))
            # update
            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        return Js(True)
    return Js(False)
PyJsHoisted_allocConstant_.func_name = 'allocConstant'
var.put('allocConstant', PyJsHoisted_allocConstant_)
@Js
def PyJsHoisted_alInOut_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'addr2', 'addr1', 'parsedLine'])
    if (var.get('parsedLine').get('operands').get('length')!=Js(2.0)):
        var.get('logError')(var.get('lineNumber'), Js('オペランドの数が不正です'))
        return var.get('undefined')
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(28673))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(0))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(28674))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(0))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.put('addr1', var.get('getAddrCheck')(var.get('parsedLine').get('operands').get('0')))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(4624))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('addr1'))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.put('addr2', var.get('getAddrCheck')(var.get('parsedLine').get('operands').get('1')))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(4640))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('addr2'))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(61440))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), var.get('code'))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(28960))
    var.get('macroFlag').callprop('set', var.get('locationCounter'))
    var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(28944))
PyJsHoisted_alInOut_.func_name = 'alInOut'
var.put('alInOut', PyJsHoisted_alInOut_)
@Js
def PyJsHoisted_alRPush_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'i', 'parsedLine'])
    if (var.get('parsedLine').get('operands').get('length')!=Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    #for JS loop
    var.put('i', Js(1.0))
    while (var.get('i')<=Js(7.0)):
        if (var.get('i')!=Js(1.0)):
            var.get('macroFlag').callprop('set', var.get('locationCounter'))
        var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), (Js(28672)+var.get('i')))
        var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), Js(0))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_alRPush_.func_name = 'alRPush'
var.put('alRPush', PyJsHoisted_alRPush_)
@Js
def PyJsHoisted_alRPop_(code, parsedLine, this, arguments, var=var):
    var = Scope({'code':code, 'parsedLine':parsedLine, 'this':this, 'arguments':arguments}, var)
    var.registers(['code', 'i', 'parsedLine'])
    if (var.get('parsedLine').get('operands').get('length')!=Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    var.get('addressTable').put(var.get('lineNumber'), var.get('locationCounter'))
    #for JS loop
    var.put('i', Js(7.0))
    while (var.get('i')>=Js(1.0)):
        if (var.get('i')!=Js(7.0)):
            var.get('macroFlag').callprop('set', var.get('locationCounter'))
        var.get('objectcode').put((var.put('locationCounter',Js(var.get('locationCounter').to_number())+Js(1))-Js(1)), (Js(28928)+(var.get('i')<<Js(4.0))))
        # update
        (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
PyJsHoisted_alRPop_.func_name = 'alRPop'
var.put('alRPop', PyJsHoisted_alRPop_)
@Js
def PyJsHoisted_isSpace_(ch, this, arguments, var=var):
    var = Scope({'ch':ch, 'this':this, 'arguments':arguments}, var)
    var.registers(['ch'])
    if (var.get('ch')<=Js(' ')):
        return Js(True)
    else:
        return Js(False)
PyJsHoisted_isSpace_.func_name = 'isSpace'
var.put('isSpace', PyJsHoisted_isSpace_)
@Js
def PyJsHoisted_Token_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('indexNext', Js(0.0))
    var.get(u"this").put('token', Js(''))
    @Js
    def PyJs_anonymous_9_(str, this, arguments, var=var):
        var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
        var.registers(['start', 'inQuote', 'ar', 'n', 'str', 'ch'])
        var.put('n', var.get(u"this").get('indexNext'))
        if (var.get('n')>=var.get('str').get('length')):
            return Js(False)
        var.put('ch', var.get('str').callprop('charAt', var.get('n')))
        if (var.get('ch')==Js(';')):
            return Js(False)
        if (var.get('ch')==Js(',')):
            var.get(u"this").put('token', Js(','))
            var.get(u"this").put('indexNext', (var.get('n')+Js(1.0)))
            return Js(True)
        if var.get('isSpace')(var.get('ch')):
            (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
            while (var.get('n')<var.get('str').get('length')):
                var.put('ch', var.get('str').callprop('charAt', var.get('n')))
                if var.get('isSpace')(var.get('ch')).neg():
                    break
                (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
            var.get(u"this").put('token', Js(' '))
            var.get(u"this").put('indexNext', var.get('n'))
            return Js(True)
        var.put('start', var.get('n'))
        var.put('inQuote', Js(False))
        var.put('ar', var.get('Array').create())
        while (var.get('n')<var.get('str').get('length')):
            var.put('ch', var.get('str').callprop('charAt', var.get('n')))
            if var.get('inQuote'):
                if (var.get('ch')==Js("'")):
                    var.put('inQuote', Js(False))
                var.get('ar').callprop('push', var.get('ch'))
            else:
                if (var.get('ch')==Js("'")):
                    var.put('inQuote', Js(True))
                else:
                    if var.get('isSpace')(var.get('ch')):
                        break
                    else:
                        if (var.get('ch')==Js(';')):
                            break
                        else:
                            if (var.get('ch')==Js(',')):
                                break
                var.get('ar').callprop('push', var.get('ch').callprop('toUpperCase'))
            (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
        var.get(u"this").put('token', var.get('ar').callprop('join', Js('')))
        var.get(u"this").put('indexNext', var.get('n'))
        return Js(True)
    PyJs_anonymous_9_._set_name('anonymous')
    var.get(u"this").put('getToken', PyJs_anonymous_9_)
PyJsHoisted_Token_.func_name = 'Token'
var.put('Token', PyJsHoisted_Token_)
@Js
def PyJsHoisted_isLabel_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    if var.get('str').callprop('match', JsRegExp('/^[A-Z][A-Z0-9]{0,7}$/')):
        if (var.get('getGR')(var.get('str'))<Js(0.0)):
            return Js(True)
    return Js(False)
PyJsHoisted_isLabel_.func_name = 'isLabel'
var.put('isLabel', PyJsHoisted_isLabel_)
@Js
def PyJsHoisted_parseLine_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'parsedLine', 'token', 'label'])
    var.put('parsedLine', var.get('ParsedLine').create())
    var.put('token', var.get('Token').create())
    if var.get('token').callprop('getToken', var.get('str')).neg():
        var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
        return var.get('parsedLine')
    if (var.get('token').get('token')!=Js(' ')):
        var.put('label', var.get('token').get('token'))
        var.get('parsedLine').put('label', var.get('label'))
        if var.get('token').callprop('getToken', var.get('str')).neg():
            var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
            return var.get('parsedLine')
    if (var.get('token').get('token')!=Js(' ')):
        var.get('logError')(var.get('lineNumber'), (Js('文法エラーです - ')+var.get('token').get('token')))
        return var.get('parsedLine')
    if var.get('token').callprop('getToken', var.get('str')).neg():
        var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
        return var.get('parsedLine')
    var.get('parsedLine').put('inst', var.get('token').get('token'))
    if var.get('token').callprop('getToken', var.get('str')).neg():
        var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
        return var.get('parsedLine')
    if (var.get('token').get('token')!=Js(' ')):
        var.get('logError')(var.get('lineNumber'), (Js('文法エラーです - ')+var.get('token').get('token')))
        return var.get('parsedLine')
    if var.get('token').callprop('getToken', var.get('str')).neg():
        var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
        return var.get('parsedLine')
    var.get('parsedLine').get('operands').callprop('push', var.get('token').get('token'))
    while Js(True):
        if var.get('token').callprop('getToken', var.get('str')).neg():
            var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
            return var.get('parsedLine')
        if (var.get('token').get('token')==Js(' ')):
            var.get('parsedLine').put('endcol', var.get('token').get('indexNext'))
            return var.get('parsedLine')
        if (var.get('token').get('token')!=Js(',')):
            var.get('logError')(var.get('lineNumber'), (Js('文法エラーです - ')+var.get('token').get('token')))
            return var.get('parsedLine')
        if ((var.get('token').callprop('getToken', var.get('str')).neg() or (var.get('token').get('token')==Js(' '))) or (var.get('token').get('token')==Js(','))):
            var.get('logError')(var.get('lineNumber'), Js('文法エラーです - ,'))
            return var.get('parsedLine')
        var.get('parsedLine').get('operands').callprop('push', var.get('token').get('token'))
PyJsHoisted_parseLine_.func_name = 'parseLine'
var.put('parseLine', PyJsHoisted_parseLine_)
@Js
def PyJsHoisted_getGR_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'ch'])
    if ((var.get('str').get('length')==Js(3.0)) and (var.get('str').callprop('substring', Js(0.0), Js(2.0))==Js('GR'))):
        var.put('ch', var.get('str').callprop('charAt', Js(2.0)))
        if ((var.get('ch')>=Js('0')) and (var.get('ch')<=Js('7'))):
            return (var.get('ch')-Js(0.0))
    return (-Js(1.0))
PyJsHoisted_getGR_.func_name = 'getGR'
var.put('getGR', PyJsHoisted_getGR_)
@Js
def PyJsHoisted_getGRCheck_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'gr'])
    var.put('gr', var.get('getGR')(var.get('str')))
    if (var.get('gr')>=Js(0.0)):
        return var.get('gr')
    var.get('logError')(var.get('lineNumber'), (Js('GRの指定が不正です - ')+var.get('str')))
    return Js(0.0)
PyJsHoisted_getGRCheck_.func_name = 'getGRCheck'
var.put('getGRCheck', PyJsHoisted_getGRCheck_)
@Js
def PyJsHoisted_getXRCheck_(operands, n, this, arguments, var=var):
    var = Scope({'operands':operands, 'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'xr', 'operands'])
    var.put('xr', Js(0.0))
    if (var.get('operands').get('length')>var.get('n')):
        var.put('xr', var.get('getGR')(var.get('operands').get(var.get('n'))))
        if (var.get('xr')<=Js(0.0)):
            var.get('logError')(var.get('lineNumber'), (Js('指標レジスタの指定が不正です - ')+var.get('operands').get(var.get('n'))))
            var.put('xr', Js(0.0))
    if (var.get('operands').get('length')>(var.get('n')+Js(1.0))):
        var.get('logError')(var.get('lineNumber'), Js('余計なオペランドがあります'))
    return var.get('xr')
PyJsHoisted_getXRCheck_.func_name = 'getXRCheck'
var.put('getXRCheck', PyJsHoisted_getXRCheck_)
@Js
def PyJsHoisted_getAddrCheck_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str1', 'str', 'val'])
    if (var.get('str').get('length')==Js(0.0)):
        var.get('logError')(var.get('lineNumber'), Js('ADDRの指定がありません'))
        return Js(0.0)
    if var.get('isLabel')(var.get('str')):
        var.get('referLabel')(var.get('str'), (var.get('locationCounter')+Js(1.0)))
        return Js(0.0)
    if (var.get('str').callprop('charAt', Js(0.0))==Js('=')):
        if (var.get('str').get('length')==Js(1.0)):
            var.get('logError')(var.get('lineNumber'), Js('リテラル定数の指定がありません'))
            return Js(0.0)
        var.put('str1', var.get('str').callprop('substring', Js(1.0)))
        if (((var.get('getDec')(var.get('str1'))>=Js(0.0)) or (var.get('getHex')(var.get('str1'))>=Js(0.0))) or (var.get('getStr')(var.get('str1'))!=var.get(u"null"))):
            var.get('referLabel')(var.get('str'), (var.get('locationCounter')+Js(1.0)))
            return Js(0.0)
        var.get('logError')(var.get('lineNumber'), (Js('リテラルの指定が不正です - ')+var.get('str')))
        return Js(0.0)
    var.put('val', var.get('getDec')(var.get('str')))
    if (var.get('val')>=Js(0.0)):
        return var.get('val')
    var.put('val', var.get('getHex')(var.get('str')))
    if (var.get('val')>=Js(0.0)):
        return var.get('val')
    var.get('logError')(var.get('lineNumber'), (Js('オペランドの指定が不正です - ')+var.get('str')))
    return Js(0.0)
PyJsHoisted_getAddrCheck_.func_name = 'getAddrCheck'
var.put('getAddrCheck', PyJsHoisted_getAddrCheck_)
@Js
def PyJsHoisted_getDec_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    if var.get('str').callprop('match', JsRegExp('/^[+-]?[0-9]+$/')):
        return ((var.get('str')-Js(0.0))&Js(65535))
    return (-Js(1.0))
PyJsHoisted_getDec_.func_name = 'getDec'
var.put('getDec', PyJsHoisted_getDec_)
@Js
def PyJsHoisted_getHex_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str'])
    if var.get('str').callprop('match', JsRegExp('/^#[0-9A-Fa-f]+$/')):
        return (var.get('parseInt')(var.get('str').callprop('substring', Js(1.0)), Js(16.0))&Js(65535))
    return (-Js(1.0))
PyJsHoisted_getHex_.func_name = 'getHex'
var.put('getHex', PyJsHoisted_getHex_)
@Js
def PyJsHoisted_getStr_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['arCharCode', 'i', 'jis8', 'str'])
    if (var.get('str').get('length')<Js(2.0)):
        return var.get(u"null")
    if (var.get('str').callprop('charAt', Js(0.0))!=Js("'")):
        return var.get(u"null")
    if (var.get('str').callprop('charAt', (var.get('str').get('length')-Js(1.0)))!=Js("'")):
        return var.get(u"null")
    var.put('arCharCode', var.get('Array').create())
    #for JS loop
    var.put('i', Js(1.0))
    while (var.get('i')<(var.get('str').get('length')-Js(1.0))):
        var.put('ch', var.get('str').callprop('charAt', var.get('i')))
        if (var.get('ch')==Js("'")):
            if ((var.get('i')<(var.get('str').get('length')-Js(1.0))) and (var.get('str').callprop('charAt', (var.get('i')+Js(1.0)))==Js("'"))):
                var.get('arCharCode').callprop('push', var.get('ch').callprop('charCodeAt', Js(0.0)))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            else:
                return var.get(u"null")
        else:
            var.put('jis8', var.get('charCodeToJis8')(var.get('str').callprop('charCodeAt', var.get('i'))))
            if (var.get('jis8')>=Js(0.0)):
                var.get('arCharCode').callprop('push', var.get('jis8'))
            else:
                var.get('arCharCode').callprop('push', Js('?').callprop('charCodeAt', Js(0.0)))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('arCharCode')
PyJsHoisted_getStr_.func_name = 'getStr'
var.put('getStr', PyJsHoisted_getStr_)
@Js
def PyJsHoisted_logError_(lineNumber, message, this, arguments, var=var):
    var = Scope({'lineNumber':lineNumber, 'message':message, 'this':this, 'arguments':arguments}, var)
    var.registers(['message', 'lineNumber'])
    var.get('errorMessages').callprop('push', var.get('ErrorItem').create(var.get('lineNumber'), var.get('message')))
PyJsHoisted_logError_.func_name = 'logError'
var.put('logError', PyJsHoisted_logError_)
@Js
def PyJsHoisted_installAsmErrorHandlers_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'ar', 'elem'])
    var.put('ar', var.get('top').get('conframe').get('document').callprop('getElementsByTagName', Js('a')))
    if var.get('ar'):
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('ar').get('length')):
            var.put('elem', var.get('ar').get(var.get('i')))
            if (var.get('elem').get('className')==Js('asm_error')):
                var.get('addEvent')(var.get('elem'), Js('click'), var.get('onClickedError'))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_installAsmErrorHandlers_.func_name = 'installAsmErrorHandlers'
var.put('installAsmErrorHandlers', PyJsHoisted_installAsmErrorHandlers_)
@Js
def PyJsHoisted_onClickedError_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'e', 'elem', 'line'])
    var.put('elem', var.get('getEventTarget')(var.get('e')))
    if var.get('elem'):
        var.put('str', var.get('elem').get('innerHTML').callprop('match', JsRegExp('/[0-9]+/')))
        if var.get('str'):
            var.put('line', (var.get('str')-Js(1.0)))
            if (var.get('errorShown')>=Js(0.0)):
                var.put('e', var.get('top').get('progframe').get('document').callprop('getElementById', (Js('line_')+var.get('errorShown'))))
                if var.get('e'):
                    var.get('e').get('style').put('backgroundColor', Js('#FFFFFF'))
            var.put('e', var.get('top').get('progframe').get('document').callprop('getElementById', (Js('line_')+var.get('line'))))
            if var.get('e'):
                var.get('e').get('style').put('backgroundColor', Js('#FFC0C0'))
                var.put('errorShown', var.get('line'))
        var.get('scrollProgToShowLine')(var.get('line'))
    var.get('preventDefault')(var.get('e'))
    return Js(False)
PyJsHoisted_onClickedError_.func_name = 'onClickedError'
var.put('onClickedError', PyJsHoisted_onClickedError_)
@Js
def PyJsHoisted_installBreakPointHandlers_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'ar', 'elem'])
    var.put('ar', var.get('top').get('progframe').get('document').callprop('getElementsByTagName', Js('a')))
    if var.get('ar'):
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('ar').get('length')):
            var.put('elem', var.get('ar').get(var.get('i')))
            if (var.get('elem').get('className')==Js('addr')):
                var.get('addEvent')(var.get('elem'), Js('click'), var.get('onClickedBreakPoint'))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_installBreakPointHandlers_.func_name = 'installBreakPointHandlers'
var.put('installBreakPointHandlers', PyJsHoisted_installBreakPointHandlers_)
@Js
def PyJsHoisted_onClickedBreakPoint_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['elem2', 'addr', 'str', 'elem', 'e'])
    var.put('elem', var.get('getEventTarget')(var.get('e')))
    if var.get('elem'):
        var.put('elem2', var.get('top').get('progframe').get('document').callprop('getElementById', (Js('addr_mark_')+var.get('elem').get('id').callprop('substring', Js(10.0)))))
        var.put('addr', var.get('parseInt')(var.get('elem').get('id').callprop('substring', Js(10.0)), Js(16.0)))
        var.put('str', var.get('elem2').get('innerHTML'))
        if (var.get('str')==Js('\u3000')):
            var.get('elem2').put('innerHTML', Js('●'))
            var.get('breakPointData').callprop('set', var.get('addr'))
        else:
            var.get('elem2').put('innerHTML', Js('\u3000'))
            var.get('breakPointData').callprop('clear', var.get('addr'))
    var.get('enableElement')(Js('button_clear_break'), var.get('breakPointData').callprop('getCount'))
    var.get('preventDefault')(var.get('e'))
    return Js(False)
PyJsHoisted_onClickedBreakPoint_.func_name = 'onClickedBreakPoint'
var.put('onClickedBreakPoint', PyJsHoisted_onClickedBreakPoint_)
@Js
def PyJsHoisted_clearAllBreakPoints_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'ar', 'elem'])
    var.put('ar', var.get('top').get('progframe').get('document').callprop('getElementsByTagName', Js('span')))
    if var.get('ar'):
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('ar').get('length')):
            var.put('elem', var.get('ar').get(var.get('i')))
            if (var.get('elem').get('className')==Js('addr_mark')):
                var.get('elem').put('innerHTML', Js('\u3000'))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('breakPointData').callprop('initialize')
    var.get('enableElement')(Js('button_clear_break'), var.get('breakPointData').callprop('getCount'))
PyJsHoisted_clearAllBreakPoints_.func_name = 'clearAllBreakPoints'
var.put('clearAllBreakPoints', PyJsHoisted_clearAllBreakPoints_)
@Js
def PyJsHoisted_setState_(state, this, arguments, var=var):
    var = Scope({'state':state, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'errorlog', 'console', 'state', 'r'])
    var.get('enableButton')(Js('go'), ((var.get('state')==var.get('STATE_UNSTARTED')) or (var.get('state')==var.get('STATE_BREAK'))))
    var.get('enableButton')(Js('pause'), (var.get('state')==var.get('STATE_RUNNING')))
    var.get('enableButton')(Js('stepin'), ((var.get('state')==var.get('STATE_UNSTARTED')) or (var.get('state')==var.get('STATE_BREAK'))))
    var.get('enableButton')(Js('stepover'), (var.get('state')==var.get('STATE_BREAK')))
    var.get('enableButton')(Js('stepout'), (var.get('state')==var.get('STATE_BREAK')))
    var.get('enableElement')(Js('button_stop'), ((var.get('state')==var.get('STATE_BREAK')) or (var.get('state')==var.get('STATE_RUNNING'))))
    var.put('r', (var.get('state')==var.get('STATE_BREAK')).neg())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        var.get('setReadOnly')((Js('GR')+var.get('i')), var.get('r'))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('setReadOnly')(Js('PR'), var.get('r'))
    var.get('setReadOnly')(Js('SP'), var.get('r'))
    var.get('setReadOnly')(Js('ZF'), var.get('r'))
    var.get('setReadOnly')(Js('SF'), var.get('r'))
    var.get('setReadOnly')(Js('OF'), var.get('r'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        var.get('setReadOnly')((Js('mem_')+var.get('i')), var.get('r'))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('console', var.get('top').get('conframe').get('document').callprop('getElementById', Js('console')))
    var.put('errorlog', var.get('top').get('conframe').get('document').callprop('getElementById', Js('errorlog')))
    var.get('console').get('style').put('position', (Js('absolute') if (var.get('state')==var.get('STATE_NONE')) else Js('relative')))
    var.get('console').get('style').put('visibility', (Js('hidden') if (var.get('state')==var.get('STATE_NONE')) else Js('visible')))
    var.get('errorlog').get('style').put('position', (Js('relative') if (var.get('state')==var.get('STATE_NONE')) else Js('absolute')))
    var.get('errorlog').get('style').put('visibility', (Js('visible') if (var.get('state')==var.get('STATE_NONE')) else Js('hidden')))
    var.put('stateCurrent', var.get('state'))
PyJsHoisted_setState_.func_name = 'setState'
var.put('setState', PyJsHoisted_setState_)
@Js
def PyJsHoisted_enableButton_(id, enable, this, arguments, var=var):
    var = Scope({'id':id, 'enable':enable, 'this':this, 'arguments':arguments}, var)
    var.registers(['image', 'enable', 'src', 'id'])
    var.get('enableElement')((Js('button_')+var.get('id')), var.get('enable'))
    var.put('image', var.get('document').callprop('getElementById', (Js('buttonimage_')+var.get('id'))))
    var.put('src', ((Js('images/')+(var.get('id') if var.get('enable') else (var.get('id')+Js('_disabled'))))+Js('.gif')))
    if (var.get('image').get('src')!=var.get('src')):
        var.get('image').put('src', var.get('src'))
PyJsHoisted_enableButton_.func_name = 'enableButton'
var.put('enableButton', PyJsHoisted_enableButton_)
@Js
def PyJsHoisted_enableElement_(id, enable, this, arguments, var=var):
    var = Scope({'id':id, 'enable':enable, 'this':this, 'arguments':arguments}, var)
    var.registers(['enable', 'elem', 'disabled', 'id'])
    var.put('elem', var.get('document').callprop('getElementById', var.get('id')))
    var.put('disabled', (Js('') if var.get('enable') else Js('disabled')))
    if (var.get('elem').get('disabled')!=var.get('disabled')):
        var.get('elem').put('disabled', var.get('disabled'))
PyJsHoisted_enableElement_.func_name = 'enableElement'
var.put('enableElement', PyJsHoisted_enableElement_)
@Js
def PyJsHoisted_setReadOnly_(id, readonly, this, arguments, var=var):
    var = Scope({'id':id, 'readonly':readonly, 'this':this, 'arguments':arguments}, var)
    var.registers(['readonly', 'elem', 'id', 'readOnly'])
    var.put('elem', var.get('document').callprop('getElementById', var.get('id')))
    var.put('readOnly', (Js('readonly') if var.get('readonly') else Js('')))
    if (var.get('elem').get('readOnly')!=var.get('readOnly')):
        var.get('elem').put('readOnly', var.get('readOnly'))
PyJsHoisted_setReadOnly_.func_name = 'setReadOnly'
var.put('setReadOnly', PyJsHoisted_setReadOnly_)
@Js
def PyJsHoisted_initializeRegMem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        var.get('gr').put(var.get('i'), Js(0.0))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('sp', var.get('spInit'))
    var.put('pr', var.get('entryPoint'))
    var.put('zf', var.put('sf', var.put('of', Js(0.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(65536.0)):
        var.get('mem').put(var.get('i'), var.get('objectcode').get(var.get('i')))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('top').get('progframe').callprop('scrollTo', Js(0.0), Js(0.0))
    var.put('consoleView', var.get('ConsoleView').create())
    var.put('sp', var.get('ea')(var.get('sp'), (-Js(1.0))))
    var.get('mem').put(var.get('sp'), var.get('spInit'))
    var.get('outputRegMem')()
PyJsHoisted_initializeRegMem_.func_name = 'initializeRegMem'
var.put('initializeRegMem', PyJsHoisted_initializeRegMem_)
@Js
def PyJsHoisted_outputRegMem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('outputReg')()
    var.get('outputMem')()
PyJsHoisted_outputRegMem_.func_name = 'outputRegMem'
var.put('outputRegMem', PyJsHoisted_outputRegMem_)
@Js
def PyJsHoisted_outputReg_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['fnc', 'i'])
    var.put('fnc', var.get('getRadix')(var.get('hex4'), var.get('unsignedDec'), var.get('signedDec')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        var.get('document').callprop('getElementById', (Js('GR')+var.get('i'))).put('value', var.get('fnc')(var.get('gr').get(var.get('i'))))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('document').callprop('getElementById', Js('SP')).put('value', var.get('fnc')(var.get('sp')))
    var.get('document').callprop('getElementById', Js('PR')).put('value', var.get('fnc')(var.get('pr')))
    var.get('document').callprop('getElementById', Js('ZF')).put('value', (Js('')+var.get('zf')))
    var.get('document').callprop('getElementById', Js('SF')).put('value', (Js('')+var.get('sf')))
    var.get('document').callprop('getElementById', Js('OF')).put('value', (Js('')+var.get('of')))
    var.get('markPR')()
PyJsHoisted_outputReg_.func_name = 'outputReg'
var.put('outputReg', PyJsHoisted_outputReg_)
@Js
def PyJsHoisted_outputMem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['fnc', 'i', 'addr'])
    var.put('address', var.get('parseInt')(var.get('document').callprop('getElementById', Js('address')).get('value'), Js(16.0)))
    if var.get('isNaN')(var.get('address')):
        var.put('address', Js(0.0))
    var.put('fnc', var.get('getRadix')(var.get('hex4'), var.get('unsignedDec'), var.get('signedDec')))
    var.put('addr', var.get('getAddress')())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        var.get('document').callprop('getElementById', (Js('addr_')+var.get('i'))).put('innerHTML', var.get('hex4')(var.get('ea')(var.get('addr'), var.get('i'))))
        # update
        var.put('i', Js(4.0), '+')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        var.get('document').callprop('getElementById', (Js('mem_')+var.get('i'))).put('value', var.get('fnc')(var.get('mem').get(var.get('ea')(var.get('addr'), var.get('i')))))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_outputMem_.func_name = 'outputMem'
var.put('outputMem', PyJsHoisted_outputMem_)
@Js
def PyJsHoisted_inputRegMem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('inputReg')()
    var.get('inputMem')()
PyJsHoisted_inputRegMem_.func_name = 'inputRegMem'
var.put('inputRegMem', PyJsHoisted_inputRegMem_)
@Js
def PyJsHoisted_inputReg_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['fnc', 'i'])
    var.put('fnc', var.get('getRadix')(var.get('fromHex'), var.get('fromDec'), var.get('fromDec')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(8.0)):
        var.get('gr').put(var.get('i'), var.get('fnc')(var.get('document').callprop('getElementById', (Js('GR')+var.get('i'))).get('value')))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('sp', var.get('fnc')(var.get('document').callprop('getElementById', Js('SP')).get('value')))
    var.put('pr', var.get('fnc')(var.get('document').callprop('getElementById', Js('PR')).get('value')))
    var.put('zf', (Js(1.0) if var.get('fromDec')(var.get('document').callprop('getElementById', Js('ZF')).get('value')) else Js(0.0)))
    var.put('sf', (Js(1.0) if var.get('fromDec')(var.get('document').callprop('getElementById', Js('SF')).get('value')) else Js(0.0)))
    var.put('of', (Js(1.0) if var.get('fromDec')(var.get('document').callprop('getElementById', Js('OF')).get('value')) else Js(0.0)))
PyJsHoisted_inputReg_.func_name = 'inputReg'
var.put('inputReg', PyJsHoisted_inputReg_)
@Js
def PyJsHoisted_inputMem_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['fnc', 'i', 'addr'])
    var.put('fnc', var.get('getRadix')(var.get('fromHex'), var.get('fromDec'), var.get('fromDec')))
    var.put('addr', var.get('getAddress')())
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        var.get('mem').put(var.get('ea')(var.get('addr'), var.get('i')), var.get('fnc')(var.get('document').callprop('getElementById', (Js('mem_')+var.get('i'))).get('value')))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_inputMem_.func_name = 'inputMem'
var.put('inputMem', PyJsHoisted_inputMem_)
@Js
def PyJsHoisted_fromHex_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'str'])
    var.put('n', var.get('parseInt')(var.get('str'), Js(16.0)))
    if var.get('isNaN')(var.get('n')):
        var.put('n', Js(0.0))
    return (var.get('n')&Js(65535))
PyJsHoisted_fromHex_.func_name = 'fromHex'
var.put('fromHex', PyJsHoisted_fromHex_)
@Js
def PyJsHoisted_fromDec_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'str'])
    var.put('n', var.get('parseInt')(var.get('str'), Js(10.0)))
    if var.get('isNaN')(var.get('n')):
        var.put('n', Js(0.0))
    return (var.get('n')&Js(65535))
PyJsHoisted_fromDec_.func_name = 'fromDec'
var.put('fromDec', PyJsHoisted_fromDec_)
@Js
def PyJsHoisted_getRadix_(hex, unsigned, signed, this, arguments, var=var):
    var = Scope({'hex':hex, 'unsigned':unsigned, 'signed':signed, 'this':this, 'arguments':arguments}, var)
    var.registers(['signed', 'unsigned', 'hex'])
    if (var.get('radix')==Js(0.0)):
        return var.get('hex')
    if (var.get('radix')==Js(1.0)):
        return var.get('unsigned')
    if (var.get('radix')==Js(2.0)):
        return var.get('signed')
PyJsHoisted_getRadix_.func_name = 'getRadix'
var.put('getRadix', PyJsHoisted_getRadix_)
@Js
def PyJsHoisted_getAddress_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('address')
PyJsHoisted_getAddress_.func_name = 'getAddress'
var.put('getAddress', PyJsHoisted_getAddress_)
@Js
def PyJsHoisted_onClickRadix_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('inputRegMem')()
    if var.get('document').callprop('getElementById', Js('radix_hex')).get('checked'):
        var.put('radix', Js(0.0))
    if var.get('document').callprop('getElementById', Js('radix_unsigned')).get('checked'):
        var.put('radix', Js(1.0))
    if var.get('document').callprop('getElementById', Js('radix_signed')).get('checked'):
        var.put('radix', Js(2.0))
    var.get('outputRegMem')()
PyJsHoisted_onClickRadix_.func_name = 'onClickRadix'
var.put('onClickRadix', PyJsHoisted_onClickRadix_)
@Js
def PyJsHoisted_onChangeAddress_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('inputMem')()
    var.put('address', var.get('parseInt')(var.get('document').callprop('getElementById', Js('address')).get('value'), Js(16.0)))
    if var.get('isNaN')(var.get('address')):
        var.put('address', Js(0.0))
    var.get('outputMem')()
PyJsHoisted_onChangeAddress_.func_name = 'onChangeAddress'
var.put('onChangeAddress', PyJsHoisted_onChangeAddress_)
@Js
def PyJsHoisted_markPR_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['nodeParent', 'elem'])
    if (var.get('markedAddress')>=Js(0.0)):
        var.put('elem', var.get('top').get('progframe').get('document').callprop('getElementById', (Js('line_addr_')+var.get('hex4')(var.get('markedAddress')))))
        if var.get('elem'):
            var.put('nodeParent', var.get('elem').get('parentNode'))
            if (var.get('nodeParent').get('id').callprop('substring', Js(0.0), Js(5.0))==Js('line_')):
                var.get('nodeParent').get('style').put('backgroundColor', Js('#FFFFFF'))
    var.put('markedAddress', (-Js(1.0)))
    var.put('elem', var.get('top').get('progframe').get('document').callprop('getElementById', (Js('line_addr_')+var.get('hex4')(var.get('pr')))))
    if var.get('elem'):
        var.put('nodeParent', var.get('elem').get('parentNode'))
        if (var.get('nodeParent').get('id').callprop('substring', Js(0.0), Js(5.0))==Js('line_')):
            var.get('nodeParent').get('style').put('backgroundColor', Js('#FFFF00'))
            var.put('markedAddress', var.get('pr'))
            var.get('scrollProgToShowLine')((var.get('nodeParent').get('id').callprop('substring', Js(5.0))-Js(0.0)))
PyJsHoisted_markPR_.func_name = 'markPR'
var.put('markPR', PyJsHoisted_markPR_)
@Js
def PyJsHoisted_scrollProgToShowLine_(lineNumber, this, arguments, var=var):
    var = Scope({'lineNumber':lineNumber, 'this':this, 'arguments':arguments}, var)
    var.registers(['lineTop', 'lineNumber', 'linesInWindow'])
    var.put('linesInWindow', (var.get('getClientHeight')(var.get('top').get('progframe'))/var.get('lineHeight')))
    var.put('lineTop', (var.get('getScrollPosY')(var.get('top').get('progframe'))/var.get('lineHeight')))
    if ((var.get('lineNumber')>=var.get('lineTop')) and (var.get('lineNumber')<((var.get('lineTop')+var.get('linesInWindow'))-Js(1.0)))):
        pass
    else:
        var.get('top').get('progframe').callprop('scrollTo', Js(0.0), (var.get('lineNumber')*var.get('lineHeight')))
PyJsHoisted_scrollProgToShowLine_.func_name = 'scrollProgToShowLine'
var.put('scrollProgToShowLine', PyJsHoisted_scrollProgToShowLine_)
@Js
def PyJsHoisted_ConsoleView_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('arrayLines', var.get('Array').create())
    var.get(u"this").put('lines', Js(25.0))
    @Js
    def PyJs_anonymous_10_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'filler'])
        var.put('filler', var.get('Array').create())
        #for JS loop
        var.put('i', var.get(u"this").get('arrayLines').get('length'))
        while (var.get('i')<var.get(u"this").get('lines')):
            var.get('filler').callprop('push', Js('<br />'))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.get('top').get('conframe').get('document').callprop('getElementById', Js('consolediv')).put('innerHTML', (var.get(u"this").get('arrayLines').callprop('join', Js(''))+var.get('filler').callprop('join', Js(''))))
    PyJs_anonymous_10_._set_name('anonymous')
    var.get(u"this").put('update', PyJs_anonymous_10_)
    @Js
    def PyJs_anonymous_11_(start, len, this, arguments, var=var):
        var = Scope({'start':start, 'len':len, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'charCode', 'start', 'arrayChars', 'str', 'len'])
        var.put('arrayChars', var.get('Array').create())
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('len')):
            var.put('charCode', var.get('jis8ToCharCode')(var.get('mem').get(var.get('zxt')((var.get('start')+var.get('i'))))))
            if (var.get('charCode')>=Js(0.0)):
                if ((var.get('charCode')<=Js(32)) or (var.get('charCode')==Js(127))):
                    var.put('charCode', Js(32))
                var.get('arrayChars').callprop('push', var.get('String').callprop('fromCharCode', var.get('charCode')))
            else:
                var.get('arrayChars').callprop('push', Js('?'))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('str', var.get('enCER')(var.get('arrayChars').callprop('join', Js(''))))
        while (var.get(u"this").get('arrayLines').get('length')>=var.get(u"this").get('lines')):
            var.get(u"this").get('arrayLines').callprop('shift')
        var.get(u"this").get('arrayLines').callprop('push', (var.get('str')+Js('<br />')))
        var.get(u"this").callprop('update')
    PyJs_anonymous_11_._set_name('anonymous')
    var.get(u"this").put('outputOneLine', PyJs_anonymous_11_)
    @Js
    def PyJs_anonymous_12_(start, lenaddr, this, arguments, var=var):
        var = Scope({'start':start, 'lenaddr':lenaddr, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'start', 'lenaddr', 'len'])
        var.put('len', var.get('mem').get(var.get('lenaddr')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('len')):
            var.get(u"this").callprop('outputOneLine', var.get('zxt')((var.get('start')+var.get('i'))), var.get('Math').callprop('min', (var.get('len')-var.get('i')), Js(80.0)))
            # update
            var.put('i', Js(80.0), '+')
    PyJs_anonymous_12_._set_name('anonymous')
    var.get(u"this").put('outputLine', PyJs_anonymous_12_)
    @Js
    def PyJs_anonymous_13_(start, lenaddr, this, arguments, var=var):
        var = Scope({'start':start, 'lenaddr':lenaddr, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'jis8', 'start', 'lenaddr', 'str', 'len'])
        var.put('str', var.get('prompt')(Js('IN命令の入力内容 （キャンセルでEOF）'), Js('')))
        if (var.get('str')!=var.get(u"null")):
            var.put('len', var.get('str').get('length'))
            if (var.get('len')>Js(256.0)):
                var.put('len', Js(256.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('len')):
                var.put('jis8', var.get('charCodeToJis8')(var.get('str').callprop('charCodeAt', var.get('i'))))
                var.get('mem').put(var.get('zxt')((var.get('start')+var.get('i'))), (var.get('jis8') if (var.get('jis8')>=Js(0.0)) else Js('?').callprop('charCodeAt', Js(0.0))))
                # update
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('mem').put(var.get('lenaddr'), var.get('len'))
            var.get(u"this").callprop('outputLine', var.get('start'), var.get('lenaddr'))
        else:
            var.get('mem').put(var.get('lenaddr'), Js(65535))
    PyJs_anonymous_13_._set_name('anonymous')
    var.get(u"this").put('inputLine', PyJs_anonymous_13_)
    var.get(u"this").callprop('update')
PyJsHoisted_ConsoleView_.func_name = 'ConsoleView'
var.put('ConsoleView', PyJsHoisted_ConsoleView_)
@Js
def PyJsHoisted_stepIn_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('stateCurrent')==var.get('STATE_NONE')):
        return var.get('undefined')
    if (var.get('stateCurrent')==var.get('STATE_UNSTARTED')):
        var.get('initializeRegMem')()
        var.get('setState')(var.get('STATE_BREAK'))
        return var.get('undefined')
    var.put('breakOnRet', Js(False))
    var.get('inputRegMem')()
    var.get('singleStep')()
    var.get('outputRegMem')()
PyJsHoisted_stepIn_.func_name = 'stepIn'
var.put('stepIn', PyJsHoisted_stepIn_)
@Js
def PyJsHoisted_stepOut_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('stateCurrent')!=var.get('STATE_BREAK')):
        return var.get('undefined')
    var.put('breakOnRet', Js(True))
    var.put('callNest', Js(0.0))
    var.get('inputRegMem')()
    var.get('setState')(var.get('STATE_RUNNING'))
    var.get('cont')()
PyJsHoisted_stepOut_.func_name = 'stepOut'
var.put('stepOut', PyJsHoisted_stepOut_)
@Js
def PyJsHoisted_stepOver_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('stateCurrent')!=var.get('STATE_BREAK')):
        return var.get('undefined')
    var.get('inputRegMem')()
    if ((var.get('mem').get(var.get('pr'))&Js(65280))==Js(32768)):
        var.put('callNest', (-Js(1.0)))
        var.put('breakOnRet', Js(True))
        var.get('setState')(var.get('STATE_RUNNING'))
        var.get('cont')()
    else:
        var.put('breakOnRet', Js(False))
        var.get('singleStep')()
        var.get('outputRegMem')()
PyJsHoisted_stepOver_.func_name = 'stepOver'
var.put('stepOver', PyJsHoisted_stepOver_)
@Js
def PyJsHoisted_go_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('stateCurrent')==var.get('STATE_NONE')):
        return var.get('undefined')
    if (var.get('stateCurrent')==var.get('STATE_UNSTARTED')):
        var.get('initializeRegMem')()
    var.put('breakOnRet', Js(False))
    var.get('inputRegMem')()
    var.get('setState')(var.get('STATE_RUNNING'))
    var.get('cont')()
PyJsHoisted_go_.func_name = 'go'
var.put('go', PyJsHoisted_go_)
@Js
def PyJsHoisted_cont_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    #for JS loop
    var.put('i', Js(0.0))
    while ((var.get('i')<Js(100.0)) and (var.get('stateCurrent')==var.get('STATE_RUNNING'))):
        var.get('singleStep')()
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('stateCurrent')==var.get('STATE_RUNNING')):
        var.get('setTimeout')(Js('cont();'), Js(1.0))
    else:
        var.get('outputRegMem')()
PyJsHoisted_cont_.func_name = 'cont'
var.put('cont', PyJsHoisted_cont_)
@Js
def PyJsHoisted_pause_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('stateCurrent')==var.get('STATE_RUNNING')):
        var.get('setState')(var.get('STATE_BREAK'))
PyJsHoisted_pause_.func_name = 'pause'
var.put('pause', PyJsHoisted_pause_)
@Js
def PyJsHoisted_stop_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if ((var.get('stateCurrent')==var.get('STATE_BREAK')) or (var.get('stateCurrent')==var.get('STATE_RUNNING'))):
        var.get('setState')(var.get('STATE_UNSTARTED'))
        var.get('alert')(Js('実行を中止しました。'))
PyJsHoisted_stop_.func_name = 'stop'
var.put('stop', PyJsHoisted_stop_)
@Js
def PyJsHoisted_singleStep_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    while 1:
        var.get('executeOneInstruction')()
        if (var.get('stateCurrent')==var.get('STATE_UNSTARTED')):
            return var.get('undefined')
        if not var.get('macroFlag').callprop('isSet', var.get('pr')):
            break
    if var.get('breakPointData').callprop('isSet', var.get('pr')):
        var.get('setState')(var.get('STATE_BREAK'))
        return var.get('undefined')
    if (var.get('breakOnRet') and (var.get('callNest')<Js(0.0))):
        var.get('setState')(var.get('STATE_BREAK'))
        return var.get('undefined')
PyJsHoisted_singleStep_.func_name = 'singleStep'
var.put('singleStep', PyJsHoisted_singleStep_)
@Js
def PyJsHoisted_INST_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['w'])
    var.get(u"this").put('code', (PyJsBshift(var.get('w'),Js(8.0))&Js(255)))
    var.get(u"this").put('gr', (PyJsBshift(var.get('w'),Js(4.0))&Js(7.0)))
    var.get(u"this").put('x', (var.get('w')&Js(7.0)))
    var.get(u"this").put('length2', Js(False))
    var.get(u"this").put('newPR', (-Js(1.0)))
    @Js
    def PyJs_anonymous_14_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['ea'])
        var.get(u"this").put('length2', Js(True))
        var.put('ea', var.get('mem').get(var.get('zxt')((var.get('pr')+Js(1.0)))))
        if var.get(u"this").get('x'):
            var.put('ea', var.get('gr').get(var.get(u"this").get('x')), '+')
        return var.get('zxt')(var.get('ea'))
    PyJs_anonymous_14_._set_name('anonymous')
    var.get(u"this").put('getEA', PyJs_anonymous_14_)
PyJsHoisted_INST_.func_name = 'INST'
var.put('INST', PyJsHoisted_INST_)
@Js
def PyJsHoisted_setFR_(value, this, arguments, var=var):
    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
    var.registers(['value'])
    var.put('zf', (Js(0.0) if (var.get('value')&Js(65535)) else Js(1.0)))
    var.put('sf', (Js(1.0) if (var.get('value')&Js(32768)) else Js(0.0)))
    var.put('of', Js(0.0))
PyJsHoisted_setFR_.func_name = 'setFR'
var.put('setFR', PyJsHoisted_setFR_)
@Js
def PyJsHoisted_setFROSigned_(value, this, arguments, var=var):
    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
    var.registers(['value'])
    var.put('zf', (Js(0.0) if (var.get('value')&Js(65535)) else Js(1.0)))
    var.put('sf', (Js(1.0) if (var.get('value')&Js(32768)) else Js(0.0)))
    var.put('of', (Js(1.0) if ((var.get('value')<(-Js(32768.0))) or (var.get('value')>Js(32767.0))) else Js(0.0)))
PyJsHoisted_setFROSigned_.func_name = 'setFROSigned'
var.put('setFROSigned', PyJsHoisted_setFROSigned_)
@Js
def PyJsHoisted_setFROUnsigned_(value, this, arguments, var=var):
    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
    var.registers(['value'])
    var.put('zf', (Js(0.0) if (var.get('value')&Js(65535)) else Js(1.0)))
    var.put('sf', (Js(1.0) if (var.get('value')&Js(32768)) else Js(0.0)))
    var.put('of', (Js(1.0) if ((var.get('value')<Js(0.0)) or (var.get('value')>Js(65535.0))) else Js(0.0)))
PyJsHoisted_setFROUnsigned_.func_name = 'setFROUnsigned'
var.put('setFROUnsigned', PyJsHoisted_setFROUnsigned_)
@Js
def PyJsHoisted_setFRC_(w1, w2, this, arguments, var=var):
    var = Scope({'w1':w1, 'w2':w2, 'this':this, 'arguments':arguments}, var)
    var.registers(['w1', 'w2'])
    if (var.get('w1')>var.get('w2')):
        var.put('sf', Js(0.0))
        var.put('zf', Js(0.0))
    else:
        if (var.get('w1')==var.get('w2')):
            var.put('sf', Js(0.0))
            var.put('zf', Js(1.0))
        else:
            var.put('sf', Js(1.0))
            var.put('zf', Js(0.0))
    var.put('of', Js(0.0))
PyJsHoisted_setFRC_.func_name = 'setFRC'
var.put('setFRC', PyJsHoisted_setFRC_)
@Js
def PyJsHoisted_InstTableItem_(fnc, fncop2, this, arguments, var=var):
    var = Scope({'fnc':fnc, 'fncop2':fncop2, 'this':this, 'arguments':arguments}, var)
    var.registers(['fnc', 'fncop2'])
    var.get(u"this").put('fnc', var.get('fnc'))
    var.get(u"this").put('fncop2', var.get('fncop2'))
PyJsHoisted_InstTableItem_.func_name = 'InstTableItem'
var.put('InstTableItem', PyJsHoisted_InstTableItem_)
@Js
def PyJsHoisted_executeOneInstruction_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'item', 'inst'])
    var.put('w', var.get('mem').get(var.get('pr')))
    var.put('inst', var.get('INST').create(var.get('w')))
    var.put('item', var.get('instTable').get(var.get('inst').get('code')))
    var.get('item').callprop('fnc', var.get('inst'))
    if (var.get('inst').get('newPR')==var.get('spInit')):
        var.get('alert')(Js('プログラムが終了しました。'))
        var.get('setState')(var.get('STATE_UNSTARTED'))
    else:
        if (var.get('inst').get('newPR')>=Js(0.0)):
            var.put('pr', var.get('inst').get('newPR'))
        else:
            if var.get('inst').get('length2'):
                var.put('pr', var.get('zxt')((var.get('pr')+Js(2.0))))
            else:
                var.put('pr', var.get('zxt')((var.get('pr')+Js(1.0))))
PyJsHoisted_executeOneInstruction_.func_name = 'executeOneInstruction'
var.put('executeOneInstruction', PyJsHoisted_executeOneInstruction_)
@Js
def PyJsHoisted_op2r_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    return var.get('gr').get(var.get('inst').get('x'))
PyJsHoisted_op2r_.func_name = 'op2r'
var.put('op2r', PyJsHoisted_op2r_)
@Js
def PyJsHoisted_op2m_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    return var.get('mem').get(var.get('inst').callprop('getEA'))
PyJsHoisted_op2m_.func_name = 'op2m'
var.put('op2m', PyJsHoisted_op2m_)
@Js
def PyJsHoisted_instInvalid_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    pass
PyJsHoisted_instInvalid_.func_name = 'instInvalid'
var.put('instInvalid', PyJsHoisted_instInvalid_)
@Js
def PyJsHoisted_instNOP_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    pass
PyJsHoisted_instNOP_.func_name = 'instNOP'
var.put('instNOP', PyJsHoisted_instNOP_)
@Js
def PyJsHoisted_instLD_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get(u"this").callprop('fncop2', var.get('inst')))))
PyJsHoisted_instLD_.func_name = 'instLD'
var.put('instLD', PyJsHoisted_instLD_)
@Js
def PyJsHoisted_instST_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('mem').put(var.get('inst').callprop('getEA'), var.get('zxt')(var.get('gr').get(var.get('inst').get('gr'))))
PyJsHoisted_instST_.func_name = 'instST'
var.put('instST', PyJsHoisted_instST_)
@Js
def PyJsHoisted_instLAD_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('gr').put(var.get('inst').get('gr'), var.get('inst').callprop('getEA'))
PyJsHoisted_instLAD_.func_name = 'instLAD'
var.put('instLAD', PyJsHoisted_instLAD_)
@Js
def PyJsHoisted_instADDA_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'inst'])
    var.put('r', (var.get('sxt')(var.get('gr').get(var.get('inst').get('gr')))+var.get('sxt')(var.get(u"this").callprop('fncop2', var.get('inst')))))
    var.get('setFROSigned')(var.get('r'))
    var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('r')))
PyJsHoisted_instADDA_.func_name = 'instADDA'
var.put('instADDA', PyJsHoisted_instADDA_)
@Js
def PyJsHoisted_instSUBA_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'inst'])
    var.put('r', (var.get('sxt')(var.get('gr').get(var.get('inst').get('gr')))-var.get('sxt')(var.get(u"this").callprop('fncop2', var.get('inst')))))
    var.get('setFROSigned')(var.get('r'))
    var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('r')))
PyJsHoisted_instSUBA_.func_name = 'instSUBA'
var.put('instSUBA', PyJsHoisted_instSUBA_)
@Js
def PyJsHoisted_instADDL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'inst'])
    var.put('r', (var.get('zxt')(var.get('gr').get(var.get('inst').get('gr')))+var.get('zxt')(var.get(u"this").callprop('fncop2', var.get('inst')))))
    var.get('setFROUnsigned')(var.get('r'))
    var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('r')))
PyJsHoisted_instADDL_.func_name = 'instADDL'
var.put('instADDL', PyJsHoisted_instADDL_)
@Js
def PyJsHoisted_instSUBL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'inst'])
    var.put('r', (var.get('zxt')(var.get('gr').get(var.get('inst').get('gr')))-var.get('zxt')(var.get(u"this").callprop('fncop2', var.get('inst')))))
    var.get('setFROUnsigned')(var.get('r'))
    var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('r')))
PyJsHoisted_instSUBL_.func_name = 'instSUBL'
var.put('instSUBL', PyJsHoisted_instSUBL_)
@Js
def PyJsHoisted_instAND_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')((var.get('gr').get(var.get('inst').get('gr'))&var.get(u"this").callprop('fncop2', var.get('inst'))))))
PyJsHoisted_instAND_.func_name = 'instAND'
var.put('instAND', PyJsHoisted_instAND_)
@Js
def PyJsHoisted_instOR_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')((var.get('gr').get(var.get('inst').get('gr'))|var.get(u"this").callprop('fncop2', var.get('inst'))))))
PyJsHoisted_instOR_.func_name = 'instOR'
var.put('instOR', PyJsHoisted_instOR_)
@Js
def PyJsHoisted_instXOR_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')((var.get('gr').get(var.get('inst').get('gr'))^var.get(u"this").callprop('fncop2', var.get('inst'))))))
PyJsHoisted_instXOR_.func_name = 'instXOR'
var.put('instXOR', PyJsHoisted_instXOR_)
@Js
def PyJsHoisted_instCPA_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFRC')(var.get('sxt')(var.get('gr').get(var.get('inst').get('gr'))), var.get('sxt')(var.get(u"this").callprop('fncop2', var.get('inst'))))
PyJsHoisted_instCPA_.func_name = 'instCPA'
var.put('instCPA', PyJsHoisted_instCPA_)
@Js
def PyJsHoisted_instCPL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('setFRC')(var.get('zxt')(var.get('gr').get(var.get('inst').get('gr'))), var.get('zxt')(var.get(u"this").callprop('fncop2', var.get('inst'))))
PyJsHoisted_instCPL_.func_name = 'instCPL'
var.put('instCPL', PyJsHoisted_instCPL_)
@Js
def PyJsHoisted_instSLA_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'bits', 'inst', 'sign'])
    var.put('bits', var.get('inst').callprop('getEA'))
    if (var.get('bits')==Js(0.0)):
        var.get('setFR')(var.get('gr').get(var.get('inst').get('gr')))
        return var.get('undefined')
    var.put('w', var.get('zxt')(var.get('gr').get(var.get('inst').get('gr'))))
    var.put('sign', (var.get('w')&Js(32768)))
    var.put('w', var.get('bits'), '<<')
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), (var.get('sign')|(var.get('w')&Js(32767)))))
    var.put('of', (Js(1.0) if (var.get('w')&Js(32768)) else Js(0.0)))
PyJsHoisted_instSLA_.func_name = 'instSLA'
var.put('instSLA', PyJsHoisted_instSLA_)
@Js
def PyJsHoisted_instSRA_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'bits', 'inst'])
    var.put('bits', var.get('inst').callprop('getEA'))
    if (var.get('bits')==Js(0.0)):
        var.get('setFR')(var.get('gr').get(var.get('inst').get('gr')))
        return var.get('undefined')
    var.put('w', var.get('sxt')(var.get('gr').get(var.get('inst').get('gr'))))
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')((var.get('w')>>var.get('bits')))))
    var.put('of', ((var.get('w')>>(var.get('bits')-Js(1.0)))&Js(1.0)))
PyJsHoisted_instSRA_.func_name = 'instSRA'
var.put('instSRA', PyJsHoisted_instSRA_)
@Js
def PyJsHoisted_instSLL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'bits', 'inst'])
    var.put('bits', var.get('inst').callprop('getEA'))
    if (var.get('bits')==Js(0.0)):
        var.get('setFR')(var.get('gr').get(var.get('inst').get('gr')))
        return var.get('undefined')
    var.put('w', var.get('zxt')(var.get('gr').get(var.get('inst').get('gr'))))
    var.put('w', var.get('bits'), '<<')
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('w'))))
    var.put('of', (Js(1.0) if (var.get('w')&Js(65536)) else Js(0.0)))
PyJsHoisted_instSLL_.func_name = 'instSLL'
var.put('instSLL', PyJsHoisted_instSLL_)
@Js
def PyJsHoisted_instSRL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['w', 'bits', 'inst'])
    var.put('bits', var.get('inst').callprop('getEA'))
    if (var.get('bits')==Js(0.0)):
        var.get('setFR')(var.get('gr').get(var.get('inst').get('gr')))
        return var.get('undefined')
    var.put('w', var.get('zxt')(var.get('gr').get(var.get('inst').get('gr'))))
    var.get('setFR')(var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(PyJsBshift(var.get('w'),var.get('bits')))))
    var.put('of', (PyJsBshift(var.get('w'),(var.get('bits')-Js(1.0)))&Js(1.0)))
PyJsHoisted_instSRL_.func_name = 'instSRL'
var.put('instSRL', PyJsHoisted_instSRL_)
@Js
def PyJsHoisted_instJMI_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    if var.get('sf'):
        var.get('instJUMP')(var.get('inst'))
    else:
        var.get('inst').put('length2', Js(True))
PyJsHoisted_instJMI_.func_name = 'instJMI'
var.put('instJMI', PyJsHoisted_instJMI_)
@Js
def PyJsHoisted_instJNZ_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    if var.get('zf').neg():
        var.get('instJUMP')(var.get('inst'))
    else:
        var.get('inst').put('length2', Js(True))
PyJsHoisted_instJNZ_.func_name = 'instJNZ'
var.put('instJNZ', PyJsHoisted_instJNZ_)
@Js
def PyJsHoisted_instJZE_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    if var.get('zf'):
        var.get('instJUMP')(var.get('inst'))
    else:
        var.get('inst').put('length2', Js(True))
PyJsHoisted_instJZE_.func_name = 'instJZE'
var.put('instJZE', PyJsHoisted_instJZE_)
@Js
def PyJsHoisted_instJUMP_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('inst').put('newPR', var.get('inst').callprop('getEA'))
PyJsHoisted_instJUMP_.func_name = 'instJUMP'
var.put('instJUMP', PyJsHoisted_instJUMP_)
@Js
def PyJsHoisted_instJPL_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    if (var.get('zf').neg() and var.get('sf').neg()):
        var.get('instJUMP')(var.get('inst'))
    else:
        var.get('inst').put('length2', Js(True))
PyJsHoisted_instJPL_.func_name = 'instJPL'
var.put('instJPL', PyJsHoisted_instJPL_)
@Js
def PyJsHoisted_instJOV_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    if var.get('of'):
        var.get('instJUMP')(var.get('inst'))
    else:
        var.get('inst').put('length2', Js(True))
PyJsHoisted_instJOV_.func_name = 'instJOV'
var.put('instJOV', PyJsHoisted_instJOV_)
@Js
def PyJsHoisted_instPUSH_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.put('sp', var.get('zxt')((var.get('sp')-Js(1.0))))
    var.get('mem').put(var.get('sp'), var.get('inst').callprop('getEA'))
PyJsHoisted_instPUSH_.func_name = 'instPUSH'
var.put('instPUSH', PyJsHoisted_instPUSH_)
@Js
def PyJsHoisted_instPOP_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('gr').put(var.get('inst').get('gr'), var.get('zxt')(var.get('mem').get(var.get('sp'))))
    var.put('sp', var.get('zxt')((var.get('sp')+Js(1.0))))
PyJsHoisted_instPOP_.func_name = 'instPOP'
var.put('instPOP', PyJsHoisted_instPOP_)
@Js
def PyJsHoisted_instCALL_(inst, fncop2, this, arguments, var=var):
    var = Scope({'inst':inst, 'fncop2':fncop2, 'this':this, 'arguments':arguments}, var)
    var.registers(['fncop2', 'inst'])
    var.get('inst').put('newPR', var.get('inst').callprop('getEA'))
    var.put('sp', var.get('zxt')((var.get('sp')-Js(1.0))))
    var.get('mem').put(var.get('sp'), var.get('zxt')((var.get('pr')+Js(2.0))))
    (var.put('callNest',Js(var.get('callNest').to_number())+Js(1))-Js(1))
PyJsHoisted_instCALL_.func_name = 'instCALL'
var.put('instCALL', PyJsHoisted_instCALL_)
@Js
def PyJsHoisted_instRET_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['inst'])
    var.get('inst').put('newPR', var.get('mem').get(var.get('sp')))
    var.put('sp', var.get('zxt')((var.get('sp')+Js(1.0))))
    (var.put('callNest',Js(var.get('callNest').to_number())-Js(1))+Js(1))
PyJsHoisted_instRET_.func_name = 'instRET'
var.put('instRET', PyJsHoisted_instRET_)
@Js
def PyJsHoisted_instSVC_(inst, this, arguments, var=var):
    var = Scope({'inst':inst, 'this':this, 'arguments':arguments}, var)
    var.registers(['ea', 'inst'])
    var.put('ea', var.get('inst').callprop('getEA'))
    if (var.get('ea')==Js(1.0)):
        var.get('consoleView').callprop('inputLine', var.get('zxt')(var.get('gr').get('1')), var.get('zxt')(var.get('gr').get('2')))
    else:
        if (var.get('ea')==Js(2.0)):
            var.get('consoleView').callprop('outputLine', var.get('zxt')(var.get('gr').get('1')), var.get('zxt')(var.get('gr').get('2')))
        else:
            var.get('setState')(var.get('STATE_BREAK'))
PyJsHoisted_instSVC_.func_name = 'instSVC'
var.put('instSVC', PyJsHoisted_instSVC_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('breakPointData', var.get('Bits64K').create())
var.put('macroFlag', var.get('Bits64K').create())
pass
var.put('aITable', Js({'NOP':var.get('AITableItem').create(Js(0), var.get('alNone')),'LD':var.get('AITableItem').create(Js(16), var.get('alRMR')),'ST':var.get('AITableItem').create(Js(17), var.get('alRM')),'LAD':var.get('AITableItem').create(Js(18), var.get('alRM')),'ADDA':var.get('AITableItem').create(Js(32), var.get('alRMR')),'SUBA':var.get('AITableItem').create(Js(33), var.get('alRMR')),'ADDL':var.get('AITableItem').create(Js(34), var.get('alRMR')),'SUBL':var.get('AITableItem').create(Js(35), var.get('alRMR')),'AND':var.get('AITableItem').create(Js(48), var.get('alRMR')),'OR':var.get('AITableItem').create(Js(49), var.get('alRMR')),'XOR':var.get('AITableItem').create(Js(50), var.get('alRMR')),'CPA':var.get('AITableItem').create(Js(64), var.get('alRMR')),'CPL':var.get('AITableItem').create(Js(65), var.get('alRMR')),'SLA':var.get('AITableItem').create(Js(80), var.get('alRM')),'SRA':var.get('AITableItem').create(Js(81), var.get('alRM')),'SLL':var.get('AITableItem').create(Js(82), var.get('alRM')),'SRL':var.get('AITableItem').create(Js(83), var.get('alRM')),'JMI':var.get('AITableItem').create(Js(97), var.get('alM')),'JNZ':var.get('AITableItem').create(Js(98), var.get('alM')),'JZE':var.get('AITableItem').create(Js(99), var.get('alM')),'JUMP':var.get('AITableItem').create(Js(100), var.get('alM')),'JPL':var.get('AITableItem').create(Js(101), var.get('alM')),'JOV':var.get('AITableItem').create(Js(102), var.get('alM')),'PUSH':var.get('AITableItem').create(Js(112), var.get('alM')),'POP':var.get('AITableItem').create(Js(113), var.get('alR')),'CALL':var.get('AITableItem').create(Js(128), var.get('alM')),'RET':var.get('AITableItem').create(Js(129), var.get('alNone')),'SVC':var.get('AITableItem').create(Js(240), var.get('alM')),'START':var.get('AITableItem').create((-Js(1.0)), var.get('alStart')),'END':var.get('AITableItem').create((-Js(1.0)), var.get('alEnd')),'DS':var.get('AITableItem').create((-Js(1.0)), var.get('alDS')),'DC':var.get('AITableItem').create((-Js(1.0)), var.get('alDC')),'IN':var.get('AITableItem').create(Js(1.0), var.get('alInOut')),'OUT':var.get('AITableItem').create(Js(2.0), var.get('alInOut')),'RPUSH':var.get('AITableItem').create((-Js(1.0)), var.get('alRPush')),'RPOP':var.get('AITableItem').create((-Js(1.0)), var.get('alRPop'))}))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('errorShown', (-Js(1.0)))
var.put('scriptAllowed', Js(False))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('v', Js(0.0))
var.put('STATE_NONE', (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1)))
var.put('STATE_UNSTARTED', (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1)))
var.put('STATE_BREAK', (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1)))
var.put('STATE_RUNNING', (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1)))
var.put('stateCurrent', var.get('STATE_NONE'))
pass
pass
pass
pass
var.put('gr', var.get('Array').create(Js(8.0)))
pass
pass
var.put('zf', Js(0.0))
var.put('sf', Js(0.0))
var.put('of', Js(0.0))
var.put('mem', var.get('Array').create(Js(65536.0)))
var.put('address', Js(0.0))
var.put('radix', Js(0.0))
var.put('markedAddress', (-Js(1.0)))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('breakOnRet', Js(False))
pass
pass
pass
pass
pass
pass
pass
pass
var.put('callNest', Js(0.0))
pass
pass
pass
pass
pass
pass
pass
pass
var.put('instTable', var.get('Array').create(Js(256.0)))
#for JS loop
var.put('i', Js(0.0))
while (var.get('i')<Js(256.0)):
    var.get('instTable').put(var.get('i'), var.get('InstTableItem').create(var.get('instInvalid'), var.get(u"null")))
    # update
    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
var.get('instTable').put('0', var.get('InstTableItem').create(var.get('instNOP'), var.get(u"null")))
var.get('instTable').put('16', var.get('InstTableItem').create(var.get('instLD'), var.get('op2m')))
var.get('instTable').put('17', var.get('InstTableItem').create(var.get('instST'), var.get(u"null")))
var.get('instTable').put('18', var.get('InstTableItem').create(var.get('instLAD'), var.get(u"null")))
var.get('instTable').put('20', var.get('InstTableItem').create(var.get('instLD'), var.get('op2r')))
var.get('instTable').put('32', var.get('InstTableItem').create(var.get('instADDA'), var.get('op2m')))
var.get('instTable').put('33', var.get('InstTableItem').create(var.get('instSUBA'), var.get('op2m')))
var.get('instTable').put('34', var.get('InstTableItem').create(var.get('instADDL'), var.get('op2m')))
var.get('instTable').put('35', var.get('InstTableItem').create(var.get('instSUBL'), var.get('op2m')))
var.get('instTable').put('36', var.get('InstTableItem').create(var.get('instADDA'), var.get('op2r')))
var.get('instTable').put('37', var.get('InstTableItem').create(var.get('instSUBA'), var.get('op2r')))
var.get('instTable').put('38', var.get('InstTableItem').create(var.get('instADDL'), var.get('op2r')))
var.get('instTable').put('39', var.get('InstTableItem').create(var.get('instSUBL'), var.get('op2r')))
var.get('instTable').put('48', var.get('InstTableItem').create(var.get('instAND'), var.get('op2m')))
var.get('instTable').put('49', var.get('InstTableItem').create(var.get('instOR'), var.get('op2m')))
var.get('instTable').put('50', var.get('InstTableItem').create(var.get('instXOR'), var.get('op2m')))
var.get('instTable').put('52', var.get('InstTableItem').create(var.get('instAND'), var.get('op2r')))
var.get('instTable').put('53', var.get('InstTableItem').create(var.get('instOR'), var.get('op2r')))
var.get('instTable').put('54', var.get('InstTableItem').create(var.get('instXOR'), var.get('op2r')))
var.get('instTable').put('64', var.get('InstTableItem').create(var.get('instCPA'), var.get('op2m')))
var.get('instTable').put('65', var.get('InstTableItem').create(var.get('instCPL'), var.get('op2m')))
var.get('instTable').put('68', var.get('InstTableItem').create(var.get('instCPA'), var.get('op2r')))
var.get('instTable').put('69', var.get('InstTableItem').create(var.get('instCPL'), var.get('op2r')))
var.get('instTable').put('80', var.get('InstTableItem').create(var.get('instSLA'), var.get(u"null")))
var.get('instTable').put('81', var.get('InstTableItem').create(var.get('instSRA'), var.get(u"null")))
var.get('instTable').put('82', var.get('InstTableItem').create(var.get('instSLL'), var.get(u"null")))
var.get('instTable').put('83', var.get('InstTableItem').create(var.get('instSRL'), var.get(u"null")))
var.get('instTable').put('97', var.get('InstTableItem').create(var.get('instJMI'), var.get(u"null")))
var.get('instTable').put('98', var.get('InstTableItem').create(var.get('instJNZ'), var.get(u"null")))
var.get('instTable').put('99', var.get('InstTableItem').create(var.get('instJZE'), var.get(u"null")))
var.get('instTable').put('100', var.get('InstTableItem').create(var.get('instJUMP'), var.get(u"null")))
var.get('instTable').put('101', var.get('InstTableItem').create(var.get('instJPL'), var.get(u"null")))
var.get('instTable').put('102', var.get('InstTableItem').create(var.get('instJOV'), var.get(u"null")))
var.get('instTable').put('112', var.get('InstTableItem').create(var.get('instPUSH'), var.get(u"null")))
var.get('instTable').put('113', var.get('InstTableItem').create(var.get('instPOP'), var.get(u"null")))
var.get('instTable').put('128', var.get('InstTableItem').create(var.get('instCALL'), var.get(u"null")))
var.get('instTable').put('129', var.get('InstTableItem').create(var.get('instRET'), var.get(u"null")))
var.get('instTable').put('240', var.get('InstTableItem').create(var.get('instSVC'), var.get(u"null")))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
casl = var.to_python()