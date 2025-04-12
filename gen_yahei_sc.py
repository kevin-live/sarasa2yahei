import utils
import shutil as fs


def gen_yahei_regular_sc(path):
    fs.copy(path + '/SarasaUiSC-Regular.ttf', path + '/SarasaUiSC-Regular-ui.ttf')

    font = utils.open_font(path + '/SarasaUiSC-Regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_regular_names(font)

    font_ui = utils.open_font(path + '/SarasaUiSC-Regular-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_regular_ui_names(font_ui)

    font.generateTtc(path + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_light_sc(path):
    fs.copy(path + '/SarasaUiSC-Light.ttf', path + '/SarasaUiSC-Light-ui.ttf')

    font = utils.open_font(path + '/SarasaUiSC-Light.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_light_names(font)

    font_ui = utils.open_font(path + '/SarasaUiSC-Light-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_light_ui_names(font_ui)

    font.generateTtc(path + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_yahei_bold_sc(path):
    fs.copy(path + '/SarasaUiSC-Bold.ttf', path + '/SarasaUiSC-Bold-ui.ttf')

    font = utils.open_font(path + '/SarasaUiSC-Bold.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_yahei_bold_names(font)

    font_ui = utils.open_font(path + '/SarasaUiSC-Bold-ui.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_yahei_bold_ui_names(font_ui)

    font.generateTtc(path + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)
